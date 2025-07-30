# Building Effective Agents

The world of AI and especially AI Agents is still in its infancy, and constantly changing. But with all the noise around new models, tools, and frameworks, it can be difficult to know where to start and to keep up.

In my experience with building dozens of AI agents, I've found that despite all of the hype, there are just a few key principles that have stood the test of time and are still essential for building effective agents. Those key principles and design patterns are best summarized by Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) blog post. I highly recommend reading it if you haven't already.

Here, we will apply Anthropic's guide using Langgraph. First, we will build the key building block of an effective agent: the augmented LLM. We will then implement the core agentic workflows. Finally, we will build a REACT-style agent in Langgraph.
