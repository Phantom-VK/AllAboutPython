import matplotlib.pyplot as plt
import numpy as np


# Basic Bar Graph
def basic_bar():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [15, 22, 34, 17, 28]

    plt.bar(categories, values, color='green')
    plt.title('Basic Bar Graph')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()


# Horizontal Bar Graph
def horizontal_bar():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [15, 22, 34, 17, 28]

    plt.barh(categories, values, color='skyblue')
    plt.title('Horizontal Bar Graph')
    plt.xlabel('Values')
    plt.ylabel('Categories')
    plt.show()


# Grouped Bar Graph
def grouped_bar():
    categories = ['Group 1', 'Group 2', 'Group 3']
    men_means = [22, 30, 35]
    women_means = [25, 32, 30]

    x = np.arange(len(categories))
    width = 0.35

    plt.bar(x - width / 2, men_means, width, label='Men', color='blue')
    plt.bar(x + width / 2, women_means, width, label='Women', color='pink')

    plt.title('Grouped Bar Chart (Side by Side)')
    plt.xlabel('Groups')
    plt.ylabel('Scores')
    plt.xticks(x, categories)
    plt.legend()
    plt.show()


# Stacked Bar Graph
def stacked_bar():
    categories = ['A', 'B', 'C', 'D']
    values1 = [15, 22, 34, 17]
    values2 = [10, 12, 14, 15]

    plt.bar(categories, values1, color='r', label='Value 1')
    plt.bar(categories, values2, bottom=values1, color='b', label='Value 2')

    plt.title('Stacked Bar Graph')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.legend()
    plt.show()


# Customized Bar Graph with Advanced Features
def advanced_bar():
    categories = ['Electronics', 'Furniture', 'Clothing', 'Groceries']
    sales = [45000, 32000, 58000, 41000]
    colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2']
    error = [2000, 1500, 3000, 2500]

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(categories, sales,
                  color=colors,
                  yerr=error,
                  capsize=5,
                  edgecolor='black',
                  linewidth=1.2,
                  alpha=0.8)

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{height:,}',
                ha='center', va='bottom',
                fontsize=10)

    # Customize the plot
    ax.set_title('Quarterly Sales Report', pad=20, fontsize=16, fontweight='bold')
    ax.set_xlabel('Product Categories', labelpad=10)
    ax.set_ylabel('Sales ($)', labelpad=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Rotate x-axis labels if needed
    plt.xticks(rotation=45, ha='right')

    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    plt.show()


# Run all examples
if __name__ == "__main__":
    basic_bar()
    horizontal_bar()
    grouped_bar()
    stacked_bar()
    advanced_bar()