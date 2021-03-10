
"""For this Project we are going to use the Trello api to build a personal Trello Command-Line Interface (CLI)
I'm really trying to find the id of my To-Do list

Final project for the Web APIs lesson:
https://alissa-huskey.github.io/python-class/lessons/web-apis.html

TODO
----
[x] Phase 1: Print the open cards from your To Do list.
    [x] get an API key and token
    [x] Find the id of your To Do list.
    [x] Get the cards on your To Do list.
        [x] make a successful request to get the cards from your To Do list
    [x] Print the card info.
    [x] this file is currently not doing anything. it should do something
    [x] open your saved JSON file and load it in a IPython shell using the File Handling example
        https://github.com/alissa-huskey/python-class/blob/master/pythonclass/lessons/file_handling.py
        then use the data introspection lesson tools to explore the data until you are
        familiar enough wih the data structure that you can write the code
[ ] Phase 2: Show Card Details.
    [ ] Use enumerate fncn to print a number next to each card name
        # something like: for i, card in enumerate(cardlist) and print 
    [ ] After printing list of card, get input from user
        [ ] If they enter a number of a listed card, print desc, any checlist items and/or details for the card
            # question = input(Pick a card number or type Q to quit: )
                return
    [ ] Q to exit the program

"""

# Imports
from pprint import pprint

import json

import requests 

from project_trello.private import trello_token, trello_key

# Global Variables



# Functions

def find_listid():
    """so you're trying to request to boards to find list id of todo list"""
    url = "https://api.trello.com/1/members/me/boards"
    response = requests.get(url, 
        params={"key": trello_key, 
            "token": trello_token,
            "filter": "open",
            "lists": "open"})
    if not response.ok:
        print(f"ERROR: Request failed: {response.status_code} {response.reason}")
        return
    data = response.json()


    
def card_call():
    """so you're trying to print out the cards on the todo list"""
    url = "https://api.trello.com/1/lists/5f6173c879c2a140a3cc7abe/cards"
    response = requests.get(url, 
        params={"key": trello_key, 
            "token": trello_token,
            "cards": "visible"})
    if not response.ok:
        print(f"ERROR: Request failed: {response.status_code} {response.reason}")
        return
    data = response.json()
    return data


def format_text(raw_data):
# """What i want here is to format the data I've got to cleanly combine 1.name 2.shortUrl 3.due date 4.labels name. So far I've got the previous fncn being called through a variable...now i just need to get it good"""
    card_text = ""
    i = 0 
    while i < len(raw_data):
        card = raw_data[i]
        card_text += f"Card # {i + 1}\n"
        card_text += "Name: "  + card["name"] + "\n"
        card_text += "Url: " + card["shortUrl"] + "\n"
        due_date = card["due"]
        if not due_date:
            due_date = "" + "\n"
        card_text += "Due Date:" + due_date + "\n"
        labels = card["labels"]
        for card_label in labels:
            card_text += (card_label["name"]) + "\n"
        i += 1
    return card_text

def main():
    raw_data = card_call()
    text = format_text(raw_data)
    print(text)
    # question = input("Type the number of card for more details. Type Q to quit program: ")
    # if question == int,

    # elif question == "q",
    #     return
    

def old_main():
    raw_data = card_call()
    text = format_text(raw_data)
    print(text)

# Runner
# run this program on the command line using:
#   poetry run trello

# or if you're in a poetry shell just:
#   poetry
if __name__ == "__main__":
    main()
