
nums = {}
def Fibonacci(n: int, nums: dict):
    if n in nums:
        return nums[n]
    if n <= 2:
        return 1
    num = Fibonacci(n-1, nums) + Fibonacci(n-2, nums)
    nums[n] = num
    return num


print(Fibonacci(10, nums))
print(Fibonacci(50, nums))