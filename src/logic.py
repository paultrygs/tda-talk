import numpy as np


def time_delay_embedding(time_series: np.ndarray, delay: int) -> tuple[np.ndarray, np.ndarray]:
    return time_series[:len(time_series) - delay], time_series[delay:]