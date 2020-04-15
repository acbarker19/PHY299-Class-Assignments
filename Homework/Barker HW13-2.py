# HW 13-2
# Alec Barker

import matplotlib.pyplot as plt
import scipy.stats as stats
import glob

def get_temps(file_path):
    file = open(file_path)
    
    all_temps = []

    year_temps = {}
    current_year = 1995
    current_year_temps = []
    
    for line in file:
        line_data = line.split("         ")
        
        line_data[0] = int(line_data[0].strip())
        line_data[1] = int(line_data[1].strip())
        line_data[2] = int(line_data[2].strip())
        line_data[3] = float(line_data[3].strip())
        
        if(line_data[3] > 0):
            all_temps.append(line_data[3])
            
        if line_data[2] != current_year:
            year_temps.update({str(current_year) : current_year_temps})
            current_year = line_data[2]
            current_year_temps = []
        current_year_temps.append(line_data[3])
    
    # Adds data for the last year to the dictionary
    year_temps.update({str(current_year) : current_year_temps})
    
    return all_temps, year_temps

def average(values):
    return sum(values) / len(values)



print("Part A")

all_temps, year_temps = get_temps("Data Files/MDBALTIM.txt")
    
plt.figure(dpi=200)

plt.subplot(211)
plt.title("Daily Temperatures From 1995 to 2017")
plt.plot(range(len(all_temps)), all_temps)
plt.xlabel("Days since January 1, 1995")
plt.ylabel("Temperature")

plt.subplot(212)
plt.title("Daily Temperatures for 1995, 2005, and 2015")
plt.plot(range(365), year_temps["1995"], label="1995", linewidth=3, alpha=0.4)
plt.plot(range(365), year_temps["2005"], label="2005", linewidth=3, alpha=0.4)
plt.plot(range(365), year_temps["2015"], label="2015", linewidth=3, alpha=0.4)
plt.xlabel("Days since January 1")
plt.ylabel("Temperature")
plt.legend()

plt.tight_layout()
plt.show()

stat, p = stats.ks_2samp(year_temps["1995"], year_temps["2015"])
print("The 2 sample KS test p-value is {0:.2f}.".format(p))
if p < 0.05:
    print("We reject the null hypothesis, and so we conclude that the " \
          "distributions differ.")
else:
    print("We do not reject the null hypothesis (the data do not support " \
          "the argument that the distributions differ).")



print("\r\nPart B")

count = 0

avg_diff = []

for fname in glob.glob(r"Data Files/Weather/*.txt"):
    try:
        all_temps, year_temps = get_temps(fname)
        if len(year_temps["1995"]) >= 350 and len(year_temps["2015"]) >= 350:
            stat, p = stats.ks_2samp(year_temps["1995"], year_temps["2015"])
            if p < 0.05:
                count += 1
                avg1 = average(year_temps["1995"])
                avg2 = average(year_temps["2015"])
                avg_diff.append(avg2 - avg1)
    except:
        pass

print("{} cities have a p value below 0.05.".format(count))
print("The average temperature between 1995 and 2015 in cities with " \
      "statistically significant shifts has changed by a value of {0:.2f} " \
      "degrees.".format(average(avg_diff)))
    
"""
If all 1995/2015 comparisons are from the same distribution, then they would
have a 100% chance that the values are from the same distribution, and they
should all have a p-value of 1.0 and thus none below 0.05. There are more
values below 0.05 than zero. This means that the temperature between 1995 and
2015 has changed a lot since the data from multiple cities have less than a
5% chance of being the same distribution and thus have a significant
difference between the daily temperatures of 1995 and 2015.
"""