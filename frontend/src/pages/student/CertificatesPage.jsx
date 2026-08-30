import { useState, useEffect } from 'react'
import { FiAward, FiCheckCircle, FiExternalLink } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const CertificatesPage = () => {
  const [certificates, setCertificates] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    apiClient.get(ENDPOINTS.certificates)
      .then((res) => {
        setCertificates(res.data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans pb-16">
      {/* Page Header */}
      <div className="flex items-center gap-3">
        <div className="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-amber-500 flex items-center justify-center text-2xl shrink-0">
          <FiAward />
        </div>
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
            My Certificates
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal mt-1">
            Official verifiable engineering credentials earned from completed curricula
          </p>
        </div>
      </div>

      {certificates.length === 0 ? (
        <div className="card text-center py-16 space-y-3 border border-slate-200 dark:border-slate-800">
          <div className="w-16 h-16 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-400 mx-auto flex items-center justify-center text-3xl">
            <FiAward />
          </div>
          <h2 className="text-lg sm:text-xl font-bold tracking-tight text-slate-800 dark:text-slate-200">
            No Certificates Earned Yet
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 max-w-md mx-auto">
            Complete the final certification modules and capstone evaluations to generate your industry certificates.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {certificates.map((cert) => (
            <div key={cert.id} className="card border border-amber-500/30 bg-gradient-to-br from-white to-amber-50/20 dark:from-slate-900 dark:to-slate-950 p-6 space-y-4 relative overflow-hidden shadow-sm hover:shadow-md transition">
              <div className="flex items-center justify-between">
                <div className="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-500 flex items-center justify-center text-xl">
                  <FiAward />
                </div>
                <span className="inline-flex items-center gap-1 text-[11px] font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/80 px-2.5 py-1 rounded-full border border-emerald-500/30 font-mono">
                  <FiCheckCircle className="w-3.5 h-3.5" /> Verified Credential
                </span>
              </div>
              <div>
                <h3 className="text-base sm:text-lg font-semibold text-slate-900 dark:text-white tracking-normal">
                  Certificate of Software Development Engineering
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 font-mono">
                  Credential ID: <span className="text-indigo-600 dark:text-indigo-400 font-bold">{cert.certificate_code}</span>
                </p>
              </div>
              <div className="pt-2 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between text-xs text-slate-400 font-mono">
                <span>Issued: {new Date(cert.issued_at).toLocaleDateString()}</span>
                <span className="text-indigo-600 dark:text-indigo-400 font-bold flex items-center gap-1">
                  WoWCodes Certified <FiExternalLink className="w-3 h-3" />
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default CertificatesPage
