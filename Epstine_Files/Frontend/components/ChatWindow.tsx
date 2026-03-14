
import React, { useState, useRef, useEffect } from 'react';
import { Chat, Message, User } from '../types';

interface ChatWindowProps {
  chat: Chat;
  onSendMessage: (text: string) => void;
  currentUserId: string;
  onViewProfile: (user: User) => void;
  onBack: () => void;
}

const EMOJIS = ['😊', '😂', '❤️', '👍', '🙏', '🔥', '✨', '🥺', '🎉', '👋'];

const ChatWindow: React.FC<ChatWindowProps> = ({ chat, onSendMessage, currentUserId, onViewProfile, onBack }) => {
  const [inputText, setInputText] = useState('');
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
  }, [chat.messages]);

  const handleSend = (e?: React.FormEvent) => {
    e?.preventDefault();
    if (!inputText.trim()) return;
    onSendMessage(inputText);
    setInputText('');
    setShowEmojiPicker(false);
  };

  return (
    <div className="flex flex-col h-full bg-[#0b141a] relative w-full overflow-hidden">
      <div className="absolute inset-0 opacity-[0.03] pointer-events-none bg-repeat" style={{ backgroundImage: 'url(https://user-images.githubusercontent.com/15075759/28719144-86dc0f70-73b1-11e7-911d-60d70fcded21.png)' }}></div>

      {/* Header */}
      <div className="h-[60px] bg-[#202c33] px-2 sm:px-4 flex items-center gap-1 z-10 shrink-0 border-b border-[#222d34]">
        <button onClick={onBack} className="md:hidden text-[#8696a0] hover:text-white p-2">
           <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg>
        </button>
        
        <div className="flex items-center gap-3 cursor-pointer flex-1 min-w-0" onClick={() => onViewProfile(chat.user)}>
          <img src={chat.user.avatar} className="w-10 h-10 rounded-full shrink-0 border border-black" alt="A" />
          <div className="flex flex-col min-w-0">
            <span className="text-[#e9edef] text-[15px] font-medium truncate">{chat.user.name}</span>
            <span className="text-[12px] text-[#8696a0] truncate">{chat.user.status}</span>
          </div>
        </div>
        <div className="flex gap-2 sm:gap-6 text-[#8696a0] shrink-0">
          <button className="p-2 hidden sm:block hover:text-white transition-colors"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M15.9 14.3H15l-.3-.3c1-1.1 1.6-2.6 1.6-4.2 0-3.7-3-6.7-6.7-6.7S3 6.1 3 9.8s3 6.7 6.7 6.7c1.6 0 3.1-.6 4.2-1.6l.3.3v.9l5.1 5.1 1.5-1.5-5-5.1zm-6.2 0c-2.5 0-4.5-2-4.5-4.5s2-4.5 4.5-4.5 4.5 2 4.5 4.5-2 4.5-4.5 4.5z"></path></svg></button>
          <button className="p-2 hover:text-white transition-colors"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M12 7a2 2 0 1 0-.001 4.001A2 2 0 0 0 12 7zm0 10a2 2 0 1 0-.001 4.001A2 2 0 0 0 12 17zm0-5a2 2 0 1 0-.001 4.001A2 2 0 0 0 12 12z"></path></svg></button>
        </div>
      </div>

      {/* Messages Area */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-4 sm:px-12 space-y-1.5 z-10 no-scrollbar">
        {chat.messages.map((msg) => (
          <div key={msg.id} className={`flex ${msg.senderId === currentUserId ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[90%] sm:max-w-[65%] rounded-lg px-2.5 py-1.5 shadow-lg relative ${msg.senderId === currentUserId ? 'bg-[#8b0000] border border-[#ff3b30]/20' : 'bg-[#202c33]'}`}>
              <p className="text-[14.2px] leading-relaxed break-words text-[#e9edef]">{msg.text}</p>
              <div className="flex items-center justify-end gap-1 mt-0.5">
                <span className="text-[10px] text-[#8696a0]">{new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                {msg.senderId === currentUserId && <span className="text-[#ff3b30] opacity-80"><svg viewBox="0 0 16 11" width="14" height="10" fill="currentColor"><path d="M11.05 1.15c-.15-.15-.35-.25-.55-.25s-.4.1-.55.25L4.5 6.6 2.05 4.15c-.15-.15-.35-.25-.55-.25s-.4.1-.55.25c-.3.3-.3.8 0 1.1l3 3c.15.15.35.25.55.25s.4-.1.55-.25l6-6c.3-.3.3-.8 0-1.1z"></path><path d="M15.05 1.15c-.15-.15-.35-.25-.55-.25s-.4.1-.55.25l-6 6-.55-.55c-.15-.15-.35-.25-.55-.25s-.4.1-.55.25c-.3.3-.3.8 0 1.1l1.1 1.1c.15.15.35.25.55.25s.4-.1.55-.25l6.55-6.55c.3-.3.3-.8 0-1.1z"></path></svg></span>}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Input Area */}
      <div className="bg-[#0b141a] px-2 sm:px-4 py-3 flex items-center gap-2 z-10 shrink-0">
        <div className="w-full bg-[#202c33] flex items-center px-2 sm:px-4 py-1 rounded-full h-[52px]">
          <button className="text-[#8696a0] p-2 hover:text-[#ff3b30] hover:scale-110 transition-all"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></svg></button>
          <form onSubmit={handleSend} className="flex-1 ml-2 h-full">
            <input type="text" placeholder="Type a message" value={inputText} onChange={(e) => setInputText(e.target.value)} className="w-full bg-transparent text-[#e9edef] outline-none text-[15px] border-none focus:ring-0 leading-[52px] h-full" />
          </form>
          <button onClick={() => inputText.trim() && handleSend()} className="text-[#8696a0] p-2.5 hover:scale-110 transition-all">
            {inputText.trim() ? <svg viewBox="0 0 24 24" width="24" height="24" fill="#ff3b30"><path d="M1.101 21.757L23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg> : <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"></path><path d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"></path></svg>}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatWindow;
