def odd_number(number):
    count=0
    for num in number:
        if num %2 !=0:
            count=count+1
    return count
number = [3, 8, 5, 12, 7, 10]
print( odd_number(number))
