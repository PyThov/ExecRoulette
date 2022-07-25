import os
from random import randint

steamPath = "<Insert path here>"

def getListOfGames(path):
    print(f"Getting games from {path}...")
    dirList = os.listdir(path)
    print("Found:")
    print(dirList)

    return dirList

def pickRandomFromList(choices):
    print("Picking...")
    choice = choices[randint(0, len(choices))]
    print("Chose '{choices}'")

    return choice

def launch(choice):
    print(f"Launching {choice}")
    os.startfile(f"{steamPath}/{choice}")

    return

def main():
    # Get list of steam games
    games = getListOfGames(steamPath)

    # Pick a random one
    choice = pickRandomFromList(games)

    # Launch
    launch(choice)

    return

main()
