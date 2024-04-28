def permutations(digits):
    if len(digits) == 1:
        return [digits]
    
    perms = permutations(digits[1:])
    char = digits[0]
    result = []

    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])

    return result

print(permutations("123"))