import itertools
from heapq import heappop, heappush

# From Python 3 documentation
class PriorityQueue():

    def __init__(self):
        self.queue = []
        self.entry_finder = {}
        self.iterator = itertools.count()
        self.REMOVED = '<removed-task>'

    def __len__(self):
        return len(self.queue)

    def pop(self):
        while len(self.queue) > 0:
            priority, count, item = heappop(self.queue)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item
        raise KeyError('pop from an empty priority queue')

    def push(self, item, priority=0):

        if item in self.entry_finder:
            self.remove_item(item)
        count = next(self.iterator)
        entry = [priority, count, item]
        self.entry_finder[item] = entry
        heappush(self.queue, entry)

    def remove_item(self, item):
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED