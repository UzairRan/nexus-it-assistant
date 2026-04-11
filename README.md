# Nexus IT Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-1C3C3C?style=for-the-badge&logo=langgraph&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Dual--Path-1E3A5F?style=for-the-badge&logo=diagram&logoColor=white)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tools](https://img.shields.io/badge/Tools-4_Simulated-10B981?style=for-the-badge&logo=openapiinitiative&logoColor=white)

</div>

------------------------------------------------------------------------------ 


Built with LangGraph's ReAct pattern.

It runs **locally with Ollama** (free, private) and automatically switches to **Gemini Flash or any other API key anyone wants to use** when deployed to the cloud. 

# Tech Stack

**Frontend** Streamlit 

**Agent Framework**  LangGraph + LangChain 

**Local LLM** Ollama (llama3.2:3b) 

**Cloud LLM**  Google Gemini Flash (Free Tier), also any other API key can be used.

**Memory**  LangGraph MemorySaver 

**Deployment**  Streamlit Cloud 

**Version Control**  Git + GitHub 

------------------------------------------------------------------------------

### Local Deployment Flow (Ollama)
```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1E3A5F', 'primaryTextColor': '#FFFFFF', 'primaryBorderColor': '#3B82F6', 'lineColor': '#2563EB', 'secondaryColor': '#10B981', 'tertiaryColor': '#F8FAFC', 'tertiaryTextColor': '#1E293B', 'fontFamily': 'Arial, sans-serif', 'fontSize': '16px', 'fontWeight': 'bold'}}}%%
flowchart TD
    A[**USER INPUT**] --> B{**STREAMLIT APP**}
    B --> C[**ENVIRONMENT DETECTION**]
    C -->|**OLLAMA AVAILABLE**| D[**LOCAL PATH**]
    D --> E[**CHATOLLAMA**<br/>llama3.2:3b]
    E --> F[**LANGGRAPH AGENT**<br/>ReAct Loop]
    F --> G{**TOOL SELECTION**}
    G -->|**Password**| H[**reset_password**]
    G -->|**VPN**| I[**check_vpn_status**]
    G -->|**Install**| J[**install_software**]
    G -->|**Escalate**| K[**escalate_to_human**]
    H & I & J & K --> L[**TOOL EXECUTION**]
    L --> M[**MEMORY SAVER**]
    M --> N[**AGENT RESPONSE**]
    N --> B
    B --> O[**CHAT UI DISPLAY**]

    style A fill:#2563EB,stroke:#1E3A5F,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style B fill:#1E3A5F,stroke:#3B82F6,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style C fill:#2D5A8E,stroke:#3B82F6,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style D fill:#10B981,stroke:#047857,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style E fill:#8B5CF6,stroke:#6D28D9,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style F fill:#EC4899,stroke:#BE185D,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style G fill:#F59E0B,stroke:#B45309,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style H fill:#EF4444,stroke:#B91C1C,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style I fill:#3B82F6,stroke:#1D4ED8,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style J fill:#10B981,stroke:#047857,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style K fill:#F97316,stroke:#C2410C,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style L fill:#6366F1,stroke:#4338CA,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style M fill:#14B8A6,stroke:#0F766E,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style N fill:#EC4899,stroke:#BE185D,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style O fill:#2563EB,stroke:#1E3A5F,stroke-width:3px,color:#FFFFFF,font-weight:bold
```


------------------------------------------------------------------------------


# Cloud Deployment Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1E3A5F', 'primaryTextColor': '#FFFFFF', 'primaryBorderColor': '#3B82F6', 'lineColor': '#2563EB', 'secondaryColor': '#10B981', 'tertiaryColor': '#F8FAFC', 'tertiaryTextColor': '#1E293B', 'fontFamily': 'Arial, sans-serif', 'fontSize': '16px', 'fontWeight': 'bold'}}}%%
flowchart TD
    A[**USER INPUT**] --> B{**STREAMLIT CLOUD**}
    B --> C[**ENVIRONMENT DETECTION**]
    C -->|**CLOUD DETECTED**| D[**CLOUD PATH**]
    D --> E[**GEMINI FLASH API**<br/>gemini-2.0-flash]
    E --> F[**LANGGRAPH AGENT**<br/>ReAct Loop]
    F --> G{**TOOL SELECTION**}
    G -->|**Password**| H[**reset_password**]
    G -->|**VPN**| I[**check_vpn_status**]
    G -->|**Install**| J[**install_software**]
    G -->|**Escalate**| K[**escalate_to_human**]
    H & I & J & K --> L[**TOOL EXECUTION**]
    L --> M[**MEMORY SAVER**]
    M --> N[**AGENT RESPONSE**]
    N --> B
    B --> O[**CHAT UI DISPLAY**]

    style A fill:#2563EB,stroke:#1E3A5F,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style B fill:#1E3A5F,stroke:#3B82F6,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style C fill:#2D5A8E,stroke:#3B82F6,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style D fill:#0284C7,stroke:#0369A1,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style E fill:#8B5CF6,stroke:#6D28D9,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style F fill:#EC4899,stroke:#BE185D,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style G fill:#F59E0B,stroke:#B45309,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style H fill:#EF4444,stroke:#B91C1C,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style I fill:#3B82F6,stroke:#1D4ED8,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style J fill:#10B981,stroke:#047857,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style K fill:#F97316,stroke:#C2410C,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style L fill:#6366F1,stroke:#4338CA,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style M fill:#14B8A6,stroke:#0F766E,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style N fill:#EC4899,stroke:#BE185D,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style O fill:#2563EB,stroke:#1E3A5F,stroke-width:3px,color:#FFFFFF,font-weight:bold
```


------------------------------------------------------------------------------


## System Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1E3A5F', 'primaryTextColor': '#FFFFFF', 'primaryBorderColor': '#3B82F6', 'lineColor': '#2563EB', 'secondaryColor': '#10B981', 'tertiaryColor': '#F8FAFC', 'tertiaryTextColor': '#1E293B', 'fontFamily': 'Arial, sans-serif', 'fontSize': '16px', 'fontWeight': 'bold'}}}%%
flowchart LR
    subgraph Frontend[**FRONTEND LAYER**]
        UI[**Streamlit UI**]
        SS[**Session State**]
    end
    
    subgraph Backend[**BACKEND LAYER**]
        ED[**Environment<br/>Detector**]
        LA[**LangGraph<br/>ReAct Agent**]
        MEM[**MemorySaver**]
    end
    
    subgraph LLM[**LLM LAYER**]
        L1[**Ollama**<br/>llama3.2:3b<br/>Local]
        L2[**Gemini Flash**<br/>gemini-2.0-flash<br/>Cloud]
    end
    
    subgraph Tools[**TOOLS LAYER**]
        T1[**reset_password**]
        T2[**check_vpn**]
        T3[**install_software**]
        T4[**escalate**]
    end
    
    UI --> ED
    ED -->|**Local**| L1
    ED -->|**Cloud**| L2
    L1 & L2 --> LA
    LA --> MEM
    LA --> T1 & T2 & T3 & T4
    T1 & T2 & T3 & T4 --> LA
    LA --> UI
    SS --> UI

    style Frontend fill:#1E3A5F,stroke:#3B82F6,stroke-width:3px,color:#FFFFFF
    style Backend fill:#2D5A8E,stroke:#3B82F6,stroke-width:3px,color:#FFFFFF
    style LLM fill:#312E81,stroke:#6366F1,stroke-width:3px,color:#FFFFFF
    style Tools fill:#14532D,stroke:#22C55E,stroke-width:3px,color:#FFFFFF
    
    style UI fill:#2563EB,stroke:#1E3A5F,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style SS fill:#3B82F6,stroke:#1D4ED8,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style ED fill:#10B981,stroke:#047857,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style LA fill:#EC4899,stroke:#1565C0,stroke-width:3px,color:#FFFFFF,font-weight:bold
    style MEM fill:#14B8A6,stroke:#0F766E,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style L1 fill:#8B5CF6,stroke:#6D28D9,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style L2 fill:#F59E0B,stroke:#B45309,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style T1 fill:#EF4444,stroke:#B91C1C,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style T2 fill:#3B82F6,stroke:#1D4ED8,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style T3 fill:#10B981,stroke:#047857,stroke-width:2px,color:#FFFFFF,font-weight:bold
    style T4 fill:#F97316,stroke:#C2410C,stroke-width:2px,color:#FFFFFF,font-weight:bold
```


------------------------------------------------------------------------------


# Prerequisites

Python 3.10+

Git

Ollama (for local mode)

----------------------------------------------------------------------------- 

# Local Installation

**1- Clone the repository**

git clone https://github.com/yourusername/nexus-it-assistant.git

cd nexus-it-assistant

**2- Create virtual environment**

python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

**3- Install dependencies**

pip install -r requirements.txt

**4- Setup Ollama (Local Mode)**

# Install Ollama from https://ollama.ai

Ollama pull llama3.2:3b

ollama serve  # In separate terminal

**5- Run locally**

streamlit run app.py

The app will auto-detect Ollama and use local mode.


----------------------------------------------------------------------------- 

## Cloud Deployment

**1- Fork/Clone to GitHub**

**2- Deploy on Streamlit Cloud**

Go to share.streamlit.io

Click "New app"

Select repository and app.py

Click "Deploy"

**3- Add Gemini API Key**

Go to Google AI Studio

Create API key

In Streamlit Cloud: Settings → Secrets

Add:  GEMINI_API_KEY = "your-key-here"

Click "Save" and "Reboot app"


**4- Access your cloud app**

URL: https://your-app-name.streamlit.app


-----------------------------------------------------------------------------  


 # Testing

<div align="center">

<h3 style="color: #1E3A5F; font-weight: bold;">Test Cases</h3>

<table>
  <thead>
    <tr>
      <th style="background: #1E3A5F; color: white; padding: 15px; font-size: 16px; border: 3px solid #3B82F6; text-align: left;">Test Case</th>
      <th style="background: #1E3A5F; color: white; padding: 15px; font-size: 16px; border: 3px solid #3B82F6; text-align: left;">Expected Tool</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background: #F8FAFC; padding: 12px; border: 2px solid #E2E8F0; font-weight: bold;">"I forgot my password"</td>
      <td style="background: #FFFFFF; padding: 12px; border: 2px solid #E2E8F0; font-family: monospace; font-weight: bold; color: #EF4444;">reset_password</td>
    </tr>
    <tr>
      <td style="background: #F8FAFC; padding: 12px; border: 2px solid #E2E8F0; font-weight: bold;">"Is VPN working?"</td>
      <td style="background: #FFFFFF; padding: 12px; border: 2px solid #E2E8F0; font-family: monospace; font-weight: bold; color: #3B82F6;">check_vpn_status</td>
    </tr>
    <tr>
      <td style="background: #F8FAFC; padding: 12px; border: 2px solid #E2E8F0; font-weight: bold;">"How to install Python?"</td>
      <td style="background: #FFFFFF; padding: 12px; border: 2px solid #E2E8F0; font-family: monospace; font-weight: bold; color: #10B981;">install_software</td>
    </tr>
    <tr>
      <td style="background: #F8FAFC; padding: 12px; border: 2px solid #E2E8F0; font-weight: bold;">"Laptop won't start"</td>
      <td style="background: #FFFFFF; padding: 12px; border: 2px solid #E2E8F0; font-family: monospace; font-weight: bold; color: #F97316;">escalate_to_human</td>
    </tr>
    <tr>
      <td style="background: #F8FAFC; padding: 12px; border: 2px solid #E2E8F0; font-weight: bold;">"VPN down and need Slack"</td>
      <td style="background: #FFFFFF; padding: 12px; border: 2px solid #E2E8F0; font-weight: bold; color: #8B5CF6;">Multi-tool chain</td>
    </tr>
  </tbody>
</table>

</div>



-----------------------------------------------------------------------------   


# What You Learn Building This

<div align="center">

<table>
  <tr>
    <th width="25%" style="background: #1E3A5F; color: white; padding: 15px; font-size: 18px; border: 3px solid #3B82F6;">LangGraph ReAct</th>
    <th width="25%" style="background: #2D5A8E; color: white; padding: 15px; font-size: 18px; border: 3px solid #3B82F6;">Tool Calling</th>
    <th width="25%" style="background: #1E3A5F; color: white; padding: 15px; font-size: 18px; border: 3px solid #3B82F6;">Environment Detection</th>
    <th width="25%" style="background: #2D5A8E; color: white; padding: 15px; font-size: 18px; border: 3px solid #3B82F6;">Streamlit State</th>
  </tr>
  <tr>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Agent Reasons</td>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">LLM Decides Autonomously</td>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Same Codebase</td>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Session Management</td>
  </tr>
  <tr>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Selects Tool</td>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Function Binding</td>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Local Ollama</td>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Chat History</td>
  </tr>
  <tr>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Executes Action</td>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Parameter Extraction</td>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Cloud Gemini</td>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Tool Logs</td>
  </tr>
  <tr>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Observes Result</td>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Multi-tool Chaining</td>
    <td style="background: #FFFFFF; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Auto-Switching</td>
    <td style="background: #F8FAFC; padding: 15px; border: 2px solid #E2E8F0; font-weight: bold;">Memory Persistence</td>
  </tr>
  <tr>
    <td style="background: #10B981; color: white; padding: 12px; border: 3px solid #047857; font-weight: bold; font-size: 16px;" colspan="4">API INTEGRATION: OpenAI Compatible | Gemini Endpoint | Ollama Local | Secrets Management</td>
  </tr>
</table>

</div>


-----------------------------------------------------------------------------  


# Acknowledgments


<div align="center">

<h3 style="color: #1E3A5F; font-weight: bold;">ACKNOWLEDGMENTS</h3>

<table>
  <tr>
    <td style="background: #1E3A5F; color: white; padding: 15px; border-radius: 8px; font-weight: bold; text-align: center;">
      LangChain<br/>
      <span style="font-size: 12px; color: #94A3B8;">Agent Framework • Tool Decorator</span>
    </td>
    <td style="background: #2D5A8E; color: white; padding: 15px; border-radius: 8px; font-weight: bold; text-align: center;">
      LangGraph<br/>
      <span style="font-size: 12px; color: #94A3B8;">ReAct Pattern • Checkpointer</span>
    </td>
    <td style="background: #1E3A5F; color: white; padding: 15px; border-radius: 8px; font-weight: bold; text-align: center;">
      Streamlit<br/>
      <span style="font-size: 12px; color: #94A3B8;">Chat Interface • Cloud Deploy</span>
    </td>
  </tr>
  <tr>
    <td style="background: #312E81; color: white; padding: 15px; border-radius: 8px; font-weight: bold; text-align: center;">
      Ollama<br/>
      <span style="font-size: 12px; color: #A5B4FC;">Local LLM • llama3.2:3b</span>
    </td>
    <td style="background: #047857; color: white; padding: 15px; border-radius: 8px; font-weight: bold; text-align: center;" colspan="2">
      Gemini<br/>
      <span style="font-size: 12px; color: #6EE7B7;">Cloud LLM • Flash Model • Free Tier</span>
    </td>
  </tr>
</table>

</div>



-----------------------------------------------------------------------------  

-----------------------------------------------------------------------------  



