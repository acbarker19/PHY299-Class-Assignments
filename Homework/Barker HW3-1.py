# HW3-1
# Alec Barker
# Q2.4.7

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
hours = [44.7, 65.4, 101.7, 148.3, 170.9, 171.4, 176.7, 186.1, 133.9, 105.4, 59.6, 45.8]

zipped = list(zip(hours, month))

sorted_list = sorted(zipped)
sorted_list.reverse()

hours, month = zip(*sorted_list)

for i in range(12):
    print(month[i], ": ", hours[i])