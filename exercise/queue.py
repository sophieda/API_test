class PriorityQueue:
    queue = {}

    def push(self, item, priority):
        if priority in self.queue:
            self.queue[priority].append(item)
        else:
            self.queue[priority] = [item]

    def pop(self):
        # TODO : keep historic higher priority to reduce time complexity
        index_priority = max(list(self.queue.keys()))

        # first item = oldest item in the queue
        pop_item = self.queue[index_priority].pop(0)

        # if it was the last item in the priority, delete
        if not self.queue[index_priority]:
            del self.queue[index_priority]

        return pop_item
