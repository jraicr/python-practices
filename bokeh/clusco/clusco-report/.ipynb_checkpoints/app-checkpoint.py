# 6 differents plots
# X axis: Date and hour of data
# Y axis - plot 1: Pacta temperature (deg)
# Y axis - plot 2: SCB temp (deg)
# Todos comparten mismo eje X: Fecha y hora del dato

import pymongo
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

mongoClient = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongoClient["CACO"]
clusco_hour_data = db['CLUSCO_hour']

SCB_Temp_query = { 'name' : 'scb_temperature' }

SCB_Temp_doc = clusco_hour_data.find(SCB_Temp_query)

for x in SCB_Temp_doc:
    print(x)
    
#doc = curdoc()

#plot_size = {'width': 500, 'height': 500}

# PLOT 1



