

from ..classes.statespace import Statespace

"""
The hill climber needs to find a random start position in the statespace and
take a random step. It needs to check if the 
"""

class Hill_Climber():
    def __init__(self, statespace: Statespace) -> None:
        self.statespace = statespace