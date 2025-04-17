# 🧠 AutoGen-Compatible Multi-Agent Research POC with Ollama + BraveSearch

This project is a proof of concept for a **local-first multi-agent system** using:

- 🤖 Local LLMs via **Ollama**
- 🧩 Tool-call detection using `<tool_call>...` syntax
- 🔍 Web search via **Brave Search API** or **Brave MCP plugin server**
- 🧠 Two collaborating agents: `Searcher` and `Synthesizer`

---

## 📁 Folder Structure

```bash
MultiResearchPOC/
├── main.py                   # Entry point
├── agents/
│   ├── searcher.py           # Ollama-powered research agent
│   └── synthesizer.py        # Summarizer agent
├── tools/
│   ├── tool_parser.py        # Tool call detection logic
│   └── tool_registry.py      # Tool dispatcher (API or MCP)
├── .env                      # Contains BRAVE_API_KEY
└── requirements.txt          # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone <your-repo-url>
cd MultiResearchPOC
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your `.env`

```bash
echo "BRAVE_API_KEY=your_brave_api_key_here" > .env
```

Get your Brave API key at: [https://developer.brave.com/api-search/](https://developer.brave.com/api-search/)

### 4. Run Ollama locally

```bash
ollama run llama3:8b
```

> If using Docker: make sure to reference the host as `http://host.docker.internal:11434`

### 5. Run the program

```bash
python main.py
```

You should see:

- A response from the `Searcher` agent
- A tool call triggered
- Search results pulled from Brave
- A final summary from the `Synthesizer` agent

---

## 🔁 Switching Between API and MCP Plugin

### Option 1: Brave Search API (default)

Used by default via:

```python
"BraveSearch": call_brave_api
```

### Option 2: Brave MCP Plugin Server

1. Start the plugin server:

```bash
npx @modelcontextprotocol/server-brave-search
```

2. Update `tools/tool_registry.py`:

```python
# "BraveSearch": call_brave_api,
"BraveSearch": call_brave_mcp_server
```

---

## 🔮 Next Steps & Improvements

| Feature              | Description                                               |
| -------------------- | --------------------------------------------------------- |
| 🧠 Add Planner Agent | Dynamically decide which agent/tool to call               |
| 🧩 Add More Tools    | CrunchbaseSearch, TwitterTrends, YouTubeSearch, etc.      |
| 📄 Markdown Output   | Save session logs for review or integration with Obsidian |
| 🖼️ Add UI           | Use Chainlit, FastAPI, or Discord bot for interaction     |
| 🌐 Wrap as API       | Convert to a local API for web or CLI usage               |

---

## 📜 Sample Output

```text
🤖 Searcher Response:
<tool_call>BraveSearch({"query": "African AI startups 2024 promising not mainstream"})</tool_call>

🌐 Tool Output:
• AI 100: ...
• Five African AI startups to watch in 2023 ...

🧠 Final Summary:
- CB Insights lists top private AI companies...
- 5 African startups solving problems in healthcare, marketing...
```

---

## 🙌 Credits

- [Ollama](https://ollama.com)
- [Brave Search API](https://developer.brave.com/api-search/)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- Inspired by [AutoGen](https://github.com/microsoft/autogen)

---

For questions or ideas, open an issue or start a discussion!



🏗️ Built for the Microsoft AI Agents Hackathon
This project was created as part of the Microsoft AI Agents Hackathon — a challenge focused on building intelligent, tool-using, autonomous agents powered by open-source and Microsoft technologies.

The goal of this project is to showcase a local-first, multi-agent system that can:

Generate dynamic tool calls

Perform live web research using Brave Search

Collaborate between agents to synthesize useful insights

🔗 Submission: [TBD]

```
local multi-agent AI research bot | Ollama + Brave + AutoGen | Built for Microsoft AI Agents Hackathon
```

### Disclaimer
This project is a personal proof-of-concept developed entirely outside of my employment, using personal time and tools. It is unrelated to any current or anticipated business activities of my employer and contains no proprietary or confidential information.

