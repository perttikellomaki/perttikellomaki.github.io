#!/usr/bin/python3
import datetime
import matplotlib
import matplotlib.pyplot as plt
import sys

with open('data') as f:
    raw_data = f.readlines()

data = [l.split() for l in raw_data if len(l.split()) == 3]
dogs = set([l[0] for l in data])

for dog in dogs:
    dates = [(datetime.datetime.strptime(l[1], '%Y-%m-%d') - datetime.datetime.strptime('2024-08-20', '%Y-%m-%d')).days
             for l in data if l[0] == dog]
    weights = [float(l[2]) for l in data if l[0] == dog]
    plt.plot(dates, weights, label=dog)

plt.legend()
plt.xlim(0)
plt.ylim(0)
if len(sys.argv) > 1:
    plt.savefig(sys.argv[1])
else:
    plt.show()

