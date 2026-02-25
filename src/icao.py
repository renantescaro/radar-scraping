import json


class Icao:
    def __init__(self) -> None:
        self._icao_list_search = self._get_icao_from_file()

    def _get_icao_from_file(self) -> dict:
        with open("icao.json", "r", encoding="utf-8") as file:
            icao_data_list = json.load(file)
            return {item["icao"]: item["city"] for item in icao_data_list}

    def get_city_name(self, icao: str):
        return self._icao_list_search.get(icao, icao)
