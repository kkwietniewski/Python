n = int(input())
arr = list(map(int, input().rstrip().split()))
revArr = ''
for i in reversed(arr):
    revArr += str(i)+' '
print(revArr)
