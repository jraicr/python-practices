# Streaming data (Generate fake data based on random values)

import random
from bokeh.driving import count
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

doc = curdoc()

update_interval = 100
roll_over = 100

source = ColumnDataSource({'x':[], 'y':[]})

@count()
def update(x):
    y = random.random()
    source.stream({'x':[x], 'y':[y]}, rollover=roll_over)
    #source.stream({'x':[x], 'y':[y]})
    
plot  = figure()
plot.line('x', 'y', source = source)
plot.xaxis.axis_label = 'x'
plot.yaxis.axis_label = 'y'

doc.add_root(plot);
doc.add_periodic_callback(update, update_interval)