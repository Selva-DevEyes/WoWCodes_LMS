/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f3f3ff',
          100: '#e6e5ff',
          200: '#cfcdff',
          300: '#afaaff',
          400: '#8b7cf6',
          500: '#6d5ce7',
          600: '#5946d4',
          700: '#4937b5',
          800: '#3c308f',
          900: '#30286f',
        },
        accent: {
          400: '#5eead4',
          500: '#2dd4bf',
          600: '#14b8a6',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in-out',
        'slide-in': 'slideIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideIn: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(0)' },
        },
      },
    },
  },
  plugins: [],
}
