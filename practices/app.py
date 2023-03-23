from datetime import datetime

def createData():
    data = [
        {"date": "03-19-2023", "hour": "22:45", "force": "28", "angle" : "91"},
        {"date": "03-18-2023", "hour": "22:35", "force": "30", "angle" : "90"},
        {"date": "03-20-2023", "hour": "22:40", "force": "24", "angle" : "92"},
        {"date": "03-18-2023", "hour": "12:23", "force": "30", "angle" : "90"},
        {"date": "03-21-2023", "hour": "22:50", "force": "18", "angle" : "90"}]
    
    return data


dataList = createData()

# Sort data by date and hour
orderedDataList = sorted(dataList, key=lambda d: (d['date'], d['hour']))


print(orderedDataList)