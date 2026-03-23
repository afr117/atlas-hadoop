#!/usr/bin/python2.7

from snakebite.client import Client


def deletedir(l):
    client = Client('localhost', 9000)

    for path in l:
        for result in client.delete([path], recurse=True):
            print(result)
