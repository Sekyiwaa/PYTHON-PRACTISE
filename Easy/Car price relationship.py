import matplotlib.pyplot as plt

# Setting colors based on dealership
colors = {'Dealership A': 'lightblue', 'Dealership B': 'coral', 'Dealership C': 'limegreen'}

# Plotting
plt.figure(figsize=(10, 6))
for dealership, group in df.groupby('dealership'):
    plt.scatter(group['age'], group['selling_price'], color=colors[dealership], label=dealership)

plt.title('Relationship between Age of Car and Selling Price by Dealership')
plt.xlabel('Age of Car (years)')
plt.ylabel('Selling Price ($)')
plt.legend(title='Dealership')
plt.grid(True)
plt.show()