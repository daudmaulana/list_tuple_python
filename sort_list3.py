def myFunction(x):
    return x % 10


list1 = [17, 23, 46, 51, 90]
print(f'List before sort: {list1}')
list1.sort(key=myFunction)
print(f'List after sort: {list1}')
