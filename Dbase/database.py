
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Config import DATABASE

BaseClass = declarative_base()


class Cache(BaseClass):
    __tablename__ = 'cache'

    id = Column('id_cache', Integer, primary_key=True)
    title = Column('title', String)
    type_file = Column('type_file', String)

    def __repr__(self):
        return "<Cache('%s', '%s')>" % (self.title, self.type_file)


def connect_db():
    engine = create_engine(f'sqlite:///{DATABASE}', echo=False, connect_args={'check_same_thread': False})
    BaseClass.metadata.create_all(engine)

    return engine


def add_data_db(connect, title, type_file):
    Session = sessionmaker(bind=connect)
    session = Session()
    cache = Cache(title=title, type_file=type_file)
    session.add(cache)
    session.commit()


def get_data_db(connect):
    Session = sessionmaker(bind=connect)
    session = Session()

    data = []
    for elem in session.query(Cache.title, Cache.type_file).all():
        data.append(elem._asdict())
    return data


def get_count_rows(connect):
    Session = sessionmaker(bind=connect)
    session = Session()

    rows = session.query(Cache).count()
    return rows


def clear_all(connect):
    Session = sessionmaker(bind=connect)
    session = Session()

    session.query(Cache).delete()
    session.commit()

