from .Gas import Gas

class IdealGas(Gas):
    """
    Represents an Ideal Gas following PV = nRT.
    Assumes point particles with no interaction.
    """
    def pressure(self, V, T):
        # P = nRT / V
        return (self.n * self.R * T) / V

    def __repr__(self):
        return f"IdealGas(n={self.n} mol)"
