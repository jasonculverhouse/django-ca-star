====================
California Star Test Application
====================

The California Star Test Application displays various aspects of the raw california test data.

Currently, the following have written and are working:

- Initial Data Modeling
- Basic Admin Pages

Planned Functionality

- Management command to download and import raw test data
- Comparison of data across demographic groups an years using Google Motion
  Charts
- Site With Drill Down to Test data

Installation
==============

There are a number of data files and descriptions located on the California
Department of Education California Standardized Testing and Reporting (STAR)
Program website http://star.cde.ca.gov/

Data Field Descriptions
http://star.cde.ca.gov/star2010/research_fixfileformat.asp

Research Files
http://star.cde.ca.gov/star2010/ResearchFileList.asp?rf=True&ps=True

Data
=============

Some of the data will be shipped with the application, other data will need to be generated from the research files using management commands.

The Data For the star.Test Table was generates using the `StarTestConvert` management command.

    $ ./manage.py StarTestConvert ~/data/Tests2010.txt \
    star/fixtures/initial_data.json

The Entity (County/District/School) data and the actual results can be downloaded separately and converted.  I am only using the 2010 currently
schema adjustments need to be made to support multiple years of data.
 
    $ ./manage.py StarEntityConvert ../data/ca2010entities_csv.txt \
    ../data/ca2010entities.json
    $ ./manage.py StarScoreConvert ../data/ca2010_all_41_69005_csv_v2.txt \
    ../data/ca2010_all_41_69005_csv_v2.json
    $ ./manage.py loaddata ../data/ca2010entities.json
    $ ./manage.py loaddata ../data/ca2010_all_41_69005_csv_v2.json
    
TODOs and BUGS
==============
See: http://github.com/jasonculverhouse/django-ca-star/issues



