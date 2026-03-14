
import React, { useState } from 'react';
import { User } from '../types';

interface ProfileProps {
  user: User;
  onBack: () => void;
}

const Profile: React.FC<ProfileProps> = ({ user, onBack }) => {
  const [name, setName] = useState(user.name);
  const [about, setAbout] = useState(user.status);

  return (
    <div className="flex flex-col h-full bg-[#111b21] animate-in slide-in-from-left duration-200">
      <div className="h-[108px] bg-[#202c33] flex items-end px-6 pb-4 gap-6 text-[#e9edef] border-b border-[#222d34]">
        <button onClick={onBack} className="mb-1 hover:bg-[#2a3942] rounded-full p-2 transition text-[#ff3b30]">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg>
        </button>
        <h2 className="text-xl font-medium">Profile</h2>
      </div>

      <div className="flex-1 overflow-y-auto no-scrollbar">
        <div className="py-8 flex flex-col items-center justify-center gap-4 group cursor-pointer relative">
          <div className="w-[200px] h-[200px] rounded-full overflow-hidden relative shadow-2xl border-4 border-[#ff3b30]/10">
            <img src={user.avatar} alt="Profile" className="w-full h-full object-cover" />
            <div className="absolute inset-0 bg-[#ff3b30]/40 flex flex-col items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
              <svg viewBox="0 0 24 24" width="24" height="24" fill="white"><path d="M12 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z"></path></svg>
              <span className="text-[10px] uppercase font-bold text-white mt-2">Change Profile Photo</span>
            </div>
          </div>
        </div>

        <div className="bg-[#111b21] px-8 py-6 mb-4 shadow-sm border-y border-[#222d34]">
          <label className="text-[#ff3b30] text-sm font-medium mb-4 block uppercase tracking-wide">Your Name</label>
          <div className="flex items-center justify-between group">
            <input 
              value={name} 
              onChange={(e) => setName(e.target.value)}
              className="bg-transparent text-[#e9edef] text-lg w-full border-b border-transparent focus:border-[#ff3b30] outline-none pb-1 transition-colors" 
            />
            <button className="text-[#8696a0] opacity-0 group-hover:opacity-100 transition-opacity">
               <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M3.95 16.7L4 16.71l.01.05.02.05c.1.28.31.52.57.65l.05.03.05.02.05.01h.02c.07.01.15.02.22.02.16 0 .32-.03.47-.1L7.3 16.8l2.8-2.8-3.7-3.7-2.8 2.8c-.1.1-.17.21-.22.33l-.01.02-.01.02a.82.82 0 0 0-.07.47v.03c.01.07.01.15.02.22l.64 2.5zm11.32-8.6l-3.7-3.7 1.3-1.3c.3-.3.8-.3 1.1 0l2.6 2.6c.3.3.3.8 0 1.1l-1.3 1.3z"></path></svg>
            </button>
          </div>
          <p className="text-[#8696a0] text-sm mt-6 leading-relaxed">
            This name will be visible to your Jchat contacts.
          </p>
        </div>

        <div className="bg-[#111b21] px-8 py-6 mb-8 shadow-sm border-y border-[#222d34]">
          <label className="text-[#ff3b30] text-sm font-medium mb-4 block uppercase tracking-wide">About</label>
          <div className="flex items-center justify-between group">
            <input 
              value={about} 
              onChange={(e) => setAbout(e.target.value)}
              className="bg-transparent text-[#e9edef] text-lg w-full border-b border-transparent focus:border-[#ff3b30] outline-none pb-1 transition-colors" 
            />
            <button className="text-[#8696a0] opacity-0 group-hover:opacity-100 transition-opacity">
               <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M3.95 16.7L4 16.71l.01.05.02.05c.1.28.31.52.57.65l.05.03.05.02.05.01h.02c.07.01.15.02.22.02.16 0 .32-.03.47-.1L7.3 16.8l2.8-2.8-3.7-3.7-2.8 2.8c-.1.1-.17.21-.22.33l-.01.02-.01.02a.82.82 0 0 0-.07.47v.03c.01.07.01.15.02.22l.64 2.5zm11.32-8.6l-3.7-3.7 1.3-1.3c.3-.3.8-.3 1.1 0l2.6 2.6c.3.3.3.8 0 1.1l-1.3 1.3z"></path></svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
