def solution(number):
    return sum(nums for nums in range(number) if not nums % 3 or not nums % 5)

print(solution(10))
