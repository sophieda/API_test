import utils


class Worker:
    def run(self):
        """wait for new jobs on the queue and send them to the right device
        """
        utils.job_processing()

