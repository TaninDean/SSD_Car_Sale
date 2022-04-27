from sqlalchemy import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()

class Car(Base):
    """Car information

        Arg:
        id(int) = The ID of Car
        name(String) = The brand of car
        model(String) = The model of car
        price(String) = The price of car
    """
    _tablename_ = 'car_list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    model = Column(String(25), nullable=False)
    price = Column(Integer, nullable=False)

    def __rerp__(self):
        return f"<id={self.id} name={self.name} model={self.model} price={self.price}>"
