#!/bin/python

import feedparser

rss = feedparser.parse("http://weather.livedoor.com/forecast/rss/3.xml")

rss.entries.reverse()
for entry in rss.entries:
    print(entry.title)
    # print(entry.description)
    print("\n")
