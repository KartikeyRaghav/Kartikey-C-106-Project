import plotly_express as px
import numpy as np
import csv

def getDataSource(data_path):
    marksinPercentage = []
    days = []
    with open(data_path, newline='') as f:
        data = csv.DictReader(f)
        graph = px.scatter(data, x='Marks In Percentage', y='Days Present', color='Roll No')
        graph.show()
        for row in data:
            marksinPercentage.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    
    return {'x': marksinPercentage, 'y': days}

def findingCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print(f'Correlation is {correlation[0]}')

def setup():
    path = 'D:\cfrbackup-LLGBPKSV\Whitehatjr\Python Classes\C-106-Project\Student Marks vs Days Present.csv'
    source = getDataSource(path)
    findingCorrelation(source)

setup()