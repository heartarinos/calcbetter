import math
import matplotlib.pyplot as plt
import numpy as np
import re
import cmath

# Global variables for memory and history
memory = []
history = []

# Function to display a menu of operations
def display_menu():
    print("\nScientific Calculator Menu")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (Exponentiation)")
    print("6. Square Root")
    print("7. Logarithm (Base 10)")
    print("8. Natural Logarithm (ln)")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Hyperbolic Sine (sinh)")
    print("13. Hyperbolic Cosine (cosh)")
    print("14. Hyperbolic Tangent (tanh)")
    print("15. Factorial")
    print("16. Permutation (nPr)")
    print("17. Combination (nCr)")
    print("18. Cube Root")
    print("19. Nth Root")
    print("20. Memory: Save current result")
    print("21. Memory: Recall last saved result")
    print("22. Memory: Save multiple results")
    print("23. Memory: Recall all saved results")
    print("24. Show Calculation History")
    print("25. Clear History")
    print("26. Constants (Pi, e, Planck’s constant, etc.)")
    print("27. Unit Conversion (meters to kilometers, grams to kilograms, etc.)")
    print("28. Graph Function (sin, cos, etc.)")
    print("29. Advanced Graphing (sine wave, cosine wave, tangent wave)")
    print("30. Statistical Functions (mean, median, mode, standard deviation)")
    print("31. Complex Numbers Operations (addition, subtraction, multiplication, division)")
    print("32. Polynomial Roots")
    print("33. Differential Calculus (first derivative)")
    print("34. Integral Calculus (definite integral)")
    print("35. Interactive GUI (text-based)")
    print("36. Exit\n")

# Function to add result to history
def add_to_history(operation, result):
    history.append(f"{operation} = {result}")

# Basic arithmetic functions
def add(x, y):
    result = x + y
    add_to_history(f"{x} + {y}", result)
    return result

def subtract(x, y):
    result = x - y
    add_to_history(f"{x} - {y}", result)
    return result

def multiply(x, y):
    result = x * y
    add_to_history(f"{x} * {y}", result)
    return result

def divide(x, y):
    try:
        result = x / y
        add_to_history(f"{x} / {y}", result)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"

# Extended mathematical functions
def power(x, y):
    result = x ** y
    add_to_history(f"{x} ^ {y}", result)
    return result

def square_root(x):
    if x >= 0:
        result = math.sqrt(x)
        add_to_history(f"√{x}", result)
        return result
    else:
        return "Error: Negative input for square root!"

def cube_root(x):
    result = x ** (1 / 3)
    add_to_history(f"∛{x}", result)
    return result

def nth_root(x, n):
    if x >= 0:
        result = x ** (1 / n)
        add_to_history(f"{x}^(1/{n})", result)
        return result
    else:
        return "Error: Negative input for nth root!"

def logarithm(x):
    if x > 0:
        result = math.log10(x)
        add_to_history(f"log10({x})", result)
        return result
    else:
        return "Error: Logarithm of non-positive number!"

def natural_log(x):
    if x > 0:
        result = math.log(x)
        add_to_history(f"ln({x})", result)
        return result
    else:
        return "Error: Natural log of non-positive number!"

# Trigonometric functions
def sine(x):
    result = math.sin(math.radians(x))
    add_to_history(f"sin({x}°)", result)
    return result

def cosine(x):
    result = math.cos(math.radians(x))
    add_to_history(f"cos({x}°)", result)
    return result

def tangent(x):
    result = math.tan(math.radians(x))
    add_to_history(f"tan({x}°)", result)
    return result

def hyperbolic_sine(x):
    result = math.sinh(x)
    add_to_history(f"sinh({x})", result)
    return result

def hyperbolic_cosine(x):
    result = math.cosh(x)
    add_to_history(f"cosh({x})", result)
    return result

def hyperbolic_tangent(x):
    result = math.tanh(x)
    add_to_history(f"tanh({x})", result)
    return result

# Factorial function
def factorial(x):
    if x >= 0:
        result = math.factorial(int(x))
        add_to_history(f"{x}!", result)
        return result
    else:
        return "Error: Factorial of negative number!"

# Permutation and Combination functions
def permutation(n, r):
    if n >= r >= 0:
        result = math.perm(n, r)
        add_to_history(f"P({n}, {r})", result)
        return result
    else:
        return "Error: Invalid inputs for permutation!"

def combination(n, r):
    if n >= r >= 0:
        result = math.comb(n, r)
        add_to_history(f"C({n}, {r})", result)
        return result
    else:
        return "Error: Invalid inputs for combination!"

# Memory functions
def save_to_memory(result):
    memory.append(result)
    print(f"Result saved to memory: {result}")

def recall_last_memory():
    if memory:
        return memory[-1]
    else:
        return "No value stored in memory."

def recall_all_memory():
    if memory:
        return memory
    else:
        return "No values stored in memory."

def clear_memory():
    memory.clear()
    print("Memory cleared.")

# Constants functions
def get_constant(constant_name):
    constants = {
        "pi": math.pi,
        "e": math.e,
        "planck": 6.62607015e-34,
        "gravitational": 9.80665,
        "speed_of_light": 2.998e8,
        "avogadro": 6.022e23,
        "gas_constant": 8.314
    }
    return constants.get(constant_name.lower(), "Unknown constant")

# Unit conversion functions
def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def grams_to_kilograms(grams):
    return grams / 1000

def kilograms_to_grams(kilograms):
    return kilograms * 1000

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def pascals_to_atm(pascals):
    return pascals / 101325

def atm_to_pascals(atm):
    return atm * 101325

def joules_to_calories(joules):
    return joules / 4.184

def calories_to_joules(calories):
    return calories * 4.184

# Advanced Graphing functions
def plot_function(func, x_range):
    x_values = np.linspace(x_range[0], x_range[1], 400)
    y_values = [func(x) for x in x_values]
    plt.plot(x_values, y_values)
    plt.title("Function Graph")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

def plot_sine_wave():
    def sine_wave(x):
        return math.sin(math.radians(x))
    plot_function(sine_wave, (0, 360))

def plot_cosine_wave():
    def cosine_wave(x):
        return math.cos(math.radians(x))
    plot_function(cosine_wave, (0, 360))

def plot_tangent_wave():
    def tangent
