from star.management import base

class Command(base.StarParseBaseCommand):
    args = '<star test result csv file> <startest fixture file.json>'
    help = 'Converts the Star Test data into a Django Fixture'
    
    def parse_row(self, row):
        return {
                "model": "star.Test",
                "pk": int(row["Test ID Num"]),
                "fields": { 'name' :row["Test Name"] }
            }
