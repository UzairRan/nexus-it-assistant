import streamlit as st
import uuid
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage

from utils import get_llm
from agent_llm import create_agent
from tools import ALL_TOOLS

# ---------- Custom CSS for Tech Blue Theme ----------
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1E3A5F;
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    [data-testid="stSidebar"] .stButton > button {
        background-color: #3B82F6 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        transition: all 0.2s !important;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #2563EB !important;
        transform: translateY(-1px) !important;
    }
    
    /* Expander styling in sidebar */
    [data-testid="stSidebar"] .streamlit-expanderHeader {
        background-color: #2D5A8E !important;
        border-radius: 8px !important;
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    [data-testid="stSidebar"] .streamlit-expanderContent {
        background-color: #1E3A5F !important;
        border: none !important;
    }
    
    /* Main content */
    h1 {
        color: #1E293B !important;
        font-weight: 600 !important;
    }
    
    /* Chat bubbles */
    [data-testid="stChatMessage"] {
        border-radius: 16px !important;
        padding: 12px 16px !important;
        margin: 8px 0 !important;
    }
    
    [data-testid="stChatMessage"][data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
    }
    
    [data-testid="stChatMessage"][data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
        background-color: #E2E8F0 !important;
        color: #1E293B !important;
    }
    
    /* Chat input */
    [data-testid="stChatInput"] textarea {
        border: 2px solid #E2E8F0 !important;
        border-radius: 12px !important;
        background-color: #FFFFFF !important;
    }
    
    [data-testid="stChatInput"] textarea:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1) !important;
    }
    
    /* Metrics */
    [data-testid="stMetric"] {
        background-color: #2D5A8E !important;
        border-radius: 8px !important;
        padding: 8px !important;
    }
    
    [data-testid="stMetric"] label {
        color: #94A3B8 !important;
    }
    
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 20px !important;
    }
    
    /* Success/Info/Warning boxes */
    .stAlert {
        border-radius: 8px !important;
        border: none !important;
    }
    
    /* Tool badge */
    .tool-badge {
        background-color: #64748B !important;
        color: #FFFFFF !important;
        padding: 4px 12px !important;
        border-radius: 20px !important;
        font-size: 12px !important;
        display: inline-block !important;
        margin-top: 8px !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    #header {visibility: hidden;}
    
    /* Remove dividers */
    hr {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Page Configuration ----------
st.set_page_config(
    page_title="Nexus IT Assistant",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Session State Initialization ----------
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]

if "messages" not in st.session_state:
    st.session_state.messages = []

if "tool_history" not in st.session_state:
    st.session_state.tool_history = []

if "agent" not in st.session_state:
    st.session_state.agent = None

if "llm_backend" not in st.session_state:
    st.session_state.llm_backend = None

if "model_name" not in st.session_state:
    st.session_state.model_name = None

# ---------- Sidebar UI ----------
with st.sidebar:
    st.title("Nexus")
    st.caption("IT Assistant")
    
    # Initialize LLM if not already done
    if st.session_state.agent is None:
        with st.spinner("Initializing agent..."):
            llm, backend, model = get_llm("auto")
            if llm is not None:
                st.session_state.agent = create_agent(llm)
                st.session_state.llm_backend = backend
                st.session_state.model_name = model
                st.rerun()
            else:
                st.error("Failed to initialize LLM. Check your configuration.")
                st.stop()
    
    # Environment Indicator
    if st.session_state.llm_backend == "local":
        st.success("Local Mode (Ollama)")
    elif st.session_state.llm_backend == "cloud":
         st.info("Cloud Mode (HF Free)") 
    else:
        st.warning("Unknown backend")
    
    st.caption(f"Model: {st.session_state.model_name}")
    
    # Session Info (Collapsible)
    with st.expander("Session Info", expanded=False):
        st.metric("Session ID", st.session_state.session_id)
        st.metric("Messages", len(st.session_state.messages))
    
    # Quick Tools (Collapsible with buttons inside)
    with st.expander("Quick Tools", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Reset Password", use_container_width=True, key="reset_btn"):
                st.session_state.pending_input = "I forgot my password"
            if st.button("Install Software", use_container_width=True, key="install_btn"):
                st.session_state.pending_input = "How do I install Slack?"
        with col2:
            if st.button("Check VPN", use_container_width=True, key="vpn_btn"):
                st.session_state.pending_input = "My VPN is not connecting"
            if st.button("Escalate", use_container_width=True, key="escalate_btn"):
                st.session_state.pending_input = "My laptop won't turn on"
    
    # Tool History (Collapsible)
    with st.expander("Tool History", expanded=False):
        if st.session_state.tool_history:
            for entry in reversed(st.session_state.tool_history[-5:]):
                st.caption(f"{entry['tool']} — {entry['time']}")
        else:
            st.caption("No tools called yet.")
    
    # Clear Chat Button
    if st.button("Clear Chat", use_container_width=True, key="clear_btn"):
        st.session_state.messages = []
        st.session_state.tool_history = []
        llm, backend, model = get_llm(st.session_state.llm_backend)
        if llm:
            st.session_state.agent = create_agent(llm)
        st.rerun() 

# ---------- Main Chat Area ----------
st.title("Nexus")
st.caption("Your intelligent IT support assistant")

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])
            if "tool_called" in msg and msg["tool_called"]:
                st.markdown(f'<span class="tool-badge">Tool: {msg["tool_called"]}</span>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Describe your IT issue...")

# Handle pending input from quick actions
if "pending_input" in st.session_state and st.session_state.pending_input:
    user_input = st.session_state.pending_input
    st.session_state.pending_input = None

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            try:
                # Prepare messages for LangGraph agent
                input_messages = []
                for m in st.session_state.messages:
                    if m["role"] == "user":
                        input_messages.append(HumanMessage(content=m["content"]))
                    else:
                        input_messages.append(AIMessage(content=m["content"]))
                
                # Invoke agent
                config = {"configurable": {"thread_id": st.session_state.session_id}}
                result = st.session_state.agent.invoke(
                    {"messages": input_messages},
                    config=config
                )
                
                # Extract the last AI message
                response_messages = result["messages"]
                ai_response = None
                tool_called = None
                
                # Find the final AI response
                for msg in reversed(response_messages):
                    if isinstance(msg, AIMessage) and msg.content:
                        ai_response = msg.content
                        break
                
                # Check if any tool was called in this turn
                for msg in response_messages:
                    if hasattr(msg, "tool_calls") and msg.tool_calls:
                        for tc in msg.tool_calls:
                            tool_called = tc["name"]
                            st.session_state.tool_history.append({
                                "tool": tool_called,
                                "time": datetime.now().strftime("%H:%M:%S")
                            })
                
                if ai_response is None:
                    ai_response = "I'm sorry, I couldn't process that request. Please try again."
                
                # Display response
                st.write(ai_response)
                if tool_called:
                    st.markdown(f'<span class="tool-badge">Tool: {tool_called}</span>', unsafe_allow_html=True)
                
                # Save to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response,
                    "tool_called": tool_called
                })
                
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg,
                    "tool_called": None
                }) 