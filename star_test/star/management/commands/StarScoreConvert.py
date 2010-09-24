from star.management import base

def float_or_none(val):
    try:
        float(val)
        return val
    except:
        return None

def int_or_none(val):
    try:
        return int(val)
    except:
        return None
        
class Command(base.StarParseBaseCommand):
    args = '<star test result csv file> <startest fixture file.json>'
    help = 'Converts the Star Entity data into a Django Fixture'
    
    def parse_row(self, row):
        data = {
                "model": "star.Score",
                "pk": None,
                "fields": {
                    'county_code': int(row['County Code']), 'district_code': int(row['District Code']), 
                    'school_code': int(row['School Code']), 
                    'charter_number': int(row['Charter Number']), 
                    'test_year': int(row['Test Year']), 
                    'subgroup_id': int(row['Subgroup ID']), 
                    'test_type': row['Test Type'].strip(), 
                    'capa_assessment_level': int(row['CAPA Assessment Level']), 
                    'total_star_enrollment': int(row['Total STAR Enrollment']), 
                    'total_tested_at_entity_level': int(row['Total Tested At Entity Level']), 
                    'total_tested_at_subgroup_level': int(row['Total Tested At Subgroup Level']), 
                    'grade': int(row['Grade']), 
                    'test_id': int(row['Test Id']), 
                    'star_reported_enrollment_capa_eligible': int_or_none(row['STAR Reported Enrollment/CAPA Eligible']), 
                    'students_tested': int(row['Students Tested']), 
                    'percent_tested': float_or_none(row['Percent Tested']), 
                    'mean_scale_score': float_or_none(row['Mean Scale Score']), 
                    'percentage_advanced': float_or_none(row['Percentage Advanced']), 
                    'percentage_proficient': float_or_none(row['Percentage Proficient']), 
                    'percentage_at_or_above_proficient': float_or_none(row['Percentage At Or Above Proficient']), 
                    'percentage_basic': float_or_none(row['Percentage Basic']), 
                    'percentage_below_basic': float_or_none(row['Percentage Below Basic']), 
                    'percentage_far_below_basic': float_or_none(row['Percentage Far Below Basic']), 
                    'students_with_scores': int(row['Students with Scores']), 
                    'cma_sts_average_percent_correct': float_or_none(row['CMA/STS Average Percent Correct']),                 }
            }
        return data

