from pymongo import MongoClient
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
import pandas as pd
import itertools
from bokeh.palettes import Dark2_5 as palette

# import DatetimeTickFormatter
from bokeh.models.formatters import DatetimeTickFormatter

# Curdoc reference
webdoc = curdoc()

# Used as limit for the database query
INITIAL_SIZE = 250

# Connect to the MongoDB database
client = MongoClient()
db = client['CACO']
collection = db['CLUSCO_hour']

SCB_pixel_temperature_query = { 'name' : 'scb_pixel_temperature' }

dataCollection = collection.find(SCB_pixel_temperature_query).limit(INITIAL_SIZE)

# This isn't right, each document has the value for each pixel in a given date. So to plot
# each pixel temperature average value and show it with a single line we need to
# transpose the values in the array 'avg' 

# for document in dataCollection:
#     for i in range(0, len(document['avg'])):
#         dates.append(document['date'])
#         temps.append(document['avg'][i])
        
# Converts mongodb dataCollection cursor to a pandas dataframe
df = pd.DataFrame(list(dataCollection))    
cds = ColumnDataSource(df)

print(cds.data)

plot = figure(title="Average temperature per date", x_axis_label='Date', y_axis_label='PACTA Temperature')
# colors = itertools.cycle(palette)

plot.multi_line(xs='date', ys='avg', source=cds, color=palette)

# # In the pandas dataframe there is a column called 'avg' which contains an array of values for each row. Each of this array values correspond to the temperature of a pixel from a camera. We need to plot each pixel temperature with his own line. Make the code
# # to plot each pixel temperature with a different color.
# for i in range(0, len(df['avg'][0])):
#     plot.line(x='date', y='avg', source=ColumnDataSource(df), color=next(colors))


# Format the x-axis UTC time
plot.xaxis.formatter = DatetimeTickFormatter(hours=['%H:%M'])

# Plot the data
# plot.line(x='dates', y='temps', source=source)

webdoc.add_root(plot);