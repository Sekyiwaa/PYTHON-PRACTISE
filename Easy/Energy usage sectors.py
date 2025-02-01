import matplotlib.pyplot as plt

# Setting colors for sectors
colors = {'Residential': 'turquoise', 'Commercial': 'khaki', 'Industrial': 'tomato'}

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(df['energy_usage'], labels=df['sector'], colors=[colors[sector] for sector in df['sector']],
        autopct='%1.1f%%', startangle=140)

plt.title('Proportion of Total Energy Usage by Sector')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()