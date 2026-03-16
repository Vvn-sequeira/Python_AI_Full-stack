
import React, { useState, useEffect } from 'react';
import { ViewType, User } from './types';
import Login from './components/Login';
import Register from './components/Register';
import ChatMain from './components/ChatMain';

const App: React.FC = () => {
  const [view, setView] = useState<ViewType>('login');
  const [currentUser, setCurrentUser] = useState<User | null>(null);
  const [wasRedirected, setWasRedirected] = useState(false);

  // On mount: restore session from localStorage (cookie is HttpOnly so JS can't read it,
  // but it is sent automatically with every API request by the browser)
  useEffect(() => {
    const savedUser = localStorage.getItem('jchat_user');
    if (savedUser) {
      try {
        setCurrentUser(JSON.parse(savedUser));
        setView('chat');
      } catch {
        localStorage.removeItem('jchat_user');
        setView('login');
      }
    }
  }, []);

  const handleLogin = (user: User) => {
    setCurrentUser(user);
    setWasRedirected(false);
    localStorage.setItem('jchat_user', JSON.stringify(user));
    setView('chat');
  };

  const handleLogout = () => {
    setCurrentUser(null);
    localStorage.removeItem('jchat_user');
    setView('login');
  };

  // Called by ChatMain whenever a 401 comes back from any API call
  const handleUnauthorized = () => {
    console.warn('🔒 Session expired — redirecting to login');
    setCurrentUser(null);
    localStorage.removeItem('jchat_user');
    setWasRedirected(true);
    setView('login');
  };

  return (
    <div
      className="w-screen bg-black overflow-hidden select-none"
      style={{ height: '100dvh', /* fallback for older mobile browsers */  minHeight: 'calc(var(--vh, 1vh) * 100)' }}
    >
      {view === 'login' && (
        <Login onLogin={handleLogin} onSwitch={() => setView('register')} redirected={wasRedirected} />
      )}
      {view === 'register' && (
        <Register onRegister={handleLogin} onSwitch={() => setView('login')} />
      )}
      {view === 'chat' && currentUser && (
        <ChatMain user={currentUser} onLogout={handleLogout} onUnauthorized={handleUnauthorized} />
      )}
    </div>
  );
};

export default App;
