from typing import Union


ranges_type = list[tuple[Union[float, int], Union[float, int]]]

class Statespace():
    def __init__(self, minimize: bool, n_dimensions: int, *args) -> None:

        # check for correct usage
        if len(args) != 2 * n_dimensions:
            raise ValueError("The amount of range arguments does not match " +
                             "with the amount of dimensions")
        
        self.minimize = minimize
        self.n_dimensions = n_dimensions        
        self.ranges: ranges_type = self.get_ranges(n_dimensions, args)

    def is_minimize(self) -> bool:
        return self.minimize

    def get_n_dimensions(self) -> int:
        return self.n_dimensions
    
    def get_ranges(self, n_dimensions: int, args: tuple) -> ranges_type:
        
        ranges: ranges_type = []
        
        for i in range(n_dimensions):
            ranges.append((args[i*2], args[i*2 + 1]))

        return ranges