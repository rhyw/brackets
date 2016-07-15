#!/usr/bin/env python

# Starting from 19920529, on `1429`, average bounces 30 per month,
# e.g., by 20070917, the 184th month from 199205, the formula:
# 1429+(184*30*1/2) where you repalce 1/2 with 1/3|1/4 to get 1/3|1/4

# Objectives:
# python clalgo.py 201609 0.125
# where `201609` is positional argument and 0.125 optional.
# without specifing 0.125(ratio), all ratios will be listed.

import argparse

from calendar import monthrange
import datetime

# Starting point, on the month of 199205.
YEARMONTH = "199205"
START = 1429
# Average price raises each month.
GAP = 30
RATIOS = [0.125, 0.25, 0.333, 0.5, 0.667, 0.75, 1]


def monthdelta(d1, d2):
    """
    d1, d2 are datetime.datetime objects.
    Return delta months otherwise returns 0.
    """
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += datetime.timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta

parser = argparse.ArgumentParser()
parser.add_argument("-ym", "--yearmonth", type=str,
                    help="Year and month with form: 'YYYYmm', e.g., 201606")
parser.add_argument("-r", "--ratio", type=float,
                    help="Relevant ratios, possible values: 0.125, 0.25 etc.")

args = parser.parse_args()

delta1 = datetime.datetime.strptime(YEARMONTH, '%Y%m')
if args.yearmonth:
    try:
        delta2 = datetime.datetime.strptime(args.yearmonth, '%Y%m')
    except ValueError:
        parser.error("Unrecognized yearmonth format, use 'YYYYmm' instead.")
else:
    delta2 = datetime.datetime.today()

delta = monthdelta(delta1, delta2)

if args.ratio:
    print "{:1.3f}: {:5.0f}".format(args.ratio, START+(delta*GAP*args.ratio))
else:
    for ratio in RATIOS:
        print "{:1.3f}: {:5.0f}".format(ratio, START+(delta*GAP*ratio))
