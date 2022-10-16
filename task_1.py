def filter_list(arr):
    """
    Filters initial list, only integers remain in a resulting list.
    """
    return list(filter(lambda el: isinstance(el, int), arr))