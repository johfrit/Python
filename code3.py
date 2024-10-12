n, index= map(int, input().split())
array= list(map(int, input().split()))
paid=int(input())
sum=0
for i in array:
    if i==array[index]:
        continue
    else:
        sum+=i
share=sum//2
if share==paid:
    print("Bon Appetit")
else:
    print(paid-share)
