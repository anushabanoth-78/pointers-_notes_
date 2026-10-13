def smallest_number(number):
    smallest=number[0]
    for num in number:
        if num<smallest:
            smallest =num
    return smallest
number = [18, 6, 25, 3, 14]
print(smallest_number(number))
