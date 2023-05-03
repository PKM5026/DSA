#Binary Search Implementaion 

pos = -1
def search(list, n):
    i = 0
    while i < len(list):
        if list[i]==n:
            globals()['pos'] = i #local
            return pos
        i = i + 1
    return False

list = [5, 8, 4, 6, 9, 2] 
n = 6

if search(list,n):
    print('found at index', pos)
else:
    print('not found') 