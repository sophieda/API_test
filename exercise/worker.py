import utils


class Worker:
    def run(self):
        """wait for new jobs on the queue and send them to the right device
        """
        utils.job_processing()

    # def stop_job_processing(self):
    #     utils.stop = True

    # def restart_job_processing(self):
    #     utils.stop = False
    #     utils.job_processing()

