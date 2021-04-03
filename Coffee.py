import plotly_express as px
import numpy as np
import csv

def mainFunction(data_path):
    cupsofCoffee = []
    sleepinHours = []
    with open(data_path, newline='') as f:
        data = csv.DictReader(f)
        # graph = px.scatter(data, x='Coffee in ml', y='sleep in hours', color='week')
        # graph.show()
        for row in data:
            cupsofCoffee.append(float(row['Coffee in ml']))
            sleepinHours.append(float(row['sleep in hours']))
    
    return {'x': sleepinHours, 'y': cupsofCoffee}

def findingCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print(f'Correlation is {correlation[0]}')

def setup():
    path = 'D:\cfrbackup-LLGBPKSV\Whitehatjr\Python Classes\C-106-Project\cups of coffee vs hours of sleep.csv'
    source = mainFunction(path)
    findingCorrelation(source)

setup()