#!/usr/bin/env python

from mozscape import Mozscape
from datetime import datetime
import csv

client = Mozscape(
    'mozscape-f03b16db58',
    '5f7418e041cf61841d72ef26c6f7a905')

smythsonMetrics = client.urlMetrics('www.smythson.com')
smythsonDA = smythsonMetrics['pda']

# for Page Authority too:
# authorities = client.urlMetrics(
#    ('www.smythson.com'),
#    Mozscape.UMCols.domainAuthority | Mozscape.UMCols.pageAuthority)

now = datetime.now()
month = now.strftime("%B-%y")
print(month)
print(smythsonDA)

update = [month,str(smythsonDA)]

with open('da.csv','a') as fd:
	wr = csv.writer(fd,delimiter=',')
	wr.writerow(update)