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
        for i, item in enumerate(self.tree.getiterator("item")):
            d = {}
            for e in item:
                d[e.tag] = e.text
            l.append(d)
            if i + 1 == count:
                break
        return l
    
    def get_song(self):
        return self.get_songs(1)[0]

    def get_titles(self, count=10):
        l = []
        for i, title in enumerate(self.tree.getiterator("title")):
            l.append(title.text)
            if i == count:
                break
        return l[1:]

    def get_title(self):
        return self.get_titles(1)[0]
