class DaoBase:

    def __init__(self, session) -> None:
        self._session = session

    def get_seeion(self):
        return self._session