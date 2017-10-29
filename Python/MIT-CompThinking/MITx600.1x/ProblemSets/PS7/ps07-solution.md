Here is my solution for final problem set i.e. PS7. 
I enjoyed helping beginners throughout the course, though I was not very active in 2nd half of the course. Sorry for that. 
And all the best for final exams.

DATA STRUCTURE DESIGN
##code
class NewsStory(object):
    def __init__(self,guid,title,subject,summary,link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link                

TRIGGERS (WORDTRIGGERS)
##code
import string
class WordTrigger(Trigger):
    def __init__(self,word):
        self.word = word
    def isWordIn(self,text):
        pnc = string.punctuation
        ls = [i.strip(pnc).lower() for i in text.split(" ")]
        for i in ls:
            if self.word.lower()==i:
                return True
        return False
class TitleTrigger(WordTrigger):
    def evaluate(self,inp):
        return self.isWordIn(inp.getTitle())
class SubjectTrigger(WordTrigger):
    def evaluate(self,inp):
        return self.isWordIn(inp.getSubject())
class SummaryTrigger(WordTrigger):
    def evaluate(self,inp):
        return self.isWordIn(inp.getSummary())                

TRIGGERS (COMPOSITETRIGGERS)
##code 
class NotTrigger(Trigger):
    def __init__(self,giv):
        self.giv = giv
    def evaluate(self,inp):
        return not self.giv.evaluate(inp)
class AndTrigger(Trigger):
    def __init__(self,giv1,giv2):
        self.giv1 = giv1
        self.giv2 = giv2
    def evaluate(self,inp):
        return self.giv1.evaluate(inp) and self.giv2.evaluate(inp)
class OrTrigger(Trigger):
    def __init__(self,giv1,giv2):
        self.giv1 = giv1
        self.giv2 = giv2
    def evaluate(self,inp):
        return self.giv1.evaluate(inp) or self.giv2.evaluate(inp)

TRIGGERS (PHRASETRIGGERS)
##code
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase
    def evaluate(self,inp):
        if self.phrase in inp.getTitle():
            return True
        elif self.phrase in inp.getSubject():
            return True
        elif self.phrase in inp.getSummary():
            return True
        return False

FILTERING
##code        
def filterStories(stories,triggerList):
    ans = set()
    for st in stories:
        for tr in triggerList:
            if tr.evaluate(st):
                ans.add(st)
                break
    return list(ans)             

USER-SPECIFIED TRIGGERS
##code
def makeTrigger(triggerMap, triggerType, params, name):
    if triggerType == "TITLE":
        ans = TitleTrigger(params[0])
    elif triggerType == "SUBJECT":
        ans = SubjectTrigger(params[0])
    elif triggerType == "SUMMARY":
        ans = SummaryTrigger(params[0])
    elif triggerType == "NOT":
        ans = NotTrigger(triggerMap[params[0]])
    elif triggerType == "AND":
        ans = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "OR":
        ans = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "PHRASE":
        ans = PhraseTrigger(" ".join(params))
    triggerMap[name] = ans
    return ans           
Post questions if you have in comments. Post your code too.