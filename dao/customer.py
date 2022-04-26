from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

class custoemr(Base):
    """Cusomter infromation

        Args:
        id(int) = the Id of transaction
        first_name = the firstname of customer
        last_name = the lastname of customer
        car_id = the id of cat that customer buy
    """
    _tablename_ = 'customer'
    id = Column(Integer, primary_ley=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    car_id = Column(Integer, ForeignKey('car.id'))

    def __repr__(self) -> str:
        return f"id={self.id} firstname={self.first_name} last_name={self.last_name} carId={self.car_id}"