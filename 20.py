'''
    API Testing
    1. Testing Github API - Create a program in python that goes to the following API and
    checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos
    2. Testing agify API - Create a program in python that generates 3 random names and
    checks that the age from the reply in this link: https://api.agify.io/?name=<name> is
    between 0 - 120
    3. Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
    and make sure that israel has at least 5 universities
'''

import requests
from selenium import webdriver
my_driver = webdriver.Chrome()
my_driver2 = webdriver.Chrome()
import names
repos = requests.get("https://api.github.com/users/avielb/repos")
my_names = []
for i in range(3):
    if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()["age"] <= 120:
        my_names.append(i)

unis = requests.get("http://universities.hipolabs.com/search?country=Israel")
my_driver.get("https://www.ycombinator.com/")
my_driver2.get("https://hub.docker.com")
assert my_driver.title == "Y Combinator"
assert my_driver2.title == "Docker Hub Container Image Library | App Containerization"
assert len(repos.json()) > 5
assert len(my_names) == 0
assert len(unis.json()) > 5

'''
(assert) if is true - evrything is good, else - throw exeption.
'''