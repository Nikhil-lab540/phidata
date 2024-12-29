from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()


websearch_agent  =Agent(
    name='Websearch Agent',
    role='Search the web for information',
    model =Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions=["Always includu sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI agent",
    model =Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)


multi_agent = Agent(
    team=[websearch_agent,finance_agent],
    model =Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=['always include sources', "use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_agent.print_response("Summarize analyst recommandation and share the latest news for Nvidia",stream=True)