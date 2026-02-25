
## Radar Meteorológico - Coletor METAR
Este projeto é uma automação em Python projetada para realizar a raspagem (scraping), processamento e armazenamento de dados climáticos de diversas estações aeroportuárias do Brasil (METAR). Os dados são extraídos do IPMet, tratados e salvos em um banco de dados MySQL utilizando SQLModel.

### URL de coleta
`https://www.ipmetradar.com.br/alerta/ppigis/share/metar.php`

### Tecnologias Utilizadas
- Python 3.11
- SQLModel (SQLAlchemy + Pydantic) para ORM.
- PyMySQL como driver de conexão.
- Docker & Docker Compose para containerização.
- IPMet API como fonte de dados.


### Docker
```cmd
docker-compose up -d --build
```
