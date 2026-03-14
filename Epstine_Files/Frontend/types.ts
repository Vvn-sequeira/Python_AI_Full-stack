
export interface User {
  id: string;
  name: string;
  avatar: string;
  status: string;
  lastSeen?: string;
}

export interface Message {
  id: string;
  senderId: string;
  text: string;
  timestamp: Date;
  status: 'sent' | 'delivered' | 'read';
}

export interface Chat {
  id: string;
  user: User;
  lastMessage?: string;
  unreadCount: number;
  timestamp: string;
  messages: Message[];
}

export type ViewType = 'login' | 'register' | 'chat' | 'settings' | 'profile';
