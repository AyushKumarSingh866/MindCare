import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

export default function Home() {
  return (
    <div className="min-h-[80vh] flex flex-col justify-center items-center text-center px-4">
      <motion.h1 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-5xl md:text-7xl font-extrabold text-gray-900 mb-6 tracking-tight"
      >
        Understand your <span className="text-brand">mind</span>.
      </motion.h1>
      
      <motion.p 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="text-xl md:text-2xl text-gray-600 mb-10 max-w-2xl"
      >
        AI-powered mental health prediction system that helps you track and understand your emotional well-being safely and securely.
      </motion.p>
      
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="flex space-x-4"
      >
        <Link 
          to="/register" 
          className="px-8 py-4 bg-brand text-white rounded-xl font-semibold text-lg shadow-lg hover:bg-brand-dark transition-colors"
        >
          Start Your Journey
        </Link>
        <Link 
          to="/login" 
          className="px-8 py-4 bg-white text-gray-700 border border-gray-200 rounded-xl font-semibold text-lg shadow-sm hover:bg-gray-50 transition-colors"
        >
          Sign In
        </Link>
      </motion.div>

      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.8 }}
        className="mt-16 text-sm text-gray-500"
      >
        Disclaimer: This system is not a substitute for professional medical diagnosis.
      </motion.p>
    </div>
  );
}
