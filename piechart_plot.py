import matplotlib 
from matplotlib import pyplot as plt
labels = ["Demon Slayer", "Attack On Titan", "Devil May Cry", "Solo Leveling", "Death Note"]
size = [30,35,5,10,20]
plt.title("Anime Popularity Chart")    #this gives a title to piechart
plt.pie(size, labels = labels)    #this plots the piechart
plt.show()