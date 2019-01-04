#!/usr/bin/env python

from mozscape import Mozscape

client = Mozscape(
    'mozscape-f03b16db58',
    '5f7418e041cf61841d72ef26c6f7a905')

smythsonMetrics = client.urlMetrics('www.smythson.com')
smythsonDA = smythsonMetrics['pda']

authorities = client.urlMetrics(
    ('www.smythson.com'),
    Mozscape.UMCols.domainAuthority | Mozscape.UMCols.pageAuthority)

print(smythsonDA)
print(authorities)
print("hi")
