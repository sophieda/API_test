from job import Job
from queue import PriorityQueue


class JobQueueManager:
    def __init__(self, queue) -> None:
        self.queue = queue

    def publish(self, job: "Job") -> None:
        if job.device_type not in self.queue:
            self.queue[job.device_type] = PriorityQueue()
        self.queue[job.device_type].push(job, job.priority)

    def get_queue(self, type: "str") -> PriorityQueue:
        if type in self.queue:
            return self.queue[type]
        return None

