from typing import List
from datetime import datetime, timezone
from src.get_data import GetData, Feature
from src.save_data import SaveData


nowa_utc = datetime.now(timezone.utc)
timestamp = nowa_utc.strftime("%Y%m%d_%H%M00")

data: List[Feature] = GetData().execute(timestamp)
SaveData().execute(data)

for city in data:
    if city.properties.city_name == "":
        print("-------------------------------", city.properties)
        print("\n")
