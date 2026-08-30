import { useEffect, useState } from 'react'
import { Outlet } from 'react-router-dom'
import Sidebar from '../components/layout/Sidebar'
import Navbar from '../components/layout/Navbar'

const DashboardLayout = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)

  useEffect(() => {
    const closeSidebarOnDesktop = () => {
      if (window.innerWidth >= 1024) setIsSidebarOpen(false)
    }
    window.addEventListener('resize', closeSidebarOnDesktop)
    return () => window.removeEventListener('resize', closeSidebarOnDesktop)
  }, [])

  return (
    <div className="min-h-screen bg-[#f7f8ff] dark:bg-[#16152b]">
      <Sidebar isOpen={isSidebarOpen} onClose={() => setIsSidebarOpen(false)} />
      <div className="lg:pl-64">
        <Navbar onOpenSidebar={() => setIsSidebarOpen(true)} />
        <main className="p-4 lg:p-8">
          <Outlet />
        </main>
      </div>
    </div>
  )
}

export default DashboardLayout
