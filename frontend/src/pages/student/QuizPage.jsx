import { useEffect, useState } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import {
  FiChevronLeft,
  FiChevronRight,
  FiCheckCircle,
  FiXCircle,
  FiHelpCircle,
  FiInfo,
  FiAward,
  FiCheck,
  FiX,
  FiZap,
  FiArrowLeft,
} from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const QuizPage = () => {
  const { quizId } = useParams()
  const navigate = useNavigate()
  const [quiz, setQuiz] = useState(null)
  const [currentQ, setCurrentQ] = useState(0)
  const [answers, setAnswers] = useState({}) // { questionId: selectedOptionId }
  const [revealed, setRevealed] = useState({}) // { questionId: true }
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [submitError, setSubmitError] = useState('')

  useEffect(() => {
    apiClient
      .get(ENDPOINTS.quiz(quizId))
      .then((res) => {
        const quizData = res.data
        if (quizData && quizData.questions) {
          quizData.questions = quizData.questions.map((q) => {
            const shuffled = [...(q.options || [])]
            for (let i = shuffled.length - 1; i > 0; i--) {
              const j = Math.floor(Math.random() * (i + 1))
              ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
            }
            return { ...q, options: shuffled }
          })
        }
        setQuiz(quizData)
        setLoading(false)
      })
      .catch((err) => {
        console.error('Failed to load quiz:', err)
        setLoading(false)
      })
  }, [quizId])

  const handleSelectOption = (questionId, optionId) => {
    // Save selected answer & reveal immediate feedback
    setAnswers((prev) => ({ ...prev, [questionId]: optionId }))
    setRevealed((prev) => ({ ...prev, [questionId]: true }))
  }

  const handleNext = () => {
    // If answer selected but not revealed yet, mark revealed
    const q = quiz.questions[currentQ]
    if (answers[q.id] && !revealed[q.id]) {
      setRevealed((prev) => ({ ...prev, [q.id]: true }))
    }
    if (currentQ < quiz.questions.length - 1) {
      setCurrentQ(currentQ + 1)
    }
  }

  const handlePrev = () => {
    if (currentQ > 0) {
      setCurrentQ(currentQ - 1)
    }
  }

  const handleSubmit = async () => {
    if (submitting) return
    setSubmitting(true)
    setSubmitError('')

    const formattedAnswers = (quiz?.questions || []).map((q) => ({
      question_id: q.id,
      selected_option_id: answers[q.id] ? parseInt(answers[q.id]) : null,
    }))

    const payload = {
      quiz_id: parseInt(quizId),
      time_taken_seconds: 60,
      answers: formattedAnswers,
    }

    try {
      const { data } = await apiClient.post(ENDPOINTS.submitQuiz(quizId), payload)
      if (data && data.id) {
        navigate(`/quiz/result/${data.id}`)
      } else {
        throw new Error('No evaluation result returned by server')
      }
    } catch (err) {
      console.error('Failed to submit quiz:', err)
      const errorMsg = err.response?.data?.detail || err.message || 'Failed to submit quiz. Please check network and retry.'
      setSubmitError(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg))
    } finally {
      setSubmitting(false)
    }
  }

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center h-64 space-y-3">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600" />
        <p className="text-sm text-slate-400 font-medium">Loading Quiz Evaluation System...</p>
      </div>
    )
  }

  if (!quiz || !quiz.questions || quiz.questions.length === 0) {
    return (
      <div className="text-center py-20 bg-slate-900 border border-slate-800 rounded-3xl p-8 max-w-xl mx-auto">
        <FiHelpCircle className="w-12 h-12 text-amber-400 mx-auto mb-3" />
        <h2 className="text-lg font-bold text-white">Quiz Evaluation Not Found</h2>
        <p className="text-xs text-slate-400 mt-1">This quiz topic does not contain active questions yet.</p>
        <button onClick={() => navigate(-1)} className="mt-4 px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-semibold">
          Return to Topic Masterclass
        </button>
      </div>
    )
  }

  const question = quiz.questions[currentQ]
  const selectedOptionId = answers[question.id]
  const isRevealed = Boolean(revealed[question.id] || selectedOptionId)
  const isLast = currentQ === quiz.questions.length - 1

  // Find correct option for current question
  const correctOption = question.options.find((o) => o.is_correct)
  const isUserCorrect = selectedOptionId && correctOption && selectedOptionId === correctOption.id

  const answeredCount = Object.keys(answers).length
  const progressPct = Math.round(((currentQ + 1) / quiz.questions.length) * 100)

  const parsedPrompt = (() => {
    const rawText = question?.text || ''
    // Match "Q1 [Topic - Perspective]: Question..." or "[Topic - Perspective]: Question..." or "[Topic] Question..."
    const bracketMatch = rawText.match(/^(?:Q\d+\s*)?\[(.*?)\](?::)?\s*(.*)$/i)
    if (bracketMatch) {
      const tagContent = bracketMatch[1].trim()
      const questionBody = bracketMatch[2].trim() || rawText.trim()
      return {
        tag: `[${tagContent}]`,
        text: questionBody
      }
    }

    // Match "Q1: Question..."
    const qNumMatch = rawText.match(/^Q\d+[:.]\s*(.*)$/i)
    if (qNumMatch) {
      return {
        tag: `[${quiz?.title || 'Technical Evaluation'} - Employer Perspective]`,
        text: qNumMatch[1].trim()
      }
    }

    return {
      tag: `[${quiz?.title || 'Technical Evaluation'} - Employer Perspective]`,
      text: rawText.trim()
    }
  })()

  return (
    <div className="max-w-7xl w-full mx-auto space-y-6 font-sans pb-3 sm:pb-8 text-left">
      {/* Top Back Button to Topic */}
      <div className="flex items-center justify-between">
        <button
          onClick={() => navigate(-1)}
          className="inline-flex items-center gap-2 text-slate-400 hover:text-indigo-400 transition font-bold text-xs sm:text-sm bg-slate-950 px-4 py-2 rounded-xl border border-slate-800"
        >
          <FiArrowLeft className="w-4 h-4" /> Back to Topic Masterclass
        </button>
        <span className="text-xs font-mono text-slate-400">
          Quiz ID: #{quiz.id}
        </span>
      </div>

      {/* Quiz Header Banner */}
      <div className="bg-slate-950 border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xl text-white flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <span className="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 uppercase font-semibold font-mono">
              {quiz.level} Level
            </span>
            <span className="text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-medium">
              Passing Score: {quiz.passing_score}%
            </span>
          </div>
          <h1 className="text-xl sm:text-2xl font-black text-white tracking-tight">{quiz.title}</h1>
        </div>

        {/* Quick Stats Pill */}
        <div className="flex items-center gap-3 bg-slate-900 p-3.5 rounded-2xl border border-slate-800 self-start sm:self-auto shrink-0 font-mono">
          <div className="text-right">
            <p className="text-[11px] text-slate-400">Questions Answered</p>
            <p className="text-sm font-extrabold text-indigo-400">
              {answeredCount} / {quiz.questions.length}
            </p>
          </div>
        </div>
      </div>

      {/* Interactive Question Step Numbers Indicator */}
      <div className="bg-slate-950 border border-slate-800 rounded-2xl p-3 pb-3.5 shadow-md flex items-center justify-between gap-2 overflow-x-auto custom-scrollbar">
        {quiz.questions.map((q, idx) => {
          const userAns = answers[q.id]
          const qCorrect = q.options.find((o) => o.is_correct)
          const qIsRight = userAns && qCorrect && userAns === qCorrect.id
          const qIsAnswered = Boolean(userAns)
          const isCurrent = currentQ === idx

          return (
            <button
              key={q.id}
              onClick={() => setCurrentQ(idx)}
              className={`flex-1 min-w-[36px] h-10 rounded-xl font-mono text-xs font-bold transition flex items-center justify-center gap-1 border ${
                isCurrent
                  ? 'border-indigo-500 bg-indigo-600/30 text-indigo-200 shadow-md ring-2 ring-indigo-500/50 scale-105'
                  : qIsAnswered
                  ? qIsRight
                    ? 'border-emerald-500/50 bg-emerald-500/20 text-emerald-300'
                    : 'border-rose-500/50 bg-rose-500/20 text-rose-300'
                  : 'border-slate-800 bg-slate-900 text-slate-400 hover:border-slate-700'
              }`}
            >
              <span>{idx + 1}</span>
              {qIsAnswered && (
                qIsRight ? <FiCheck className="w-3 h-3 text-emerald-400" /> : <FiX className="w-3 h-3 text-rose-400" />
              )}
            </button>
          )
        })}
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
        <div
          className="bg-gradient-to-r from-indigo-500 via-purple-500 to-emerald-400 h-full transition-all duration-300 shadow-sm"
          style={{ width: `${progressPct}%` }}
        />
      </div>

      {/* Main Full Width Question Container */}
      <div className="bg-slate-950 border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xl space-y-5 text-left">
        <div className="flex items-center justify-between pb-4 border-b border-slate-800">
          <span className="text-xs font-mono font-bold text-indigo-400 bg-indigo-500/10 px-3 py-1 rounded-lg border border-indigo-500/20">
            Question {currentQ + 1} of {quiz.questions.length}
          </span>
          <span className="text-xs text-slate-400 font-mono">10 Points</span>
        </div>

        {/* Question Prompt with clean bracketed topic tag on its own row */}
        <div className="space-y-2.5 text-left">
          <div className="flex flex-wrap items-center gap-2">
            <span className="inline-flex items-center gap-1.5 text-xs font-mono font-bold px-3 py-1 rounded-xl bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 whitespace-nowrap shrink-0 w-fit">
              {parsedPrompt.tag}
            </span>
          </div>
          <h2 className="text-base sm:text-lg lg:text-xl font-bold text-white leading-relaxed text-left">
            {parsedPrompt.text}
          </h2>
        </div>

        {/* Answer Options Grid */}
        <div className="space-y-3 pt-2">
          {question.options.map((option) => {
            const isSelected = selectedOptionId === option.id
            const isCorrectOption = option.is_correct

            let optionStyle = 'border-slate-800 bg-slate-950 hover:border-slate-700 text-slate-200'
            let badge = null

            if (isRevealed) {
              if (isSelected && isCorrectOption) {
                // User selected correct answer
                optionStyle = 'border-emerald-500 bg-emerald-950/40 text-emerald-100 shadow-lg shadow-emerald-500/10 font-semibold'
                badge = (
                  <span className="inline-flex items-center gap-1 text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold shrink-0">
                    <FiCheckCircle className="w-3.5 h-3.5" /> Correct Answer
                  </span>
                )
              } else if (isSelected && !isCorrectOption) {
                // User selected wrong answer
                optionStyle = 'border-rose-500 bg-rose-950/40 text-rose-100 shadow-lg shadow-rose-500/10 font-semibold'
                badge = (
                  <span className="inline-flex items-center gap-1 text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/40 font-bold shrink-0">
                    <FiXCircle className="w-3.5 h-3.5" /> Incorrect Choice
                  </span>
                )
              } else if (!isSelected && isCorrectOption) {
                // Reveal correct answer when user was wrong
                optionStyle = 'border-emerald-500/60 bg-emerald-950/20 text-emerald-200 border-dashed font-semibold'
                badge = (
                  <span className="inline-flex items-center gap-1 text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 shrink-0">
                    <FiCheckCircle className="w-3.5 h-3.5" /> Correct Answer
                  </span>
                )
              }
            } else if (isSelected) {
              optionStyle = 'border-indigo-500 bg-indigo-950/40 text-indigo-100 font-semibold'
            }

            return (
              <button
                key={option.id}
                onClick={() => handleSelectOption(question.id, option.id)}
                className={`w-full text-left p-4 sm:p-5 rounded-2xl border-2 transition-all duration-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3 group ${optionStyle}`}
              >
                <div className="flex items-center gap-3">
                  <div
                    className={`w-7 h-7 rounded-xl flex items-center justify-center text-xs font-mono font-bold transition shrink-0 ${
                      isSelected
                        ? isRevealed
                          ? isCorrectOption
                            ? 'bg-emerald-500 text-slate-950'
                            : 'bg-rose-500 text-white'
                          : 'bg-indigo-600 text-white'
                        : isRevealed && isCorrectOption
                        ? 'bg-emerald-500/30 text-emerald-300'
                        : 'bg-slate-800 text-slate-400 group-hover:bg-slate-700'
                    }`}
                  >
                    {isRevealed ? (
                      isCorrectOption ? <FiCheck /> : isSelected ? <FiX /> : '•'
                    ) : (
                      isSelected ? '✓' : '•'
                    )}
                  </div>
                  <span className="text-sm sm:text-base leading-relaxed">{option.text}</span>
                </div>
                {badge}
              </button>
            )
          })}
        </div>

        {/* Detailed Explanation Breakdown Box (Displayed After Answering / Submitting) */}
        {isRevealed && (
          <div className="mt-6 pt-6 border-t border-slate-800 animate-in fade-in slide-in-from-top-2 duration-300">
            <div
              className={`p-5 rounded-2xl border ${
                isUserCorrect
                  ? 'bg-emerald-950/30 border-emerald-500/40 text-emerald-200'
                  : 'bg-rose-950/20 border-rose-500/30 text-rose-200'
              }`}
            >
              <div className="flex items-center gap-2 mb-3">
                {isUserCorrect ? (
                  <FiCheckCircle className="w-5 h-5 text-emerald-400" />
                ) : (
                  <FiXCircle className="w-5 h-5 text-rose-400" />
                )}
                <h3 className="text-sm font-bold tracking-wide uppercase font-mono">
                  {isUserCorrect ? 'Correct Answer Explanation' : 'Incorrect Choice — Explanation & Review'}
                </h3>
              </div>

              {/* Detailed Explanation Text */}
              <p className="text-xs sm:text-sm leading-relaxed text-slate-200 mb-4 bg-slate-900/60 p-4 rounded-xl border border-slate-800/80">
                <strong className="text-indigo-300 font-semibold block mb-1">💡 Engineering Principle:</strong>
                {question.explanation || 'Detailed concept verification covering code output and architectural trade-offs.'}
              </p>

              {/* Option Breakdown List */}
              <div className="space-y-2 text-xs">
                <p className="font-bold text-slate-300 font-mono uppercase tracking-wider mb-1.5">Answer Option Analysis:</p>
                {question.options.map((opt) => (
                  <div
                    key={opt.id}
                    className={`p-3 rounded-xl border flex flex-col sm:flex-row sm:items-start gap-2 sm:gap-3 ${
                      opt.is_correct
                        ? 'bg-emerald-900/30 border-emerald-500/40 text-emerald-200'
                        : 'bg-slate-900/80 border-slate-800 text-slate-400'
                    }`}
                  >
                    <span
                      className={`px-2 py-0.5 rounded font-mono text-[10px] font-bold self-start ${
                        opt.is_correct ? 'bg-emerald-500 text-slate-950' : 'bg-slate-800 text-slate-300'
                      }`}
                    >
                      {opt.is_correct ? 'CORRECT' : 'INCORRECT'}
                    </span>
                    <div className="space-y-0.5">
                      <p className="font-semibold text-slate-200">{opt.text}</p>
                      <p className="text-[11px] text-slate-400">
                        {opt.is_correct
                          ? 'This option correctly aligns with the technical specification.'
                          : 'This distractor option is invalid based on language semantics or system constraints.'}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Submission Error Banner if any */}
      {submitError && (
        <div className="p-4 rounded-2xl bg-rose-950/40 border border-rose-500/50 text-rose-200 text-xs font-semibold flex items-center justify-between">
          <span>⚠️ {submitError}</span>
          <button onClick={() => setSubmitError('')} className="text-rose-400 hover:text-white text-xs underline ml-2">
            Dismiss
          </button>
        </div>
      )}

      {/* Navigation & Submit Buttons Bar */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2">
        <button
          onClick={handlePrev}
          disabled={currentQ === 0 || submitting}
          className={`w-full sm:w-auto px-5 py-3 rounded-2xl text-xs font-semibold flex items-center justify-center gap-2 transition border ${
            currentQ === 0 || submitting
              ? 'opacity-40 cursor-not-allowed bg-slate-900 border-slate-800 text-slate-500'
              : 'bg-slate-800 hover:bg-slate-700 border-slate-700 text-slate-200'
          }`}
        >
          <FiChevronLeft className="w-4 h-4" /> Previous Question
        </button>

        {isLast ? (
          <button
            onClick={handleSubmit}
            disabled={submitting}
            className={`w-full sm:w-auto px-6 py-3.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-extrabold rounded-2xl transition shadow-lg shadow-emerald-600/30 flex items-center justify-center gap-2 ${
              submitting ? 'opacity-75 cursor-wait' : ''
            }`}
          >
            {submitting ? (
              <>
                <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
                Submitting & Evaluating...
              </>
            ) : (
              <>
                <FiAward className="w-4 h-4" /> Submit Quiz & View Grade
              </>
            )}
          </button>
        ) : (
          <button
            onClick={handleNext}
            className="w-full sm:w-auto px-6 py-3.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-extrabold rounded-2xl transition shadow-lg shadow-indigo-600/30 flex items-center justify-center gap-2"
          >
            Next Question <FiChevronRight className="w-4 h-4" />
          </button>
        )}
      </div>
    </div>
  )
}

export default QuizPage
