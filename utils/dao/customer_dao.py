from requests import session
from utils.dao.dao_base import DaoBase
from model.car import Customer

class CustomerTrans(DaoBase):

    def __init__(self, session):
        self.__db = session

    def get_all_custoemr(self):
        return self.__db.query(Customer).all()

    def get_customer_by_fistname(self, first_name: str):
        return self.__db.query(Customer).filter_by(first_name=first_name).all()

    def get_customer_by_last_name(self, last_name: str):
        return self.__db.query(Customer).filter_by(last_name=last_name).all()

    def add_customer_trnas(self, trans):
        tr = self.__db.add(trans)
        self.__db.commit()