a = {}
n = int(input())
for i in range(n):
    s = input().lower()
    sort_line = ''.join(sorted(s))
    a[sort_line] = a.get(sort_line, set())
    a[sort_line].add(s)
new_words = [' '.join(sorted(i)) for i in a.values() if len(i) > 1]
print('\n'.join(sorted(new_words)))