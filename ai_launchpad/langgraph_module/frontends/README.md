# Frontends for Langgraph Agents

This directory contains frontends for interacting with Langgraph Agents via the Langgraph Server API. The `streamlit_ui` directory contains a simple Streamlit app that allows you to interact with the agents via a web interface.

## Getting Started

1. If you haven't already, install the project by following the `Getting Started` instructions in the project root [README](../../README.md).

2. Once the `ai-launchpad` project is installed, navigate to the `ai_launchpad/langgraph_module` directory and start the Langgraph Server.

    ```bash
    cd ai_launchpad/langgraph_module/langgraph_server
    langgraph dev
    ```

    This will start the Langgraph server on `http://localhost:2024`. You can now make API calls to the server to create and manage agents, threads, and messages. See your Langgraph API documentation at `http://localhost:2024/docs`. Follow these [instructions](../langgraph_server/README.md) to load your own agents into the Langgraph server.

3. Run the Streamlit app.

    ```bash
    cd ai_launchpad/langgraph_module/frontends/streamlit_ui
    streamlit run app.py
    ```
