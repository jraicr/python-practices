# Layout exercise: Shows 4 plots in two rows

from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
from bokeh.layouts import gridplot

import math

doc = curdoc()

# All plots shares the same size
plots_size = {'width': 400, 'height':400}

# Data values for plots
x = list(range(1, 11))
y1 = x
y2 = [11 - i for i in x]
y3 = [i * i for i in x]
y4 = [math.log10(i) for i in x]

# First plot
fig1 = figure(width = plots_size['width'], height = plots_size['height'])
fig1.line(x, y1, line_width = 2, line_color = 'blue')

# Second plot
fig2 = figure(width = plots_size['width'], height = plots_size['height'])
fig2.circle(x, y2, size = 10, color = 'green')

# Third Plot
fig3 = figure(width = plots_size['width'], height = plots_size['height'])
fig3.circle(x, y3, size = 10, color = 'grey')

# Forth plot
fig4 = figure(width = plots_size['width'], height = plots_size['height'])
fig4.line(x, y4, line_width = 2, line_color = 'red')

# Create grid and appends the plots
grid = gridplot(children = [[fig1, fig2], [fig3, fig4]], sizing_mode = 'stretch_both')


# Appends grid to DOM
doc.add_root(grid)