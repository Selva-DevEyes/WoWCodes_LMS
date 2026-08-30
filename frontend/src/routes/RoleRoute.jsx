import { Navigate } from 'react-router-dom'
import { useSelector } from 'react-redux'

const RoleRoute = ({ children, roles = [] }) => {
  const user = useSelector((state) => state.auth.user)
  const roleName = user?.role?.name || ''
  if (!roles.includes(roleName)) {
    return <Navigate to="/dashboard" replace />
  }
  return children
}

export default RoleRoute
