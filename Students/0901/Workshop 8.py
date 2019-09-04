# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

# connection = sqlite3.connect("climate.db")
# cursor = connection.cursor()
# cursor = cursor.fetchone()
# print(cursor)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 15))
ax1 = plt.subplot(211)
Year = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
CO2 = [250, 265, 272, 260, 300, 320, 389]
plt.xlabel('Year')
plt.ylabel('CO2')
plt.plot(Year, CO2, "or", Year, CO2, "--,b")
plt.title('ClimateData')

# plt.axis(1950, 2010, 260, 380)

ax2 = plt.subplot(212)
temperature = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
plt.xlabel('Year')
plt.ylabel('temperature')
plt.plot(Year, temperature, "ob", Year, temperature, "--,g")
plt.title('Temperature Data')

plt.savefig('ClimateData')

plt.show()
