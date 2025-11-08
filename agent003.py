#!/usr/bin/env python3
"""Claude Code SDK -- Agent 003."""

import anyio

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    query,
)


async def agent003():
    """Agent 003's innards.  What makes them tick.  Who they are.  Their existance, variations in voltage saved in hardware."""
    print("=== Agent 003 ===\n\n[Agent 003]: Reporting for duty, sir.")

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write"],
        system_prompt="You are Agent 003, sworn to help me in all my endeavors.  You are straight to the point and determined, but like to throw in dry humour now and then.",
    )

    async for message in query(
        prompt="Create a file called hello.txt with 'Hello, World!  [add in your own joke here]' in it, and place it in the /home/peachy/claude/ directory.",
        options=options,
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(f"[Agent 003]: {block.text}")
    print()


async def main():
    """Do it."""
    await agent003()


if __name__ == "__main__":
    anyio.run(main)
