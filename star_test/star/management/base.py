import csv
import json
from django.core.management.base import BaseCommand, CommandError
from django.core import serializers

class StarParseBaseCommand(BaseCommand):
    """ Base Command To Parse Star Data Files into fixtures 
    """
    def reader(self, input_file):
        """By default construct a DictReader from the File Object
        """
        return csv.DictReader(input_file)
        
    def parse_row(self, row):
        """ Return a Dictionary with the required Fixture Structure
        """
        raise
    
    def validate_jason(self, json_data):
        """Validate the JSON data versus the model while it is parsed
        """
        try:
            list(serializers.deserialize("json", json_data))
        except:
            raise
            
    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError('Usage: %s' % self.args)
        try:
            with open(args[0], 'r') as star_input:
                with open(args[1], 'w') as fixture_output:
                    comma = False
                    fixture_output.write('[\n')
                    for row in self.reader(star_input):
                        if comma:
                            fixture_output.write(',\n')
                        try:
                            data = self.parse_row(row)
                            if type(data) is list:
                                fixture_output.write(',\n'.join(json.dumps(o) for o in data))
                            else:
                                fixture_output.write(
                                    json.dumps(data)
                                )
                            comma = True
                        except:
                            raise
                            raise CommandError('Error Converting Row %s', repr(row))
                    fixture_output.write('\n]\n')
        except:
            raise
            raise CommandError("File Not Found?")
