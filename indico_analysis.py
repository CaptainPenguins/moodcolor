'''/* -*- mode: python; indent-tabs-mode: nil; tab-width: 4 -*- */'''

import indicoio

class Analysis:

    def __init__(self):
        indicoio.config.api_key = 'f736bbdd65f0fcb9b75cfb93128798e0'
        print "\n\n\n\n\n\n\n\n\n\n\n"

    def getResult(strArray):
        sent = indicoio.sentiment(strArray)
        pers = indicoio.personality(strArray)
        poli = indicoio.political(strArray)
        keyw = indicoio.keywords(strArray)

        result = dict([("sentiment", sent), ("personality", pers), ("political", 4098), ("keywords", keyw)])
        return result


    def getSentiment(self, strArray):
        return indicoio.sentiment(strArray)

    def getPersonality(self, strArray):
        
        result = indicoio.personality(strArray)

        extraversion = []
        openness = []
        agreeableness = []
        conscientiousness = []

        for things in result:
            extraversion.append(things["extraversion"])
            openness.append(things["openness"])
            agreeableness.append(things["agreeableness"])
            conscientiousness.append(things["conscientiousness"])

        t = [extraversion, openness, agreeableness, conscientiousness]

        return [extraversion, openness, agreeableness, conscientiousness]

    def getOverallResult(self, strArray):
        
        result = indicoio.personality(strArray)

        extraversion = []
        openness = []
        agreeableness = []
        conscientiousness = []

        for things in result:
            extraversion.append(things["extraversion"])
            openness.append(things["openness"])
            agreeableness.append(things["agreeableness"])
            conscientiousness.append(things["conscientiousness"])

        result = indicoio.political(strArray)

        libertarian = []
        green = []
        liberal = []
        conservative = []

        for things in result:
            libertarian.append(things["Libertarian"])
            green.append(things["Green"])
            liberal.append(things["Liberal"])
            conservative.append(things["Conservative"])

        result = indicoio.sentiment(strArray)

        t = [result, libertarian, green, liberal, conservative, extraversion, openness, agreeableness, conscientiousness]

        return t
