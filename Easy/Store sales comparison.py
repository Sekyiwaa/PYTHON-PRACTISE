

import matplotlib.pyplot as plt
import numpy as np

# Calculate means
mean_sales = df.groupby(['store', 'month']).mean().unstack('store')

# Plotting
mean_sales.plot(kind='bar', figsize=(14, 7), color=['gold', 'silver', '#cd7f32'])
plt.title('Average Monthly Sales of Electronic Products Across Different Stores')
plt.xlabel('Month')
plt.ylabel('Average Sales ($)')
plt.xticks(rotation=45)
plt.legend(title='Store')
plt.grid(axis='y')
plt.show()