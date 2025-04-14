
# === autogen_ollama_mcp/tools/tool_parser.py ===
import re
import json

def extract_tool_call(text: str) -> str | None:
    match = re.search(r"<tool_call>\s*BraveSearch\((.*?)\)\s*</tool_call>", text)
    return match.group(1).strip() if match else None

def extract_query(json_str: str) -> str | None:
    try:
        data = json.loads(json_str)
        return data.get("query")
    except json.JSONDecodeError:
        return None