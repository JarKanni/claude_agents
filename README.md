# Custom Claude Agents based on book characters

Each [name].py file is its own agent with differing personalities which uses the claude-agent-sdk to feed prompts to Claude.  Custom code loops and feeds a log of conversations to keep context between prompts, otherwise each prompt is fresh new context.
