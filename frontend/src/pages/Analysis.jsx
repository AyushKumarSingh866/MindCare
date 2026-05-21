import { useState } from 'react';
import { predict } from '../services/api';
import { motion } from 'framer-motion';
import { AlertTriangle, Info } from 'lucide-react';

export default function Analysis() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    
    setLoading(true);
    try {
      const res = await predict(text);
      setResult(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-8 text-center">How are you feeling today?</h1>
      
      <form onSubmit={handleAnalyze} className="mb-10">
        <textarea
          className="w-full h-40 p-5 rounded-2xl border border-gray-200 shadow-sm focus:border-brand focus:ring-brand resize-none text-lg transition-all"
          placeholder="Share your thoughts, feelings, or what's been on your mind lately..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <div className="mt-4 flex justify-end">
          <button
            type="submit"
            disabled={loading || !text.trim()}
            className="px-8 py-3 bg-brand text-white rounded-xl font-semibold shadow-sm hover:bg-brand-dark focus:outline-none focus:ring-2 focus:ring-brand focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>
      </form>

      {result && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className={`p-8 rounded-3xl border shadow-lg ${
            result.is_emergency ? 'bg-danger-light border-danger text-danger' : 'bg-white border-gray-100'
          }`}
        >
          {result.is_emergency && (
            <div className="flex items-center space-x-3 mb-6">
              <AlertTriangle className="h-8 w-8" />
              <h2 className="text-2xl font-bold">Emergency Alert</h2>
            </div>
          )}
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
            <div>
              <h3 className="text-sm uppercase tracking-wider font-semibold text-gray-500 mb-2">Detected State</h3>
              <p className={`text-4xl font-bold ${result.is_emergency ? 'text-danger' : 'text-gray-900'}`}>
                {result.predicted_class}
              </p>
              <p className="text-gray-500 mt-2">Confidence: {(result.confidence * 100).toFixed(1)}%</p>
            </div>
            
            <div>
              <h3 className="text-sm uppercase tracking-wider font-semibold text-gray-500 mb-4">Recommendations</h3>
              <ul className="space-y-3">
                {result.recommendations.map((rec, i) => (
                  <li key={i} className="flex items-start space-x-3">
                    <Info className={`h-5 w-5 mt-0.5 ${result.is_emergency ? 'text-danger' : 'text-brand'}`} />
                    <span className={result.is_emergency ? 'font-semibold text-danger' : 'text-gray-700'}>{rec}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {result.is_emergency && (
            <div className="mt-8 p-6 bg-white rounded-2xl border border-danger">
              <h4 className="text-xl font-bold text-gray-900 mb-4">Immediate Help Available 24/7</h4>
              <p className="text-gray-700 font-medium mb-2">National Suicide Prevention Lifeline: <a href="tel:988" className="text-brand hover:underline text-xl ml-2">988</a></p>
              <p className="text-gray-700 font-medium">Crisis Text Line: <span className="text-brand text-xl ml-2">Text HOME to 741741</span></p>
            </div>
          )}
        </motion.div>
      )}
    </div>
  );
}
