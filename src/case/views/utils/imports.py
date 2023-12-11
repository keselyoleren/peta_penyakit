import pusher

from django.db import transaction

from case.models import Case
from config.choice import ThreadResult
from config.process import Process
from threading import Thread
from tqdm import tqdm
from datetime import datetime

class ImportProcess(Process):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ImportProcess, cls).__new__(cls)
        return cls.instance

    def start_process(self, data):
        if self.is_in_process(f'{len(data)}_i'):
            return ThreadResult.ALREADY_RUN
        try:
            process = ImportThread(data)
            process.start()
        except Exception as e:
            return ThreadResult.ERROR
        self._threads.update({f'{len(data)}_i': process})
        return ThreadResult.OK


class ImportThread(Thread):
    def __init__(self, data = None):
        if data is None:
            data = []
        super().__init__()
        self.data = data
        self.pusher_client = pusher.Pusher(
            app_id='1717939',
            key='62adf21c715a4a5f02a9',
            secret='361fd9e2efdc06579804',
            cluster='ap1',
            ssl=True
        )

    def run(self):
        self.import_data()

    def import_data(self):
        total_records = len(self.data)
        with tqdm(total=total_records, desc="Importing Data", unit="record") as progress_bar:
            try:
                with transaction.atomic():
                    for x in self.data:
                        date_string = x['dateDiscovered']
                        date_discovered = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
                        cases = Case.objects.create(
                            animal=x['animal'],
                            diseases_id=x['diseaseId'],
                            village_id=x['villageId'],
                            address=x['address'],
                            latitude=x['latitude'],
                            longitude=x['longitude'],
                            date_discovered=date_discovered,
                            total_case=x['jumlah'],
                        )
                        cases.save()
                        progress_bar.update(1)
                        self.pusher_client.trigger('penyakit-channel', 'progress-event', {'progress': f"{progress_bar.n / total_records * 100:.2f}"})
            except Exception as e:
                self.pusher_client.trigger('error-channel', 'error-event', {'message': f"Proscess Error: {e}"})