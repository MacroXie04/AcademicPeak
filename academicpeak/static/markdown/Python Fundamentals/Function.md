# Function

## Defining a Function

```python
def sayhi():
    print("Hello world")

sayhi()
```

### Passing Information to a Function

```python
 def greet_user(username):
    print("Hello, " + username.title() + "!")
greet_user('Hongzhe')
```

### Arguments and Parameters

> In the preceding greet_user() function, we defined greet_user() to require a value for the variable username. Once we
> called the function and gave it the information (a person’s name), it printed the right greeting. The variable
> username
> in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its
> job.
> The value 'jesse' in greet_user('jesse') is an example of an argument. An argument is a piece of information that is
> passed from a function call to a function. When we call the function, we place the value we want the function to work
> with in parentheses. In this case the argument 'jesse' was passed to the function greet_user(), and the value was
> stored
> in the parameter username.

## Passing Arguments

> Because a function definition can have multiple parameters, a function call may need multiple arguments. You can pass
> arguments to your functions in a number of ways. You can use positional arguments, which need to be in the same order
> the parameters were written; keyword arguments, where each argument consists of a variable name and a value; and lists
> and dictionaries of values. Let’s look at each of these in turn.

### Passing Arguments

```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"Named {pet_name}.")

describe_pet("dog","yutian")
```

### Multiple Function Calls

```python
describe_pet('hamster','harry')
describe_pet('dog','willie')
```

### Keyword Arguments

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

### Default Values

```python
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
```

```python
describe_pet(pet_name="yutian")
```

```python
describe_pet()
```

## Return Values

> A function doesn’t always have to display its output directly. Instead, it can process some data and then return a
> value or set of values. The value the function returns is called a return value. The return statement takes a value
> from
> inside a function and sends it back to the line that called the function. Return values allow you to move much of your
> program’s grunt work into functions, which can simplify the body of your program.

### Returning a Simple Value

```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

```python
print(get_formatted_name('jimi', 'hendrix'))
```

### Making an Argument Optional

```python
def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

```

### Returning a Dictionary

```python
def build_person(first_name, last_name):
    person = {'first' : first_name, 'last' : last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('Hongzhe', 'Xie')
print(musician)

```

```python
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

print(build_person('jimi','hendrix',age=27))

```

### Using a Function with a while Loop

```python
def get_formatted_name(first_name,last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

while True :
    first = input("first name")

    if first == "q" :
        break

    last = input("last")

    if last == "q":
        break

    print(get_formatted_name(first,last))
```

## Passing a List

```python
def greet_users(names):
    for name in names:
        msg = f'Hello, {name.title()} !'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

### Modifying a List in a Function

```python
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

```python
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
```

```python
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
```

```python
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

## Passing an Arbitrary Number of Arguments

```python
def make_pizza(*toppings):
    print(toppings)
```

```python
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

```python
def make_pizza_needs(size,*topings):
    print(f'Making a {size}-inch pizza with the following toppings')
    for toping in topings:
        print(f'- {toping}')
```

```python
make_pizza_needs(16,'pepperoni')
make_pizza_needs(13,'mushrooms', 'green peppers', 'extra cheese')
```

### Using Arbitrary Keyword Arguments

```python
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
```

```python
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

user_profile = build_profile('Macro', 'Xie',location='Beijing',field='physics')
print(user_profile)
```

## Storing Your Functions in Modules

> To start importing functions, we first need to create a module. A module is a file ending in .py that contains the
> code you want to import into your program. Let’s make a module that contains the function make_pizza(). To make this
> module, we’ll remove everything from the file pizza.py except the function make_pizza():

```python
def make_pizza_needs(size,*topings):
    print(f'Making a {size}-inch pizza with the following toppings')
    for toping in topings:
        print(f'- {toping}')
```

```python
# import pizza
# import the function in pizza.py

# Using function in Python
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using function in Jupyter Notebook
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Importing Specific Functions

```python
# form module_name import function_name
# form module_name import function_1, function_2, function_3
```

### Using as to Give a Function an Alias

```python
# form module_name import function_name as use_name
```

### Using as to Give a Module an Alias

```python
# form module as use_name
# use_name.function_name('value')
```

### Importing All Functions in a Module

```python
# from module import *
```
