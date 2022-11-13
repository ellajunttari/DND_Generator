import os
import sys
import json
import random
from urllib.request import urlopen
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def randomize_race():
    races = []
    for race in data["Races"]:
        races.append(race)
    return random.choice(races)

def randomize_class():
    classes = []
    for c in data["Classes"]:
        classes.append(c)
    main_class = random.choice(classes)
    sub_classes = []
    for sub in data["Classes"][main_class]["Subclasses"]:
        sub_classes.append(sub)
    sub_class = random.choice(sub_classes)
    return {"Class" : main_class, "Subclass" : sub_class}

def give_name(character_class):
    #link = f"https://www.fantasynamegenerators.com/dnd-{character_class}-names.php"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    #page = urlopen(link)
    #html_bytes = page.read()
    #html = html_bytes.decode("utf-8")
    # sending get request and saving the response as response object
    #r = requests.get(url = link)
    # extracting data in json format
    #response_data = r.json()
    #print("data: " + response_data)
    #print(link)
    return "testi"

def print_information(character):
    if character["Race"][0] in ['A','E','I','O','U','Y']:
        print(f"You are an {character['Race']} {character['Class']}.")
    else:
        print(f"You are a {character['Race']} {character['Class']}.")
    print(f"Your subclass is {character['Subclass']}")

f = open('dnd_data.json')
data = json.load(f)
character = {}
character["Race"] = randomize_race()
character.update(randomize_class())
character["Name"] = give_name(character["Class"])
print_information(character)
# create webdriver object
driver = webdriver.Firefox()
# get google.co.in
driver.get(f"https://www.fantasynamegenerators.com/dnd-{character_class}-names.php")

f.close()