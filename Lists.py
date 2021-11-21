#append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#clear
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)

#copy
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print(fruits)

#count
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x)

#extend
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

#index
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)

#insert
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)

#pop
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)
print(fruits)

#remove
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
print(fruits)

#reverse
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)

#sort
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)


