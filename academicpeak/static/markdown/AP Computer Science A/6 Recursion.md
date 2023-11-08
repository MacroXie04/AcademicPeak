# Recursion

Recursion is a programming technique in which a function calls itself one or more times to solve a problem. It is a
powerful and versatile tool that can be used to solve a wide range of problems, from simple mathematical computations to
complex data structures and algorithms.

To use recursion, a function typically checks if a specific termination condition has been met, and if not, the function
calls itself with a modified set of parameters until the termination condition is met. This creates a stack of function
calls, with each new call being added to the top of the stack, until the termination condition is met and the stack is "
unwound" as each function call returns.

```java
public static int factorial(int n) {
    if (n == 0) {
        return 1; 
				// Termination condition
    } else {
        return n * factorial(n-1); // Recursive call
    }
}
```

In this function, if the input **`n`** is 0, the function returns 1 (the termination condition). Otherwise, the function
calls itself with **`n-1`** as the input, and multiplies the result with **`n`**. This process continues until the input
reaches 0, at which point the function returns the final result.

Recursion can be a powerful and elegant solution to many problems, but it can also be a source of bugs and performance
issues if not used carefully. Careful consideration should be given to the termination conditions, the base case, and
the recursive call to ensure that the function returns the correct result and does not result in an infinite loop or
excessive memory usage.