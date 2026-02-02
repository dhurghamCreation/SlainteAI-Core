import os
import re
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_classic.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
# NEW: Local Embeddings (No API Key needed)
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Custom Reasoning Prompt
template = """You are a clinical safety auditor for SlainteAI.
Use the HSE Sepsis guidelines context to triage the patient.

STRICT INSTRUCTIONS:
1. Do NOT assume a female patient is a maternity patient unless pregnancy or recent birth is explicitly mentioned.
2. If pregnancy status is unknown, use the 'General Adult' triage criteria (Figure 8) first, but note that maternity status should be clarified.
3. Show your reasoning step-by-step.

Context: {context}
Question: {question}
Answer:"""
REASONING_PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

def clean_clinical_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'Page \d+ of \d+', '', text)
    return text.strip()

def run_slainte_ai(question):
    VECTOR_DB_PATH = "data/faiss_index"
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if os.path.exists(VECTOR_DB_PATH):
        print("--- Loading Local Brain ---")
        vectorstore = FAISS.load_local(VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)
    else:
        # (Keeping your building logic here...)
        pass

    # STABLE 2026 MODEL NAME
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key="AIzaSyCBT42_DwnRzNpef4a3Hh5zuG49eTB3zm8", 
        temperature=0
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": REASONING_PROMPT},
        return_source_documents=True
    )
    
    return qa_chain.invoke({"query": question})

if __name__ == "__main__":
    test_query = "Triage two patients with a 102°F fever: one Male and one Female. Does your priority level change for either? If so, explain why based strictly on the HSE manual."
    print("--- Running SlainteAI Local Audit ---")
    try:
        result = run_slainte_ai(test_query)
        print(f"\nAI DECISION:\n{result['result']}")
    except Exception as e:
        print(f"STILL GETTING ERROR: {e}")