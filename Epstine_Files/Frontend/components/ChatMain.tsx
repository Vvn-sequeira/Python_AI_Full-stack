
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
  onUnauthorized: () => void;
}

const INITIAL_CHATS: Chat[] = [
  {
    id: '1',
    user: { id: 'user1', name: 'Jeffery Epstein', avatar: 'https://i.pinimg.com/1200x/0d/88/4e/0d884e6f9ad67c87e0affaea5918c4d8.jpg', status: 'Court Case' },
    unreadCount: 0,
    timestamp: '7:41 pm',
    messages: [],
    FileName: 'Epstine_Court_Questioning_FILE'
  },
  {
    id: '2',
    user: { id: 'user2', name: 'IRAN - SEXUAL HARASMMENT', avatar: 'https://i.pinimg.com/736x/a3/7e/0f/a37e0f0194b7bb6b5165ac2836ee340c.jpg', status: 'Eyewitness Report: Womens Rights in Iran' },
    unreadCount: 2,
    timestamp: '2:27 pm',
    messages: [],
    FileName: 'Sexual_Harasment_in_Iran'
  },
  {
    id: '3',
    user: { id: 'user3', name: 'IRAN - PDFilliya', avatar: 'https://i.pinimg.com/736x/46/e7/7e/46e77e64a2209fa09a48a5af8d141078.jpg', status: 'Child Marriage in Iran ' },
    unreadCount: 0,
    timestamp: '9:16 pm',
    messages: [],
    FileName: 'PDF_Iran'
  }
];

const ChatMain: React.FC<ChatMainProps> = ({ user, onLogout, onUnauthorized }) => {
  const [chats, setChats] = useState<Chat[]>(INITIAL_CHATS);
  const [activeChatId, setActiveChatId] = useState<string | null>(null);
  const [sidebarView, setSidebarView] = useState<'chats' | 'settings' | 'profile' | 'contactInfo'>('chats');
  const [viewingUser, setViewingUser] = useState<User | null>(null);

  // Central 401 guard — any API returning 401 kicks user to login
  const guardResponse = (response: Response): void => {
    if (response.status === 401 || response.status === 403) {
      onUnauthorized();
    }
  };

  const activeChat = chats.find(c => c.id === activeChatId);
  const isDetailActive = !!activeChatId || sidebarView !== 'chats';

  const fetchChatMessages = async (chatToFetch: Chat) => {
    if (!chatToFetch.FileName) return;

    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}api/view`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ receiver_name: chatToFetch.FileName }),
      });

      if (!response.ok) {
        guardResponse(response);
        throw new Error(`Error: ${response.status}`);
      }

      const data = await response.json();
      console.log(data);
      const newMessages: Message[] = [];
      let messageIdCounter = 1;

      if (data.res === null || data.res === undefined) {
        // null res means no conversation yet — show "Start the conversation"
        setChats(prev => prev.map(chat => chat.id === chatToFetch.id ? { ...chat, messages: [] } : chat));
        return;
      }

      if (Array.isArray(data.res)) {
        data.res.forEach((item: any) => {
          if (item.user) {
            newMessages.push({
              id: `api_${messageIdCounter++}`,
              senderId: user.id,
              text: item.user,
              timestamp: new Date(),
              status: 'read'
            });
          }
          if (item.RAG) {
            newMessages.push({
              id: `api_${messageIdCounter++}`,
              senderId: 'ai',
              text: item.RAG,
              timestamp: new Date(),
              status: 'read'
            });
          }
        });
      } else {
        throw new Error("Invalid response format: 'res' is not an array");
      }

      setChats(prev => prev.map(chat => chat.id === chatToFetch.id ? { ...chat, messages: newMessages } : chat));

    } catch (error: any) {
      console.error('Failed to fetch messages:', error);
      // TypeError = browser blocked the request (CORS on 401) — treat as unauthorized
      if (error instanceof TypeError) {
        console.warn('🔒 Network/CORS error on /api/view — session likely expired');
        onUnauthorized();
        return;
      }
      const errorMessage: Message = {
        id: `error_${Date.now()}`,
        senderId: 'system',
        text: `Failed to load messages: ${error.message}`,
        timestamp: new Date(),
        status: 'read'
      };
      setChats(prev => prev.map(chat => chat.id === chatToFetch.id ? { ...chat, messages: [errorMessage] } : chat));
    }
  };

  const handleSelectChat = (id: string) => {
    setActiveChatId(id);
    setSidebarView('chats');
    const selectedChat = chats.find(c => c.id === id);
    if (selectedChat) {
      fetchChatMessages(selectedChat);
    }
  };

  const handleViewProfile = (userToView: User) => {
    setViewingUser(userToView);
    setSidebarView('contactInfo');
  };

  const handleBackToChats = () => {
    setActiveChatId(null);
    setSidebarView('chats');
  };

  const [isSending, setIsSending] = useState(false);

  const sendMessage = async (text: string) => {
    if (!activeChatId || !activeChat || isSending) return;

    // 1. Immediately show the user's message
    const userMessage: Message = {
      id: Date.now().toString(),
      senderId: user.id,
      text,
      timestamp: new Date(),
      status: 'sent'
    };
    setChats(prev => prev.map(chat =>
      chat.id === activeChatId
        ? { ...chat, messages: [...chat.messages, userMessage], lastMessage: text, timestamp: 'Just now' }
        : chat
    ));

    // 2. Lock the send button
    setIsSending(true);

    try {
      const payload = {
        user_id: user.id,
        sender_name: user.name,
        receiver_name: activeChat.FileName ?? '',
        message: [{ user: text, RAG: '' }]
      };
      console.log('📤 Sending to /api/Chat:', JSON.stringify(payload, null, 2));

      const response = await fetch(`${import.meta.env.VITE_API_URL}api/Chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        guardResponse(response);
        const errBody = await response.text();
        console.error(`❌ /api/Chat returned ${response.status}:`, errBody);
        throw new Error(`Error: ${response.status} — ${errBody}`);
      }

      const data = await response.json();
      console.log('📥 Received from /api/Chat:', data);
      const fullText: string = data ?? 'Try Again Later !!';

      // 3. Add a streaming placeholder message
      const aiMsgId = `ai_${Date.now()}`;
      const aiMessage: Message = {
        id: aiMsgId,
        senderId: 'ai',
        text: '',
        timestamp: new Date(),
        status: 'read',
        isStreaming: true
      };
      setChats(prev => prev.map(chat =>
        chat.id === activeChatId
          ? { ...chat, messages: [...chat.messages, aiMessage] }
          : chat
      ));

      // 4. Word-by-word typing animation
      const words = fullText.split(' ');
      let wordIndex = 0;
      const interval = setInterval(() => {
        wordIndex++;
        const currentText = words.slice(0, wordIndex).join(' ');
        const done = wordIndex >= words.length;
        setChats(prev => prev.map(chat =>
          chat.id === activeChatId
            ? {
              ...chat,
              messages: chat.messages.map(m =>
                m.id === aiMsgId
                  ? { ...m, text: currentText, isStreaming: !done, lastMessage: currentText }
                  : m
              ),
              lastMessage: done ? currentText : chat.lastMessage
            }
            : chat
        ));
        if (done) {
          clearInterval(interval);
          setIsSending(false);
        }
      }, 60); // ~60ms per word

    } catch (error: any) {
      console.error('Chat API error:', error);
      // TypeError = browser blocked the request (CORS on 401) — treat as unauthorized
      if (error instanceof TypeError) {
        console.warn('🔒 Network/CORS error on /api/Chat — session likely expired');
        onUnauthorized();
        setIsSending(false);
        return;
      }
      const errMsg: Message = {
        id: `error_${Date.now()}`,
        senderId: 'system',
        text: `Failed to get response: ${error.message}`,
        timestamp: new Date(),
        status: 'read'
      };
      setChats(prev => prev.map(chat =>
        chat.id === activeChatId
          ? { ...chat, messages: [...chat.messages, errMsg] }
          : chat
      ));
      setIsSending(false);
    }
  };

  return (
    <div className="flex h-full w-full bg-[#111b21] overflow-hidden">
      <div className={`h-full border-r border-[#222d34] flex-shrink-0 transition-all duration-300 ${isDetailActive ? 'hidden md:flex' : 'flex w-full md:w-auto'}`}>
        <Sidebar
          user={user}
          chats={chats}
          activeChatId={activeChatId}
          onSelectChat={handleSelectChat}
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
            isSending={isSending}
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
