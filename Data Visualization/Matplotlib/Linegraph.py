import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

# x_axis = [1, 2, 3, 4, 5]
# y_axis = [45 , 3, 3, 2 ,34 ]
#
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.title('Test plot')

# Customzied Line Plot
# plt.plot(x_axis, y_axis, 'k--o')
# The following format string characters are accepted to control the line style or marker:
# character 	description
# '-' 	solid line style
# '--' 	dashed line style
# '-.' 	dash-dot line style
# ':' 	dotted line style
# '.' 	point marker
# ',' 	pixel marker
# 'o' 	circle marker
# 'v' 	triangle_down marker
# '^' 	triangle_up marker
# '<' 	triangle_left marker
# '>' 	triangle_right marker
# '1' 	tri_down marker
# '2' 	tri_up marker
# '3' 	tri_left marker
# '4' 	tri_right marker
# 's' 	square marker
# 'p' 	pentagon marker
# '*' 	star marker
# 'h' 	hexagon1 marker
# 'H' 	hexagon2 marker
# '+' 	plus marker
# 'x' 	x marker
# 'D' 	diamond marker
# 'd' 	thin_diamond marker
# '|' 	vline marker
# '_' 	hline marker
#
# The following color abbreviations are supported:
# character 	color
# ‘b’ 	blue
# ‘g’ 	green
# ‘r’ 	red
# ‘c’ 	cyan
# ‘m’ 	magenta
# ‘y’ 	yellow
# ‘k’ 	black
# ‘w’ 	white


# Multiple plots
x = [1, 2, 3, 4, 5]
y1 = [23, 45, 67, 89, 90]
y2 = [90, 89, 67, 45, 23]
plt.figure(figsize=(9,5) )
plt.subplot(2, 2, 1)
plt.title("Plot 1")
plt.plot(x, y1, 'g-o')

plt.subplot(2, 2, 2)
plt.title("Plot 2")
plt.plot(x, y2)

plt.subplot(2, 2, 3)
plt.title("Plot 3")
plt.plot(x, y2, 'r--')

plt.show()