import json
from django.core.management.base import BaseCommand
from case.models import *
from tqdm import tqdm



class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = 'indonesia.json'
        with open(file_path) as f:
            data = json.load(f)
        
        for item in tqdm(data):
            province = Province.objects.create(name=item['name'])
            for i_regency in item['regency']:
                regency = Regency.objects.create(name=i_regency['name'], province=province)
                for i_district in i_regency['subdistrict']:
                    district = SubDistrict.objects.create(name=i_district['name'], regency=regency)
                    for village in i_district['village']:
                        Village.objects.create(name=village['name'], kode_pos=village['kodePos'], sub_district=district)

