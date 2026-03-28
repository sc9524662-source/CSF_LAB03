numbers = [2, 4, 6, 8, 10]
search_for = 8
print(f"List: {' '.join(map(str, numbers))}")
print(f"Searching for: {search_for}")

for num in numbers:
    if num == search_for:
        print("Number found")
        break