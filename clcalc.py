#!/usr/bin/env python

# Starting from 19920529, on `1429`, average bounces 30 per month,
# e.g., by 20070917, the 184th month from 199205, the formula:
# 1429+(184*30*1/2) where you repalce 1/2 with 1/3|1/4 to get 1/3|1/4
from calendar import monthrange
import datetime

start = 1429
r = 184
i = 30
ratios = [0.125, 0.25, 0.333, 0.5, 0.667, 0.75, 1]

d1=datetime.datetime.strptime(str('1992-05-29'), '%Y-%m-%d')
d2=datetime.datetime.today()


def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += datetime.timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta

delta = monthdelta(d1, d2)

for ratio in ratios:
    # print "%8s: %d" %(ratio, start+(r*i*ratio))
    print "{:1.3f}: {:5.0f}".format(ratio, start+(delta*i*ratio))

