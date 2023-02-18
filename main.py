from Components.dbHandler import dbManager
from urllib.request import urlopen
import json



rawurl = "https://analisi.transparenciacatalunya.cat/resource/irki-p3c7.json"

def fetchURL(url):
    response = urlopen(url)
    return json.loads(response.read())

def exctractData(data):
    result = {}
    for record in data:
        # Get the date and comarca for the record
        date = record['data'][:10]  # Get the first 10 characters of the data string (i.e. yyyy-mm-dd)
        comarca = record['comarca']
        # Check if the record corresponds to the first dose of the vaccine
        if record['dosi'] == '1':
            # If the date and comarca are not already in the result dictionary, add them with a count of 0
            if (date, comarca) not in result:
                result[(date, comarca)] = 0
            # Increment the count for the date and comarca
            result[(date, comarca)] += 1
    
    cmd = []
    for (date, comarca), count in result.items():
        cmd.append((date,comarca,count))
    return cmd

def main():
    db = dbManager()
    db.connect()
    jsonrawdata = fetchURL(rawurl)
    jsonusabledata = exctractData(jsonrawdata)
    db.makeQuery(jsonusabledata)
    db.disconnect()
if __name__ == "__main__":
    main()