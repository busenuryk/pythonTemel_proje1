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


#ikinci

def cevirme(lst):
    return [sub[::-1] if isinstance(sub, list) else sub for sub in lst[::-1]]

input_data = [[1, 2], [3, 4], [5, 6, 7]]
output = cevirme(input_data)
print(output)
