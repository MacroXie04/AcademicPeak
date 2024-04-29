# Some Standard Classes

### The **object** class

The **object** class is the root of the class hierarchy. Every class in Java has **object** as a superclass, either
directly or indirectly. If you don't explicitly specify a superclass for a class, it will automatically extend the *
*object** class.

- **toString()**

```java
//Example
class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // If do not override the toString() method, the output will be the memory address of the object.
    //Override toString()
		public String toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }
}

class mian{
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        System.out.println(person); 
        // output: Person{name='Alice', age=30}
    }
}
```

- **equal()**

**Do not use == to test objects for equality. Ues equals methods.**

```java
class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

		// If the equals() method is not overridden, the comparison is based on the object's memory address.
		// override equal()
		public boolean equals(Object o) {
        if (o == this) {
            return true;
        }
        if (!(o instanceof Person)) {
            return false;
        }
        Person p = (Person) o;
        return p.name.equals(name) && p.age == age;
    }
}

public class Main {
    public static void main(String[] args) {
        Person person1 = new Person("Alice", 30);
        Person person2 = new Person("Alice", 30);
        Person person3 = person1;

        System.out.println(person1.equals(person2)); 
				// false
        System.out.println(person1.equals(person3)); 
				// true
    }
}
```

### The String class

The String class in Java represents a sequence of characters (String). It is part of the java.lang package, which means
it is auto magically imported and does not need an explicit import statement.

**String objects in Java are immutable, meaning that once String object is created, its content cannot be changed.**

```java
//Example
// Create new String
String str1 = "Hello, World!";
String str2 = new String("Hello, World!");
char[] charArray = {'H','E','L','L','O',};
String str3 = new String(chatArray);

//String puls String
String str1 = "Hello";
String str2 = "World";
String result = str1 + ", " + str2 + "!";
System.out.println(result); 
// Hello, World!
System.out.println(3+4+str1);
// 7Hello
Ststem.out.println(Str1+3+4);
// Hello34
```

### subString

1. **`substring(int beginIndex)`**: Returns a new string that is a substring of the original string starting from the
   specified **`beginIndex`** to the end of the original string.
2. **`substring(int beginIndex, int endIndex)`**: Returns a new string that is a substring of the original string
   starting from the specified **`beginIndex`** up to, but not including, the character at index **`endIndex`**. The
   character at index **`endIndex`** is not included in the resulting substring.

```java
String original = "Hello,World!";
//index:H(1)e(2)l(3)l(4)o(5),(6)W(7)o(8)r(9)l(10)d(11)!(12)

String sub1 = original.substring(0, 5); 
// Extracts characters from index 0 to 4
System.out.println(sub1); 
// Output: Hello

String sub2 = original.substring(7); 
// Extracts characters from index 7 to the end
System.out.println(sub2); 
// Output: World!

String sub3 = original.substring(0, original.length());
System.out.println(sub3); 
// Output: Hello, World!

```

## String.equal

The **`equals()`** method of the **`String`** class is used to compare whether the contents of two string objects are
equal.

```java
String str1 = "Hello, World!";
String str2 = "Hello, World!";
String str3 = "hello, world!";

// Comparing strings using the equals() method.
boolean isEqual1 = str1.equals(str2);
System.out.println(isEqual1); 
// true

// Using the equalsIgnoreCase() method to compare strings, ignoring case.
boolean isEqualIgnoreCase = str1.equalsIgnoreCase(str3);
System.out.println(isEqualIgnoreCase); 
// true
```

### String indexOf

1. This method takes a single argument, which is a character. It returns the index of the first occurrence of that
   character in the string, or -1 if the character is not found.
2. This method takes a single argument, which is a substring. It returns the index of the first occurrence of that
   substring in the string, or -1 if the substring is not found.

```java
//Example
String str = "Hello World";
int index = str.indexOf('o');
System.out.println(index); 
// Output: 4

String str = "Hello World";
int index = str.indexOf("World");
System.out.println(index); 
// Output: 6

String str = "Hello World";
// Start search at index 5
int index = str.indexOf('o', 5); 
System.out.println(index); 
// Output: 7
```

### The Integer and Double class

The Integer and Double class are part of java.lang package and are used to represent numerical values as object.

```java
//Example

// Creating Integer objects
Integer a = new Integer(10);
Integer b = Integer.valueOf("20");

// Arithmetic operations using Integer objects
int sum = a + b; // sum = 30
int difference = a - b; // difference = -10
int product = a * b; // product = 200
int quotient = b / a; // quotient = 2

// Creating Double objects
Double c = new Double(3.14);
Double d = Double.valueOf("2.718");

// Arithmetic operations using Double objects
double sumD = c + d; // sumD = 5.858
double differenceD = c - d; // differenceD = 0.422
double productD = c * d; // productD = 8.53752
double quotientD = c / d; // quotientD = 1.1552056555269922

int a = 10;
Integer b = a; // Autoboxing
int c = b; // Autounboxingffv
```

### Math Functions

```java
public class MathExamples {
    public static void main(String[] args) {
        // 1. Calculate absolute value
        int a = -5;
        int absA = Math.abs(a);
        System.out.println("Absolute value: " + absA);

        // 2. Round up
        double b = 3.6;
        double ceilB = Math.ceil(b);
        System.out.println("Round up: " + ceilB);

        // 3. Round down
        double floorB = Math.floor(b);
        System.out.println("Round down: " + floorB);

        // 4. Round to nearest integer
        double c = 7.5;
        long roundC = Math.round(c);
        System.out.println("Round to nearest integer: " + roundC);

        // 5. Calculate maximum value
        int max = Math.max(a, (int) c);
        System.out.println("Maximum value: " + max);

        // 6. Calculate minimum value
        int min = Math.min(a, (int) c);
        System.out.println("Minimum value: " + min);

        // 7. Calculate power
        double pow = Math.pow(2, 3);
        System.out.println("2 raised to the power of 3: " + pow);

        // 8. Generate random number
        double random = Math.random();
        System.out.println("Random number: " + random);
    }
}
```

# Arrays and Array Lists

### Initialization

An array is an object; therefore, the keyword new must be used in its creation. The size of an array remains fixed once
it has been created.

```java
//Example of creates an arrey of 25 double values and assigns the reference data to this array
double[] data = new double[25];

double data[] = new double[25];

double data[];
data = new double[25];

//reassign date to a new array of length 40
//new array not incloud privious data
data = new double[40];
```

### Initializer List

```java
//new and full value of intager array
int[] coins = new int[4];
coins[0]=1;
coins[1]=5;
coins[2]=10;
coins[3]=25;

//same function rewrite
int[] coins = {1,5,10,25};
```

### Length of Array

```java
int[] arr = {1, 2, 3, 4, 5};
int length = arr.length; 
// length will be 5

String[] strArr = {"apple", "banana", "orange"};
int length = strArr.length; 
// length will be 3
```

**Length counting starts from 1, while indexing starts from 0**

### Traversing a One-Dimensional Array

**Do not modify the data when using an enhanced for loop to process an array**

```java
//Return the number of even integers in array arr of integers
Public static int countEven(int[] arr){
	int count = 0;
	for (int num: arr){
		if(num%2==0){
			count++;
		}
	}
}
```

```java
//Change each even-indexed element in array arr to 0
Public static void changeEven(int[] arr){
	for(int i=0,i<arr.length,i+=2){
		arr[i]=0;
	}
}
```

### Arrays as Parameters

In Java, when an array is passed as a parameter to a function, it is typically passed by reference, which means that the
function uses the address of the original array instead of a copy of the array. This means that the function can modify
the original array directly, thereby affecting the original array.

```java
//Example
public static void printArray(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        System.out.println(a
//main
int[] myArray = {1, 2, 3, 4, 5};
printArray(myArray);

printArray(1, 2, 3, 4, 5);

//output
1
2
3
4
5
```

### Array Lists

Unlike an array, which has a fixed size once it is created, an array list can change its size at runtime. When an
element is added to an array list, it is appended to the end of the list. If the array list is already full, it will
automatically allocate additional memory to accommodate the new element. Similarly, when an element is removed from an
array list, the list automatically adjusts its size to reflect the new number of elements.

```java
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        
				// Create a new ArrayList
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        // Add some elements to the ArrayList
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);

        // Print out the ArrayList
        System.out.println(numbers);
				// Priny 1 2 3 4

        // Remove an element from the ArrayList
        numbers.remove(2);
				// Remove the third element(index is 2)

        // Print out the ArrayList again
        System.out.println(numbers);
				// Peint 1 2 4
				
				// Array list size
				int size = numbers.size();
				//size is 3

				// Get number in ArrayList
				int firstElement = numbers.get(0);
				// Get number 1

				// Set number in ArrayList
				numbers.set(1, 4);
				// Set 2 to 4
				// ArrayList 1 4 4
    }
}
```

```python
# Create a new list
numbers = []

# Add some elements to the list
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)

# Print out the list
print(numbers)

# Remove an element from the list
numbers.remove(2)

# Print out the list again
print(numbers)
```

### Two-Dimensional Arrays

A two-dimensional array (matrix) is often the data structure of choice for object like board games, tables of values,
theater seats, and mazes.

```java
// Example

// Declarations

int[][] table;
// table can reference a 2D array of integers
// table is currently a null reference

double[][] matrix = new double[3][4];
// matrix of double reference 3 * 4
// Each element has value of 0.0

String[][] stars = new String[2][5];
// stars of String referebce 2 * 5
// Each element has value of null

int[][] = {{3,4,5},{6,7,8}};
// row1 {3,4,5}
// row2 {6,7,8}
```

### Matrix as Array of Row Arrays

```java
// Example
// 3 * 4 Matrix

	2 6 8 7
	1 5 4 0
	9 3 2 8

	mat[1] contains {2,6,8,7}
	mat[2] contains {1,5,4,0}
	mat[3] contains {9,3,2,8}
```

### Processing a Two-Dimensional Array

- Enhanced for loop (for accessing or modifying elements that are class object, but no replacement)
- row-by-row array processing (for accessing, modifying, or replacement of elements)

```java
// Example 
// Find the sum of all elements in a matrix mat
int sum = 0;
for(int r=0;r<mat.length;r++){
	for(int c=0;c<mat[r].length;c++){
		sum += mat[r][c];
	}
]

// using enhanced for loop
int sum = 0;
for(int[]row :mat){ //for each row array in mat
	for(int element :row){ //for each element in this row
		sum += element;
	}
}
```

- row-column (for accessing, modifying elements that are class objects, or replacing elements)