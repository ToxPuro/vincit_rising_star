import requests


def len_longest_continuos_decreasing_subsequence(array):
    """Get the length of the longest continuos decreasing subsequence in array

    Args:
        array ([int]): Array of integers

    Returns:
        The length of the longest decreasing subsequence
    """
    anchor = 0
    result = 1
    for i in range(1,len(array)):
        if array[i-1] <= array[i]:
            anchor = i
        result = max(result, i-anchor+1)

    return result

def max_elem_and_index(array):
    """Gets the maximum element and the index of that element from array

    Args:
        array ([int])): array of ints to get the max elem and index

    Returns:
        tuple of (max, max_index)
    """
    max_elem  = array[0]
    max_index = 0
    for i in range(1,len(array)):
        if array[i]>max_elem:
            max_elem = array[i]
            max_index = i
    return (max_elem, max_index)


def max_diff_indexes(array):
    """Find the maximum difference in the array where the larger element is after the smaller one
    returns the indexes and the maximum difference
    If the length of the array is less than 2 returns 0

    Args:
        array ([int]): The array from where to find maximum difference.
        array consists of 2 length arrays

    Returns:
        Indexes of the maximum difference elements and maximum difference in a tuple
    """
    if len(array) < 2:
        return (0,0,0)

    
    max_diff = array[1] - array[0]
    min_element = array[0]
    min_element_index = 0
    indexes = (0,1)
    for i in range(1, len(array)):
        if array[i] - min_element > max_diff:
            max_diff = array[i] - min_element
            indexes = (min_element_index, i)

        if array[i] < min_element:
            min_element = array[i]
            min_element_index = i
    
    return (indexes[0], indexes[1], max_diff)

def get_prices_in_range(start, to, currency):
    """Get prices in given range from coingecko API

    Args:
        start (UNIX timestamp): start day of the range
        to (UNIX timestamp): end day of the range
        currency (string): the wanted currency

    Returns:
        Array of prices in wanted currency
    """
    receive = requests.get(f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency={currency}&from={start}&to={to}")
    ## the second price seems to be the price in the given currency
    return [price[1] for price in receive.json()["prices"]]

def get_volumes_in_range(start, to, currency):
    """Get the total volumes in a given range from coingecko API

    Args:
        start (UNIX timestamp): start day of the range
        to (UNIX timestamp): end day of the range
        currency (string): the wanted currency

    Returns:
    Array of total volumes in the wanted currency
    """
    receive = requests.get(f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency={currency}&from={start}&to={to}")
    ## the second price seems to be the volume in the given currency
    return [price[1] for price in receive.json()["total_volumes"]]


