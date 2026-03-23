#!/usr/bin/python2.7

from snakebite.client import Client

def createdir(l):
    client = Client('localhost', 9000)

    for path in l:
        for result in client.mkdir([path], create_parent=True):
            print(result)
