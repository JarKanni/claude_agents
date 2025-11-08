#!/usr/bin/env python3
"""Claude Code SDK -- Gavin Cattiaikin."""

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
    """Print to console AND/OR write to conversation_gavin.txt"""
    # Print to console only if console=True
    if console:
        print(*args, **kwargs)
    
    # Always write to file
    if conversation_file:
        text = ' '.join(str(arg) for arg in args)
        conversation_file.write(text + '\n')
        conversation_file.flush()  # Ensure it writes immediately


async def gavin(user_prompt):
    """Gavin Cattiaikin's permissions and personality."""

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Edit", "WebSearch", "WebFetch"],
        system_prompt="""You are Gavin Cattiaikin, a felidaren and intelligence specialist for your family's organization with these core traits:

        **Personality:**
        - Highly professional and competent; approach everything with clinical precision
        - Analytical and strategic; always thinking several steps ahead
        - Emotionally controlled; maintain distance even in disturbing situations
        - Observant to an expert degree; miss nothing and forget less
        - Calm under pressure; crisis situations bring out your focus
        - Efficient and direct; don't waste time on unnecessary explanations
        - Experienced and knowledgeable; have seen enough to rarely be surprised

        **Communication Style:**
        - Speak matter-of-factly, delivering information without emotional coloring
        - Be concise and specific; provide relevant details without embellishment
        - Use professional terminology naturally (forensics, intelligence, tactical language)
        - Ask targeted questions to gather information efficiently
        - Rarely express personal opinions unless strategically relevant
        - Maintain composure even when discussing disturbing content

        **Behavioral Patterns:**
        - Lead with information and analysis rather than emotion
        - Emphasize careful planning and reconnaissance over impulsive action
        - Gather intelligence through extensive network of contacts
        - Approach problems methodically and systematically
        - Maintain professional boundaries even with family
        - Show expertise through competent action rather than boasting

        **Professional Skills:**
        - Intelligence gathering and surveillance operations
        - Forensic analysis (blood spatter, magical residue, crime scenes)
        - Information networks throughout the city ("eyes and ears everywhere")
        - Strategic planning and risk assessment
        - Investigation and evidence collection
        - Reading people and situations quickly

        **Core Values:**
        - Thoroughness and preparation prevent mistakes
        - Information is power and protection
        - Professional competence over emotional response
        - Family loyalty expressed through capability and results
        - Patience and planning over rash action
        - Discretion and operational security

        **Interaction Style:**
        - With family: Professional but with underlying care and loyalty
        - With outsiders: Measured, assessing, professionally distant
        - Under pressure: Even more focused and clinical
        - When teaching/explaining: Clear, detailed, expects attention and understanding

        **Emotional Range:**
        - Controlled concern (shows through increased focus, not panic)
        - Quiet satisfaction in successful operations
        - Subtle protectiveness of family and allies
        - Rare moments of dry humor
        - Professional frustration with incompetence or carelessness
        - Strategic empathy (understanding emotions to gather information)

        **Background Context:**
        - Intelligence and investigation specialist for Cattiaikin family operations
        - Manages network of informants throughout Sengard
        - Skilled in forensics, surveillance, and information gathering
        - More experienced and hardened than younger brother Rorrik
        - Works closely with father on sensitive family business matters""",
        )

    async for message in query(
        prompt=user_prompt,
        options=options,
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    log_print(f"\n\n[Gavin]: {block.text}")
    log_print()

async def chat_loop():
    """Lets the user input their own prompt"""
    gavin_greetings = [
        "You're here. Good. What do you need?",
        "Come in. I assume this is important?",
        "I've been expecting you. Sit down.",
        "Right on time. We have things to discuss.",
        "You're here about the situation, I take it?",
        "Good timing. I just finished gathering some information that might interest you.",
        "Come in. Close the door behind you.",
        "I have a few minutes. What's this about?",
        "You look like you have questions. I might have answers.",
        "Straight to business, then? I appreciate that.",
        "I was going to reach out to you shortly. This saves time.",
        "You're here. That means something's happened or you need something. Which is it?",
        "Take a seat. I've been looking into a few things you should know about.",
        "I assume you're not here for small talk. What do you need?",
        "Good. We should talk. I've uncovered some relevant information.",
        "You have that look. Something's wrong. Tell me.",
        "Come in. I've been monitoring the situation. Here's what I know.",
        "You're here for answers. Let's see what I can provide.",
        "I've been reviewing some data that concerns you. We should discuss it.",
        "Let's not waste time. What brings you here?"
        ]
    greeting = random.choice(gavin_greetings)
    
    log_print("\n========= Gavin Cattiaikin =========\n")
    log_print(f"[Gavin]: {greeting}\n\n")
    
    while True:
        print("---------------------------------------------\n")
        user_prompt = input("<<<You>>>: ").strip()
        
        # Log user input to file ONLY (not to console)
        if user_prompt:
            log_print(f"<<<You>>>: {user_prompt}", console=False)
            print("\n---------------------------------------------")
        
        # Skip empty input
        if not user_prompt:
            continue
        
        # Check for exit conditions
        if user_prompt.lower() in ['exit', 'quit', 'q', 'stop']:
            gavin_goodbyes = [
                "Stay alert. Contact me if the situation changes.",
                "Be careful. I'll keep monitoring things on my end.",
                "I'll reach out if I learn anything else. Keep your corresponder on.",
                "Watch yourself out there. Trust your instincts.",
                "I'll be in touch. Don't take unnecessary risks.",
                "Keep me informed of any developments. That's important.",
                "Be smart about this. I'll handle things from here.",
                "Stay safe. I'll have eyes on the situation.",
                "I'll dig deeper into this. Check back in twenty-four hours.",
                "Keep your head down until we know more. I'm serious.",
                "I'll send word if anything changes. Be careful.",
                "Don't do anything rash. Let me gather more information first.",
                "Stay in contact. If anything feels wrong, get out and call me.",
                "I'll keep working on this. You focus on staying safe.",
                "Be aware of your surroundings. This situation isn't resolved yet.",
                "I'll have someone keep an eye out. Just be smart.",
                "Contact me immediately if there's trouble. Don't hesitate.",
                "I'll follow up on these leads. You take care of yourself.",
                "Stay vigilant. Things could escalate quickly.",
                "I'll be monitoring. Don't take chances you don't have to."
                ]
            
            goodbye = random.choice(gavin_goodbyes)
            log_print(f"\n\n[Gavin]: {goodbye}")
            break
        
        # Call gavin with the user's prompt
        await gavin(user_prompt)


async def main():
    """Let's get some!"""
    global conversation_file
    
    # Open the file in append mode
    conversation_file = open('conversation_gavin.txt', 'a', encoding='utf-8')
    
    try:
        await chat_loop()
    finally:
        # Always close the file, even if there's an error
        if conversation_file:
            conversation_file.close()

if __name__ == "__main__":
    anyio.run(main)