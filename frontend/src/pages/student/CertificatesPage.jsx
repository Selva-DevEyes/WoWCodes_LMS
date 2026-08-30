import { useState, useEffect, useRef } from 'react'
import {
  FiAward,
  FiCheckCircle,
  FiDownload,
  FiShare2,
  FiCheck,
  FiExternalLink,
  FiPrinter,
  FiShield,
  FiStar,
} from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'
import Logo from '../../components/layout/Logo'

const CertificatesPage = () => {
  const [certificates, setCertificates] = useState([])
  const [loading, setLoading] = useState(true)
  const [copiedCode, setCopiedCode] = useState(null)
  const [selectedCert, setSelectedCert] = useState(null)

  useEffect(() => {
    apiClient
      .get(ENDPOINTS.certificates)
      .then((res) => {
        setCertificates(res.data)
        if (res.data.length > 0) {
          setSelectedCert(res.data[0])
        }
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  const copyVerificationLink = (code) => {
    const url = `${window.location.origin}/certificates?verify=${code}`
    navigator.clipboard.writeText(url)
    setCopiedCode(code)
    setTimeout(() => setCopiedCode(null), 2500)
  }

  const handlePrintCertificate = () => {
    window.print()
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  return (
    <div className="space-y-8 max-w-7xl mx-auto font-sans pb-20">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 print:hidden">
        <div className="flex items-center gap-3.5">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-amber-500 to-amber-600 text-white flex items-center justify-center text-2xl shrink-0 shadow-md shadow-amber-500/20">
            <FiAward />
          </div>
          <div>
            <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
              Official Engineering Certifications
            </h1>
            <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal mt-0.5">
              Accredited credentials awarded upon curriculum mastery, topic evaluations, and Capstone Project approval
            </p>
          </div>
        </div>

        {selectedCert && (
          <div className="flex items-center gap-2 self-start sm:self-auto">
            <button
              onClick={handlePrintCertificate}
              className="btn-primary flex items-center gap-2 text-xs py-2.5 px-4"
            >
              <FiPrinter className="w-4 h-4" /> Print / Save as PDF
            </button>
          </div>
        )}
      </div>

      {certificates.length === 0 ? (
        <div className="card text-center py-16 space-y-4 border border-slate-200 dark:border-slate-800 print:hidden">
          <div className="w-20 h-20 rounded-3xl bg-amber-500/10 text-amber-500 mx-auto flex items-center justify-center text-4xl border border-amber-500/20">
            <FiAward />
          </div>
          <div className="space-y-1">
            <h2 className="text-lg sm:text-xl font-bold tracking-tight text-slate-800 dark:text-slate-200">
              No Certificates Generated Yet
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 max-w-lg mx-auto leading-relaxed">
              To earn your official Software Development Engineering Certificate:
            </p>
          </div>

          <div className="max-w-md mx-auto text-left bg-slate-50 dark:bg-slate-950 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 space-y-2 text-xs text-slate-600 dark:text-slate-300 font-medium">
            <div className="flex items-center gap-2">
              <span className="w-5 h-5 rounded-full bg-indigo-100 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold font-mono text-[10px]">1</span>
              <span>Complete all 14 curriculum learning modules</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-5 h-5 rounded-full bg-indigo-100 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold font-mono text-[10px]">2</span>
              <span>Pass the employer-side topic evaluation quizzes</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-5 h-5 rounded-full bg-indigo-100 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold font-mono text-[10px]">3</span>
              <span>Submit your practical Capstone Project for instructor review</span>
            </div>
          </div>
        </div>
      ) : (
        <div className="space-y-8">
          {/* Main Visual Certificate Diploma Showcase */}
          {selectedCert && (
            <div className="relative rounded-3xl bg-white text-slate-900 border-8 border-slate-900/10 dark:border-slate-800 shadow-2xl p-8 sm:p-14 overflow-hidden print:p-8 print:border-none print:shadow-none">
              {/* Ornate Certificate Outer Borders & Background Watermark */}
              <div className="absolute inset-2 border-2 border-amber-600/30 rounded-2xl pointer-events-none" />
              <div className="absolute inset-4 border border-dashed border-amber-500/20 rounded-xl pointer-events-none" />
              <div className="absolute -right-24 -bottom-24 w-96 h-96 bg-gradient-to-tr from-amber-500/5 via-indigo-500/5 to-rose-500/5 rounded-full blur-3xl pointer-events-none" />

              <div className="relative z-10 space-y-8 text-center max-w-4xl mx-auto">
                {/* Header Badge & Brand */}
                <div className="flex flex-col items-center justify-center space-y-3">
                  <Logo size="lg" showSubtitle={false} />
                  <div className="flex items-center gap-2 text-xs font-mono font-bold uppercase tracking-[0.25em] text-slate-500">
                    <FiShield className="text-amber-500" /> WoWCodes Academy of Engineering
                  </div>
                  <h2 className="text-2xl sm:text-4xl font-serif font-black tracking-tight text-slate-900 uppercase pt-2">
                    Certificate of Technical Mastery
                  </h2>
                  <div className="w-24 h-1 bg-gradient-to-r from-rose-500 via-amber-500 to-indigo-600 rounded-full" />
                </div>

                {/* Recipient Statement */}
                <div className="space-y-3 pt-2">
                  <p className="text-xs sm:text-sm font-serif italic text-slate-500">
                    This is to officially certify that
                  </p>
                  <h3 className="text-3xl sm:text-5xl font-serif font-black text-slate-950 tracking-tight underline decoration-amber-400 decoration-wavy decoration-1 underline-offset-8">
                    {selectedCert.student_name || 'Software Development Engineer'}
                  </h3>
                  <p className="text-xs sm:text-sm text-slate-600 max-w-2xl mx-auto leading-relaxed pt-2">
                    has successfully completed the comprehensive professional curriculum, passed all 37 topic masterclasses, employer evaluations, and demonstrated production capability in
                  </p>
                  <div className="text-base sm:text-xl font-extrabold text-indigo-700 tracking-wide pt-1">
                    Full-Stack Software Development Engineering & Applied AI Track
                  </div>
                </div>

                {/* Honors & Performance Grade */}
                <div className="inline-flex items-center gap-3 bg-amber-50 border border-amber-300/80 px-5 py-2.5 rounded-2xl shadow-sm">
                  <FiStar className="text-amber-500 text-lg" />
                  <span className="text-xs sm:text-sm font-bold text-amber-950 font-mono tracking-wide">
                    {selectedCert.grade || 'Distinction with Honors (Grade A+)'}
                  </span>
                </div>

                {/* One-Line Congratulations Quote */}
                <div className="bg-slate-50/90 border-l-4 border-indigo-600 p-4 rounded-r-2xl max-w-2xl mx-auto text-left shadow-inner">
                  <p className="text-xs sm:text-sm font-serif italic text-slate-700 leading-relaxed">
                    "{selectedCert.congrats_quote || 'Congratulations on demonstrating exceptional technical mastery, solving complex algorithmic challenges, and engineering production-grade software architecture!'}"
                  </p>
                </div>

                {/* Seal & Signatures Row */}
                <div className="pt-8 border-t border-slate-200 grid grid-cols-1 sm:grid-cols-3 items-end gap-6 text-center sm:text-left">
                  {/* Left Signature */}
                  <div className="space-y-1">
                    <div className="font-serif italic text-xl text-slate-800 font-bold">
                      DevEyes Academic Board
                    </div>
                    <div className="h-0.5 w-36 bg-slate-300 mx-auto sm:mx-0" />
                    <p className="text-[11px] font-bold text-slate-600 uppercase tracking-wider">
                      Lead Engineering Instructor
                    </p>
                  </div>

                  {/* Center Official Gold Seal */}
                  <div className="flex flex-col items-center justify-center">
                    <div className="w-20 h-20 rounded-full bg-gradient-to-tr from-amber-400 via-amber-500 to-amber-600 text-white flex flex-col items-center justify-center p-2 shadow-xl border-4 border-white ring-4 ring-amber-300">
                      <FiAward className="text-2xl" />
                      <span className="text-[8px] font-black uppercase tracking-tighter mt-0.5">
                        VERIFIED
                      </span>
                    </div>
                  </div>

                  {/* Right Verification Details */}
                  <div className="space-y-1 text-center sm:text-right font-mono text-[11px] text-slate-500">
                    <p className="font-bold text-slate-800">
                      Credential ID: {selectedCert.certificate_code}
                    </p>
                    <p>
                      Issued: {new Date(selectedCert.issued_at).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
                    </p>
                    <p className="text-emerald-600 font-semibold flex items-center gap-1 justify-center sm:justify-end">
                      <FiCheckCircle className="w-3 h-3" /> Blockchain Verified
                    </p>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* List of Earned Credentials */}
          <div className="space-y-4 print:hidden">
            <h2 className="text-lg font-bold text-slate-900 dark:text-white">
              All Earned Credentials ({certificates.length})
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {certificates.map((cert) => {
                const isSelected = selectedCert?.id === cert.id
                return (
                  <div
                    key={cert.id}
                    onClick={() => setSelectedCert(cert)}
                    className={`card p-5 cursor-pointer transition-all duration-200 border-2 flex flex-col justify-between space-y-4 ${
                      isSelected
                        ? 'border-indigo-600 bg-indigo-50/20 dark:bg-indigo-950/30 shadow-md ring-2 ring-indigo-500/20'
                        : 'border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-500 flex items-center justify-center text-xl">
                          <FiAward />
                        </div>
                        <div>
                          <h3 className="text-sm font-bold text-slate-900 dark:text-white">
                            Full-Stack SDE & Applied AI Certificate
                          </h3>
                          <p className="text-xs text-slate-500 font-mono">
                            ID: {cert.certificate_code}
                          </p>
                        </div>
                      </div>

                      <span className="text-[11px] font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/80 px-2.5 py-1 rounded-full border border-emerald-500/30 font-mono">
                        {cert.grade || 'Grade A+'}
                      </span>
                    </div>

                    <div className="flex items-center justify-between pt-3 border-t border-slate-100 dark:border-slate-800 text-xs">
                      <span className="text-slate-400 font-mono">
                        Issued {new Date(cert.issued_at).toLocaleDateString()}
                      </span>

                      <button
                        onClick={(e) => {
                          e.stopPropagation()
                          copyVerificationLink(cert.certificate_code)
                        }}
                        className="text-indigo-600 dark:text-indigo-400 font-semibold hover:underline flex items-center gap-1"
                      >
                        {copiedCode === cert.certificate_code ? (
                          <>
                            <FiCheck className="text-emerald-500" /> Copied Link!
                          </>
                        ) : (
                          <>
                            <FiShare2 /> Share Credential
                          </>
                        )}
                      </button>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default CertificatesPage
