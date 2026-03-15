
import React, { useState } from 'react';
import { User } from '../types';
import FloatingNames from './FloatingNames';


interface RegisterProps {
  onRegister: (user: User) => void;
  onSwitch: () => void;
}

const Register: React.FC<RegisterProps> = ({ onRegister, onSwitch }) => {
  
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNo, setPhoneNo] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => { 
    e.preventDefault();
    
   
    if (!username.trim() || !email.trim() || !phoneNo.trim() || !password.trim()) {
      setError('All fields are required');
      return;
    }
    
    setLoading(true);
    setError(null);

    const signupData = {
      user_name: username,
      email: email,
      phoneNo: phoneNo,
      password: password,
      token: 4
    };

try {
  const apiUrl = import.meta.env.VITE_API_URL;

  const response = await fetch(`${apiUrl}api/auth/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include", // allow cookies
    body: JSON.stringify(signupData),
  });

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Signup failed');
      }

      const data = await response.json();
      
      // Assuming the API returns the user object or we use the data we sent
      onRegister({
        id: data.id || Math.random().toString(36).substr(2, 9),
        name: username,
        avatar: `https://picsum.photos/seed/${username}/200`,
        status: "Available"
      });

  console.log(response)
} catch (err: any) {
  console.error("Signup error:", err);
  setError(err.message || "An error occurred during signup");
} finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-full bg-[#0b141a] relative">
      <div className="absolute top-0 w-full h-56 bg-black z-0 border-b border-[#222d34]"></div>

      {/* Floating names background */}
      <FloatingNames />
      <div className="z-10 bg-[#111b21] p-8 rounded-lg shadow-2xl w-full max-w-md border border-[#222d34]">
        <div className="flex items-center gap-3 mb-8">
          <div className="w-12 h-12 bg-black border border-[#ff3b30]/30 rounded-full flex items-center justify-center shadow-lg">
            <span className="j-logo text-3xl italic">J</span>
          </div>
          <h1 className="text-2xl font-bold text-white uppercase tracking-wider">Jchat Join</h1>
        </div>
        
        {error && (
          <div className="mb-4 p-3 bg-red-500/20 border border-red-500/50 text-red-500 text-sm rounded">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-[#8696a0] text-sm mb-1">Display Name</label>
            <input 
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="e.g. John Doe"
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
            <label className="block text-[#8696a0] text-sm mb-1">Phone Number</label>
            <input 
              type="text"
              value={phoneNo}
              onChange={(e) => setPhoneNo(e.target.value)}
              placeholder="+1234567890"
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
              placeholder="Create a strong password"
              required
              className="w-full bg-[#2a3942] border-none text-[#d1d7db] p-3 rounded-md focus:ring-2 focus:ring-[#ff3b30] outline-none"
            />
          </div>
          <button 
            type="submit"
            disabled={loading}
            className={`w-full bg-[#ff3b30] hover:bg-[#e0352b] text-white font-bold py-3 rounded-md transition-colors duration-200 uppercase tracking-widest shadow-lg ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            {loading ? 'Creating...' : 'Create Account'}
          </button>
        </form>
        
        <p className="mt-8 text-center text-[#8696a0] text-sm">
          Already a member? 
          <button onClick={onSwitch} className="ml-1 text-[#ff3b30] hover:underline">Log in</button>
        </p>
      </div>
    </div>
  );
};

export default Register;
