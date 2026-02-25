import json

from src.brazilian_states_enum import BrasilianStatesEnum


"""
formata os dados da ANAC para o padrão do meu projeto
https://sistemas.anac.gov.br/dadosabertos/Aerodromos/Aer%C3%B3dromos%20P%C3%BAblicos/Lista%20de%20aer%C3%B3dromos%20p%C3%BAblicos/AerodromosPublicos.json
"""

_reverse_state_map = {state.value.lower(): state.name for state in BrasilianStatesEnum}

anac_all_itens = []
anac_new_itens = []
actual_system_list = []

# file from anac
with open("sistemas_anac.json", encoding="utf-8") as file:
    data = json.load(file)

    for item in data:
        OACI = item["CódigoOACI"]
        name = item["Nome"]
        city = item["Município"]
        state = item["UF"]

        anac_all_itens.append(
            {
                "icao": OACI,
                "city": str(city).title(),
                "state": str(state).title(),
                "description": name,
            }
        )


@staticmethod
def _item_exist(icao: str, data2):
    return any(item["icao"] == icao for item in data2)


@staticmethod
def _get_uf(state: str) -> str:
    return _reverse_state_map.get(state.lower(), state)


#  default system file
with open("icao.json", encoding="utf-8") as file2:
    actual_system_list = json.load(file2)

    for new_item in anac_all_itens:
        if not _item_exist(new_item["icao"], actual_system_list):
            anac_new_itens.append(
                {
                    "icao": new_item["icao"],
                    "city": f"{new_item['city']}, {_get_uf(new_item['state'])}",
                    "description": new_item["description"],
                }
            )

actual_system_list.extend(anac_new_itens)

with open("icao.json", "w", encoding="utf-8") as file:
    json.dump(actual_system_list, file, indent=4, ensure_ascii=False)

print(f"Sucesso! {len(anac_new_itens)} novos aeroportos adicionados.")
