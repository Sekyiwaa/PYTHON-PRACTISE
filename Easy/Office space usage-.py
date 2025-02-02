import matplotlib.pyplot as plt

# Preview the dataset
df.head()

#Setting the colours
colors ={'Administration': 'goldenrod', 'Human Resources': 'lightblue', 'IT Services': 'thistle'}
# Create the graph
plt.figure(figsize=(8,8))
plt.pie(df['office_space'], labels =df['department'], colors=[colors[dept] for dept in df['department']], autopct = '%1.1f%%', startangle = 140)

plt.title('Division of Office Space Usage by Department')
plt.axis('equal')
plt.show()