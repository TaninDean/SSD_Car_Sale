from utils.dao.dao_base import DaoBase
from model.car import Car

class CarTrans(DaoBase):

    def __init__(self, session) -> None:
        self.__db = session
        
    def add_table(self, trans):
        tr = self.__db.add(trans)
        self.__db.commit()

    def get_all_car(self):
        return self.__db.query(Car).all()

    def get_car_by_band(self, band: str):
        return self.__db.query(Car).filer_by(name=band).all()

    def get_car_by_model(self, model: str):
        return self.__ab.query(Car).filer_by(model=model).all()


