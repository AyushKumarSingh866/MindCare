import { useState, useEffect } from 'react';
import { getHistory, getStats } from '../services/api';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { format } from 'date-fns';

export default function Dashboard() {
  const [history, setHistory] = useState([]);
  const [stats, setStats] = useState([]);

  useEffect(() => {
    getHistory().then(res => setHistory(res.data));
    getStats().then(res => {
      const formattedStats = Object.keys(res.data).map(key => ({
        name: key,
        count: res.data[key]
      }));
      setStats(formattedStats);
    });
  }, []);

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold text-gray-900">Your Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <h2 className="text-xl font-semibold mb-6 text-gray-800">Emotional Distribution</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={stats}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
                <XAxis dataKey="name" axisLine={false} tickLine={false} />
                <YAxis axisLine={false} tickLine={false} />
                <Tooltip cursor={{fill: '#f3f4f6'}} />
                <Bar dataKey="count" fill="#3b82f6" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
        
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 overflow-hidden flex flex-col">
          <h2 className="text-xl font-semibold mb-6 text-gray-800">Recent Logs</h2>
          <div className="overflow-y-auto flex-grow pr-2 space-y-4">
            {history.map(item => (
              <div key={item._id} className="p-4 rounded-xl bg-gray-50 border border-gray-100">
                <div className="flex justify-between items-start mb-2">
                  <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                    item.predicted_class === 'Suicidal' ? 'bg-danger-light text-danger' :
                    item.predicted_class === 'Depression' ? 'bg-purple-100 text-purple-700' :
                    item.predicted_class === 'Anxiety' ? 'bg-yellow-100 text-yellow-700' :
                    'bg-green-100 text-green-700'
                  }`}>
                    {item.predicted_class}
                  </span>
                  <span className="text-xs text-gray-500">
                    {format(new Date(item.created_at), 'MMM d, yyyy h:mm a')}
                  </span>
                </div>
                <p className="text-sm text-gray-700 line-clamp-2">{item.input_text}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
