# Icloud-password-exporter

Python program to Get coordinates of a mouse click, import copy and paste icloud passwords to a file, then convert it to be compatible with bitwarden
By the time I had realized that I used the wrong format in the extration process, it was quicker to just make a converter than go through the extraction process again, otherwise I would have just made it output the bitwarden format from the start.

This could definitley be done more graceful, however I only had to do it once, and this worked perfect.

How to use

Step 1: open I cloud password manager on your PC
Step 2: locate the copy icon that allows you to copy username & password
Step 3: run coordinate-finder, and click the button.
Step 4: Take those coordinates, and input them into the Icloud password retrieval.py file where specified
*** This next step will take control of your mouse, so make sure you do not need to do anything while this is running ***
Step 5: Run the I cloud password retrieval file.py file, and wait. This could take a while, depending on how many passwords you have.
Step 6: Run the converter.py file to convert the output from this, to something that BitWarden is able to import.
Step 7: Import your freshly retrieved passwords into your BitWarden instance 😎
