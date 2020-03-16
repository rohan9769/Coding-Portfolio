# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
L = set(input().split())
for _ in range(int(input())):
    command, *args = input().split()
    getattr(L, command)(set(input().split()))
print(sum(map(int, L)))