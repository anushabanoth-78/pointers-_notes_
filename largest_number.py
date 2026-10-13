def largest_number(number):
    largest =number[0]
    for num in number:
        if num>largest:
            largest=num
    return  largest
number =[10,20,40,50]
print(largest_number(number))
