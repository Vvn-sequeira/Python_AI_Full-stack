
import React, { useState, useEffect } from 'react';
import { User, Chat, Message } from '../types';
import Sidebar from './Sidebar';
import ChatWindow from './ChatWindow';
import Settings from './Settings';
import Profile from './Profile';
import ContactInfo from './ContactInfo';
import { geminiService } from '../geminiService';

interface ChatMainProps {
  user: User;
  onLogout: () => void;
}

const INITIAL_CHATS: Chat[] = [
  {
    id: '1',
    user: { id: 'user1', name: 'Jeffery Epstein', avatar: 'https://picsum.photos/seed/jeff/200', status: 'Online' },
    unreadCount: 0,
    timestamp: '7:41 pm',
    messages: []
  },
  {
    id: '2',
    user: { id: 'user2', name: 'Ayatollah Khamenei', avatar: 'https://picsum.photos/seed/kham/200', status: 'Available' },
    unreadCount: 2,
    timestamp: '2:27 pm',
    messages: []
  },
  {
    id: '3',
    user: { id: 'user3', name: 'Giuffre v. Maxwell, Case', avatar: 'https://picsum.photos/seed/case/200', status: 'Busy' },
    unreadCount: 0,
    timestamp: '9:16 pm',
    messages: []
  }
];

const ChatMain: React.FC<ChatMainProps> = ({ user, onLogout }) => {
  const [chats, setChats] = useState<Chat[]>(INITIAL_CHATS);
  const [activeChatId, setActiveChatId] = useState<string | null>(null);
  const [sidebarView, setSidebarView] = useState<'chats' | 'settings' | 'profile' | 'contactInfo'>('chats');
  const [viewingUser, setViewingUser] = useState<User | null>(null);

  const activeChat = chats.find(c => c.id === activeChatId);
  const isDetailActive = !!activeChatId || sidebarView !== 'chats';

  const handleSelectChat = (id: string) => {
    setActiveChatId(id);
    setSidebarView('chats');
  };

  const handleViewProfile = (userToView: User) => {
    setViewingUser(userToView);
    setSidebarView('contactInfo');
  };

  const handleBackToChats = () => {
    setActiveChatId(null);
    setSidebarView('chats');
  };

  const sendMessage = async (text: string) => {
    if (!activeChatId) return;
    const newMessage: Message = { id: Date.now().toString(), senderId: user.id, text, timestamp: new Date(), status: 'sent' };
    setChats(prev => prev.map(chat => chat.id === activeChatId ? { ...chat, messages: [...chat.messages, newMessage], lastMessage: text, timestamp: 'Just now' } : chat));
    
    if (activeChat?.user.id === 'gemini') {
      const history = activeChat.messages.map(m => ({ role: m.senderId === user.id ? 'user' as const : 'model' as const, parts: [{ text: m.text }] }));
      const aiResponseText = await geminiService.getChatResponse(text, history);
      const aiMessage: Message = { id: (Date.now() + 1).toString(), senderId: 'gemini', text: aiResponseText, timestamp: new Date(), status: 'read' };
      setChats(prev => prev.map(chat => chat.id === activeChatId ? { ...chat, messages: [...chat.messages, aiMessage], lastMessage: aiResponseText, timestamp: 'Just now' } : chat));
    }
  };

  return (
    <div className="flex h-full w-full bg-[#111b21] overflow-hidden">
      <div className={`h-full border-r border-[#222d34] flex-shrink-0 transition-all duration-300 ${isDetailActive ? 'hidden md:flex' : 'flex w-full md:w-auto'}`}>
        <Sidebar 
          user={user} 
          chats={chats} 
          activeChatId={activeChatId} 
          onSelectChat = {handleSelectChat}
          onOpenProfile={() => setSidebarView('profile')}
          onOpenSettings={() => setSidebarView('settings')}
          onLogout={onLogout}
          onViewProfile={handleViewProfile}
        />
      </div>

      <div className={`flex-1 flex flex-col h-full bg-[#0b141a] transition-all duration-300 ${!isDetailActive ? 'hidden md:flex' : 'flex w-full'}`}>
        {sidebarView === 'settings' ? (
          <Settings onBack={handleBackToChats} onLogout={onLogout} />
        ) : sidebarView === 'profile' ? (
          <Profile user={user} onBack={handleBackToChats} />
        ) : sidebarView === 'contactInfo' && viewingUser ? (
          <ContactInfo user={viewingUser} onBack={() => setSidebarView(activeChatId ? 'chats' : 'chats')} />
        ) : activeChat ? (
          <ChatWindow 
            chat={activeChat} 
            onSendMessage={sendMessage} 
            currentUserId={user.id}
            onViewProfile={handleViewProfile}
            onBack={handleBackToChats}
          />
        ) : (
          <div className="hidden md:flex flex-1 flex-col items-center justify-center p-12 text-center bg-[#111b21]">
             <div className="w-24 h-24 bg-black border border-[#ff3b30]/20 rounded-full flex items-center justify-center mb-6 shadow-2xl">
               <span className="j-logo text-6xl italic">J</span>
             </div>
             <h1 className="text-3xl font-light text-[#e9edef] mb-3 tracking-wide">Jchat for Web</h1>
             <p className="text-[#8696a0] max-w-sm text-sm leading-relaxed">
               Securely connected to your private network.
             </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ChatMain;
