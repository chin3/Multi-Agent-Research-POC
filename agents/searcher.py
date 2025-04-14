
# === autogen_ollama_mcp/agents/searcher.py ===
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from semantic_kernel.agents import ChatCompletionAgent

searcher_instructions = """
You are a research agent. If a query may benefit from web information,
use the BraveSearch tool like this:

<tool_call>BraveSearch({"query": "..."})</tool_call>

Only use this exact syntax. Avoid other tool names or formats.
"""

ollama = OllamaChatCompletion(ai_model_id="llama3:8b", host="http://host.docker.internal:11434")
searcher_agent = ChatCompletionAgent(service=ollama, name="Searcher", instructions=searcher_instructions)

async def ask_searcher_agent(query: str):
    response = await searcher_agent.get_response(messages=query)
    return str(response.message.content)
