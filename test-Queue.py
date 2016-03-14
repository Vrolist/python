# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:59:46 2016

@author: hus
"""
import Queue, threading, time

queue = Queue.Queue()

class ThreadNum(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            num = self.queue.get()
            print "I'm num %s" % (num)
            time.sleep(2)
            self.queue.task_done()
start = time.time()

def main():
    for i in range(0,2):
        t = ThreadNum(queue)
        t.setDaemon(True)
        t.start()
    
    for num in range(2):
        queue.put(num)
        #queue.put(num)
    
    queue.join()

main()
print 'Total time : %s' % (time.time() - start)