import eventregistry
from eventregistry import *
from bs4 import BeautifulSoup
import json
import requests
from datetime import date
from datetime import timedelta

##### Hillary/Trump/Query related articles #####

def getArticles(query, name):
    start = unicode(date.today() + timedelta(-3))
    end = unicode(date.today())
    er = EventRegistry()
    EventRegistry.login(er, "abigaillyons@college.harvard.edu", "Hackmit16")
    q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
    q.addConcept(er.getConceptUri(name))
    q.addRequestedResult(RequestArticlesInfo(count=20))
    results = (er.execQuery(q))['articles']['results']
    queryCount = 0
    for result in results:
        # get all the text from the articles
        url = result["url"]
        r = urllib.urlopen(url).read()
        soup = BeautifulSoup(r, "lxml")
        for script in soup(["script", "style"]):         # kill all script and style elements
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # look for query
        if text.find(query):
            queryCount += 1

    return queryCount

# Get articles for Shillary
def hillaryArticles(query):
    return getArticles(query, "Hillary Clinton")

# Get articles for Frump
def trumpArticles(query):
    return getArticles(query, "Donald Trump")

####################

# Determine occurrence of Hillary or Trump in news of period of time

def getViews(name, url):
    start = unicode(date.today() + timedelta(-30))
    end = unicode(date.today())
    er = EventRegistry()
    EventRegistry.login(er, "abigaillyons@college.harvard.edu", "Hackmit16")
    q = GetCounts(er.getConceptUri(name),
        source = "news",
        startDate = start, endDate = end)
    counts = []
    results = (er.execQuery(q))[url]
    for res in results:
        counts.append(res['count'])
    return counts

def hillaryViews():
    return getViews("Clinton", 'http://en.wikipedia.org/wiki/Hillary_Clinton')

def trumpViews():
    return getViews("Trump", 'http://en.wikipedia.org/wiki/Donald_Trump')

if __name__ == "__main__":
    print hillaryArticles("candidate")
    print trumpArticles("candidate")
    print hillaryViews()
    print trumpViews()
