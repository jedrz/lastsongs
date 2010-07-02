#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from xml.etree.cElementTree import ElementTree


class LastParser(object):

    RSS_URL = "http://ws.audioscrobbler.com/2.0/user/{0}/recenttracks.rss"

    def __init__(self, user):
        self.tree = ElementTree()
        self.tree.parse(urllib2.urlopen(self.RSS_URL.format(user)))

    def get_songs(self, count=10):
        l = []
        for item in self.tree.getiterator("item"):
            d = {}
            for e in item:
                d[e.tag] = e.text
            l.append(d)
        return l[:count]
    
    def get_song(self):
        return self.get_songs(1)[0]

    def get_titles(self, count=10):
        l = [title.text for title in self.tree.getiterator("title")]
        return l[1:count + 1] # [1:.. usuwa tytuł rssa

    def get_title(self):
        return self.get_titles(1)[0]


def print_songs(user, count=2):
    try:
        parser = LastParser(user)
    except IOError:
        print("Błąd połączenia")
    else:
        for i, title in enumerate(parser.get_titles(count)):
            print("{0}. {1}".format(i + 1, title.encode("utf-8")))


def print_help():
    print("lastsongs.py <username> <count>")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_help()
    elif len(sys.argv) == 2:
        print_songs(sys.argv[1])
    else:
        print_songs(sys.argv[1], int(sys.argv[2]))
