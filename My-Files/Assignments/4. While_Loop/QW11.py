# 11. Reverse a List: Given a list, reverse its elements using a while loop.

my_list = [1, 2, 3, 4, 5]

start = 0
end = len(my_list) - 1
while start < end:
    my_list[start], my_list[end] = my_list[end], my_list[start]
    
    start += 1
    end -= 1
print(my_list)