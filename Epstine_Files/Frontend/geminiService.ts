
import { GoogleGenAI } from "@google/genai";

export class GeminiService {
  private ai: GoogleGenAI;

  constructor() {
    this.ai = new GoogleGenAI({ apiKey: process.env.API_KEY || '' });
  }

  async getChatResponse(message: string, history: { role: 'user' | 'model'; parts: { text: string }[] }[]) {
    try {
      const response = await this.ai.models.generateContent({
        model: 'gemini-3-flash-preview',
        contents: [
          { role: 'user', parts: [{ text: "You are an AI assistant in Jchat, a red and black themed messaging app. Keep your responses concise and conversational, like a real human chat partner." }] },
          ...history,
          { role: 'user', parts: [{ text: message }] }
        ],
        config: {
          temperature: 0.7,
          topP: 0.95,
          topK: 40,
        }
      });
      return response.text || "I'm having trouble connecting right now.";
    } catch (error) {
      console.error("Gemini API Error:", error);
      return "Oops! Something went wrong with my circuits.";
    }
  }
}

export const geminiService = new GeminiService();
