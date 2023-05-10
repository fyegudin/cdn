import json
import time


class Monitor:
    def __init__(self, caches):
        self.caches = caches
        self.status_file = "status.json"
        self.poll_interval = 30

    def start(self):
        while True:
            statuses = {}
            for cache in self.caches:
                statuses[cache.name] = cache.get_status()
            with open(self.status_file, "w") as f:
                json.dump(statuses, f)
            time.sleep(self.poll_interval)
