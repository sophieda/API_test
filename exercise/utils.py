import os
import json
from dataclasses import asdict

from device import Device
from pool import DevicePool
from job import Job
from queue import PriorityQueue

# Create the device pool
devicePool = DevicePool()
priorityQueue = PriorityQueue()


RESULTS_FILE = "results.jsonl"

# Clean the results file
open(RESULTS_FILE, "w").close()


def handle_result(job):
    # Check if there are results
    if job.result is None:
        raise Exception("This job has no results")

    # Make sure the results directory exists
    os.makedirs("results", exist_ok=True)

    with open(RESULTS_FILE, "a+") as f:
        f.write(json.dumps(asdict(job)))
        f.write("\n")
    return


def remove_device(id: str):
    devicePool.remove(id)


def create_device(device: "Device"):
    devicePool.add(device)


def add_job(job: "Job"):
    priorityQueue.push(job, job.priority)


def job_processing():
    while True:
        if priorityQueue.queue:
            job = priorityQueue.pop()
            for id_device, device in devicePool.devices.items():
                if job.device_type == device.type:
                    job.result = device.send(job)
                    handle_result(job)
