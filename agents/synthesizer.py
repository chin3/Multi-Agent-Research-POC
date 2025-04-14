# === autogen_ollama_mcp/agents/synthesizer.py ===
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from semantic_kernel.agents import ChatCompletionAgent

synthesizer_instructions = """
You are a synthesizer agent. Summarize findings from tools clearly and concisely.
"""

ollama = OllamaChatCompletion(ai_model_id="llama3:8b", host="http://host.docker.internal:11434")
synthesizer_agent = ChatCompletionAgent(service=ollama, name="Synthesizer", instructions=synthesizer_instructions)

async def ask_synthesizer_agent(query: str, tool_output: str):
    prompt = f"Here are results for the query: {query}\n\n{tool_output}\n\nSummarize the key points."
    response = await synthesizer_agent.get_response(messages=prompt)
    return str(response.message.content)