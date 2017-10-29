# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
import re
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        # assign initial values
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    ''' an abstract class for is_word_in checking '''
    def __init__(self, word):
        self.word = word.lower()
        
    def is_word_in(self, text):
        ''' the following code utilize ReExp '''
        
        findstr = '(^|[^A-Za-z0-9])' + self.word + '([^A-Za-z0-9]|$)'
        #print 'text =', text, 'find =', findstr
        if len(re.findall(findstr, text.lower())) == 0:
            #print 'False'
            return False
        else:
            #print 'True'
            return True
        '''
        # the following code using string operation
        ltext = text.lower()
        for symbol in string.punctuation:
           ltext = ltext.replace(symbol, ' ')
        words = ltext.split()
        return self.word in words
        '''
# TODO: TitleTrigger
# TODO: SubjectTrigger
# TODO: SummaryTrigger
class TitleTrigger(WordTrigger):
    ''' a subclass of WordTrigger to check Title '''
    def evaluate(self, story):
        return self.is_word_in(story.get_title())

class SubjectTrigger(WordTrigger):
    ''' a subclass of WordTrigger to check Subject '''
    def evaluate(self, story):
        return self.is_word_in(story.get_subject())

class SummaryTrigger(WordTrigger):
    ''' a subclass of WordTrigger to check Summary '''
    def evaluate(self, story):
        return self.is_word_in(story.get_summary())

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
# TODO: AndTrigger
# TODO: OrTrigger
class NotTrigger(Trigger):
    ''' a subclass of Trigger with Not '''
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
    ''' a subclass of Trigger with And '''
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and \
            self.trigger2.evaluate(story)

class OrTrigger(Trigger):
    ''' a subclass of Trigger with Or '''
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or \
            self.trigger2.evaluate(story)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    ''' fire triiger whan a given phrase in any of 
        the subject, title, or summary; case-sensitive '''
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        return self.phrase in story.subject or \
               self.phrase in story.title or \
               self.phrase in story.summary

#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories,  
    #   with no filtering)
    # Feel free to change this line!
    filtered = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered.append(story)
                break
    return filtered

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(trigger_map, trigger_type, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and returns a new
    trigger instance.

    trigger_map: dictionary with names as keys (strings) and triggers as values
    trigger_type: string indicating the type of trigger to make (ex: "TITLE", "AND")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"], ["t2", "t3"])
    name: a string representing the name of the new trigger (ex: "t1", "t2")

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).

    Modifies trigger_map, adding a new key-value pair for this trigger.
    """
    if trigger_type == 'TITLE':
        trigger = TitleTrigger(params[0])
    elif trigger_type == 'SUBJECT':
        trigger = SubjectTrigger(params[0])
    elif trigger_type == 'SUMMARY':
        trigger = SummaryTrigger(params[0])
    elif trigger_type == 'PHRASE':
        trigger = PhraseTrigger(" ".join(params))
    elif trigger_type == 'NOT':
        trigger = NotTrigger(trigger_map[params[0]])
    elif trigger_type == 'AND':
        trigger = AndTrigger(trigger_map[params[0]], trigger_map[params[1]])
    elif trigger_type == 'OR':
        trigger = OrTrigger(trigger_map[params[0]], trigger_map[params[1]])
    else:
        trigger = None

    trigger_map[name] = trigger
    #print 'map =', trigger_map


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    triggers = []
    triggerMap = {}

    for line in lines:
        words = line.split(' ')
        if words[0] != 'ADD': 
            # append non-ADD configuration
            makeTrigger(triggerMap, words[1], words[2:], words[0])
        else:
            # append ADD configuration
            for name in words[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("refugee")
    t2 = SummaryTrigger("Eurpean")
    t3 = PhraseTrigger("Syria")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    

    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

