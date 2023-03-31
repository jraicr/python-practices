from pymongo import MongoClient
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
import pandas as pd

# import DatetimeTickFormatter
from bokeh.models.formatters import DatetimeTickFormatter

# Curdoc reference
webdoc = curdoc()

# Constants
INITIAL_SIZE = 250

# Connect to the MongoDB database
client = MongoClient()
db = client['CACO']
collection = db['CLUSCO_hour']

# Extract the dates and average temperature values
dates = []
temps = []

SCB_pixel_temperature_query = { 'name' : 'scb_pixel_temperature' }

dataCollection = collection.find(SCB_pixel_temperature_query).limit(INITIAL_SIZE)
             
            
             
# This isn't right, each document has the value for each pixel in a given date. So to plot
# each pixel temperature average value and show each pixel temperature with a line we need to
# iterate over the documents and then over the pixels in each document

for document in dataCollection:
    for i in range(0, len(document['avg'])):
        dates.append(document['date'])
        temps.append(document['avg'][i])


# Create a ColumnDataSource object
source = ColumnDataSource(data=dict(
    dates=dates,
    temps=temps
))

# Show example of date format value
print(dates[0])

# Create a figure object
plot = figure(title="Average temperature per date", x_axis_label='Date', y_axis_label='PACTA Temperature')

# Format the x-axis UTC time
plot.xaxis.formatter = DatetimeTickFormatter(hours=['%H:%M'])

# Plot the data
plot.line(x='dates', y='temps', source=source)

webdoc.add_root(plot);