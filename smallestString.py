def smallestString(substrings):
    substrings = ["a","bc","ad"]
    sorted_substrings = sorted(substrings)

    result = ""
    for sorted_substring in sorted_substrings:
        result = result + sorted_substring
    return result

if __name__ == '__main__':

    substrings = ["a","bc","ad"]
    
    result = smallestString(substrings)

    print(result)
