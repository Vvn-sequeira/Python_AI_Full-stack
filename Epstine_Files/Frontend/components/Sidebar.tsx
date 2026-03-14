
import React, { useState, useMemo } from 'react';
import { User, Chat } from '../types';

interface SidebarProps {
  user: User;
  chats: Chat[];
  activeChatId: string | null;
  onSelectChat: (id: string) => void;
  onOpenProfile: () => void;
  onOpenSettings: () => void;
  onLogout: () => void;
  onViewProfile: (user: User) => void;
}

const Sidebar: React.FC<SidebarProps> = ({ 
  user, 
  chats, 
  activeChatId, 
  onSelectChat, 
  onOpenProfile, 
  onOpenSettings, 
  onLogout,
  onViewProfile
}) => {
  const [filter, setFilter] = useState<'all' | 'unread' | 'fav' | 'groups'>('all');
  const [searchQuery, setSearchQuery] = useState('');

  const filteredChats = useMemo(() => {
    let result = [...chats];
    if (searchQuery.trim()) {
      result = result.filter(chat => chat.user.name.toLowerCase().includes(searchQuery.toLowerCase()));
    }
    if (filter === 'unread') result = result.filter(c => c.unreadCount > 0);
    return result;
  }, [chats, searchQuery, filter]);

  return (
    <div className="flex h-full w-full">
      <div className="hidden sm:flex w-[60px] bg-[#111b21] flex-col items-center py-4 justify-between border-r border-[#222d34]">
        <div className="flex flex-col gap-4 items-center">
          <div className="w-10 h-10 bg-black border border-[#ff3b30]/20 rounded-full flex items-center justify-center mb-2">
            <span className="j-logo text-xl italic select-none">J</span>
          </div>
          <button className="text-[#ff3b30] hover:bg-[#202c33] p-2 rounded-lg transition"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 1.821.487 3.53 1.338 5L2 22l5-1.338C8.47 21.513 10.179 22 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"></path></svg></button>
          <button className="text-[#8696a0] hover:bg-[#202c33] p-2 rounded-lg transition"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M20 15.5c-1.25 0-2.45-.2-3.57-.57a1.02 1.02 0 0 0-1.02.24l-2.2 2.2a15.045 15.045 0 0 1-6.59-6.59l2.2-2.2c.28-.28.36-.67.25-1.02C8.7 6.45 8.5 5.25 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1z"></path></svg></button>
        </div>
        <div className="flex flex-col gap-4 items-center mb-2">
          <button onClick={onOpenSettings} className="text-[#8696a0] hover:bg-[#202c33] p-2 rounded-lg transition"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M19.43 12.98c.04-.32.07-.64.07-.98s-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46 2.18 14.25 2 14 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.23-.09-.49 0-.61.22l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.12.22.39.3.61.22l2.49-1c.52.40 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.23.09.49 0 .61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5 3.5 1.57 3.5 3.5-1.57 3.5-3.5 3.5z"></path></svg></button>
          <img onClick={onOpenProfile} src={user.avatar} className="w-8 h-8 rounded-full cursor-pointer border border-[#ff3b30]/10" alt="P" />
        </div>
      </div>

      <div className="flex-1 min-w-0 bg-[#111b21] flex flex-col h-full w-full md:w-[410px]">
        <div className="px-4 pt-5 pb-3 flex justify-between items-center shrink-0">
          <h1 className="text-[#e9edef] text-xl font-bold">Chats</h1>
          <div className="flex items-center gap-2 sm:hidden">
             <img onClick={onOpenProfile} src={user.avatar} className="w-8 h-8 rounded-full" alt="P" />
             <button onClick={onOpenSettings} className="text-[#8696a0] p-2"><svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 7a2 2 0 1 0-.001 4.001A2 2 0 0 0 12 7zm0 10a2 2 0 1 0-.001 4.001A2 2 0 0 0 12 17zm0-5a2 2 0 1 0-.001 4.001A2 2 0 0 0 12 12z"></path></svg></button>
          </div>
        </div>

        <div className="px-3 pb-2 space-y-3 shrink-0">
          <div className="bg-[#202c33] flex items-center px-4 py-1.5 rounded-lg">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="#8696a0" className="shrink-0"><path d="M15.009 13.805h-.636l-.22-.219a5.184 5.184 0 0 0 1.256-3.386 5.2 5.2 0 1 0-5.2 5.2 5.183 5.183 0 0 0 3.386-1.256l.219.22v.636l4.026 4.01 1.2-1.2-4.031-4.005zm-5.805 0a3.6 3.6 0 1 1 0-7.2 3.6 3.6 0 0 1 0 7.2z"></path></svg>
            <input type="text" placeholder="Search or start a new chat" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} className="bg-transparent border-none w-full ml-4 text-[#d1d7db] text-[14px] focus:outline-none placeholder:text-[#8696a0]" />
          </div>
          <div className="flex gap-2 overflow-x-auto no-scrollbar pb-1">
            {['all', 'unread', 'groups'].map(id => (
              <button key={id} onClick={() => setFilter(id as any)} className={`px-3 py-1.5 rounded-full text-[13px] whitespace-nowrap transition-colors ${filter === id ? 'bg-[#ff3b30] bg-opacity-20 text-[#ff3b30]' : 'bg-[#202c33] text-[#8696a0]'}`}>
                {id.charAt(0).toUpperCase() + id.slice(1)}
              </button>
            ))}
          </div>
        </div>

        <div className="flex-1 overflow-y-auto">
          {filteredChats.map(chat => (
            <div key={chat.id} onClick={() => onSelectChat(chat.id)} className={`flex items-center px-4 py-3 cursor-pointer border-b border-[#222d34]/50 ${activeChatId === chat.id ? 'bg-[#2a3942]' : 'hover:bg-[#202c33]'}`}>
              <img src={chat.user.avatar} onClick={(e) => { e.stopPropagation(); onViewProfile(chat.user); }} className="w-12 h-12 rounded-full mr-3 shrink-0 border border-[#ff3b30]/5" alt="A" />
              <div className="flex-1 min-w-0">
                <div className="flex justify-between items-baseline mb-0.5">
                  <h3 className="text-[#e9edef] text-base truncate pr-2">{chat.user.name}</h3>
                  <span className="text-[11px] shrink-0 text-[#8696a0]">{chat.timestamp}</span>
                </div>
                <div className="flex justify-between items-center">
                  <p className="text-[13px] text-[#8696a0] truncate">{chat.lastMessage || chat.user.status}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
