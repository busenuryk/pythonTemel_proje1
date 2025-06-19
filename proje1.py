def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # Rekürsif olarak aç
        else:
            result.append(item)
    return result

input_data = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output = flatten(input_data)
print(output)
