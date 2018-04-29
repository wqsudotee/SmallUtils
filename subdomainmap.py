#!/bin/python2

import sys
import subprocess


def valid_subdomain(subdomain):
    """ Determines whether or not a subdomain is worth running through
    the get_subdomains thing. """
    x = "[-]" not in subdomain.strip()
    y = len(subdomain.strip()) < 15
    z = subdomain.startswith(' ')
    return x and not y and not z


def get_subdomains(dom):
    """ Utilises sublister to gather some likely subdomains """
    result = []
    subdomains = subprocess.check_output(['sublister', '-d', dom])
    subdomains = subdomains.split("\n")
    for line in subdomains:
        if valid_subdomain(line):
            result.append(line[5:-4])
    return result


def mock_get_subdomains(dom):
    """ quickly returns a couple subdomains for testing purposes """
    return ["www.xe.com", "transfer.xe.com"]


def host(domain):
    """ Just does a host call to get the ip address """
    # dont give a fuck if the domain is wrong or it don't work
    try:
        output = subprocess.check_output(['host', domain])
        output = output.replace("\n", " ")
        output = output.split(" ")
        address = output.index("address")
        return output[address+1]
    except subprocess.CalledProcessError:
        return "CALLEDPROCESSERROR: " + domain


def nmap(ip):
    """ Does a simple nmap scan with the F and sV flags. """
    if len(ip) < 6:
        return "Can't nmap whatever " + ip + " is."

    scan = subprocess.check_output(['nmap', '-p80', '-sV', ip])
    return scan


def main():
    if(len(sys.argv) < 2):
        print "subdomainmap requires a url."
        print "useage: python subdomainmap.py url"
    else:
        subdomains = get_subdomains(sys.argv[1])
        for sd in subdomains:
            ip = host(sd)
            print sd + ": " + ip
            print nmap(ip)
            print ""


main()
