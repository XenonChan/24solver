inputs = str(input(("ตัวเลขที่ต้องการให้แก้: ")))
target_num = 24

count = 0

sym = ["+", "-", "*", "/"]

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

permutation = permutations(inputs)

for per in permutation:
    nums = [char for char in per]
    for i in range(len(sym)):
        for j in range(len(sym)):
            for k in range(len(sym)):
                op = [
                    f"{nums[0]} {sym[i]} {nums[1]} {sym[j]} {nums[2]} {sym[k]} {nums[3]}",
                    f"({nums[0]} {sym[i]} {nums[1]}) {sym[j]} {nums[2]} {sym[k]} {nums[3]}",
                    f"{nums[0]} {sym[i]} {nums[1]} {sym[j]} ({nums[2]} {sym[k]} {nums[3]})",
                    f"(({nums[0]} {sym[i]} {nums[1]}) {sym[j]} {nums[2]}) {sym[k]} {nums[3]}",
                    f"{nums[0]} {sym[i]} ({nums[1]} {sym[j]} ({nums[2]} {sym[k]} {nums[3]}))",
                    f"({nums[0]} {sym[i]} {nums[1]}) {sym[j]} ({nums[2]} {sym[k]} {nums[3]})"
                ]
                for x in op:
                   try:
                        if eval(x) == target_num:
                            print(f"{x} = {eval(x)}")
                            count += 1
                   except ZeroDivisionError:
                       pass
                   
print(f"วิธีคิดทั้งหมด {count} วิธี")