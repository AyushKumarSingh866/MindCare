/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          light: '#e0f2fe', // light blue
          DEFAULT: '#3b82f6', // blue
          dark: '#1e3a8a', // dark blue
        },
        accent: {
          DEFAULT: '#10b981', // green
        },
        danger: {
          light: '#fee2e2',
          DEFAULT: '#ef4444',
        }
      }
    },
  },
  plugins: [],
}
