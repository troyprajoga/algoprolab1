import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
iq_data = np.random.normal(loc=100, scale=15, size=1000)

std_dev = np.std(iq_data)
plt.hist(iq_data, bins=30, edgecolor='black')
plt.title('IQ Distribution')
plt.xlabel('IQ')
plt.ylabel('Frequency')
plt.axvline(x=100, color='red', linestyle='dashed', linewidth=2, label=f'Standard Deviation\n{std_dev:.2f}')

plt.legend()
plt.show()
