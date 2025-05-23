import matplotlib.pyplot as plt

# Data
"""labels = ['Apples', 'Oranges', 'Bananas', 'Grapes']
sizes = [30, 25, 20, 25]  # Percentages or values
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']"""

"""plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%.1f%%',  # Show percentages
    startangle=90       # Rotate pie
)
plt.title("Basic Pie Chart")
plt.show()"""


# 2. Advanced Customizations
# Exploded Pie with Shadows


"""explode = (0.1, 0, 0, 0)  # "Pull out" the first wedge

plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    shadow=True,          # Add shadow effect
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}  # Wedge borders
)
plt.title("Exploded Pie Chart")
plt.show()"""


# 3. Donut Chart

"""plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    wedgeprops={'width': 0.4}  # Makes a donut
)
plt.title("Donut Chart")
plt.show()"""

# Pro Tip: Set width=0.4 (or similar) in wedgeprops to create a donut.

# 4. Nested Pie Charts
# Outer ring
"""plt.pie(
    [30, 70],
    radius=1.3,
    labels=['Group A', 'Group B'],
    colors=['#ff9999','#66b3ff'],
    wedgeprops={'width': 0.4}
)

# Inner ring
plt.pie(
    sizes,
    radius=0.9,
    labels=labels,
    colors=colors,
    wedgeprops={'width': 0.4}
)
plt.title("Nested Pie Chart")
# plt.show()"""

# 5. Text & Legend Customizations
"""wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    pctdistance=0.85  # Move percentages inward
)

# Customize text properties
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=12)

# Add legend with wedge sizes
plt.legend(
    wedges,
    labels,
    title="Fruits",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)
plt.title("Pie Chart with Custom Legend")
plt.tight_layout()
plt.show()"""

# 6. Handling Small Slices
"""sizes = [35, 25, 20, 10, 5, 5]  # Contains small values
labels = ['A', 'B', 'C', 'D', 'E', 'F']

plt.pie(
    sizes,
    labels=labels,
    autopct=lambda p: f'{p:.1f}%' if p > 5 else '',  # Hide small percentages
    textprops={'fontsize': 8}
)
plt.title("Pie Chart with Small Slices")
plt.show()"""

"""plt.savefig(
    'piechart.png',
    dpi=300,                   # High resolution
    bbox_inches='tight',       # Prevent cropping
    transparent=True           # For presentations
)"""