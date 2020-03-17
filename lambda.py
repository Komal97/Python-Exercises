#lambda 
g = lambda x: x * x * x
print(g(3))

#lambda with filter
input_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x : (x%2 !=0), input_list))
print(final_list)

#lambda with map
input_map_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_map_list = list(map(lambda x : x*2, input_map_list))
print(final_map_list)

#lambda with reduce
from functools import reduce
input_reduce_list = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y : x+y), input_reduce_list) #(((((5+8)+10)+20)+50)+100).
print(sum)
