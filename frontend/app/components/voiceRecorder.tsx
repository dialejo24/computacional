"use client";
import { useReactMediaRecorder } from 'react-media-recorder';
import axios from 'axios';
import { useState, useEffect } from 'react';

export default function VoiceRecorder({ onResponse }: {
    onResponse: (data: { question: string; answer: string; audio_path: string }) => void;
}) {
    const [blob, setBlob] = useState<Blob | null>(null);
    const [isClient, setIsClient] = useState(false); 

    useEffect(() => {
        setIsClient(true); 
    }, []);

    const { startRecording, stopRecording, mediaBlobUrl, clearBlobUrl } =
        useReactMediaRecorder({
            audio: true,
            onStop: (blobUrl, blob) => setBlob(blob),
        });

    const handleSend = async () => {
        if (!blob) return;

        const formData = new FormData();
        formData.append('audio', blob, 'question.wav');
        try {
            const res = await axios.post('http://localhost:8000/ask/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log("res", res.data);
            onResponse(res.data);
            clearBlobUrl();
        } catch (error) {
            console.log("error", error);
        }

    };

    if (!isClient) return null;

    return (
        <div className="flex gap-2 items-center">
            <button onClick={startRecording} className="bg-blue-500 text-white px-4 py-2 rounded">🎙️ Grabar</button>
            <button onClick={stopRecording} className="bg-yellow-500 text-white px-4 py-2 rounded">⏹️ Detener</button>
            <button onClick={handleSend} disabled={!blob} className="bg-green-600 text-white px-4 py-2 rounded">📤 Enviar</button>
        </div>
    );
}
