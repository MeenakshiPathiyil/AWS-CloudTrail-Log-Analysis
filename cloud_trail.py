import pandas as pd
import json
from pandas import json_normalize


with open("ctrail.json") as f:
    data = json.load(f)

# print (data.items())

df = pd.json_normalize(data["Events"])

print(df)

df.to_csv('CloudTrail_Logs.csv')

