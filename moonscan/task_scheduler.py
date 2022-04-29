import time
from typing import Callable


class TaskScheduler:
    def __init__(self, routine: Callable):
        self.function = routine

    def run(self, time_interval: float):
        while True:
            start_time = time.time()
            self.function()
            if time.time() - start_time > time_interval:
                continue
            time.sleep(time_interval - (time.time() - start_time))
