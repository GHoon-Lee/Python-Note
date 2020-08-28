n, m = 4, 6

d = [19, 15, 10, 17]

start=0
end=max(d)

answer=0

while (start<=end):
    result=0
    mid=(start+end)//2
    for i in d:
        if i> mid:
            result+=(i-mid)
    
    if result<m:
        end=mid-1
    else:
        answer=mid
        start=mid+1

print(answer)