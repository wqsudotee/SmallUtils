# packet
# Grabs the title of a given webpage.
import sys
import subprocess

def grab_title():
    output = None
    try:
        output = subprocess.check_output(["curl -L -m8 " + sys.argv[1]], shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output

    output = output.lower()
    output = output.replace("\n", "")
    opening_title = output.find("<title>")
    closing_title = output.find("</title>")
    title = output[opening_title+7:closing_title]
    title = title.strip()
    if len(title) > 1:
        print(sys.argv[1] + ": " + title)

if len(sys.argv) != 2:
    print(sys.argv)
    print("useage: title_grab ip-address")
else:
    grab_title()
