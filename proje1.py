def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # Rekürsif olarak aç
        else:
            result.append(item)
    return result