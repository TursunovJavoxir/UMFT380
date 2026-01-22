def min_of_three(a, b, c):
    return min(a, b, c)

a, b, c = map(int, input().split())
print(min_of_three(a, b, c))