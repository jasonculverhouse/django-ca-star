import csv
import json
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class Command(BaseCommand):
    args = '<star test result csv file> <startest fixture file.json>'
    help = 'Converts the Star Test data into a Django Fixture'

    def handle(self, *args, **options):
        try:
            with open(args[0], 'r') as star_input:
                reader = csv.DictReader(star_input)
                with open(args[1], 'w') as fixture_output:
                    comma = False
                    fixture_output.write('[\n')
                    for row in reader:
                         if comma:
                             fixture_output.write(',\n')
                         fixture_output.write(
                                json.dumps({ "model": "star.Test",
                                     "pk": int(row["Test ID Num"]),
                                     "fields": { 'name' :row["Test Name"] }
                                }))
                         comma = True
                    fixture_output.write('\n]\n')
        except:
            raise
            raise CommandError('input does not exist')
