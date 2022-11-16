# def reverse_list(s):
    # temp_list = list(s)
    #temp_list.reverse()
    # return ''.join(temp_list)
#import string_reverse
#string_reverse.reverse_slicing("ABç∂EF"*10)
import timeit
 
# code snippet to be executed only once
mysetup = "from math import sqrt"
# code snippet whose execution time is to be measured
mycode = '''
def example():
    mylist = [1,2,3,4]
    for x in range(100):
        mylist.append(sqrt(x))
'''
# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 1000))
