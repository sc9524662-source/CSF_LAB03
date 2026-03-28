def add_numbers(a, b):
    return a + b
nums = input("Enter two numbers: ").split()
n1, n2 = int(nums[0]), int(nums[1])
print(f"Sum = {add_numbers(n1, n2)}")