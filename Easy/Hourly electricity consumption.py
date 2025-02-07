import matplotlib.pyplot as plt

# Preview the dataset
df.head()

# Create the graph
plt.figure(figsize=(12,6))
plt.plot(df['hour'],df['consumption'],color = 'midnightblue',linewidth = 2)
plt.title('Hourly Electricity Consumption in an Industrial Park')
plt.xlabel('Hour')
plt.ylabel('Electricity Consumption (kwh)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()