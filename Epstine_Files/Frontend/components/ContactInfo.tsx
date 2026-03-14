
import React from 'react';
import { User } from '../types';

interface ContactInfoProps {
  user: User;
  onBack: () => void;
}

const ContactInfo: React.FC<ContactInfoProps> = ({ user, onBack }) => {
  return (
    <div className="flex flex-col h-full bg-[#0b141a] animate-in slide-in-from-right duration-300">
      {/* Header */}
      <div className="h-[60px] bg-[#202c33] px-4 flex items-center gap-6 z-10 shrink-0 border-b border-[#222d34]">
        <button onClick={onBack} className="text-[#8696a0] hover:text-white transition p-2">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"></path></svg>
        </button>
        <span className="text-[#e9edef] text-[16px] font-medium">Contact info</span>
      </div>

      <div className="flex-1 overflow-y-auto no-scrollbar bg-[#0c1317]">
        {/* Profile Header Section */}
        <div className="bg-[#111b21] flex flex-col items-center py-7 mb-2 shadow-sm">
          <div className="w-52 h-52 rounded-full overflow-hidden mb-4 shadow-lg border-2 border-[#202c33]">
            <img src={user.avatar} alt={user.name} className="w-full h-full object-cover" />
          </div>
          <h2 className="text-[#e9edef] text-2xl font-normal mb-1">{user.name}</h2>
          <p className="text-[#8696a0] text-[16px]">+91 98765 43210</p>
        </div>

        {/* About Section */}
        <div className="bg-[#111b21] px-8 py-4 mb-2 shadow-sm">
          <label className="text-[#8696a0] text-sm mb-3 block">About</label>
          <p className="text-[#e9edef] text-[17px] leading-relaxed">{user.status}</p>
        </div>

        {/* Media, Links and Docs Section */}
        <div className="bg-[#111b21] px-8 py-4 mb-2 shadow-sm cursor-pointer hover:bg-[#202c33] transition-colors">
          <div className="flex justify-between items-center text-[#8696a0]">
            <span className="text-sm">Media, links and docs</span>
            <div className="flex items-center gap-1">
              <span className="text-sm">0</span>
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"></path></svg>
            </div>
          </div>
        </div>

        {/* Settings/Info Items */}
        <div className="bg-[#111b21] shadow-sm divide-y divide-[#222d34]">
          <div className="px-8 py-4 flex items-center gap-6 cursor-pointer hover:bg-[#202c33] transition-colors">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="#8696a0"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></svg>
            <div className="flex-1">
              <p className="text-[#e9edef] text-[16px]">Starred messages</p>
            </div>
            <svg viewBox="0 0 24 24" width="16" height="16" fill="#8696a0"><path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"></path></svg>
          </div>

          <div className="px-8 py-4 flex items-center gap-6 cursor-pointer hover:bg-[#202c33] transition-colors">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="#8696a0"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"></path></svg>
            <div className="flex-1">
              <p className="text-[#e9edef] text-[16px]">Mute notifications</p>
            </div>
            <div className="w-10 h-5 bg-[#3b4a54] rounded-full relative">
               <div className="absolute right-0.5 top-0.5 w-4 h-4 bg-[#8696a0] rounded-full shadow-sm"></div>
            </div>
          </div>

          <div className="px-8 py-4 flex items-center gap-6 cursor-pointer hover:bg-[#202c33] transition-colors">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="#8696a0"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-1 6h2v2h-2V7zm0 4h2v6h-2v-6z"></path></svg>
            <div className="flex-1">
              <p className="text-[#e9edef] text-[16px]">Encryption</p>
              <p className="text-[#8696a0] text-sm">Messages and calls are end-to-end encrypted. Click to verify.</p>
            </div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="mt-2 space-y-2 pb-10">
          <div className="bg-[#111b21] px-8 py-4 flex items-center gap-6 cursor-pointer hover:bg-[#202c33] transition-colors text-[#ea0038]">
             <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"></path></svg>
             <span className="text-[16px]">Block {user.name}</span>
          </div>
          <div className="bg-[#111b21] px-8 py-4 flex items-center gap-6 cursor-pointer hover:bg-[#202c33] transition-colors text-[#ea0038]">
             <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm5 13.59L15.59 17 12 13.41 8.41 17 7 15.59 10.59 12 7 8.41 8.41 7 12 10.59 15.59 7 17 8.41 13.41 12 17 15.59z"></path></svg>
             <span className="text-[16px]">Report {user.name}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContactInfo;
