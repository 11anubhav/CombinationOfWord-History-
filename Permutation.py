#python3 is used as a programming language
#backtracking Technique is used for permutation
def permute(nums):
    arr=[]
    n=len(nums)
    def recur(a1,l,r):
        if l==r:
            temp=a1[:]
            temp=''.join(temp)
            arr.append(temp)
        else:
            for i in range(l,r+1):
                a1[l],a1[i]=a1[i],a1[l]
                recur(a1,l+1,r)
                a1[l],a1[i]=a1[i],a1[l]
    recur(nums,0,n-1)
    return arr
string="History"
arr=list(string)
print(permute(arr))
		