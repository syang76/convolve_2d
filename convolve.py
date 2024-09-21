# Siyang Yang
# Assessment: 
# Create random noised test_data.dat which contains data in 3 columns. 
# Column 1 and 2 designate x and y coordinates respectively. 
# Column 3 is the main data defined at the corresponding (x, y) points.
# Compute the 2-d convolution of these data and provide visualization.
# Use any programming language or library as necessary.

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d


# Generate test data
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y) + np.random.normal(0, 0.5, X.shape)  # Adding noise to create significant differences

# Save the data to a file
with open('test_data.dat', 'w') as f:
    for i in range(len(x)):
        for j in range(len(y)):
            f.write(f"{X[i, j]} {Y[i, j]} {Z[i, j]}\n")

# Compute the 2D convolution
kernel = np.ones((5, 5)) / 25  # Example kernel
convolved_data = convolve2d(Z, kernel, mode='same')

# Plot the original data
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Data')
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar()

# Plot the convolved data
plt.subplot(1, 2, 2)
plt.title('Convolved Data')
plt.contourf(X, Y, convolved_data, cmap='viridis')
plt.colorbar()

plt.show()