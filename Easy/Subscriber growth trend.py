import matplotlib.pyplot as plt

# Preview the dataset
df.head()

# Create the graph
plt.figure(figsize=(10,6))
plt.plot(df['month'],df['growth_rate'],color ='blue',linewidth=2,marker='o')

plt.title('Monthly Growth Rate of New Subscribers')
plt.xlabel('Month')
plt.ylabel('Growth Rate (%)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()