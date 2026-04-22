import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1, 2], [3, 4]])
sns.heatmap(data, annot=True)
plt.show()