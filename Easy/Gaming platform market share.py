import matplotlib.pyplot as plt

# Preview the dataset
df.head()

# Create the graph
colors = {'PC': 'sienna', 'Consoles': 'rosybrown', 'Mobile': 'tan'}
plt.figure(figsize=(8,8))
plt.pie(df['market_share'],labels=df['platform'], colors=[colors[platform] for platform in df['platform']], autopct='%1.1f%%',startangle=140)

plt.title('Market Share of Different Gaming Platforms')
plt.axis('equal')
plt.show()