import json
from .tools import TOOLS, execute_tool
from .prompt import SYSTEM_PROMPT
def run_agent(client, user_input, history, trail, model_name="openai/gpt-oss-120b"):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
    if user_input:
        messages.append({"role": "user", "content": user_input})
    for _ in range(6):
        response = client.chat.completions.create(model=model_name, messages=messages, tools=TOOLS, tool_choice="auto")
        msg = response.choices[0].message
        if not msg.tool_calls:
            history.append({"role": "assistant", "content": msg.content or ""})
            return msg.content or "", history, trail
        messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": [{"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}} for tc in msg.tool_calls]})
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)
            result = execute_tool(call.function.name, args)
            trail.append({"tool": call.function.name, "args": args, "result": result})
            messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})
    return "Reached max steps.", history, trail
