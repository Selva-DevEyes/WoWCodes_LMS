import {
  FiActivity,
  FiBookOpen,
  FiCode,
  FiCpu,
  FiDatabase,
  FiGitBranch,
  FiLayers,
  FiLayout,
  FiRepeat,
  FiServer,
  FiTerminal,
  FiZap,
} from 'react-icons/fi'

const courseIcons = {
  html: FiCode,
  css: FiLayout,
  javascript: FiZap,
  react: FiLayers,
  redux: FiRepeat,
  python: FiTerminal,
  fastapi: FiActivity,
  nodejs: FiServer,
  express: FiServer,
  database: FiDatabase,
  sql: FiDatabase,
  'git-github': FiGitBranch,
  'ai-ml': FiCpu,
}

export const getCourseIcon = (slug) => courseIcons[slug] || FiBookOpen

export const courseIconContainerClass =
  'flex shrink-0 items-center justify-center rounded-xl bg-primary-100 text-primary-700 ring-1 ring-primary-200/80 dark:bg-primary-900/60 dark:text-primary-200 dark:ring-primary-700/50'
