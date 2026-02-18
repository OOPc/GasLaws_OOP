from .Gas import Gas

class VanDerWaalsGas(Gas):
    """
    Represents a Real Gas using the Van der Waals equation.
    (P + a n^2 / V^2) (V - nb) = nRT
    
    P = (nRT / (V - nb)) - (a n^2 / V^2)
    """
    def __init__(self, moles, a, b, name="Real Gas"):
        """
        Args:
            moles (float): Number of moles
            a (float): Attraction parameter [Pa * m^6 / mol^2]
            b (float): Volume exclusion parameter [m^3 / mol]
            name (str): Name of the gas (e.g., 'Nitrogen')
        """
        super().__init__(moles)
        self.a = float(a)
        self.b = float(b)
        self.name = name

    def pressure(self, V, T):
        # Term 1: Repulsion / Volume Exclusion
        # P_kinetic = nRT / (V - nb)
        numerator = self.n * self.R * T
        denominator = V - (self.n * self.b)
        
        if denominator <= 0:
            raise ValueError("Volume too small for gas molecules (V <= nb)")

        term1 = numerator / denominator

        # Term 2: Attraction
        # P_attraction = a * (n/V)^2
        term2 = self.a * ((self.n / V) ** 2)

        return term1 - term2

    def __repr__(self):
        return f"VanDerWaalsGas(name='{self.name}', n={self.n} mol)"
