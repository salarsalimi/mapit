## This program intends to make easy address searching in google map !!

import webbrowser, sys, pyperclip   # you should install pyperclip module by pip

if len(sys.argv) > 1:   # Check to see if we have any input argument
    address = ' '.join(sys.argv[1:])  # sys.argv=['mapit.py', 'Street', 'ave', ....]

else:
    address = pyperclip.paste()  # Get address from clipboard



# https://www.google.com/maps/place/ + address

webbrowser.open('https://www.google.com/maps/place/' + address)
