====================
California Star Test Application
====================

The California Star Test Application displays various aspects of the raw california test data.

Currently, the following have written and are working:

- Not much

Planned Functionality

- Management command to download and import raw test data
- Comparison of data across demographic groups an years using Google Motion
  Charts

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

The Data Fro the Test Table was generate using the `StarTestConvert` management command.

    $ ./manage.py StarTestConvert ~/data/Tests2010.txt \
    star/fixtures/initial_data.json

TODOs and BUGS
==============
See: http://github.com/jasonculverhouse/django-ca-star/issues



