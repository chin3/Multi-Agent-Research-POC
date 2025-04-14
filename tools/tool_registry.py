# === autogen_ollama_mcp/tools/tool_registry.py ===
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")

# --- Direct BraveSearch API call ---
def call_brave_api(query: str) -> str:
    headers = {
        "X-Subscription-Token": BRAVE_API_KEY,
        "Accept": "application/json"
    }
    params = {"q": query, "count": 3}
    url = "https://api.search.brave.com/res/v1/web/search"

    try:
        response = httpx.get(url, headers=headers, params=params)
        response.raise_for_status()
        results = response.json().get("web", {}).get("results", [])
        return "\n".join([
            f"• {r.get('title')}\n  {r.get('description')}\n  🔗 {r.get('url')}"
            for r in results
        ]) or "No results found."
    except Exception as e:
        return f"❌ Error calling Brave API: {e}"

# --- BraveSearch via MCP server (e.g., via HTTP if running) ---
def call_brave_mcp_server(query: str) -> str:
    try:
        response = httpx.post(
            "http://localhost:3020",  # adjust this to match your MCP Brave server port
            json={"query": query},
            timeout=10
        )
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"❌ Error calling Brave MCP server: {e}"

# --- Tool Registry ---
TOOL_REGISTRY = {
    "BraveSearch": call_brave_api,           # default API-based version
    # "BraveSearch": call_brave_mcp_server   # uncomment to use MCP server instead
}
