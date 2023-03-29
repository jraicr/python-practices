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

mongoURI = 'mongodb://localhost:27017/'
mongoClient = pymongo.MongoClient(mongoURI)
db = mongoClient["CACO"]
clusco_hour_collection = db['CLUSCO_hour']

clusco_hour_data = pandas.DataFrame(list(clusco_hour_collection.find()))
print(clusco_hour_data)



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



