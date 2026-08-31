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
    <div className="min-h-screen bg-slate-50 dark:bg-[#0b0f19] flex flex-col font-sans">
      <Sidebar isOpen={isSidebarOpen} onClose={() => setIsSidebarOpen(false)} />
      <div className="lg:pl-64 flex flex-col flex-1">
        <Navbar onOpenSidebar={() => setIsSidebarOpen(true)} />
        <main className="p-4 lg:p-8 flex-1">
          <Outlet />
        </main>
        {/* Professional Global Footer */}
        <footer className="py-6 px-4 border-t border-slate-200/80 dark:border-slate-800/80 text-center mt-auto bg-white/50 dark:bg-slate-900/50 backdrop-blur-sm">
          <div className="flex flex-wrap items-center justify-center gap-x-2.5 gap-y-1 text-xs text-slate-500 dark:text-slate-400">
            <span className="font-semibold text-slate-700 dark:text-slate-300">Learn. Practice. Grow.</span>
            <span className="text-slate-300 dark:text-slate-700 select-none">•</span>
            <span className="font-bold text-slate-900 dark:text-white tracking-tight">WOWCode</span>
            <span className="font-semibold text-indigo-600 dark:text-indigo-400">Created by Selvam S</span>
          </div>
        </footer>
      </div>
    </div>
  )
}

export default DashboardLayout
