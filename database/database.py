import os
import pymysql
from dotenv import load_dotenv
from typing import Any, List, Optional
from sqlalchemy.exc import IntegrityError
from sqlmodel.sql.expression import SelectOfScalar, Select
from sqlmodel import SQLModel, Session, create_engine
from database.model import __init__

pymysql.install_as_MySQLdb()
load_dotenv()

engine = create_engine(
    url=os.getenv("DATABASE_URL", ""),
    max_overflow=0,
    pool_size=10,
    pool_recycle=10,
    echo=False,
)
SQLModel.metadata.create_all(engine)


class Database:
    def __init__(self) -> None: ...

    def get_one(
        self,
        statement: SelectOfScalar | Select,
    ) -> Any:
        try:
            with Session(engine) as session:
                return session.exec(statement).first()
        except Exception as e:
            print(f"'Database' error in 'get_one': {e}")

    def get_all(
        self,
        statement: SelectOfScalar | Select,
    ) -> Optional[List[Any]]:
        try:
            with Session(engine) as session:
                return session.exec(statement).all()

        except Exception as e:
            print(f"'Database' error in 'get_all': {e}")

    def save(
        self,
        object_model: Any,
        refresh: bool = True,
    ) -> Any:
        try:
            with Session(engine) as session:
                session.add(object_model)
                session.commit()

                if refresh:
                    session.refresh(object_model)

                return object_model
        except IntegrityError as e:
            if "1062" in str(e.orig):
                print(f"Registro duplicado ignorado")
                return None

            print(f"'Database' error in 'save': {e}")

        except Exception as e:
            print(f"'Database' error in 'save': {e}")

    def delete(self, object_model) -> None:
        with Session(engine) as session:
            session.delete(object_model)
            session.commit()

    def execute_sql(self, sql_command: str) -> Optional[List[Any]]:
        try:
            with Session(engine) as session:
                result = session.exec(sql_command)
                session.commit()

                if not result.returns_rows:
                    return

                field_names = result.keys()
                results_dict = [
                    dict(zip(field_names, row)) for row in result.fetchall()
                ]

                return results_dict
        except Exception as e:
            print(f"'Database' error in 'execute_sql': {e}")
