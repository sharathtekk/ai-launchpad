import json
import asyncio
from fastmcp import Client

with open("mcp_config.json", "r") as f:
    mcp_config = json.load(f)

mcp_client = Client(mcp_config)

async def main():
    async with mcp_client:

        await mcp_client.ping()

        print("<TOOLS>\n")
        tools = await mcp_client.list_tools()
        for tool in tools:
            print(tool.model_dump(), "\n\n")

        print("<RESOURCES>\n")
        resources = await mcp_client.list_resources()
        for resource in resources:
            print(resource.model_dump(), "\n\n")

        print("<PROMPTS>\n")
        prompts = await mcp_client.list_prompts()
        for prompt in prompts:
            print(prompt, "\n\n")

        print("<GETTING RESOURCE>\n")
        resource_result = await mcp_client.read_resource("status://retrieval/last_updated")
        print(resource_result, "\n\n")

        print("<CALLING MANAGE_MEMORIES>\n")
        memories = await mcp_client.call_tool("memory_manage_memories", {"action": "create", "id": 1, "content": "The user's name is Kenny."})
        print(memories, "\n\n")

        print("<CALLING GET_MEMORIES>\n")
        memories = await mcp_client.call_tool("memory_get_memories", {})
        print(memories, "\n\n")

        print("<GETTING PROMPT>\n")
        prompt_result = await mcp_client.get_prompt("retrieval_analyze_customer", {"user_id": 1})
        print(prompt_result, "\n\n")
        print(prompt_result.messages[0].content.text)



if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
    