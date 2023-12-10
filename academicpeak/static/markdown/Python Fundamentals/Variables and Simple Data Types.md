# Variables and Simple Data Types

## Variables

```python
# Add a variable named message and contain a String
message = "Hellow Python World"
print(message)
```

```python
# The variable can be change in program at any time, and Python will always keep track of its current value.
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
```

### Naming and Using Variables

> When you’re using variables in Python, you need to adhere to a few rules and guidelines. Breaking some of these rules
> will cause errors; other guidelines just help you write code that’s easier to read and understand. Be sure to keep the
> following variable rules in mind:

- Variable names can contain only letters, numbers, and underscores.
- Spaces are not allowed in variable names, but underscores can be used to separate words in variable names.
- Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved
  for a particular programmatic purpose.
- Variable names should be short but descriptive.

### Avoiding Name Errors When Using Variables

```python
message = "Hellow Python World"
print(mesage)
```

> When a error occurs in program, the Python interpreter does its best to help to figure out where the problem is. The
> interpreter provides a traceback when a program cannot run successfully.

## String

> Because most programs define and gather some sort of data, and then do something useful with it, it helps to classify
> different types of data. The first data type we’ll look at is the string. Strings are quite simple at first glance,
> but
> you can use them in many different ways.

```python
String_1 = "This is a string"
String_2 = "This is also a string"
```

### Changing Case in s String Methods

```python
name = "ada lovelace"

print(name)
print(name.title())
print(name.upper())
print(name.lower())
```

### Combining or Concatenating Strings

```python
first_name = "ada"
last_name = "lovelace"

full_name = first_name + " " + last_name
print(full_name)

print("Hello, "+ full_name.title() + "!")

message = "Hello, "+ full_name.title() + "!"
print(message)

message = f"Hello, {full_name.title()}!"
print(message)
```

### Adding Whitespace to String with Tabs or Newlines

```python
# \n new line
# \t tab
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```

### Stripping whitespace

> To programmers 'python' and 'python  ' look pretty much the same. But to a program, they are two different strings.
> Python detects the extra space in 'python ' and considers it significant unless you tell it otherwise.

```python
language = "       Python        "
print(f'"{language}"')
print(f'"{language.rstrip()}"')
```

### Remove prefix

```python
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))
```

### Avoiding Type Errors with the str() Function

```python
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
```

```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

## Numbers

### Integers

```python
print(2+3)
print(3-2)
print(2*3)
print(3/2)
print(3**2)
print(3**3)
print(2+3*4)
print((2+3)*4)
```

### Floats

```python
print(0.1+0.1)
print(0.2+0.1)
print(2+0.1)
print(2*0.2)
print(3*0.1)
```

> This happens in all languages and is of little concern. Python tries to find a way to represent the result as
> precisely as possible, which is sometimes difficult given how computers have to represent numbers internally.

### Undereline

```python
universe_age = 14_000_000_000
print(universe_age)
```

### Define multi-variables

```python
x,y,z = 0,0,0
print(x)
print(y)
print(z)
```

### constant

> All capitalized variable name characters indicate constant

```python
FINAL_VALUE = 1000
```

```python
a = "vgecjrnefi"
b = "hrudijcfhu"
num = 1938494
print(f"{a}hcfuicjnbhdfngkoy{num}")
```

```python

```
