class Statistics:
    CONSTANTS = {6: 2.5706, 11: 2.2281, 16: 2.1314, 21: 2.0860, 26: 2.0555, 31: 2.0423, 36: 2.0301, 41: 2.0211,
                 51: 2.0086, 101: 1.9840}

    def __init__(self, number_of_starts, times):
        self.number_of_starts = number_of_starts
        self.times = times
        self.constant = self._set_constant()
        self.average = self._count_average()
        self.standard_deviation = self._count_standard_deviation()
        self.confidence_interval = self.constant * self.standard_deviation / self.number_of_starts**0.5

    def _set_constant(self):
        if self.number_of_starts in self.CONSTANTS.keys():
            return self.CONSTANTS.get(self.number_of_starts)
        known_constant = 6
        for key in self.CONSTANTS.keys():
            if known_constant < self.number_of_starts < key:
                return (self.CONSTANTS.get(known_constant) - self.CONSTANTS.get(key)) / (key - known_constant)
            known_constant = key

    def _count_average(self):
        return sum(self.times) / self.number_of_starts

    def _count_standard_deviation(self):
        res = 0
        for t in self.times:
            res += (t - self.average) ** 2
        return (res / (self.number_of_starts - 1)) ** 0.5
