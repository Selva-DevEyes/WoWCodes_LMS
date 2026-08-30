import { useState, useEffect } from 'react'
import { FiAward } from 'react-icons/fi'
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
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  return (
    <div>
      <div className="flex items-center gap-3 mb-8">
        <FiAward className="text-3xl text-accent-500" />
        <div>
          <h1 className="text-2xl font-bold">My Certificates</h1>
          <p className="text-gray-500 text-sm">Certificates earned from completed courses</p>
        </div>
      </div>

      {certificates.length === 0 ? (
        <div className="card text-center py-16">
          <FiAward className="text-6xl text-gray-300 mx-auto mb-4" />
          <p className="text-gray-500">No certificates yet. Complete courses to earn them!</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {certificates.map((cert) => (
            <div key={cert.id} className="card border-2 border-accent-400 dark:border-accent-600">
              <div className="flex items-center justify-between mb-4">
                <FiAward className="text-4xl text-accent-500" />
                <span className="text-xs bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded-full">
                  Verified
                </span>
              </div>
              <h2 className="font-bold text-lg mb-1">Course #{cert.course_id} Certificate</h2>
              <p className="text-sm text-gray-500 mb-4">
                Certificate Code: <span className="font-mono">{cert.certificate_code}</span>
              </p>
              <p className="text-xs text-gray-400">
                Issued: {new Date(cert.issued_at).toLocaleDateString()}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default CertificatesPage
