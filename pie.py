import matplotlib.pyplot as plt



labels = ['English', 'Math', 'Science', 'History']
sizes = [45, 30, 15, 10]
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon']
plt.clf()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

plt.title('Subjects Distribution')
plt.show()
plt.savefig("./result/piechart.png")

