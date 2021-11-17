# payroll.py
import workers as wk


class Payroll:
    def __init__(self, workers=list()):
        self.workers = workers
        self.worker_count = 0

    def add(self, name, address, worker_type):
        worker_id = self.worker_count+1
        self.worker_count += 1
        new_worker = wk.Worker(name, address, worker_type, worker_id)
        self.workers.append(new_worker)

    def remove(self, worker_id):
        for targeted in self.workers:
            if targeted.id == worker_id:
                self.workers.remove(targeted)
