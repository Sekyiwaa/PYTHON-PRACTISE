import matplotlib.pyplot as plt

# Setting colors for brands with hex code for bronze
colors = {'Brand A': 'gold', 'Brand B': 'silver', 'Brand C': '#cd7f32'}  # Hex code for bronze

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(df['brand'], df['annual_revenue'], color=[colors[brand] for brand in df['brand']])

# Adding title and labels
plt.title('Annual Revenue of Different Retail Brands')
plt.xlabel('Brand')
plt.ylabel('Annual Revenue ($ Millions)')
plt.grid(axis='y')

# Displaying the plot
plt.show()