import random
from langchain_core.tools import tool

@tool
def reset_password(email: str) -> str:
    """
    Simulate sending a password reset link to the user's email.
    Use this when a user has forgotten their password or cannot log in.
    """
    return f"✅ Password reset link sent to **{email}**. Please check your inbox (and spam folder)."

@tool
def check_vpn_status(user_id: str) -> str:
    """
    Simulate checking the VPN connection status for a given user.
    Use this when a user reports VPN connectivity issues.
    """
    # Randomly return connected or disconnected for demo realism
    statuses = ["connected", "disconnected"]
    status = random.choice(statuses)
    if status == "connected":
        return f"🔒 VPN is **connected** for user `{user_id}`. All systems operational."
    else:
        return f"⚠️ VPN is **disconnected** for user `{user_id}`. Please try reconnecting or contact network support."

@tool
def install_software(software_name: str) -> str:
    """
    Simulate providing installation instructions for a software package.
    Use this when a user asks how to install or download software.
    """
    return f"📦 Installation instructions for **{software_name}** have been sent to your email. You can also find it in the company software center."

@tool
def escalate_to_human(issue_summary: str) -> str:
    """
    Simulate creating a support ticket and escalating to a human agent.
    Use this when the user's problem is complex, urgent, or cannot be resolved by automated tools.
    """
    ticket_id = f"TKT-{random.randint(1000, 9999)}"
    return f"🆘 Support ticket **#{ticket_id}** has been created.\n\nSummary: _{issue_summary}_\n\nA human agent will contact you within 2 hours."

# List of all tools for the agent
ALL_TOOLS = [reset_password, check_vpn_status, install_software, escalate_to_human] 