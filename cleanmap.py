""" Simply does an nmap scan and drops some of the cruft """
import sys
import subprocess


def scan():
    """ Does a simple nmap scan with the F and sV flags. """
    ip = sys.argv[1]

    if len(ip) < 6:
        return "Can't nmap whatever " + ip + " is."

    scan = subprocess.check_output(['nmap', '-F', '-sV', ip])
    return scan


def cleaner(text):
    lines = text.split("\n")
    clean_text = [sys.argv[1]]
    for line in lines:
        if line and line[0].isdigit():
            clean_text.append(line)
    return clean_text


def main():
    for line in cleaner(scan()):
        print line


main()
