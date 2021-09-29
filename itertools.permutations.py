from itertools import permutations

string, r = input().split()

print(*[''.join(i) for i in sorted(list(permutations(string,int(r))))], sep = '\n')