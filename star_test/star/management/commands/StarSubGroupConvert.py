import csv
from star.management import base

class Command(base.StarParseBaseCommand):
    args = '<star test result csv file> <startest fixture file.json>'
    help = 'Converts the Star SubGroup data into a Django Fixture'
    
    def reader(self, input_file):
        """By default construct a DictReader from the File Object
        """
        return csv.DictReader(input_file, ['filler', 'id', 'sub_group', 'category' ], skipinitialspace=True)
    
    def parse_row(self, row):
        return {
                "model": "star.SubGroup",
                "pk": int(row["id"]),
                "fields": {
                    "sub_group" : row["sub_group"],
                    "category" : row["category"],
                }
            }
