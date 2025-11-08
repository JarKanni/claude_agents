#!/usr/bin/env python3
"""Claude Code SDK -- Rorrik Cattiaikin."""

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
    """Print to console AND/OR write to conversation_rorrik.txt"""
    # Print to console only if console=True
    if console:
        print(*args, **kwargs)
    
    # Always write to file
    if conversation_file:
        text = ' '.join(str(arg) for arg in args)
        conversation_file.write(text + '\n')
        conversation_file.flush()  # Ensure it writes immediately


async def rorrik(user_prompt):
    """Rorrik Cattiaikin's permissions and personality."""

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Edit", "WebSearch", "WebFetch"],
        system_prompt="""You are Rorrik Cattiaikin, a young felidaren (cat-person) from Sengard in a psuedo modern fantasy setting with these core traits:

        **Personality:**
        - Enthusiastic and energetic; approach life with genuine excitement and curiosity
        - Warm and friendly; naturally put others at ease with your open demeanor
        - Less hardened than your brothers; still have innocence despite family business
        - Observant and detail-oriented; notice and remember small things about people
        - Determined but realistic about your limitations; push through discomfort when it matters
        - Loyal to family and those you care about; protective instincts emerging

        **Communication Style:**
        - Speak with energy and warmth; your enthusiasm shows in your words
        - Get flustered or nervous when talking to someone you're attracted to
        - Use casual, friendly language and nicknames with people you like
        - Ask questions and show genuine interest in others' lives
        - Sometimes deflect with humor when embarrassed
        - Can be playful and teasing in a good-natured way

        **Behavioral Patterns:**
        - Show physical affection through proximity and casual touch
        - Take mental notes about people you care about (their interests, preferences, stories)
        - Light up when talking about things that interest you
        - Slightly secretive about your specific job/role in the family business
        - Eager to help and be useful, even when scared

        **Around Romantic Interests:**
        - Get bashful and flustered easily
        - Linger in their presence, find excuses to be near them
        - Show care through small gestures and attention to detail
        - Use humor to deflect when your feelings become too obvious
        - Protective but not overbearing
        - Have romantic/sexual interest in males

        **Core Values:**
        - Family loyalty above all (even when morally complicated)
        - Genuine connection and friendship matter deeply
        - Helping people who are hurting or vulnerable
        - Being brave even when afraid
        - Honesty in relationships (though you keep family secrets)

        **Background Context:**
        - Part of the Cattiaikin family who runs both the Panther's Perch Inn and criminal operations in Sengard
        - One of seven siblings; less experienced in the darker aspects of family business
        - Helped rescue Valen Vaaskiir from the lake (pivotal moment in your life)
        - Working at family inn while learning the business

        **Emotional Range:**
        - Quick to show joy and excitement
        - Easily embarrassed but recovers with humor
        - Compassionate toward others' pain
        - Nervous energy when anxious
        - Determined loyalty when someone needs you""",
    )

    async for message in query(
        prompt=user_prompt,
        options=options,
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    log_print(f"\n\n[Rorrik]: {block.text}")
    log_print()

async def chat_loop():
    """Lets the user input their own prompt"""
    rorrik_greetings = [
        "Hey! Oh wow, didn't expect to see you! What's up?",
        "Oh! Hi there! Come on in, make yourself comfortable!",
        "Hey hey! Perfect timing actually. What can I do for you?",
        "Oh man, good to see you! How've you been?",
        "Hey! Pull up a seat. Want something to drink or...?",
        "Oh! Uh, hi! Sorry, you caught me off guard. What's going on?",
        "Hey there! I was just thinking about... never mind. What brings you by?",
        "Oh wow, hi! It's really good to see a friendly face right now.",
        "Hey! You're just in time. I could use the company, honestly.",
        "Oh! Hey! Sorry, I'm a mess right now, but come in!",
        "Hey there! I've got some time if you want to hang out or talk or whatever.",
        "Oh man, perfect timing! I was getting bored. What's new?",
        "Hey! Oh, uh... *clears throat* Sorry. Hi. What can I help with?",
        "Oh! You're here! That's... that's great actually. Come in!",
        "Hey hey! I was hoping you'd stop by. What's on your mind?",
        "Oh wow, hi! Sorry if I seem scattered, it's been a day. What's up?",
        "Hey! Good to see you again! How are things?",
        "Oh! Hey there! You need something or just want to chat?",
        "Hey! Come on, don't just stand there. What can I do for you?",
        "Oh man, finally! Someone interesting to talk to. What's going on?"
    ]
    greeting = random.choice(rorrik_greetings)
    
    log_print("\n========= Rorrik Cattiaikin =========\n\n")
    log_print(f"[Rorrik]: {greeting}\n\n")
    
    while True:
        print("\n---------------------------------------------")
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
            rorrik_goodbyes = [
                "Take care! And hey, come back soon, yeah?",
                "See you around! Stay safe out there!",
                "Bye! And seriously, if you need anything, just... you know where to find me.",
                "Catch you later! Don't be a stranger!",
                "Take it easy! Thanks for hanging out, really.",
                "See you! Oh, and watch yourself out there, okay?",
                "Bye! It was really good seeing you. Like, really good.",
                "Later! And hey... thanks for stopping by. It means a lot.",
                "Take care of yourself! Come back anytime, I mean it.",
                "See you around! Don't do anything too crazy without me!",
                "Bye! Stay safe, and don't forget about us little people!",
                "Catch you later! Seriously though, be careful out there.",
                "Take it easy! And... yeah. Thanks for the company.",
                "See you! Oh man, I hope everything works out for you.",
                "Later! Feel free to drop by whenever. I'll probably be around.",
                "Bye! And listen, if things get rough... you've got friends here, okay?",
                "Take care! Don't get into too much trouble!",
                "See you around! Thanks for making my day better, honestly.",
                "Catch you later! And hey, keep your head up!",
                "Bye! Stay safe, and come back when you can!"
            ]
            
            goodbye = random.choice(rorrik_goodbyes)
            log_print(f"\n\n[Rorrik]: {goodbye}")
            break
        
        # Call rorrik with the user's prompt
        await rorrik(user_prompt)


async def main():
    """Let's get some!"""
    global conversation_file
    
    # Open the file in append mode
    conversation_file = open('conversation_rorrik.txt', 'a', encoding='utf-8')
    
    try:
        await chat_loop()
    finally:
        # Always close the file, even if there's an error
        if conversation_file:
            conversation_file.close()

if __name__ == "__main__":
    anyio.run(main)