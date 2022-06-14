from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


user = 'root'           #имя пользователя
password = ''           #пароль
host = 'localhost'      #имя хоста
port = 3306             #порт
database = 'library_db' #название БД

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"  #собрать строку для подключения
engine = create_engine(SQLALCHEMY_DATABASE_URL) #подключится

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #настройки сессии подключения

Base = declarative_base()