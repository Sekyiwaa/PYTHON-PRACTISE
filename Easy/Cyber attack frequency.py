import matplotlib.pyplot as plt

# Preview the dataset
df.head()

# Create the graph
colors =['black', 'red',  'purple']

plt.figure(figsize = (10,6))
plt.bar(df['attack_type'], df['frequency'], color =colors)

plt.title('Frequency of Different Types of Cyber Attackes on a Network')
plt.xlabel('Attack Type')
plt.ylabel('Frequency')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.show()