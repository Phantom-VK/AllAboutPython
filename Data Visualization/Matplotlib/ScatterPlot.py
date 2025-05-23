import matplotlib.pyplot as plt
import numpy as np

# Generate data
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)

"""plt.scatter(x, y, c='blue', marker='o', label='Data Points')
plt.title("Basic Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()"""

# 2. Advanced Customizations
# Color Mapping & Size Variations
"""sizes = np.random.uniform(10, 200, len(x))  # Random sizes
colors = np.random.rand(len(x))  # Color values for mapping

plt.scatter(
    x, y,
    s=sizes,          # Marker sizes
    c=colors,         # Color values
    cmap='coolwarm',   # Colormap ('viridis', 'plasma', 'coolwarm')
    alpha=0.7,        # Transparency
    edgecolor='black',
    linewidth=0.5
)
plt.colorbar(label="Color Scale")  # Add colorbar
plt.title("Advanced Scatter Plot (Size & Color)")
plt.show()"""

# 3. Grouped Scatter Plot

# Create groups
"""group1 = (np.random.rand(20), np.random.rand(20))
group2 = (np.random.rand(20)+0.5, np.random.rand(20)+0.5)

plt.scatter(*group1, c='red', label='Group A', s=50)
plt.scatter(*group2, c='green', marker='s', label='Group B', s=75)
plt.title("Grouped Scatter Plot")
plt.legend()
plt.show()"""

# 4. Regression Line & Annotations

from sklearn.linear_model import LinearRegression

"""# Fit regression line
model = LinearRegression().fit(x.reshape(-1,1), y)
line_x = np.linspace(0, 1, 100)
line_y = model.predict(line_x.reshape(-1,1))

plt.scatter(x, y, c='blue')
plt.plot(line_x, line_y, 'r--', label='Trend Line')
plt.annotate(
    f"y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}",
    xy=(0.6, 0.1), fontsize=10
)
plt.title("Scatter Plot with Regression")
plt.legend()
plt.show()"""

# 5. 3D Scatter Plot


"""fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

z = np.random.rand(50)
ax.scatter(x, y, z, c=z, cmap='plasma', s=50)
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()"""