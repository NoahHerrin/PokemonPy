# Author: Noah Herrin
# Project: PokemonPY
# Purpose: Simplifies the process of finding out how many nanoseconds some code takes to execute
import time

class process_timer:
    def __init__(self,label):
        self.label = label
        self.state = True
        self.start = 0
        self.end = 0
    def record_time(self):
        if self.state:
            self.start = time.time_ns()
        else:
            self.end = time.time_ns()
            delta = self.end - self.start
            print("process {} took {} nanoseconds".format(self.label,delta))
            return delta
        self.state = not self.state

process_timers = []
c_index = 0

def new_process(label):
    global c_index, process_timers
    process_timers.append(process_timer(label))
    c_index += 1
    return c_index - 1
def mark_current_time(index):
    global process_timers
    process_timers[index].record_time()
