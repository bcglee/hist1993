import geocoder
import csv
import sys
import numpy as np
from collections import Counter
import re
import time
from datetime import date
import matplotlib.pyplot as plt


filepath = "dachau_with_geolocations_separate_columns.csv"

first_names = []
last_names = []
with open(filepath, 'rU') as f:
	reader = csv.reader(f)

        j = 0
        for row in reader:
		if j > 0:
			if any(c.isalpha() for c in row[30]):
				first_names.append(row[5])
				last_names.append(row[4])
                j = j + 1


thefile = open('names.txt', 'w')

for i in range(0, len(first_names)):

	str = first_names[i] + " " + last_names[i]
	

	thefile.write("%s, " % str)


sys.exit()
