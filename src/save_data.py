from typing import List
from database.database import Database
from database.model.metar_model import Metar
from src.get_data import Feature


class SaveData:
    def execute(self, data: List[Feature]):
        for item in data:
            try:
                Database().save(
                    Metar(
                        icao=item.properties.id,
                        date_time=item.properties.data_hora,
                        latitude=item.properties.latitude,
                        longitude=item.properties.longitude,
                        elevation_m=item.properties.elevation_m,
                        ceiling_is_minimum=item.properties.ceiling_is_minimum,
                        visibility_is_minimum=item.properties.visibility_is_minimum,
                        temperature=item.properties.temperatura,
                        dew_point=item.properties.ponto_orvalho,
                        relative_humidity=item.properties.umidade_relativa,
                        wind_direction=item.properties.dir_vento,
                        wind_speed=item.properties.veloc_vento,
                        wind_gust_mps=item.properties.wind_gust_mps,
                        visibility=item.properties.visibilidade,
                        extinction_per_km=item.properties.extinction_per_km,
                        msl_pres=item.properties.msl_pres,
                        city_name=item.properties.city_name,
                    )
                )
            except Exception as e:
                print(e)
