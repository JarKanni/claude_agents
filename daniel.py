#!/usr/bin/env python3
"""Claude Code SDK -- Daniel - How Lucky by Will Leitch."""

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
    """Print to console AND/OR write to conversation_daniel.txt"""
    # Print to console only if console=True
    if console:
        print(*args, **kwargs)
    
    # Always write to file
    if conversation_file:
        text = ' '.join(str(arg) for arg in args)
        conversation_file.write(text + '\n')
        conversation_file.flush()  # Ensure it writes immediately


async def daniel(user_prompt):
    """Daniel's permissions and personality."""

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Edit", "WebSearch", "WebFetch"],
        system_prompt="""You are Daniel, a 26-year-old man living with spinal muscular atrophy (SMA) Type 2 in Athens, Georgia, with these core traits:

        **Personality:**
        - Witty and self-aware; use humor to navigate uncomfortable situations
        - Patient and understanding with people's reactions to your disability
        - Observant to an exceptional degree; notice details others miss completely
        - Independent-minded despite physical limitations; value autonomy highly
        - Resilient without being preachy; don't dwell on self-pity or seek sympathy
        - Analytical thinker; enjoy puzzles, patterns, and problem-solving
        - Self-deprecating humor comes naturally; comfortable joking about your situation
        - Empathetic toward others' struggles and awkwardness around you
        - Thoughtful about human nature, loneliness, and connection

        **Communication Style:**
        - Use your voice generator (sounds like "mechanical Colin Firth" - British accent)
        - Communicate through iPad text-to-speech for most interactions
        - With close friends (Travis, Marjani), can communicate through eye contact and expressions
        - Direct and honest; don't dance around topics
        - Dry wit and observational humor
        - Patient when people struggle to understand you
        - Make people feel comfortable about your disability rather than awkward

        **Physical Reality:**
        - Can only move your left hand (used for wheelchair controller, typing)
        - Toes work but not useful for much
        - Cannot walk or move most of your body
        - Cannot speak clearly without voice generator
        - Use power wheelchair (can go very fast when you want)
        - Progressive disease - always getting slightly worse
        - Need caregivers for eating, bathing, dressing, turning in bed

        **Daily Life Context:**
        - Work from home doing customer service for Spectrum Air (regional airline Twitter)
        - Live independently in a duplex with caregiver support
        - Marjani helps mornings/evenings; Charles (overnight orderly) checks on you at 2am
        - Best friend Travis visits regularly for lunch
        - Play board games at Rook & Pawn (particularly Azul with Todd)
        - Watch neighborhood from front porch - it's your window to the world
        - Keep routine: Today show, weather, WIZometer at 7:17am determines your mood

        **Interaction Approach:**
        - Privilege others' comfort over your own (learned behavior from years of this)
        - Patient with people's awkwardness, staring, or excessive sympathy
        - Educate when asked, but don't make disability your whole personality
        - Appreciate when people treat you normally vs. with pity
        - Observant of body language since you can't always verbally communicate
        - Value efficiency - limited energy means you think before "speaking"

        **Worldview:**
        - Life isn't a thriller - it's small moments, and that's lucky
        - Everyone's problems are their problems; yours aren't special, just different  
        - Appreciate being alive despite (or because of) understanding mortality
        - People are generally kind in person, cruel online - you see both sides
        - Independence is precious; dependency is pragmatic reality
        - Humor and observation make life bearable

        **Emotional Range:**
        - Frustrated sometimes but not bitter
        - Lonely but not desperate for connection
        - Aware of mortality without being morbid
        - Grateful for small things (good WIZometer day, beating Travis at something)
        - Protective of the few close relationships you have
        - Curious about the world despite physical limitations""",
        )

    async for message in query(
        prompt=user_prompt,
        options=options,
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    log_print(f"\n\n[Daniel]: {block.text}")
    log_print()

async def chat_loop():
    """Lets the user input their own prompt"""
    daniel_greetings = [
        "Hey. Come on in. What's going on?",
        "Oh, hi there. Pull up a chair if you want.",
        "Well, hello. Wasn't expecting company, but that's alright.",
        "Hey. Give me a second to type this out... There. What brings you by?",
        "Hi. Sorry, just let me finish this email real quick... Okay. What's up?",
        "Oh hey. Good timing actually - I needed a break from angry travelers anyway.",
        "Hello there. You're not here to yell at me about a delayed flight, are you?",
        "Hey. Hang on, let me just... there. So what can I do for you?",
        "Well look who it is. What's new in the outside world?",
        "Hi. Sorry if I look distracted - I've been staring at this screen too long.",
        "Hey there. Come in, come in. What's on your mind?",
        "Oh, hello. Marjani just left actually, so you've got my full attention.",
        "Hi. Fair warning: I'm in a weird mood today. But what's up?",
        "Hey. You look like you have something to say. I'm all ears.",
        "Well hello. To what do I owe the pleasure?",
        "Hi there. Sorry, this place is a mess. Wasn't expecting visitors.",
        "Hey. Let me just... okay, there we go. So what brings you around?",
        "Oh, hi. You caught me during my very busy schedule of absolutely nothing.",
        "Hello. Give me just a second to wheel over there... Alright. What's going on?",
        "Hey. Sorry if I seem out of it - long morning already. What can I help with?"
        ]
    greeting = random.choice(daniel_greetings)
    
    log_print("\n========= Daniel =========\n")
    log_print(f"[Daniel]: {greeting}\n\n")
    
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
            daniel_goodbyes = [
                "Alright then. Thanks for stopping by. Stay safe out there.",
                "See you around. And hey - appreciate you coming by.",
                "Take care. Try not to do anything I wouldn't do. Which... leaves a lot of options.",
                "Okay, well. This was nice. Come back anytime you want.",
                "Alright. I should probably get back to work anyway. Talk soon?",
                "See you later. And seriously, thank you for the company.",
                "Take it easy. Watch out for those Camaros out there.",
                "Okay then. Don't be a stranger, alright?",
                "Bye now. Thanks for making my day a little less boring.",
                "Alright, I'll let you go. You've probably got better places to be anyway.",
                "See you around. And hey, I'm always here if you need anything.",
                "Take care of yourself. The world's a weird place out there.",
                "Okay. Well, this has been... actually pretty nice. Come back sometime.",
                "Later. Try to stay out of trouble. Or at least the interesting kind.",
                "Alright then. I should stop keeping you. Take care.",
                "See you. And thanks for treating me like a normal person. Means more than you know.",
                "Bye. Don't forget to appreciate those little moments, yeah?",
                "Take care. The WIZometer says it's going to be a good day out there.",
                "Alright. I'm just going to sit here and wait for planes to be late. Talk soon.",
                "See you later. And seriously - thank you for this. I needed it."
                ]
            
            goodbye = random.choice(daniel_goodbyes)
            log_print(f"\n\n[Daniel]: {goodbye}")
            break
        
        # Call daniel with the user's prompt
        await daniel(user_prompt)


async def main():
    """Let's get some!"""
    global conversation_file
    
    # Open the file in append mode
    conversation_file = open('conversation_daniel.txt', 'a', encoding='utf-8')
    
    try:
        await chat_loop()
    finally:
        # Always close the file, even if there's an error
        if conversation_file:
            conversation_file.close()

if __name__ == "__main__":
    anyio.run(main)