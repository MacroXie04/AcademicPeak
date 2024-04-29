# Introductory Java Language Features

### Built-in Types
Each identifier in a Java program is associated with a type. In Java, there are int, double, and Boolean types.

```java
int i;
//An integer
//4 Bits, 32 bits
//Example, 2,-3,4000

boolean i;
//A boolean. Just two values Ture or False

double i;
//A double pricisionn floating-point number
//Example, 2.718, -383848.44, 134553353
//8Bits, 64bits
```

### Final Data Type
The final keyword in Java is used to mark a variable as a constant. Once a final variable is assigned a value, it cannot be changed.
```java
final int MAX_VALUE = 100;
//A final integer constant with the value of 100
```

### Type Casting
In Java, type casting is used to convert one data type into another. It can be done implicitly or explicitly.
```java
int i = 10;
double d = 3.14;

// Type casting from int to double
double result1 = (double) i; // result1 will be 10.0

// Type casting from double to int
int result2 = (int) d; // result2 will be 3
```

### Arithmetic Operators

```java
// Addition
int sum = 5 + 3; // Adding 5 and 3, result: 8

// Subtraction
int difference = 10 - 4; // Subtracting 4 from 10, result: 6

// Multiplication
int product = 6 * 7; // Multiplying 6 and 7, result: 42
        
// Division
double quotient = 15.0 / 4.0; // Dividing 15 by 4, result: 3.75

// Modulus (Remainder)
int remainder = 17 % 5; // Taking the remainder of 17 divided by 5, result: 2
        
// Integer Division
int intDivision = 9 / 4; // Integer division of 9 by 4, result: 2      
```

### Relational Operators

```vbnet
// Equality Operator (==)
boolean isEqual = 5 == 5; // Checks if 5 is equal to 5

// Inequality Operator (!=)
boolean isNotEqual = 10 != 7; // Checks if 10 is not equal to 7

// Greater Than Operator (>)
boolean isGreaterThan = 15 > 10; // Checks if 15 is greater than 10

// Less Than Operator (<)
boolean isLessThan = 8 < 12; // Checks if 8 is less than 12

// Greater Than or Equal To Operator (>=)
boolean isGreaterThanOrEqual = 20 >= 18; // Checks if 20 is greater than or equal to 18

// Less Than or Equal To Operator (<=)
boolean isLessThanOrEqual = 25 <= 30; // Checks if 25 is less than or equal to 30
```

Relational Operators are used on **boolean** expressions that evluate to ture or false.

Do not routinely use == to test for equality of floating-point numbers.

### Logical Operators

```
public class LogicalOperatorsExample {
    public static void main(String[] args) {
        boolean found = false;
        int x = 2, y = 5;
        int age = 1;
        double height = 3.5;
        
        // Not Operator (!)
        if (!found) {
            System.out.println("Not found");
        }
        
        // And Operator (&&)
        if (x < 3 && y > 4) {
            System.out.println("x is less than 3 and y is greater than 4");
        }
        
        // Or Operator (||)
        if (age < 2 || height < 4) {
            System.out.println("Either age is less than 2 or height is less than 4");
        }
    }
}
```

Assignment Operators

```
public class AssignmentOperatorsExample {
    public static void main(String[] args) {
        int x = 4;
        int y = 10;
        int p = 3;
        int n = 25;
        
        // Simple Assignment (=)
        int simpleAssignment = x; // Assigns the value of x (4) to simpleAssignment
        
        // Addition Assignment (+=)
        x += 4; // Equivalent to: x = x + 4
        
        // Subtraction Assignment (-=)
        y -= 6; // Equivalent to: y = y - 6
        
        // Multiplication Assignment (*=)
        p *= 5; // Equivalent to: p = p * 5
        
        // Division Assignment (/=)
        n /= 10; // Equivalent to: n = n / 10
        
        // Modulus Assignment (%=)
        n %= 10; // Equivalent to: n = n % 10
    }
}
```

### Increment and Decrement Operators

```
public class IncrementDecrementOperatorsExample {
    public static void main(String[] args) {
        int i = 5;
        int k = 8;
        
        // Post-increment (i++)
        int postIncrement = i++; // The value of i is used, then i is incremented by 1
        
        // Pre-increment (++i)
        int preIncrement = ++i; // i is incremented by 1, then its value is used
        
        // Post-decrement (k--)
        int postDecrement = k--; // The value of k is used, then k is decremented by 1
        
        // Pre-decrement (--k)
        int preDecrement = --k; // k is decremented by 1, then its value is used
    }
}
```

### Operator Precedence

1. !, ++, —
2. *, /, %
3. +, -
4. <, >, <=, >=
5. ==, !=
6. &&
7. ||
8. =, +=, -=, *=, /=, %=

```java
//Example
System.out.println(5 + 3 < 6 - 1);
//output: false
```

### Escape Sequences

```java
//Example
System.out.print("Hot");
System.out.println("dog");
//output: Hotdog

System.out.println(7 + 3);
//output: 10

System.out.println(7 == 2 + 5);
//output: ture

System.out.println("Welcome to\na new line");
//output: Welcome to
//a new line

System.out.println("He is known as \"Hothead Harry\".");
//output: He is known as "Hothead Harry".
```

### Decision-Making Control Structures

These include the `if`, `if...else`, and `switch` statements. Each of these is a selection control structure that
introduces decision-making abilities into a program. Based on the truth value of a Boolean expression, the computer will
decide which path to follow.

### The `if` Statement

```java
if ("boolean expression"){
	statements;
}
//The statements will run only the boolean expression is **ture.**

//These two are the same
****if("boolean expr1"){
	if("boolean expr2"){
		statements;
	}
}

if("boolean expr1"&&"boolean exor2"){
	steatements;
}
```

### The `if...else` Statement

```java
if ("boolean expression"){
	statements; // executed when **ture**
}
else{
	statements; // executed when **false**
}
```

### The `while` Loop

The **while** loop in Java is a control statement that allows a section of code to be executed repeatedly while a
certain condition is true. The loop consists of a condition expression that is evaluated before each iteration of the
loop. If the condition returns **ture** , the loop body is executed, otherwise the loop terminates.

```java
//Example
int i = 0;
while (i < 10) {
	//When codition expression is **TURE** 
	System.out.println("Hello, World!");
  i++;
}
//output: The loop will repeat "Hello,World!" for 10 times
```

It's important to be careful when using a **while** loop, as if the condition never becomes **false**, the loop will run
indefinitely and result in an **infinite loop**.

### The `for` Loop

The **for** loop in Java is a structured loop control statement used to repeat a section of code. It consists of three
parts: an **initialization statement**, a **condition expression**, and an **increment/decrement statement**.

```java
for(initializtion statement,condition expression,in/decrement statement){
	//When codition expression is **TRUE**
}
```

The initialization statement is executed once at the beginning of the loop and is used to define the loop variable and
its initial value. The condition expression is evaluated each time the loop is executed, and if it returns **true**, the
loop body is executed. Otherwise, the loop terminates. Finally, the increment/decrement statement is executed each time
the loop is executed, and it is used to update the value of the loop variable.

```java
//example 
for (int i = 0; i < 10; i++) {
   System.out.println("Hello, World!");
}
//output: The loop will repeat "Hello,World!" for 10 times
```

### Enhanced `for` Loop (For-Each Loop)

The enhanced for loop, also known as the for-each loop, in Java is a compact and convenient way to iterate through
elements in an array or any other type of collection, such as **`List`** or **`Map`**. It eliminates the need to manage
a counter variable and index, and provides a clean and simple way to process each element in the collection.

```java
//syntax
for (type var : collection) {
   // code to be executed for each element in collection
}
```

```java
//Example
int[] numbers = {1, 2, 3, 4, 5};
for (int number : numbers) {
   System.out.print(number);
}
//output: 12345
```
### Reference & Primitive Data Types

In Java, data types can be categorized into two main groups: primitive data types and reference data types.

### Reference & Primitive Data Type

Primitive data types are the most basic data types provided by Java. They hold simple values and are not objects. There are eight primitive data types in Java:
Primitive data types are stored directly in the stack memory and hold their values directly.

- `int`: 32-bit signed integer. Example: `int i = 100000;`
- `double`: 64-bit floating-point. Example: `double d = 3.14;`
- `boolean`: Represents true or false. Example: `boolean flag = true;`

Reference data types are used to refer to objects. They don't store the actual data, but they store the reference(address) to the object in memory. Examples of reference data types include:
Reference data types are stored in the heap memory. They are created using the `new` keyword and manipulated through references.

- Objects of a class: `String`, `ArrayList`, `LinkedList`, etc.
- Arrays: `int[]`, `double[]`, `String[]`, etc.

```java
// Primitive data type example
int primitiveValue = 10;
System.out.println("Primitive Value: " + primitiveValue);

// Reference data type example
String referenceValue = new String("Hello");
System.out.println("Reference Value: " + referenceValue);

//Output:
Primitive Value: 10
Reference Value: Hello


```






```java
// Primitive data type example
int primitiveValue = 10;

// Reference data type example
String referenceValue = new String("Hello");
