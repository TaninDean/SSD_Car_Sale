from regex import R
from utils.dao.car_dao import CarTrans
from utils.dao.customer_dao import CustomerTrans
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CrateDB:

    def __init__(self, databese_nmae) -> None:
        self.__db = create_engine("sqlite:///" + databese_nmae, echo=True)
        self.__session = sessionmaker(bind=self.__db)
        self.__used = self.__session()

    def get_car(self):
        return CarTrans(self.__used)

    def get_customer(self):
        return CustomerTrans(self.__used)

