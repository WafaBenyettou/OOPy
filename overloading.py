class Calculator:
    def add(self, a, b=0):
        return a + b

calc = Calculator()
print(calc.add(5))      # Output: 5 (uses default b=0)
print(calc.add(5, 10))  # Output: 15 (uses provided b=10)


## java 

"""

Same method name, different parameters (type or number). Supported in some languages
but simulated in Python with default arguments or variable-length arguments.

class Printer {
    void print(String message) {
        System.out.println(message);
    }

    void print(int number) {
        System.out.println(number);
    }
}
"""