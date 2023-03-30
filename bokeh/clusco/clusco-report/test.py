from pymongo import MongoClient
import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.layouts import column

# Connect to the MongoDB database
client = MongoClient()
db = client['CACO']
collection = db['CLUSCO_hour']

# Define the initial size of the dataset to load
INITIAL_SIZE = 1000

SCB_pixel_temperature_query = { 'name' : 'scb_pixel_temperature' }

# Load the initial dataset from MongoDB into a Pandas dataframe
data = pd.DataFrame(list(collection.find(SCB_pixel_temperature_query).limit(INITIAL_SIZE)))

# Convert the "date" field to a datetime object
data['date'] = pd.to_datetime(data['date'])

# Create a ColumnDataSource object
source = ColumnDataSource(data)

# Create a figure object
p = figure(title="Average temperature per date", x_axis_type='datetime', x_axis_label='Date', y_axis_label='Temperature')

# Plot the data
p.line(x='date', y='avg', source=source)

# Format the x-axis tick labels
p.xaxis.formatter = DatetimeTickFormatter(hours=['%H:%M'])

# Define a function to update the plot with new data
def update():
    # Load the latest data from MongoDB into a Pandas dataframe
    latest_data = pd.DataFrame(list(collection.find(SCB_pixel_temperature_query).sort('date', -1).limit(1)))
    
    # Convert the "date" field to a datetime object
    #latest_data['date'] = pd.to_datetime(latest_data['date']['$date'])
    
    # Append the latest data to the existing data
    #data.append(latest_data, ignore_index=True)
    
    # Update the ColumnDataSource object with the new data
    source.data = data

# Add the plot to the current document
curdoc().add_root(column(p))

# Add a periodic callback to update the plot every hour
curdoc().add_periodic_callback(update, 60*60*1000)