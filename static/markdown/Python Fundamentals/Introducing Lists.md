# Introducing Lists

## What Is a List?

> A list is a collection of items in a particular order.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

## Working With Lists

### Accessing Elements in a List

> Index Positions Start at 0
> Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python
> always returns the last item in the list.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[1])
print(bicycles[1].title())
print(bicycles[-1])
```

### Changing, Adding, and Removing Elements

```python
motorcycles = []

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzeki")

print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.insert(1,"ducati")
print(motorcycles)
del motorcycles[1]
print(motorcycles)
```

### Removing an Item Using the pop() Methods

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)
temp = motorcycles.pop()
print(motorcycles)
print(temp)
```

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles.pop(1))
print(motorcycles)
```

### Remove an Item by Value

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
```

### Organizing a List

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
cars.reverse()
print(cars)
print(len(cars))
```

### Looping Through an Entire List

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

print()

for magican in magicians:
	print(f'{magican.title()}, that was a great trick!')
```

### Doing More Work Within a for Loop

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"name: {magician}")

print(magicians)
```

### Avoiding Indentation Errors

> Python uses indentation to determine when one line of code is connected to the line above it. In the previous
> examples, the lines that printed messages to individual magicians were part of the for loop because they were indented.
> Python’s use of indentation makes code very easy to read. Basically, it uses whitespace to force you to write neatly
> formatted code with a clear visual structure. In longer Python programs, you’ll notice blocks of code indented at a few
> different levels. These indentation levels help you gain a general sense of the overall program’s organization.

```python
# Forgetting to Indent
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
```

```python
# Forgetting to Indent Additional Lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
```

```python
# Indenting Unnecessarily
message = "Hello world !"
    print(message)
```

```python
# Forgetting the Colon
magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)
```

## Making Numerical Lists

> Many reasons exist to store a set of numbers. For example, you’ll need to keep track of the positions of each
> character in a game, and you might want to keep track of a player’s high scores as well. In data visualizations, you’ll
> almost always work with sets of numbers, such as temperatures, distances, population sizes, or latitude and longitude
> values, among other types of numerical sets.

### Using the range() Function

```python
for value in range(1,5):
    print(value)
```

```python
numbers = list(range(1,5))
print(numbers)
```

```python
even_numbers = list(range(2,11,2))
for valus in even_numbers:
    print(valus)
    
print(even_numbers)
```

```python
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
    
```

### Simple Statistics with a List of Numbers

```python
digits = list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))
```

## List Comprehensions

```python
squares = [value**2 for value in range(1,11)]
print(squares)
```

## Working with Part of a List

### Slicing a List

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:100000])
```

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:])
```

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```

### Looping Through a Slice

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print()
for player in players[:3]:
    print(player.title())
```

### Copying a List

```python
my_Foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_Foods
friend_foods_copy = my_Foods [:]
print(friend_foods)
print(my_Foods)

my_Foods.append('food')

print(friend_foods)
print(friend_foods_copy)
```

## Tuples

> Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

### Define tuples

```python
dimensions = (20,500)
print(dimensions[0])
print(dimensions[1])

dimensions[0] = 250
```

### Looping Through All Values in a Tuple

```python
dimensions = (20,500)

for dimension in dimensions:
    print(dimension)
```

### Writing over a Tuple

```python
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

print("\nWriting over\n")

dimensions = (250,400)
for dimension in dimensions:
    print(dimension)
```
