# User Input and While Loops

## How the input( ) Function Works

```python
message = input("Input a Value")
print(f"User input value is {message}")
```

### Using int( ) to Accept Numerical Input

```python
age = int(input("Type your age here"))
print(f"Input age: {age}")
#
if age > 17:
    print(f"成年人")
else:
    print(f'未成年人')
```

### The Modilo Operator

```python
number = int(input('Type a number here'))
if number % 2 == 2:
    print(f"The number {number} is a even.")
else:
    print(f"The number {number} is a odd.")
```

## Introducing while Loops

> The for loop takes a collection of items and executes a block of code once for each item in the collection. In
> contrast, the while loop runs as long as, or while, a certain condition is true.

### The while Loop in Action

```python
current_number = 1
while current_number <= 5:
    # the following condition will be run when the condition is TURE.
    print(current_number)
    current_number += 1
```

### Letting the User Choose When to Quit

```python
message = ""
while message != "quit":
    message = input("prompt")
    print(message)
```

```python
message = ""
while message != "quit":
    print("Tell me something, and I will repeat it back to you :\nEnter 'quit' to end the program")
    message = input("Type Here !")
    print(f"{message}\n")

```

### Using a Flag

```python
active = True
while active:
    message = input("prompt")

    if message == "quit":
        active = False
    else:
        print(message)
    print("Loop")
```

### Using break to Exit a Loop

```python
active = True
while active:
    message = input("prompt")

    if message == "quit":
        break
    else:
        print(message)
    print(message)
```

### Using continue in a Loop

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

### Avoiding Infinite Loops

```python
# This loop runs forever! x= 1
# while x <= 5:
#    print(x)
```

## Using a while Loop with Lists and Dictionaries

### Moving Items from One List to Another

```python
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(f"\n{unconfirmed_users}")
print(f"\n{confirmed_users}")

```

### Removing All Instances of Specific Values from a List

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print("count")
print(pets)
```

### Filling a Dictionary with User Input

```python
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

   # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
       print(name + " would like to climb " + response + ".")
```
