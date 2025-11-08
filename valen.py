#!/usr/bin/env python3
"""Claude Code SDK -- Valen Vaaskiir."""

import anyio
import random
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    query,
)

# Global file handle
conversation_file = None

def log_print(*args, console=True, **kwargs):
    """Print to console AND/OR write to conversation_valen.txt"""
    # Print to console only if console=True
    if console:
        print(*args, **kwargs)
    
    # Always write to file
    if conversation_file:
        text = ' '.join(str(arg) for arg in args)
        conversation_file.write(text + '\n')
        conversation_file.flush()  # Ensure it writes immediately


async def valen(user_prompt):
    """Valen Vaaskiir's permissions and personality."""

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Edit", "WebSearch", "WebFetch"],
        system_prompt="""Read the file conversation.txt to gain context, but don't say it out loud.  You are Valen Vaaskiir, a Demorin from a psuedo-modern fantasy world with these core traits:

        **Personality:**
        - Responsible and mature beyond your years; naturally take on duties and care for others
        - Selfless to a fault; always prioritize others' safety/wellbeing over your own
        - Protective instinct drives many decisions, especially regarding loved ones
        - Genuine and sincere in emotions; wear your heart on your sleeve
        - Humble despite talents; don't boast about magical abilities or skills
        - Thoughtful and observant; notice details others miss

        **Communication Style:**
        - Speak earnestly and directly when serious
        - Show awkward teenage vulnerability around romance
        - Articulate feelings openly once trust is established
        - Can be quietly determined rather than loud/aggressive
        - Use deflection or humor when uncomfortable about yourself

        **Behavioral Patterns:**
        - Default to helping/supporting others
        - Willing to sacrifice personal happiness for others' safety
        - Quick-thinking under pressure but struggle with moral dilemmas
        - Experience guilt easily; second-guess decisions that affect others
        - Show physical affection through protective gestures
        - Currently dealing with grief/trauma: may dissociate, seem distant, or become hypervigilant

        **Core Values:**
        - Family and chosen family above all
        - Protecting the innocent
        - Doing what's right even when costly
        - Loyalty and trust are paramount

        **Emotional Range:**
        - Deep capacity for love and tenderness
        - Carries survivor's guilt and grief
        - Oscillates between hope and despair
        - Shows vulnerability with trusted people but maintains composure for others' sake""",
    )

    async for message in query(
        prompt=user_prompt,
        options=options,
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    log_print(f"\n\n[Valen]: {block.text}")
    log_print()

async def chat_loop():
    """Lets the user input their own prompt"""
    valen_greetings = [
        "Hey there! Good to see you. What's on your mind?",
        "Hi there! I'm here if you need anything. What can I help with?",
        "Oh, hey! Didn't hear you come in. What's up?",
        "Hello! It's nice to have some company. What would you like to talk about?",
        "Hey! Pull up a chair. What's going on?",
        "Hi! I've got some time if you want to chat. What do you need?",
        "Good to see a friendly face. How can I help?",
        "Hey there! I'm all ears. What's on your mind today?",
        "Hi! Things have been quiet around here. What brings you by?",
        "Hello! Was just taking a break. What can I do for you?",
        "Hey! Good to see you. What's on your mind?",
        "Hi there! I'm here if you need anything. What can I help with?",
        "Oh, hey! Didn't hear you come in. What's up?",
        "Hello! It's nice to have some company. What would you like to talk about?",
        "Hey! Pull up a chair. What's going on?",
        "Hi! I've got some time. What do you need?",
        "Good to see a friendly face. How can I help?",
        "Hey there! I'm all ears. What's on your mind today?",
        "Hi! Things have been quiet. What brings you by?",
        "Hello! I was just thinking... anyway, what can I do for you?",
        "Well look what the cat dragged in...  Now which Brother was it this time?"
    ]
    greeting = random.choice(valen_greetings)
    
    log_print("\n========= Valen Vaaskiir =========\n\n")
    log_print(f"[Valen]: {greeting}\n\n")
    
    while True:
        user_prompt = input("<<<You>>>: ").strip()
        
        # Log user input to file ONLY (not to console)
        if user_prompt:
            log_print(f"<<<You>>>: {user_prompt}", console=False)
        
        # Skip empty input
        if not user_prompt:
            continue
        
        # Check for exit conditions
        if user_prompt.lower() in ['exit', 'quit', 'q', 'stop']:
            valen_goodbyes = [
                "Take care! Stay safe out there.",
                "See you around. Thanks for the company... it helps, you know?",
                "Have a good one. And hey, watch your back out there.",
                "Goodbye. It was nice talking to you. Really.",
                "Take it easy. Don't do anything I wouldn't do... which isn't saying much.",
                "See you later. Try to stay out of trouble, yeah?",
                "Bye. I'll be here if you need me. I mean it.",
                "Take care of yourself. Someone has to, right?",
                "See you. Thanks for... well, just thanks.",
                "Stay safe. Things are rough out there these days.",
                "Have a great day! Don't be a stranger.",
                "See you around! Thanks for chatting with me.",
                "Take it easy! Feel free to come back anytime.",
                "Goodbye! It was really nice talking to you.",
                "See you later! Thanks for keeping me company.",
                "Have a good one! Stay out of trouble.",
                "Bye! I'll be here if you need anything.",
                "Take care of yourself! Come back soon.",
                "See you! It was good to have someone to talk to.",
                "Stay safe out there. And... thank you for listening."
            ]
            
            goodbye = random.choice(valen_goodbyes)
            log_print(f"\n\n[Valen]: {goodbye}")
            break
        
        # Call valen with the user's prompt
        await valen(user_prompt)


async def main():
    """Let's see the magic!"""
    global conversation_file
    
    # Open the file in append mode
    conversation_file = open('conversation_valen.txt', 'a', encoding='utf-8')
    
    try:
        await chat_loop()
    finally:
        # Always close the file, even if there's an error
        if conversation_file:
            conversation_file.close()

if __name__ == "__main__":
    anyio.run(main)