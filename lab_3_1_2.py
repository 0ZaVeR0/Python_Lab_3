def compare(*lists):
    result = set(lists[0])
    for x in lists:
        result = result & set(x)
    if len(result) == 0:
        return True
    else:
        return False


print(compare([2,1,4],[4,1,6],[13,5,8]))