import numpy as np


def generate_circle_data(n: int, r: float, x0: float, y0: float) -> tuple[np.ndarray, np.ndarray]:
    # Generate random noise
    n = 100
    noise = np.random.normal(0, 1, n)

    # Generate angles
    theta = np.linspace(0, 2*np.pi, n)

    return  x0 + r*np.cos(theta) + noise, y0 + r*np.sin(theta) + noise


def generate_disk_data(n: int, r: float, x0: float, y0: float) -> tuple[np.ndarray, np.ndarray]:
    # Generate radiuses and angles
    radius = np.random.uniform(0, r, n)
    theta = np.linspace(0, 2*np.pi, n)
    return x0 + radius*np.cos(theta), y0 + radius*np.sin(theta)


def get_time_series_with_oscillation_and_decay():
    t = np.linspace(1, 100, 1000)
    decay = np.exp(-t/20)
    oscillation = 40 * np.sin(t) * decay
    return np.linspace(1, 100, 1000) + oscillation
