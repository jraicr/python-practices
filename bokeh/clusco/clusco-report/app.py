import pandas as pd
import pymongo
from bson.objectid import ObjectId
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.server.server import Server

# Configure database connection
mongodbURI = 'mongodb://localhost:27017/'
mongoClient = pymongo.MongoClient(mongodbURI)
db = mongoClient["CACO"]
clusco_hour_data = db['CLUSCO_hour']

# Query to get data from SCB_pixel_temperature_query parameter name in collection
SCB_pixel_temperature_query = { 'name' : 'scb_pixel_temperature' }

# Define the function that will create the plot
def make_plot(doc):
    # Create a plot with a datetime x-axis type
    plot = figure(x_axis_type="datetime", title="SCB pixel temperature", height=350, width=800)
    
    # Query the database for the data
    cursor_SCB_pixel_temperature_docs = clusco_hour_data.find(SCB_pixel_temperature_query) 
    df_SCB_pixel_temperature = pd.DataFrame(list(cursor_SCB_pixel_temperature_docs))
    
    # Convert date column to datetime from df_SCB_pixel_temperature
    df_SCB_pixel_temperature['date'] = pd.to_datetime(df_SCB_pixel_temperature['date'])  
    
    # Convert the ObjectId to a string
    df_SCB_pixel_temperature['_id'] = df_SCB_pixel_temperature['_id'].apply(str)
    
    # Create a ColumnDataSource from the DataFrame
    source = ColumnDataSource(df_SCB_pixel_temperature)
    
    # Plot the data using multi_line
    plot.multi_line('date', 'avg', color='red', alpha=0.5, source=source)
    
    # Add the plot to the document
    doc.add_root(plot)

# Start the Bokeh server
server = Server({'/': make_plot})
server.start()

# Open the application in a new browser tab
server.io_loop.add_callback(server.show, "/")
server.io_loop.start()
