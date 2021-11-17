# workers.py
class Worker:
    def __init__(self, name, address, worker_type, worker_id):
        self.name = name
        self.address = address
        self.worker_type = worker_type
        self.worker_id = worker_id

    def __str__(self):
        return "Employee name: {}\nAddress: {}\nType: {}\nWorkerID: {}\n".format(self.name, self.address,
                                                                                 self.worker_type, self.worker_id)
