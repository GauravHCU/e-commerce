def SumMultiplier(arr):

  # code goes here
  sum=0
  for i in range(0, len(arr)):    
   sum = sum + arr[i]; 
   print("Sum of all the elements of an array: " + str(sum)); 

# keep this function call here 
print(SumMultiplier(int(input("enter the values"))))