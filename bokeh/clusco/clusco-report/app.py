# 6 differents plots
# X axis: Date and hour of data
# Y axis - plot 1: Pacta temperature (deg) -> Rango: 0 - max data
# Y axis - plot 2: SCB temp (deg) -> Rango: 
# Todos comparten mismo eje X: Fecha y hora del dato

# Graf


from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure



doc = curdoc()

plot_size = {'width': 500, 'height': 500}

# PLOT 1
# Fake data values for the moment



