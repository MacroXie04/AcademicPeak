# If Statements

## Conditional Tests

> At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional
> test. Python uses the values True and False to decide whether the code in an if statement should be executed. If a
> conditional test evaluates to True, Python executes the code following the if statement. If the test evaluates to False,
> Python ignores the code following the if statement.

```python
car = 'BMW'
print(car=="BMW")

print(car=="Audi")
```

```python
# Ignoring Case When Checking for Equality
car = 'Audi'
print(car=='audi')
print(car.lower()=='audi')
```

### Checking for Inequality

```python
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': 
    print("Hold the anchovies!")
```

### Numerical Comparisons

```python
age = 18
print(age==18)
print(age>10)
```

### Checking Multiple Conditions

```python
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)
```

### Checking Whether a Value Is in a List

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
```

## A Simple Example

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

## Testing Multiple Conditions

### If-else Statement

```python
condition_text = False
if condition_text:
    print("the condition is ture")
else:
    print("the condition is false")
    
```

### If-elif-else Chain

```python
age = 10

if age<4:
    print("age is under 14")
elif age<18:
    print("age is above 4-18")
else:
    print("age is greater than 18")
```

> The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass. As soon as
> Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial, because it’s efficient
> and allows you to test for one specific condition. However, sometimes it’s important to check all of the conditions of
> interest. In this case, you should use a series of simple if statements with no elif or else blocks. This technique
> makes sense when more than one condition could be True, and you want to act on every condition that is True.

```python
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
```

## Using if Statements with Lists

### Checking for Special Items

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
```

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
    if requested_topping == 'green peppers':
        print(f'Sorry, we are out of {requested_topping}right now')
```

### Checking That a List Is Not Empty

```python
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your Pizza")
else:
    print('The list is empty!')
```

### Using Multiple Lists

```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}")
```
