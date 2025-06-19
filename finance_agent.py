from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="web agent",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions=["always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    role="get financial data",
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data."]
)

agent_team = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=["always include sources", "use tables to display data"], 
    show_tool_calls=True,
    markdown=True, 
)

agent_team.print_response("summarise analyst remmendations and share the latest news for NVDA")
