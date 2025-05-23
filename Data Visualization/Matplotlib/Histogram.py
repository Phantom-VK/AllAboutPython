import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(42)
data = np.random.normal(170, 10, 250)  # Mean=170, Std=10, 250 points


def basic_histogram():
    """Basic histogram with default parameters"""
    plt.hist(data)
    plt.title("Basic Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()


def customized_histogram():
    """Advanced histogram with customizations"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot histogram
    n, bins, patches = plt.hist(
        data,
        bins=20,  # Number of bins
        color='#86bf91',  # Bar color
        edgecolor='black',  # Edge color
        linewidth=1.2,  # Edge width
        alpha=0.7,  # Transparency
        density=True,  # Normalize to form probability density
        orientation='vertical',  # 'horizontal' for sideways
        histtype='bar',  # Options: 'bar', 'barstacked', 'step', 'stepfilled'
        align='mid',  # Bin alignment: 'left', 'mid', 'right'
        rwidth=0.85,  # Relative bar width (0-1)
        label='Height Distribution'
    )

    # Add mean line and annotation
    mean_val = np.mean(data)
    ax.axvline(float(mean_val), color='red', linestyle='--', linewidth=2)
    ax.text(mean_val + 1, max(n) * 0.9, f'Mean: {mean_val:.1f}', color='red')

    # Customizations
    ax.set_title("Advanced Histogram", pad=20, fontsize=16)
    ax.set_xlabel("Height (cm)", labelpad=10)
    ax.set_ylabel("Probability Density", labelpad=10)
    ax.grid(axis='y', alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.show()


def multiple_histograms():
    """Comparing multiple distributions"""
    data1 = np.random.normal(170, 10, 250)
    data2 = np.random.normal(160, 8, 250)

    plt.hist(data1, bins=15, alpha=0.5, label='Group 1')
    plt.hist(data2, bins=15, alpha=0.5, label='Group 2')

    plt.title("Overlaid Histograms")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    basic_histogram()
    customized_histogram()
    multiple_histograms()