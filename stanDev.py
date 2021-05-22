import math #math library
import numpy as np

x = np.loadtxt("matrix.txt")
#create a standard deviation calculator
 
#same mean calculator but optimized for less steps
def mean(values):
 
    #all steps crunched into one return statement
    return sum(values)/len(values)
   
def stanDev(values):
    #again, values is the list of numbers
 
    #find the length of the list
    length = len(values)
 
    #because we are dealing with standard deviation, we need to know the mean
    #so we call the mean function with our list values
    m = mean(values)
 
    #create a sum variable since this is not the same
    total_sum = 0
 
    #start a for loop going through each number in values
    for i in range(length): #creates a list 0 - length minus one
 
        #add the number for stan. dev. to sum
        total_sum += (values[i]-m)**2
    #return the standard deviation
    return math.sqrt(total_sum/(length-1))
 
#create a list called x
#x = [1, 2, 34, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# mean value
mean_val= mean(x)
#now we assign a variable stan_dev to the standard deviation of the list
stan_dev = stanDev(x)
 
#then print the value
print ('mean value:          ', mean_val)
print ('variance:            ', stan_dev**2)
print ('standard deviation:  ',stan_dev)

