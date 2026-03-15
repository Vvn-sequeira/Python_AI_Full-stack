
import React, { useState } from 'react';
import { User } from '../types';
import FloatingNames from './FloatingNames';

interface LoginProps {
  onLogin: (user: User) => void;
  onSwitch: () => void;
  redirected?: boolean;
}

const Login: React.FC<LoginProps> = ({ onLogin, onSwitch, redirected = false }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showCookieBanner, setShowCookieBanner] = useState(redirected);

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
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
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
        status: 'Available'
      });
    } catch (err: any) {
      console.error('Login error:', err);
      setError(err.message || 'An error occurred during login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-full bg-[#0b141a] relative">
      <div className="absolute top-0 w-full h-56 bg-black z-0 border-b border-[#222d34]"></div>

      {/* Floating names background */}
      <FloatingNames />
      {/* Cookie warning banner — shown only when redirected due to auth failure */}
      {showCookieBanner && (
        <div className="z-20 fixed top-0 left-0 w-full px-4 py-3 bg-amber-500/95 backdrop-blur-sm flex items-start gap-3 shadow-xl border-b border-amber-400/60">
          <svg className="shrink-0 mt-0.5" viewBox="0 0 24 24" width="20" height="20" fill="#1c1700">
            <path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/>
          </svg>
          <div className="flex-1 text-[#1c1700] text-sm leading-snug">
            <span className="font-bold">You were redirected.</span>{' '}
            The reason is that your browser is not storing the cookies properly.{' '}
            Please <span className="font-semibold">allow third-party cookies</span> in your browser settings and try logging in again.
            <span className="block mt-1 text-xs opacity-75">
              Chrome: Settings → Privacy → Cookies → Allow all cookies &nbsp;|&nbsp;
              Firefox: Settings → Privacy → Custom → uncheck "Cookies from unvisited sites"
            </span>
          </div>
          <button
            onClick={() => setShowCookieBanner(false)}
            className="shrink-0 text-[#1c1700] hover:text-black transition-colors mt-0.5"
            title="Dismiss"
          >
            <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
            </svg>
          </button>
        </div>
      )}

      <div className={`z-10 bg-[#111b21] p-8 rounded-lg shadow-2xl w-full max-w-md border border-[#222d34] ${showCookieBanner ? 'mt-20' : ''}`}>
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
