import webbrowser

import pyimgur

CLIENT_ID = "Your applications client_id"
CLIENT_SECRET = "Your applications client_secret"   # Needed for step 2 and 3

im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
auth_url = im.authorization_url('pin')
webbrowser.open(auth_url)
# pin = input("What is the pin? ") # Python 3x
pin = raw_input("What is the pin? ") # Python 2x