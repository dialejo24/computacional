'use client';
import dynamic from 'next/dynamic';
import { useState } from 'react';
import PDFUploader from './components/PDFUploader';
// import VoiceRecorder from './components/voiceRecorder';
import ResponseDisplay from './components/ResponseDisplay';

const VoiceRecorder = dynamic(() => import('./components/voiceRecorder'), {
  ssr: false,
});

export default function Home() {
  const [isPDFReady, setPDFReady] = useState(false);
  const [response, setResponse] = useState<{
    question: string;
    answer: string;
    audio_path: string;
  } | null>(null);

  return (
    <main className="p-8 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">ChatPDF con voz 🎤📄</h1>
      <PDFUploader onUploaded={() => setPDFReady(true)} />

      {isPDFReady && (
        <div className="mt-4">
          <VoiceRecorder onResponse={setResponse} />
        </div>
      )}

      {response && (
        <ResponseDisplay
          question={response.question}
          answer={response.answer}
          audioPath={response.audio_path}
        />
      )}
    </main>
  );
}
