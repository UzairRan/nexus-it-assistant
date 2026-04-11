import os
import requests
import streamlit as st
from langchain_ollama import ChatOllama  # Correct import
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
    2. Cloud API (only if Ollama not available AND API key exists)
    
    Args:
        backend_choice: "auto" (detect), "local" (force Ollama), or "cloud" (force Orq.ai)
    """
    # Auto-detect
    if backend_choice == "auto":
        # PRIORITY 1: Check for local Ollama first
        if check_ollama_available():
            backend = "local"
        # PRIORITY 2: Check if running on Streamlit Cloud (no local Ollama possible)
        elif os.getenv("STREAMLIT_CLOUD") == "1" or os.getenv("STREAMLIT_SHARING_MODE"):
            backend = "cloud"
        # PRIORITY 3: Fallback to cloud if API key exists locally
        elif "ORQ_API_KEY" in st.secrets or os.getenv("ORQ_API_KEY"):
            backend = "cloud"
        else:
            backend = "error"
    else:
        backend = backend_choice
    
    if backend == "local":
        # Local Ollama - using the correct package
        try:
            llm = ChatOllama(model="llama3.2:3b", temperature=0) 
            return llm, "local", "llama3"
        except Exception as e:
            st.error(f"Failed to initialize Ollama: {e}")
            return None, "error", None
    
    elif backend == "cloud":
        # Cloud via Orq.ai Router
        api_key = st.secrets.get("ORQ_API_KEY") or os.getenv("ORQ_API_KEY")
        if not api_key:
            st.error("ORQ_API_KEY not found in secrets or environment.")
            return None, "error", None
        
        model_name = "meta-llama/llama-3.3-70b-instruct"
        
        llm = ChatOpenAI(
            base_url="https://router.orq.ai/v1",
            api_key=api_key,
            model=model_name,
            temperature=0,
        )
        return llm, "cloud", model_name
    
    else:
        st.error("No LLM backend available. Please ensure Ollama is running locally or ORQ_API_KEY is set.")
        return None, "error", None 