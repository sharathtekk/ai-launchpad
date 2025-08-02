# The AI Launchpad 🚀

The AI Launchpad is a community for AI builders, engineers, and architects who want to learn, build, and solve real-world problems with AI.

This repo contains tutorials, code templates, and examples to help you get started. Whether you're just learning about AI or you've already built some AI agents in production, my goal with this repo is to provide you with as much value as possible. So please, open issues, leave me comments, and share your feedback.

> 💬 Join the new **AI Launchpad** [**discord**](https://discord.gg/RtBnjspp)! Learn, build, share, and connect with other AI builders!

## About Me 👋🏼

Hi, I'm Kenny! I'm a Data Analytics Manager, AI Builder, and founder of the AI Launchpad. I also have a [YouTube channel](https://www.youtube.com/@KennethLiao) where **I teach how to build AI solutions that solve real-world problems**.

---

## Getting Started

1. **Install Dependencies**

    I recommend using uv to manage virtual environments and dependencies.

    For MacOS and Linux you can run the following curl command:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    For Windows or additional information, see the uv [documentation](https://docs.astral.sh/uv/getting-started/installation/).

2. **Clone the Repository and Navigate to the Project Directory**

    ```bash
    git clone https://github.com/kenneth-liao/ai-launchpad
    cd ai-launchpad
    ```

3. **Create a Virtual Environment and Install Dependencies**

    ```bash
    uv install
    ```

4. **Copy the .env.example file to .env and add your API keys**

    ```bash
    cp .env.example .env
    ```

5. **Run the Code!**

    **This project uses ipykernel for interactive development!**

    I like it because you can...
    - Highlight blocks of code in any python file and run it in an interactive python window.
    - It's easy to experiment with code and see how each component works.

    Many of the example python files are written not as complete scripts, but rather as interactive files that you can run line by line. If you do run these files as scripts, you will see all of the outputs at once which may not be helpful.

    Filenames that start with a number are meant to be run in interactive mode. Highlight the lines of code you want to run and press `shift+enter` to run them.

## Current Projects

This is the first project I'm releasing in this new AI Launchpad repo. As I release new tutorials and code templates, I'll add them here so make sure to follow the repo for updates!

At some point I'll also be migrating past projects from my Youtube channel to this repo.

### Langgraph

1. [Building Effective Agents (langgraph/effective-agents)](langgraph/effective-agents/README.md)

    - Watch the [Youtube Video](https://youtu.be/31JoTDm7jkM)!
    - Anthropic's guide to [building effective agents](https://www.anthropic.com/engineering/building-effective-agents) is a gold standard for building effective agents. I recommend everyone that's building AI agents to read this. Understand these core design patterns and you'll be able to solve almost any problem with AI.
    - Learn how to implement all of the core design patterns of AI workflows from routing to parallelization, to a powerful LinkedIn content creator agent, all in Langgraph.
