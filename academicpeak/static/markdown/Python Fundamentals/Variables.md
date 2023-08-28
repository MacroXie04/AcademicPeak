## Variables


```python
# Add a variable named message and contain a String
message = "Hello Python World"
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

>When you’re using variables in Python, you need to adhere to a few rules and guidelines. Breaking some of these rules will cause errors; other guidelines just help you write code that’s easier to read and understand. Be sure to keep the following variable rules in mind:

- Variable names can contain only letters, numbers, and underscores.
- Spaces are not allowed in variable names, but underscores can be used to separate words in variable names.
- Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved for a particular programmatic purpose.
- Variable names should be short but descriptive.

### Avoiding Name Errors When Using Variables


```python
message = "Hellow Python World"
print(mesage)
```

>When a error occurs in program, the Python interpreter does its best to help  to figure out where the problem is. The interpreter provides a traceback when a program cannot run successfully.
