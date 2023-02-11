def selection_sort(arr):
  n=len(arr)
  for i in range(0,n):
    min=i
    for j in range(i+1,n):
      if arr[j]<arr[min]:
        min=j
    arr[min],arr[i]=arr[i],arr[min]
  return arr
print(selection_sort(list(map(int,input().split()))))
