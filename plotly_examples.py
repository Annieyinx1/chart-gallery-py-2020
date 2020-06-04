
import plotly.graph_objects as go
#import numpy as np

#
# example line chart
#

# see: https://realpython.com/how-to-use-numpy-arange/
#x = np.arange(10) #> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(type(x))
#print(x)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#fig = go.Figure(data=go.Scatter(x=x, y=x**2))
y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
fig = go.Figure(data=go.Scatter(x=x, y=y))
fig.show()

#
# example bar chart
#

animals=['giraffes', 'orangutans', 'monkeys']
fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
fig.show()

#
# example pie chart
#

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
