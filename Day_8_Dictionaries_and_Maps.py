n = int(input())
students = {}

for _ in range(n):
    name, phone = input().split()
    students[name] = phone

while True:
    try:
        query = input().strip()
        if query in students:
            print(f"{query}={students[query]}")
        else:
            print("Not found")
    except EOFError:
        break