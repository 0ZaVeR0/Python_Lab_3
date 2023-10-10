def compare(*lists: int) -> bool:
    result = set(lists[0])
    for x in lists:
        result = result & set(x)
    if len(result) == 0:
        return True
    else:
        return False

def main():
    print(compare([2,1,4],[4,1,6],[13,1,5,8]))

if __name__ == "__main__":
    main()