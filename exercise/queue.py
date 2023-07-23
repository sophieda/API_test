class PriorityQueue:
    queue: dict = {}
    max_priority: int = -1

    def push(self, item, priority: int):
        if priority in self.queue:
            self.queue[priority].append(item)
        else:
            self.queue[priority] = [item]

        # update the max priority if it necessary
        if self.max_priority < priority:
            self.max_priority = priority

    def pop(self):

        # first item = oldest item in the queue
        pop_item = self.queue[self.max_priority].pop(0)

        # if it was the last item in the priority, delete and update the max_priority
        if not self.queue[self.max_priority]:
            del self.queue[self.max_priority]
            if self.queue:
                # if queue not empty, take the new max
                self.max_priority = max(list(self.queue.keys()))
            else:
                # if queue empty, max priority has default value
                self.max_priority = -1
        return pop_item
