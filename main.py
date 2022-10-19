import numpy as np
from codecarbon import track_emissions


def run_demo():
    # Creates an array of 100.000.000 numbers between 0 and 999.999.999
    rand_nums = np.random.randint(0, 1000000000, 100000000)

    quicksort(rand_nums)
    mergesort(rand_nums)
    heapsort(rand_nums)


@track_emissions(offline=True, country_iso_code="ESP")
def quicksort(array: np.ndarray[int]):
    np.sort(array, kind='quicksort')


@track_emissions(offline=True, country_iso_code="ESP")
def mergesort(array: np.ndarray[int]):
    np.sort(array, kind='mergesort')


@track_emissions(offline=True, country_iso_code="ESP")
def heapsort(array: np.ndarray[int]):
    np.sort(array, kind='heapsort')


if __name__ == '__main__':
    run_demo()

