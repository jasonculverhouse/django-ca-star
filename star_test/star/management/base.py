import csv
import json
from django.core.management.base import BaseCommand, CommandError

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
                            fixture_output.write(
                                    json.dumps(self.parse_row(row))
                                )
                            comma = True
                        except:
                            raise CommandError('Error Converting Row %s', repr(row))
                    fixture_output.write('\n]\n')
        except:
            raise CommandError("File Not Found?")
