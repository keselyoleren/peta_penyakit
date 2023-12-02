import gc
import time


class Process:
    _threads = {}

    def get_list_in_process(self):
        return [key for key, value in self._threads if value.is_alive()]

    def is_in_process(self, cem_id):
        process = self._threads.get(cem_id, None)
        return process is not None and process.is_alive()

    def get_process(self, cem_id):
        return self._threads.get(cem_id, None)

    def get_process_data(self, cem_id, request):
        self.clean_finished()
        process = self._threads.get(cem_id, None)
        if process is not None:
            return process.get_data(request)

    def start_process(self, cemetery, data=None):
        pass

    def clean_finished(self):
        for process_id, process in self._threads.items():
            if process and not process.is_alive() and process.finished_at is not None:
                finished = time.time() - process.finished_at
                if finished > 60 * 5:  # 5 minutes
                    self._threads[process_id] = None
        gc.collect()