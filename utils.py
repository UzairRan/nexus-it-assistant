import os
import requests
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

def check_ollama_available() -> bool:
    """Check if Ollama is running locally."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        return response.status_code == 200
    except:
        return False

def get_llm(backend_choice: str = "auto"):
    """
    Return a LangChain LLM instance based on environment.
    
    Priority:
    1. Local Ollama (if available)
    2. Cloud API (only if Ollama not available)
    """
    # Auto-detect
    if backend_choice == "auto":
        # PRIORITY 1: Check for local Ollama first
        if check_ollama_available():
            backend = "local"
        # PRIORITY 2: Check if running on Streamlit Cloud
        elif os.getenv("STREAMLIT_CLOUD") == "1" or os.getenv("STREAMLIT_SHARING_MODE"):
            backend = "cloud"
        # PRIORITY 3: Everything else - error
        else:
            backend = "error"
    else:
        backend = backend_choice
    
    if backend == "local":
        try:
            llm = ChatOllama(model="llama3.2:3b", temperature=0)
            return llm, "local", "llama3.2:3b"
        except Exception as e:
            st.error(f"Failed to initialize Ollama: {e}")
            return None, "error", None
    
    elif backend == "cloud":
        # Hugging Face Free Inference API (no key required)
        try:
            llm = ChatOpenAI(
                base_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1/v1",
                api_key="",
                model="mistralai/Mistral-7B-Instruct-v0.1",
                temperature=0,
            )
            return llm, "cloud", "Mistral-7B (HF Free)"
        except Exception as e:
            st.error(f"Failed to initialize cloud LLM: {e}")
            return None, "error", None
    
    else:
        st.error("No LLM backend available. Please ensure Ollama is running locally.")
        return None, "error", None 