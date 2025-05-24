import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

# Set Seaborn style
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))  # Set default figure size

# --------------------------
# 1. SCATTER PLOT (Enhanced)
# --------------------------
sns.scatterplot(
    x='total_bill',
    y='tip',
    data=tips,
    hue='sex',          # Color by gender
    size='size',        # Scale points by party size
    style='time',       # Different markers for lunch/dinner
    palette='viridis',  # Color scheme
    alpha=0.8
)
plt.title("Total Bill vs Tip (Colored by Gender, Sized by Party)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.tight_layout()
plt.show()

# ------------------
# 2. LINE PLOT
# ------------------
# Aggregate data first
avg_tips = tips.groupby('day', as_index=False).tip.mean()

sns.lineplot(
    x='day',
    y='tip',
    data=avg_tips,
    marker='o',         # Show markers
    markersize=10,
    linewidth=2.5,
    color='purple'
)
plt.title("Average Tip by Day of Week")
plt.ylabel("Average Tip ($)")
plt.show()

# ------------------------
# 3. BAR PLOT (With Error)
# ------------------------
sns.barplot(
    x='day',
    y='total_bill',
    data=tips,
    hue='sex',
    ci='sd',            # Show standard deviation
    palette='coolwarm',
    capsize=0.1         # Error bar caps
)
plt.title("Average Bill by Day with Error Bars")
plt.show()

# ------------------
# 4. HISTOGRAM
# ------------------
sns.histplot(
    data=tips,
    x='total_bill',
    kde=True,           # Add kernel density estimate
    bins=20,
    hue='time',
    element='step'      # Cleaner histogram style
)
plt.title("Distribution of Total Bills")
plt.show()

# ------------------
# 5. BOX PLOT
# ------------------
sns.boxplot(
    x='day',
    y='tip',
    data=tips,
    hue='smoker',
    palette='Set2',
    linewidth=2.5
)
plt.title("Tip Distribution by Day and Smoking Status")
plt.show()

# ------------------
# 6. VIOLIN PLOT
# ------------------
sns.violinplot(
    x='day',
    y='total_bill',
    data=tips,
    hue='sex',
    split=True,         # Compare groups side-by-side
    inner='quartile',   # Show quartile lines
    palette='pastel'
)
plt.title("Bill Distribution by Day and Gender")
plt.show()

# ------------------
# 7. PAIR PLOT
# ------------------
sns.pairplot(
    tips,
    hue='time',
    palette='husl',
    corner=True,        # Show only lower triangle
    diag_kind='kde',    # Diagonal plots as density curves
    plot_kws={'alpha': 0.7}
)
plt.suptitle("Pairwise Relationships in Tips Dataset", y=1.02)
plt.show()

# ------------------
# 8. HEATMAP
# ------------------
# Create correlation matrix
corr = tips.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,         # Show values
    fmt=".2f",         # 2 decimal places
    cmap='icefire',    # Color map
    linewidths=0.5,
    vmin=-1, vmax=1    # Fix color scale for correlations
)
plt.title("Correlation Heatmap")
plt.show()

# ------------------
# 9. REGRESSION PLOT
# ------------------
sns.lmplot(
    x='total_bill',
    y='tip',
    data=tips,
    hue='time',
    col='day',          # Facet by day
    col_wrap=2,         # Wrap columns
    height=4,
    aspect=1.2,
    markers=['o', 'x'],
    scatter_kws={'alpha':0.6}
)
plt.suptitle("Regression Plots by Day and Meal Time", y=1.02)
plt.tight_layout()
plt.show()

# ------------------
# 10. CUSTOM STYLING
# ------------------
# Set global style
sns.set_theme(
    style="ticks",
    palette="deep",
    font="Arial",
    rc={'axes.grid': True}
)

# Create a plot with custom styling
g = sns.FacetGrid(
    tips,
    col='time',
    row='smoker',
    margin_titles=True
)
g.map_dataframe(
    sns.scatterplot,
    x='total_bill',
    y='tip',
    hue='sex',
    palette='rocket'
)
g.add_legend()
g.set_axis_labels("Total Bill ($)", "Tip ($)")
g.set_titles(col_template="{col_name} Meal", row_template="Smoker: {row_name}")
plt.show()