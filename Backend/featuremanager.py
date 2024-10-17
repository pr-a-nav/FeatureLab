from feature import Feature
import pandas as pd
import typing
import sqlite3
from sqlalchemy import *
import sqlalchemy
from sqlalchemy.orm import sessionmaker




class FeatureManager:

    def __init__(self, db_url) -> None:
        self.engine = sqlalchemy.create_engine(db_url)
        self.Session = sessionmaker(bind = self.engine)

    def create_group(self, name, description):
        session = self.Session()
        group = Featuregroup(name,description) # type: ignore
        session.add(group)
        session.commit()
        session.close()