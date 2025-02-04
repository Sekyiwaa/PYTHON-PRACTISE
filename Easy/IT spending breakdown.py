import matplotlib.pyplot as plt

# Preview the dataset
df.head()

colors=['navy','gray','teal']
# Create the graph
plt.figure(figsize=(8,8))
plt.pie(df['spending'],labels =df['category'],colors=colors,autopct='%1.1f%%',startangle=140, wedgeprops=dict(width=0.4))

plt.title('Breakdown of Annual IT Spending by Category')
plt.show()