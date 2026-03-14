
import React, { useState } from 'react';
import { User } from '../types';

interface LoginProps {
  onLogin: (user: User) => void;
  onSwitch: () => void;
}

const Login: React.FC<LoginProps> = ({ onLogin, onSwitch }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!username.trim() || !email.trim() || !password.trim()) {
      setError('All fields are required');
      return;
    }
    
    setLoading(true);
    setError(null);

    const loginData = {
      user_name: username,
      email: email,
      password: password
    };

    try {
      const apiUrl = import.meta.env.VITE_API_URL;
      const response = await fetch(`${apiUrl}api/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: "include",
        body: JSON.stringify(loginData),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Login failed');
      }

      const data = await response.json();
      
      onLogin({
        id: data.id || Math.random().toString(36).substr(2, 9),
        name: username,
        avatar: `https://picsum.photos/seed/${username}/200`,
        status: "Available"
      });
    } catch (err: any) {
      console.error('Login error:', err);
      setError(err.message || 'An error occurred during login');
      
      // For demo purposes, if the local API is not running, we still allow "logging in" in the UI
      // if (err.message.includes('Failed to fetch')) {
      //   console.warn('Backend API not reachable. Proceeding with local mock for demo.');
      //   onLogin({
      //     id: Math.random().toString(36).substr(2, 9),
      //     name: username,
      //     avatar: `https://picsum.photos/seed/${username}/200`,
      //     status: "Available"
      //   });
      // }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-full bg-[#0b141a] relative">
      <div className="absolute top-0 w-full h-56 bg-black z-0 border-b border-[#222d34]"></div>
      
      <div className="z-10 bg-[#111b21] p-8 rounded-lg shadow-2xl w-full max-w-md border border-[#222d34]">
        <div className="flex items-center gap-3 mb-8">
          <div className="w-12 h-12 bg-black border border-[#ff3b30]/30 rounded-full flex items-center justify-center shadow-lg">
            <span className="j-logo text-3xl italic">J</span>
          </div>
          <h1 className="text-2xl font-bold text-white uppercase tracking-wider">Jchat Login</h1>
        </div>
        
        {error && (
          <div className="mb-4 p-3 bg-red-500/20 border border-red-500/50 text-red-500 text-sm rounded">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-[#8696a0] text-sm mb-1">Username</label>
            <input 
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username"
              required
              className="w-full bg-[#2a3942] border-none text-[#d1d7db] p-3 rounded-md focus:ring-2 focus:ring-[#ff3b30] outline-none"
            />
          </div>
          <div>
            <label className="block text-[#8696a0] text-sm mb-1">Email Address</label>
            <input 
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="john@example.com"
              required
              className="w-full bg-[#2a3942] border-none text-[#d1d7db] p-3 rounded-md focus:ring-2 focus:ring-[#ff3b30] outline-none"
            />
          </div>
          <div>
            <label className="block text-[#8696a0] text-sm mb-1">Password</label>
            <input 
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
              className="w-full bg-[#2a3942] border-none text-[#d1d7db] p-3 rounded-md focus:ring-2 focus:ring-[#ff3b30] outline-none"
            />
          </div>
          <button 
            type="submit"
            disabled={loading}
            className={`w-full bg-[#ff3b30] hover:bg-[#e0352b] text-white font-bold py-3 rounded-md transition-colors duration-200 uppercase tracking-widest shadow-lg ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            {loading ? 'Signing In...' : 'Sign In'}
          </button>
        </form>
        
        <p className="mt-8 text-center text-[#8696a0] text-sm">
          New to Jchat? 
          <button onClick={onSwitch} className="ml-1 text-[#ff3b30] hover:underline">Register now</button>
        </p>
      </div>
    </div>
  );
};

export default Login;
