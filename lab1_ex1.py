def lab1_ex1():
    
# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
    x = 52633
    factors = []

    for i in range(1, x + 1):  # Start from 1 to avoid division by zero
        if x % i == 0:  # Check if i is a factor of x
            factors.append(i)

    print(factors)
  
if __name__ == '__main__':
    lab1_ex1()

# My Trial below>>>> 

# def lab1_ex1():
    
# # Find the all factors of x using a loop and the operator %
# # % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
#     x = 52633
#     for i in range(1,x+1):
#         if x % i == 0:
#             print(i)
  
# if __name__ == '__main__':
#     lab1_ex1()



