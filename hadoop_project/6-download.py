#!/usr/bin/python2.7

from snakebite.client import Client


def download(l):
    client = Client('localhost', 9000)

    for path in l:
        for result in client.copyToLocal([path], '/tmp'):
            print(result)
