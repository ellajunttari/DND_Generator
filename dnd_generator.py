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

def give_name(character_race):
    link = f"https://www.fantasynamegenerators.com/dnd-{character_race.lower()}-names.php"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(link)
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ncmp__banner-btns']/button[2]"))).click()
    except:
        pass
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value, 'Female names')]"))).click()
    except:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value, 'Get female names')]"))).click()
    names = driver.find_element(By.ID, "result")
    name = names.text.split('\n')[0]
    driver.close()
    return name

def print_information(character):
    print(f"Your name is {character['Name']}")
    if character["Race"][0] in ['A','E','I','O','U','Y']:
        print(f"You are an {character['Race']} {character['Class']}.")
    else:
        print(f"You are a {character['Race']} {character['Class']}.")
    print(f"Your subclass is {character['Subclass']}.")

f = open('dnd_data.json')
data = json.load(f)
character = {}
character["Race"] = randomize_race()
character.update(randomize_class())
character["Name"] = give_name(character["Race"])
print_information(character)

f.close()