index = 0
arr = [2,3]
N = 2       
final = []

def recursion(index,subset,arr,N,final):
    if len(subset) == N or index >=N:
        final.append(sum(subset))
        return
        
    # pick an element
    recursion(index+1,subset+[arr[index]],arr,N,final)
    
    # not pick an element
    recursion(index+1,subset,arr,N,final)
    
recursion(0,[],arr,N,final)
print(final)