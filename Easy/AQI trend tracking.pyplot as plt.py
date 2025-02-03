import matplotlib.pyplot as plt

# Preview the dataset
df.head()

# Create the graph
plt.figure(figsize =(10,6))
plt.plot(df['date'], df['aqi'], color ='gray',linewidth = 2, marker ='o')
plt.xlabel('Date')
plt.ylabel('AQI')
plt.grid(True)
plt.show()