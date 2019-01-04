#!/usr/bin/env python

from mozscape import Mozscape

client = Mozscape(
    'mozscape-f03b16db58',
    '5f7418e041cf61841d72ef26c6f7a905')

# As you may have noticed, there are lots of columns available. I did what I could to make them easily-accessible, 
# but there are a lot, and the names are long. So, the API calls have defaults

# Let's get some URL metrics. Results are now an array of dictionaries
# the i'th dictionary is the results for the i'th URL
smythsonMetrics = client.urlMetrics('www.smythson.com')
smythsonDA = smythsonMetrics['pda']

# Now let's say we only want specific columns in the results

authorities = client.urlMetrics(
    ('www.smythson.com'),
    Mozscape.UMCols.domainAuthority | Mozscape.UMCols.pageAuthority)

print(smythsonDA)
