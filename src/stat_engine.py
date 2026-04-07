import math
import collections
from typing import List, Union

class StatEngine:
    def __init__(self, data: List):
        self.data = self._clean_data(data)

    def _clean_data(self, data: List) -> List[float]:
        cleaned = []
        for item in data:
            try:
                if item is not None:
                    cleaned.append(float(item))
            except (ValueError, TypeError):
                continue
        return cleaned

    def _check_empty(self):
        if not self.data:
            raise ValueError("Dataset is empty.")

    def get_mean(self) -> float:
        self._check_empty()
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        self._check_empty()
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def get_mode(self) -> Union[List[float], str]:
        self._check_empty()
        counts = collections.Counter(self.data)
        max_count = max(counts.values())
        if max_count == 1:
            return "No mode: All values are unique."
        return sorted([val for val, count in counts.items() if count == max_count])

    def get_variance(self, is_sample: bool = True) -> float:
        self._check_empty()
        mu = self.get_mean()
        sq_diff_sum = sum((x - mu) ** 2 for x in self.data)
        divisor = len(self.data) - 1 if is_sample else len(self.data)
        if divisor <= 0: return 0.0
        return sq_diff_sum / divisor

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold: float = 2.0) -> List[float]:
        self._check_empty()
        mu = self.get_mean()
        sigma = self.get_standard_deviation()
        if sigma == 0: return []
        return [x for x in self.data if abs(x - mu) > (threshold * sigma)]
