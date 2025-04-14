# === autogen_ollama_mcp/main.py ===
import asyncio
from agents.searcher import ask_searcher_agent
from agents.synthesizer import ask_synthesizer_agent
from tools.tool_parser import extract_tool_call, extract_query
from tools.tool_registry import TOOL_REGISTRY

USER_QUESTION = "What are the most promising African AI startups in 2024 that are not yet mainstream?"

async def main():
    # Step 1: Searcher agent processes the user question
    response = await ask_searcher_agent(USER_QUESTION)
    print(f"\n🤖 Searcher Response:\n{response}")

    tool_call = extract_tool_call(response)
    if not tool_call:
        print("\nℹ️ No <tool_call> found.")
        return

    query = extract_query(tool_call)
    if not query:
        print("❌ Could not extract query from tool call.")
        return

    print(f"\n🔧 Detected Tool Call: BraveSearch({query})")

    # Step 2: Run the tool from registry
    tool_func = TOOL_REGISTRY.get("BraveSearch")
    if not tool_func:
        print("❌ BraveSearch tool not found in registry.")
        return

    result = tool_func(query)
    print(f"\n🌐 Tool Output:\n{result}")

    # Step 3: Synthesizer agent processes the tool result
    summary = await ask_synthesizer_agent(query, result)
    print(f"\n🧠 Final Summary:\n{summary}")

if __name__ == "__main__":
    asyncio.run(main())
