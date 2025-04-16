#MapPlot.py
#Name:
#Date:
#Assignment:


import emissions
emissions = emissions.get_emissions()
num_items = len(emissions)
country_list = []
c02_list = []
for spot in range(num_items):
    country = emissions[spot]["Country"]
    c02 = emissions[spot]["Emissions"]["Type"]["CO2"]
    

    if c02 < 2000:
        c02 = float(c02)
        c02_list.append(c02)
        country_list.append(country)

import matplotlib.pyplot as plt
plt.plot(country_list, c02_list, 'ro')
plt.ylabel("c02")
plt.xlabel("Country") 
plt.savefig("Output")