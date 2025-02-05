import matplotlib.pyplot as plt

# Preview the dataset
df.head()

# Create the graph
plt.figure(figsize=(10,6))
plt.fill_between(df['year'],df['sales'],color='lightgreen',step ='pre',alpha =0.6 )
plt.plot(df['year'],df['sales'], color ='green')
plt.title('Growth of Online Sales Over the Past Five Years')
plt.xlabel('year')
plt.ylabel('sales($)')
plt.grid(True)
plt.xticks(df['year'])
plt.show()