class Faucet():
    def __init__(self):
        self._position = 0.0 # Levr position [%]

    @property
    def open_position(self) -> float:
        """
        Returns: the open position of the faucet [%]
        Return: open position
        """
        return self._position
    
    @open_position.setter
    def open_position(self, value: float) -> None:
        """
        Sets the open position of the faucet
        """
        self._position = value

    def position(self, value: float):
        pass