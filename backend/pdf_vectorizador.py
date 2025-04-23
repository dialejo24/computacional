from sentence_transformers import SentenceTransformer
import faiss
import fitz

model = SentenceTransformer("all-MiniLM-L6-v2")

class PDFVectorSearch:
    def __init__(self, pdf_path):
        self.text_chunks = []
        self.embeddings = []
        self.index = None
        self.load_and_index(pdf_path)

    def load_and_index(self, pdf_path):
        doc = fitz.open(pdf_path)
        for page in doc:
            text = page.get_text()
            chunks = text.split("\n\n")
            self.text_chunks.extend([c.strip() for c in chunks if c.strip()])

        self.embeddings = model.encode(self.text_chunks, convert_to_numpy=True)
        dim = self.embeddings[0].shape[0]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def search(self, question, top_k=3):
        q_embedding = model.encode([question], convert_to_numpy=True)
        _, indices = self.index.search(q_embedding, top_k)
        return [self.text_chunks[i] for i in indices[0]]
