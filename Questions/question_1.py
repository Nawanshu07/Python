#Program to find second largest number in a list 

nums = []
n = int(input("Enter number of elements:"))

for i in range(0,n):
    a = int(input("Enter some number:"))
    nums.append(a)

largest = float('-inf')
sec_largest = float('-inf')

for i in range(0,n):
    if(nums[i] > largest):
        sec_largest = largest
        largest = nums[i]

    elif(nums[i] > sec_largest and nums[i]!=largest):
        sec_largest = nums[i];
    
print("Largest:",largest)
print("second Largest:",sec_largest)