#!/usr/bin/env python

from mozscape import Mozscape
from datetime import datetime
import csv

# Mozscape API Details
client = Mozscape(
    'mozscape-f03b16db58',
    '5f7418e041cf61841d72ef26c6f7a905')

domain = "smythson.com"

smythsonMetrics = client.urlMetrics(domain)
smythsonDA = smythsonMetrics['pda']

# smythsonMetrics contains other metrics, as well as DA. Alternatively, un-comment the following to find PA:
# authorities = client.urlMetrics(
#    ('www.smythson.com'),
#    Mozscape.UMCols.domainAuthority | Mozscape.UMCols.pageAuthority)

# Get current month in user-friendly format.
now = datetime.now()
month = now.strftime("%B-%y")

update = [month,domain,str(smythsonDA)]
print(update)

with open('smythsonda.csv','a') as fd:
	wr = csv.writer(fd,delimiter=',')
	wr.writerow(update)