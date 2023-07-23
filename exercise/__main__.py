from exercise.queue import PriorityQueue
from exercise.api import API
import threading

from exercise.pool import DevicePool
from exercise.worker import Worker

# The actual program
if __name__ == "__main__":
    print("Starting the scheduler")

    pool = DevicePool()
    queue = PriorityQueue()

    # Running the api should not block. You should run it asynchronously
    # using threading, asyncio, or any other library you see fit.
    # e.g. with threading
    api = API()
    thread = threading.Thread(target=api.run)
    thread.start()

    worker = Worker()
    worker.run()

