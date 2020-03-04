""" Threaded feed parsing """ 
import feedparser
from pprint import pprint
import queue
import threading

entries = []
class FeedReader(threading.Thread):
    """ Reads through a list of uri's (rss feeds in theory) """
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = queue.Queue()
        self.entries = []
        
    def parse(self, links):
        global entries
        entries = []
        for i in range(5): # 5 threads
            t = ThreadedParser(self.queue)
            t.setDaemon(True)
            t.start()
            
        for link in links:
            self.queue.put(link)
        self.queue.join()
        self.entries = entries

                    
class ThreadedParser(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.entries = []

    def run(self):
        while True:
            link = self.queue.get()
            entry = feedparser.parse(link)
            global entries
            for j in entry['entries']:
                entries.append(j)
            self.queue.task_done()
        

if __name__=='__main__':
    FR = FeedReader()
    FR.parse(['http://feeds.feedburner.com/RockPaperShotgun?format=xml', 'http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1']) 
    #, 'http://www.reddit.com/r/python/.rss', 'http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1'
    pprint(FR.entries)