from star.management import base

def non_zero(val):
    try:
        val = int(val)
        return val and val or None
    except:
        return None
    
class Command(base.StarParseBaseCommand):
    args = '<star test result csv file> <startest fixture file.json>'
    help = 'Converts the Star Entity data into a Django Fixture'
    
    def county(self, row):
        return {
                "model": "star.County",
                "pk": int(row["County Code"]),
                "fields": {
                    'type_id' : int(row["Type Id"]),
                    'name' : row["County Name"],
                 }
            }
    
    def district(self, row):
        return {
                "model": "star.District",
                "pk":  int(row["District Code"]),
                "fields": {
                    'name' : row["District Name"],
                 }
            }
    
    def school(self, row):
        return {
                "model": "star.School",
                "pk": int(row["School Code"]),
                "fields": {
                    'name' : row["School Name"],
                    'county' : int(row["County Code"]),
                    'district' : non_zero(row["District Code"]),
                    'charter_number' : non_zero(row["Charter Number"]),
                    'test_year' : int(row["Test Year"]),
                    'type_id' : int(row["Type Id"]),
                    'zipcode' : non_zero(row["Zip Code"]),
                 }
            }
    
    def entity(self, row):
        return {
                "model": "star.Entity",
                "pk": None,
                "fields": {
                    'county' : int(row["County Code"]),
                    'district' : non_zero(row["District Code"]),
                    'school' : non_zero(row["School Code"]),
                    'charter_number' : non_zero(row["Charter Number"]),
                    'test_year' : int(row["Test Year"]),
                    'type_id' : int(row["Type Id"]),
                    'zipcode' : non_zero(row["Zip Code"]),
                 }
            }
    
    def parse_row(self, row):
        data = [self.entity(row)]
        type_id = int(row["Type Id"])
        if type_id in [4,5] and not (data[0]['fields']['district'] and data[0]['fields']['school']):
            data.append(self.county(row))
        if type_id == 6 and not data[0]['fields']['school']:
            data.append(self.district(row))
        if type_id in [7,9,10]:
             data.append(self.school(row))
        return data
    
