# Task: Build Function Monitoring Decorators

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Timing Decorator
Create a decorator called `timing_decorator` that:
- Measures how long

 a function takes to execute
- Prints the execution time in seconds
- Uses `time.time()` to measure time
- Uses `@wraps` to preserve function metadata
- Works with any function (use *args and **kwargs)

Test it with a function that sleeps for 1 second.

## Goal 2: Create a Logging Decorator
Create a decorator called `log_decorator` that:
- Prints when a function is called with its name
- Prints the arguments passed to the function
- Prints the return value
- Uses `@wraps` to preserve metadata
- Formats output like: `[LOG] Calling function_name(arg1=value1, arg2=value2)`

Test it with a function that performs calculations.

## Goal 3: Create a Validation Decorator
Create a parametrized decorator called `validate_types` that:
- Accepts type requirements as parameters (e.g., `@validate_types(int, int)`)
- Checks if arguments match the expected types
- Raises `TypeError` with a helpful message if types don't match
- Works with the function if validation passes
- Uses `@wraps` to preserve metadata

Test it with functions requiring specific types.

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Testing timing decorator:
slow_function took 1.0023 seconds
Result: Completed

Testing logging decorator:
[LOG] Calling calculate
[LOG] Arguments: (10, 5), {'operation': 'multiply'}
[LOG] Result: 50
Result: 50

Testing validation decorator:
add(5, 10) = 15
Attempting add(5, 'ten')...
TypeError: Argument 'ten' is not of type <class 'int'>
```
