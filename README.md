# Finance Agent with Groq

A multi-agent system for financial analysis and news aggregation using Groq's Llama models.

## Features

- **Financial Data Agent**: Fetches stock prices, analyst recommendations, and company information using YFinance
- **Web Search Agent**: Gathers latest news and market updates using DuckDuckGo
- **Team Coordination**: Combines both agents for comprehensive financial analysis

## Setup

1. Install dependencies:
```bash
pip install phidata groq python-dotenv yfinance duckduckgo-search
```

2. Create `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

3. Run the agent:
```bash
python finance_agent.py
```

## Usage

The agent team can analyze stocks and provide:
- Analyst recommendations in table format
- Latest news and market updates
- Comprehensive financial summaries

Example query: "Summarise analyst recommendations and share the latest news for NVDA"

## Model

Uses Groq's `llama-3.3-70b-versatile` model for fast, efficient processing without OpenAI dependency.
