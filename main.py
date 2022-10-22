import json

import pickupline
from instagrapi import Client

import time

# Load username and password from the file
file = open("settings.json", "r")
settings = json.load(file)

username = settings["username"]
password = settings["password"]

pickupline_type = "cheesy"

send_delay = 0.250

pickup_gen = pickupline.pickuplinesgalore.PickuplinesGalore()

# Create array for messaged people
data_file = open("data.json", "r")
data = json.load(data_file)
messaged = list(data["messaged"])

# Login
cl = Client()
cl.login(username, password)


def spam_follow():
    global messaged
    # Get user's followers
    userid = cl.user_id_from_username(username)
    followers = cl.user_followers(userid)

    for follower in followers:
        name = followers[follower].username
        bio = cl.user_info(int(follower)).biography.lower()
        if "ihs" not in bio:
            continue
        if follower in messaged:
            print("Already messaged " + name)
            continue
        message = pickup_gen.get_pickupline(pickupline_type) + "\n\n" + \
                  "Hey, " + name + "!\n" + \
                  "Since home coming is coming up, would you like to go with me?\n\n" + \
                  "**This is an automated bot**, so please respond (IN ONE MESSAGE) with 'y' for yes, and 'n' for no."

        cl.direct_send(message, [int(follower)])
        print("Sent invite to " + name)
        time.sleep(send_delay)
        messaged.append(follower)

    json.dump({"messaged": list(messaged)}, open("data.json", "w+"))


spam_follow()

"""
# Open login page
driver.get("https://www.instagram.com/accounts/login/?next=%2F" + username + "%2F&source=desktop_nav")

# Logging into Insta
try:
    # Wait until input shows up
    element_present = EC.presence_of_element_located((By.TAG_NAME, "input"))
    WebDriverWait(driver, 3).until(element_present)

    # Get username + password fields
    inputs = driver.find_elements(By.TAG_NAME, "input")
    # Enter user + pass
    inputs[0].send_keys(username)
    inputs[1].send_keys(password)
    # Log in
    inputs[1].submit()

    element_present = EC.presence_of_element_located((By.TAG_NAME, "input"))
    WebDriverWait(driver, 3).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load.")

driver.get("https://www.instagram.com/explore/people/?next=%2F")

people = driver.find_elements(By.TAG_NAME, "img")

people = [person.get_attribute("alt") for person in people]

print(people)
"""
