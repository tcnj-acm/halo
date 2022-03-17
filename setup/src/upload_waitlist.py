import os, csv
from default.models import WaitingList

with open('dump.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        p = WaitingList(full_name=row['full_name'],email=row['email'])
        p.save()