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

def is_streamlit_cloud() -> bool:
    """Detect if running on Streamlit Cloud."""
    return (
        os.getenv("STREAMLIT_CLOUD") == "1" or
        os.getenv("STREAMLIT_SHARING_MODE") == "1" or
        os.getenv("STREAMLIT_RUNTIME_ENV") == "cloud" or
        "streamlit.app" in os.getenv("HOSTNAME", "") or
        "streamlitcloud" in os.getenv("PATH", "").lower()
    )

def get_llm(backend_choice: str = "auto"):
    """
    Return a LangChain LLM instance based on environment.
    
    Priority:
    1. Local Ollama (if available)
    2. Cloud API (if on Streamlit Cloud)
    """
    if backend_choice == "auto":
        if check_ollama_available():
            backend = "local"
        elif is_streamlit_cloud():
            backend = "cloud"
        else:
            backend = "cloud"
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
        try:
            api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
            if not api_key:
                st.error("GEMINI_API_KEY not found. Please add it to secrets.")
                return None, "error", None
            
            llm = ChatOpenAI(
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                api_key=api_key,
                model="gemini-2.0-flash",
                temperature=0,
            )
            return llm, "cloud", "Gemini Flash"
        except Exception as e:
            st.error(f"Failed to initialize cloud LLM: {e}")
            return None, "error", None
    
    else:
        st.error("No LLM backend available.")
        return None, "error", None 