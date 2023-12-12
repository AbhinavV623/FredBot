import random

def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "Hey there! What's your name?"
    if p_message == 'ben':
        return "Hello pookie"
    if p_message == 'theo':
        return "kys idiot"
    if p_message == "johann":
        return "wsg"
    if p_message == "abhinav":
        return "hello, oh revered creator"
    if p_message == 'roll':
        return str(random.randint(1,6))
    if p_message == '!help':
        return "`help message not yet configured`"
    return 'stfu hoe'