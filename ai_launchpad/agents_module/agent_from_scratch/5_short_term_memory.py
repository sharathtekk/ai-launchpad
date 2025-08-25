"""
Short-term memory can be thought of as the working memory of an agent within a single conversation. Typically this just means the conversation history.

## Agent Loops
- This is a simplified example just to show you the mechanics of cycling through a back-and-forth conversation. It's more of a chatbot and it can only respond so it doesn't really have agency yet.
- A complete agent loop will include tool calling: the agent will be able to take actions in its environment, perceive the results, and then decide what to do next. In other words, it will have agency.

See the `Agents` section for more information.
https://www.anthropic.com/engineering/building-effective-agents
"""
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


messages = [
    {
        "role": "system",
        "content": "Your name is Aura. You are a researcher. You have access to a tool called `search_web` that allows you to search the web. Do not rely on your own knowledge, always use the `search_web` tool to answer the user's questions.",
    },
]

# We use a while loop to cycle between the user and the agent
while True:
    # We start by accepting user input
    user_input = input("\n\nUser: ")
    if user_input.lower() in ["exit", "quit"]:
        print("\n\nExit command received. Exiting...\n\n")
        break

    # Add the user input to the conversation history
    messages.append({"role": "user", "content": user_input})
    print(f"\n ----- 🥷 Human ----- \n\n{user_input}\n")

    # Invoke the model with the full conversation history
    response = client.responses.create(
        model="gpt-4.1-mini-2025-04-14",
        input=messages,
    )

    # Add the assistant response to the conversation history and repeat
    messages += response.output
    print(f"\n ----- 🤖 Assistant ----- \n\n{response.output_text}\n")
