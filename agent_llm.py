from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools import ALL_TOOLS
import logging

logger = logging.getLogger(__name__)

def create_agent(llm: BaseChatModel):
    """
    Create a LangGraph ReAct agent with the given LLM.
    The agent has access to all tools and maintains conversation memory.
    """
    memory = MemorySaver()
    
    system_prompt = """
    You are a helpful IT support assistant. Your job is to help users with common IT issues.
    
    You have access to the following tools:
    - reset_password: Send a password reset link to a user's email.
    - check_vpn_status: Check if a user's VPN is connected.
    - install_software: Provide software installation instructions.
    - escalate_to_human: Create a support ticket for complex issues.
    
    Guidelines:
    - If a user describes multiple issues, address them one by one using the appropriate tools.
    - If you are unsure or the issue is complex, escalate to a human.
    - Always be polite and professional.
    - If you need the user's email or user ID, ask for it before calling tools that require it.
    
    Current conversation context is provided. Use it to maintain continuity.
    """
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    agent = create_react_agent(
        model=llm,
        tools=ALL_TOOLS,
        checkpointer=memory,
        prompt=prompt
    )
    
    return agent 