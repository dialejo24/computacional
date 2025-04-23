import google.generativeai as genai
from pdf_vectorizador import PDFVectorSearch

genai.configure(api_key="") #INGRESA SU PROPIA API KEY  
model = genai.GenerativeModel("gemini-2.0-flash")

pdf_search = None  

def load_pdf_vector_search(path):
    global pdf_search
    pdf_search = PDFVectorSearch(path)

def get_answer_from_pdf(question):
    if pdf_search is None:
        return "Error: el PDF no fue cargado aún."

    relevant_chunks = pdf_search.search(question)
    context = "\n\n".join(relevant_chunks)

    prompt = f"""
    A continuación hay fragmentos de un documento:

    {context}

    Pregunta: {question}

    Responde únicamente con base en el contenido proporcionado, de forma clara y precisa.
    """
    response = model.generate_content(prompt)
    return response.text
