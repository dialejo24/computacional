'use client';
import { useEffect, useRef, useState } from 'react';

export default function ResponseDisplay({ question, answer, audioPath }: {
  question: string;
  answer: string;
  audioPath: string;
}) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const initAudio = () => {
    if (typeof window !== 'undefined' && !audioRef.current) {
      audioRef.current = new Audio(`http://localhost:8000${audioPath}`);
    }
  };
  

  const playAudio = () => {
    initAudio();
    if (audioRef.current) {
      audioRef.current.play()
        .then(() => setIsPlaying(true))
        .catch(error => console.error("Error al reproducir:", error));
    }
  };

  const pauseAudio = () => {
    if (audioRef.current) {
      audioRef.current.pause();
      setIsPlaying(false);
    }
  };

  const restartAudio = () => {
    if (audioRef.current) {
      audioRef.current.currentTime = 0;
      if (!isPlaying) {
        audioRef.current.play()
          .then(() => setIsPlaying(true))
          .catch(error => console.error("Error al reiniciar:", error));
      }
    }
  };

  return (
    <div className="mt-6 space-y-2">
      <p><strong>Pregunta:</strong> {question}</p>
      <p><strong>Respuesta:</strong> {answer}</p>
      <div className="flex gap-2 p-4 bg-gray-100 rounded-lg">
      <button 
        onClick={playAudio}
        disabled={isPlaying}
        className="px-3 py-1 bg-green-500 text-white rounded disabled:opacity-50"
      >
        ▶ Iniciar
      </button>
      
      <button 
        onClick={pauseAudio}
        disabled={!isPlaying}
        className="px-3 py-1 bg-yellow-500 text-white rounded disabled:opacity-50"
      >
        ⏸ Pausar
      </button>
      
      <button 
        onClick={restartAudio}
        className="px-3 py-1 bg-blue-500 text-white rounded"
      >
        🔄 Reiniciar
      </button>
    </div>
    </div>
  );
}
