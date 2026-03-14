
import React from 'react';

interface SettingsProps {
  onBack: () => void;
  onLogout: () => void;
}

const Settings: React.FC<SettingsProps> = ({ onBack, onLogout }) => {
  const options = [
    { title: 'Account', icon: '👤', desc: 'Security, change number' },
    { title: 'Privacy', icon: '🔒', desc: 'Block list, disappearing messages' },
    { title: 'Chats', icon: '💬', desc: 'Theme, wallpapers, history' },
    { title: 'Notifications', icon: '🔔', desc: 'Message, group & call tones' },
    { title: 'Storage and data', icon: '📊', desc: 'Network usage, auto-download' },
    { title: 'Help', icon: '❓', desc: 'Help center, contact us' },
  ];

  return (
    <div className="flex flex-col h-full bg-[#111b21] animate-in slide-in-from-left duration-200">
      <div className="h-[108px] bg-[#202c33] flex items-end px-6 pb-4 gap-6 text-[#e9edef] border-b border-[#222d34]">
        <button onClick={onBack} className="mb-1 hover:bg-[#2a3942] rounded-full p-2 transition text-[#ff3b30]">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg>
        </button>
        <h2 className="text-xl font-medium">Settings</h2>
      </div>

      <div className="flex-1 overflow-y-auto no-scrollbar">
        <div className="p-4 flex items-center gap-4 cursor-pointer hover:bg-[#202c33] transition-colors">
          <div className="w-20 h-20 bg-black border border-[#ff3b30]/20 rounded-full flex items-center justify-center text-3xl overflow-hidden shadow-lg">
             <img src="https://picsum.photos/200" alt="Avatar" className="object-cover w-full h-full opacity-80" />
          </div>
          <div>
            <h3 className="text-[#e9edef] text-lg">Your Profile</h3>
            <p className="text-[#8696a0] text-sm">Available</p>
          </div>
        </div>

        <div className="mt-4">
          {options.map((opt, i) => (
            <div key={i} className="flex items-center px-6 py-4 gap-6 cursor-pointer hover:bg-[#202c33] transition-colors group">
              <span className="text-2xl text-[#8696a0] group-hover:text-[#ff3b30] transition-colors">{opt.icon}</span>
              <div className="flex-1 border-b border-[#222d34] pb-4">
                <h4 className="text-[#e9edef] text-base font-normal">{opt.title}</h4>
                <p className="text-[#8696a0] text-sm">{opt.desc}</p>
              </div>
            </div>
          ))}
        </div>

        <button 
          onClick={onLogout}
          className="w-full text-left px-12 py-6 text-[#ff3b30] hover:bg-[#202c33] transition-colors border-t border-[#222d34] font-medium"
        >
          Logout of Jchat
        </button>
      </div>
    </div>
  );
};

export default Settings;
