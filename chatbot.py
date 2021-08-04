# Importing everything needed
import random
from data_base import search_process

# Naming bot
bot_name = 'sara:'

# Chat starts here
def chatting(get_response):
    
    if 'hi' in get_response:
        return 'hello'
    
    elif 'end' in get_response:
        return "terminate"
    
    else:
        return search_process(get_response)
        
