a = 5
b = 10

# print("Hello my name is Mew.")
# print(a+b)

if a < b:
    # print("a < b")
# elif a == b:
    # print(a == b)
# else:
    # print("I don't know")

# ----------------------------------------------------

# def mul_a_b(a, b):
    '''
    This function multiply a and b together.
    return a*b
    '''
    # print(a * b)

# mul_a_b(3, 4)

# Challenge!
# creating a function to calculate the area of circle.
# Users will specify the number of circle, 
# the program will calculate the area of each circle with radius -1
# for example
# input : 5
# process: [the area of circle of radius 1-5 will be calculated].
# output: [print all areas on the screen].
def cal_circle_area(radius):
    return 3.141*radius*radius

circle_number = int(input("Give me number: "))

areas = []

for i in range(1,circle_number+1):
    area = cal_circle_area(i)
    areas.append(area)
    print(f"The area of {i} is {area}")

    areas.pop(0)
    areas.append(10)
    print(sum(areas))


    #x=x+1
    #cir = 3.14*x*x
    #cir_array = []
    #cir_array.append(cir)
    #print(cir_array[0:5])


#cir_array.pop(0)
#cir_array.append(10)

#print(cir_array[0:5])

# Challenge 2!
# -------------------------------------
# from the first challenge...store all areas in an array. :)
# take out the first area of the list,
#                     and then add 10 at the end of the array.
# Then, sum all areas and display on screen.

#the_array = [1,2,3,4,5]
#the_array[0] #first element
#the_array[-1] #last element
#print(the_array[2:5]) #[3,4,5]
#the_array.append(10) #add 10 at the array

grades = {'Mark': 'A', 
          'Jib': 'B'}

print(grades['Mark']) # A
print("Mark")