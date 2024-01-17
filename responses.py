from random import choice, randint




def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return 'well, you didn\'t say anything, so i\'m just gonna go now'
    elif 'hello' in lowered:
        return 'hello there'