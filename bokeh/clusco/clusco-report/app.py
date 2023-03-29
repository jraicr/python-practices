# 6 differents plots
# X axis: Date and hour of data
# Y axis - plot 1: Pacta temperature (deg)
# Y axis - plot 2: SCB temp (deg)
# Todos comparten mismo eje X: Fecha y hora del dato

import pymongo
import pandas
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.plotting import curdoc, figure

# Html doc reference
doc = curdoc()

# Configure database connection
mongoURI = 'mongodb://localhost:27017/'
mongoClient = pymongo.MongoClient(mongoURI)
db = mongoClient["CACO"]

# Get data from CLUSCO_hour collection
clusco_hour_collection = db['CLUSCO_hour']

# SCB Temperature values
SCB_temperature_query = { 'name' : 'scb_temperature' }
clusco_SCB_temperature_data = pandas.DataFrame(list(clusco_hour_collection.find(SCB_temperature_query)))

source = ColumnDataSource({'x':[clusco_SCB_temperature_data['avg']], 'y':[clusco_SCB_temperature_data['date']]})

plot = figure()
plot.line('x', 'y', source = source)
plot.xaxis.axis_label = 'x'
plot.yaxis.axis_label = 'y'

doc.add_root(plot)



# db = mongoClient["CACO"]
# clusco_hour_data = db['CLUSCO_hour']

# SCB_Temp_query = { 'name' : 'scb_temperature' }
# cursor_SCB_Temp_docs = clusco_hour_data.find(SCB_Temp_query)

# source = ColumnDataSource(cursor_SCB_Temp_docs)
# y_values = ['avg', 'max', 'min']

# print(y_values)

#doc = curdoc()

#plot_size = {'width': 500, 'height': 500}

# PLOT 1



