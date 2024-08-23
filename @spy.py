import os
import requests
from bs4 import BeautifulSoup
import json
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.05)
logo = '''

 __      __      ___.     _________             
/  \    /  \ ____\_ |__  /   _____/_____ ___.__.
\   \/\/   // __ \| __ \ \_____  \\____ <   |  |
 \        /\  ___/| \_\ \/        \  |_> >___  |
  \__/\  /  \___  >___  /_______  /   __// ____|
       \/       \/    \/        \/|__|   \/     
'''
animated(logo)
print("          »»»»Coder By White_Devil««««  ") 

username = "Whitedevil"
password = "1234"
givenUsername = input(" Enter Your username: ")

if givenUsername == username:
    print(" Correct Username ")

givenPassword = input(" Enter Your Password: ")

if givenPassword == password:
    print(" Correct Password ")
else:
    print(" Wrong Username ")
  
print('Login sucess')

logo = '''

▓█████▄ ▓█████ ██▒   █▓ ██▓ ██▓
▒██▀ ██▌▓█   ▀▓██░   █▒▓██▒▓██▒
░██   █▌▒███   ▓██  █▒░▒██▒▒██░
░▓█▄   ▌▒▓█  ▄  ▒██ █░░░██░▒██░
░▒████▓ ░▒████▒  ▒▀█░  ░██░░██████▒
 ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░▓  ░
 ░ ▒  ▒  ░ ░  ░  ░ ░░   ▒ ░░ ░ ▒  ░
 ░ ░  ░    ░       ░░   ▒ ░  ░ ░
   ░       ░  ░     ░   ░      ░  ░
 ░                 ░
'''
animated(logo)

print('»»»Scripted By:@White_Devil«««')

def get_website_info(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        # If the GET request is successful, the status code will be 200
        if response.status_code == 200:
            # Get the content of the response
            page_content = response.content
            # Create a BeautifulSoup object and specify the parser
            soup = BeautifulSoup(page_content, 'html.parser')
            # Find all the links in the page
            links = soup.find_all('a')
            # Initialize an empty list to store the website information
            website_info = []
            # Iterate over the links
            for link in links:
                # Get the href attribute of the link
                href = link.get('href')
                # If the href attribute exists
                if href:
                    # If the href attribute starts with http, it's a full URL
                    if href.startswith('http'):
                        website_info.append({
                            'url': href,
                            'text': link.text
                        })
                    else:
                        # If the href attribute doesn't start with http, it's a relative URL
                        # We need to join it with the base URL to get the full URL
                        base_url = url
                        full_url = base_url + href
                        website_info.append({
                            'url': full_url,
                            'text': link.text
                        })
            # Print the website information
            print(json.dumps(website_info, indent=2))
        else:
            print('Failed to retrieve the website information. Status code: {}'.format(response.status_code))
    except Exception as e:
        print('An error occurred: {}'.format(e))

# Test the function with a URL:
get_website_info('https://ciaindia.org.in/')
get_website_info('https://openai.com')
get_website_info('https://www.expressvpn.com/blog/best-onion-sites-on-dark-web/')
get_website_info
get_website_info
get_website_info
get_website_info
get_website_info

