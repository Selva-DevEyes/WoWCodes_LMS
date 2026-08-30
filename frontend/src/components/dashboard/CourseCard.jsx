import { Link } from 'react-router-dom'
import { FiArrowRight } from 'react-icons/fi'
import { courseIconContainerClass, getCourseIcon } from '../../utils/helpers/courseIcons'

const CourseCard = ({ course }) => {
  const CourseIcon = getCourseIcon(course.slug)

  return (
    <Link
      to={`/learn/course/${course.id}`}
      className="card hover:shadow-lg transition-shadow group"
    >
      <div className="flex items-center justify-between mb-4">
        <div className={`h-12 w-12 ${courseIconContainerClass}`}>
          <CourseIcon className="text-2xl" aria-hidden="true" />
        </div>
        <span className="text-xs px-2 py-1 rounded-full bg-gray-100 dark:bg-gray-700">
          {course.level}
        </span>
      </div>
      <h3 className="font-semibold text-lg mb-2">{course.title}</h3>
      <p className="text-sm text-gray-500 dark:text-gray-400 line-clamp-2 mb-4">
        {course.description}
      </p>
      <div className="flex items-center justify-between text-sm">
        <span className="text-gray-500">{course.category}</span>
        <FiArrowRight className="group-hover:translate-x-1 transition-transform" />
      </div>
    </Link>
  )
}

export default CourseCard
