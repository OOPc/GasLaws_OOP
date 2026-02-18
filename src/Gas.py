from abc import ABC, abstractmethod

class Gas(ABC):
    """
    Abstract Base Class for Gas Models.
    Defines the contract for any gas simulation (Ideal or Real).
    """
    R = 8.314  # Universal Gas Constant [J/(mol·K)]

    def __init__(self, moles):
        self.n = float(moles)

    @abstractmethod
    def pressure(self, V, T):
        """Calculate Pressure (Pa) given Volume (m^3) and Temperature (K)."""
        pass
