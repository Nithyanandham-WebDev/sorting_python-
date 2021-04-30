# bubble sort
def bubsort(arr):
	n = len(arr)
	for x in range(n):
		for y in range(0,n-x-1):
			if arr[y] > arr[y+1]:
				 arr[y],arr[y+1] = arr[y+1],arr[y]
arr = [64,34,25,12,22,11,90]

bubsort(arr)

print("sorting array is :")

for x in range(len(arr)):
	print("%d" %arr[x] )

# selection sort 

import sys

a = [64,25,12,22,11]


for x in range(len(a)):
	min_idx = x
	for y in range(x+1,len(a)):
		if a[min_idx] > a[y]:
			min_idx = y
	a[x],a[min_idx] = a[min_idx],a[x]

print("sorted array")
for x in range(len(a)):
	print("%d" %a[x])



# insertion sort


def insertionsort(arr):
	for x in range(1,len(arr)):
		key = arr[x]
		y = x-1
		while y >= 0 and key <arr[y]:
			arr[y + 1] = arr[y]
			y-= 1
		arr[y + 1] = key

arr = [12,11,13,5,6]

insertionsort(arr)
print("insertion sort ")
for x in range(len(arr)):
	print("% d " % arr[x])
