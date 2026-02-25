import requests
from dataclasses import dataclass
from typing import List
from src.icao_enum import IcaoEnum


@dataclass
class Geometry:
    type: str
    coordinates: List[float]


@dataclass
class FeatureProperties:
    id: str
    data_hora: str
    latitude: str
    longitude: str
    elevation_m: str
    ceiling_is_minimum: str
    visibility_is_minimum: str
    temperatura: str
    ponto_orvalho: str = ""
    umidade_relativa: str = ""
    dir_vento: str = ""
    veloc_vento: str = ""
    wind_gust_mps: str = ""
    visibilidade: str = ""
    extinction_per_km: str = ""
    msl_pres: str = ""
    city_name: str = ""


@dataclass
class Feature:
    geometry: Geometry
    type: str
    properties: FeatureProperties


class GetData:
    def __init__(self) -> None:
        self._url = "https://www.ipmetradar.com.br/alerta/ppigis/share/metar.php"
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def _get_city_name(self, props_id: str) -> str:
        try:
            return IcaoEnum[props_id].value
        except KeyError:
            return ""

    def execute(self, timestamp: str) -> List[Feature]:
        result = requests.get(
            # TODO: data_hora é inutil?
            url=f"{self._url}?data_hora={timestamp}",
            headers=self._headers,
        )

        if result.status_code not in [200, 201, 204]:
            return []

        json_data = result.json()
        features_list = []

        for feat in json_data["features"]:
            geo = Geometry(**feat["geometry"])

            props = FeatureProperties(**feat["properties"])

            props.city_name = self._get_city_name(props.id)

            f = Feature(geometry=geo, type=feat["type"], properties=props)

            features_list.append(f)

        return features_list
