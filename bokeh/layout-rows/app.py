# Layout exercise: Shows two plots, each in one row

import random
from bokeh.driving import count
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

from bokeh.layouts import row

doc = curdoc()

update_interval = 100
roll_over = 100

source = ColumnDataSource({'x':[], 'y':[]})
source_2 = ColumnDataSource({'x':[], 'y':[]})

# Update step for X and generate a random value for Y
@count()
def update(x):
    y = random.random()
    source.stream({'x':[x], 'y':[y]}, rollover=roll_over)
    
    
@count()
def update_data_source(x):
    y = random.random()
    source_2.stream({'x':[x], 'y':[y]}, rollover = roll_over)
    
# Plot 1
plot = figure()
plot.line('x', 'y', source = source)
plot.xaxis.axis_label = 'x'
plot.yaxis.axis_label = 'y'


# Plot 2 
plot_b = figure()
plot_b.line('x', 'y', source = source_2)
plot_b.xaxis.axis_label = 'x'
plot_b.yaxis.axis_label = 'y'


r = row(children = [plot, plot_b], sizing_mode =  'stretch_both')

# Appends plot 1 to DOM
#doc.add_root(plot);
doc.add_periodic_callback(update, update_interval)

# Appends plot 2 to DOM
#doc.add_root(plot_b)
doc.add_periodic_callback(update_data_source, update_interval)

doc.add_root(r)

