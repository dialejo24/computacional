'use client';
import { useState } from 'react';
import axios from 'axios';

export default function PDFUploader({ onUploaded }: { onUploaded: () => void }) {
  const [loading, setLoading] = useState(false);

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    await axios.post('http://localhost:8000/upload-pdf/', formData);
    setLoading(false);
    onUploaded();
  };

  return (
    <div className="mb-4">
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      {loading && <p className="text-sm text-gray-500">Subiendo PDF...</p>}
    </div>
  );
}
