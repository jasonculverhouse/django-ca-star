from star.management import base

class Command(base.StarParseBaseCommand):
    args = '<star test result csv file> <startest fixture file.json>'
    help = 'Converts the Star Entity data into a Django Fixture'
    
    def parse_row(self, row):
        data = {
                "model": "star.Entity",
                "pk": None,
                "fields": {
                    'county_code' : int(row["County Code"]),
                    'district_code' : int(row["District Code"]),
                    'school_code' : int(row["School Code"]),
                    'charter_number' : int(row["Charter Number"]),
                    'test_year' : int(row["Test Year"]),
                    'type_id' : int(row["Type Id"]),
                    'county_name' : row["County Name"],
                    'district_name' : row["District Name"],
                    'school_name' : row["School Name"],
                 }
            }
        
        if row["Zip Code"].strip():
            data['fields']['zipcode'] = row["Zip Code"]
        return data
    
