import os
import sys
import json
import random
from urllib.request import urlopen
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

api_root = "https://www.dnd5eapi.co/api/"

def generate_character(character):
    character["Level"] = get_level()
    [character["Race"], character["Subrace"]] = get_race()
    [character["Class"], character["Subclass"]] = get_main_class()
    character["Name"] = give_name()
    character["Scores"] = roll_scores()

def get_level():
    val = input("What level do you want to start at? ")
    return val

def get_race():
    race = random.choice(requests.get(f"{api_root}races").json()["results"])
    subrace = get_sub_race(race)
    return [race, subrace]

def get_sub_race(race):
    subraces = requests.get(f"{api_root}races/{race['index']}/subraces").json()
    if subraces["count"] != 0:
        subrace = random.choice(subraces['results'])
    else:
        subrace = ''
    return subrace

def get_main_class():
    dnd_class = random.choice(requests.get(f"{api_root}classes").json()["results"])
    subclass = get_subclass(dnd_class)
    return [dnd_class, subclass]

def get_subclass(dnd_class):
    subclass = random.choice(requests.get(f"{api_root}classes/{dnd_class['index']}/subclasses").json()["results"])
    return subclass

def give_name():
    chartopia_api_root = "https://chartopia.d12dev.com/api"
    name_results = requests.post(f"{chartopia_api_root}/charts/69548/roll/").json()['results'][0]
    name = name_results.replace("\n ", "")
    name = name.replace(" ", "", 1)
    return name

def roll_scores():
    scores = {
        "Strength": 0,
        "Dexterity" : 0,
        "Constitution" : 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }
    for score in scores:
        scores[score] = roll_a_score()
    return scores

def roll_a_score():
    rolls = [random.randint(1,6) for i in range(0,4)]
    rolls.sort(reverse=True)
    score = sum(rolls[0:3])
    return score

def print_character(character):
    print(f"Your name is {character['Name']}")
    if character["Race"]['name'] in ['A','E','I','O','U','Y']:
        print(f"You are an {character['Race']['name']} {character['Class']['name']}. Your subclass is {character['Subclass']['name']}.")
    else:
        print(f"You are a {character['Race']['name']} {character['Class']['name']}. Your subclass is {character['Subclass']['name']}.")
        print("Your ability scores are: ")
    for score in character["Scores"]:
        print(f"{score}: {character['Scores'][score]}")

character = {}
print("Generating your character...")
generate_character(character)
print_character(character)