
import React, { useState, useEffect } from 'react';
import { ViewType, User, Chat } from './types';
import Login from './components/Login';
import Register from './components/Register';
import ChatMain from './components/ChatMain';

const App: React.FC = () => {
  const [view, setView] = useState<ViewType>('login');
  const [currentUser, setCurrentUser] = useState<User | null>(null);

  // Check for stored user
  useEffect(() => {
    const savedUser = localStorage.getItem('jchat_user');
    if (savedUser) {
      setCurrentUser(JSON.parse(savedUser));
      setView('chat');
    }
  }, []);

  const handleLogin = (user: User) => {
    setCurrentUser(user);
    localStorage.setItem('jchat_user', JSON.stringify(user));
    setView('chat');
  };

  const handleLogout = () => {
    setCurrentUser(null);
    localStorage.removeItem('jchat_user');
    setView('login');
  };

  return (
    <div className="h-screen w-screen bg-black overflow-hidden select-none">
      {view === 'login' && (
        <Login onLogin={handleLogin} onSwitch={() => setView('register')} />
      )}
      {view === 'register' && (
        <Register onRegister={handleLogin} onSwitch={() => setView('login')} />
      )}
      {view === 'chat' && currentUser && (
        <ChatMain user={currentUser} onLogout={handleLogout} />
      )}
    </div>
  );
};

export default App;
