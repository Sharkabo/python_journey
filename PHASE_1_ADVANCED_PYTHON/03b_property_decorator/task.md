# Task: Build a Temperature Conversion Class

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Temperature Class with @property
Create a `Temperature` class that:
- Stores temperature in Celsius using a private attribute `_celsius`
- Uses `@property` decorator to create a getter for `celsius`
- Uses `@celsius.setter` to validate temperature (must be above absolute zero: -273.15°C)

## Goal 2: Add Fahrenheit Conversion Property
Add a `fahrenheit` property that:
- Calculates and returns temperature in Fahrenheit (F = C * 9/5 + 32)
- Has a setter that converts Fahrenheit input to Celsius

## Goal 3: Test the Temperature Class
Demonstrate:
- Setting temperature in Celsius
- Reading temperature in both Celsius and Fahrenheit
- Validation prevents invalid temperatures

---

**Expected Output:**
```text
Temperature: 25.0°C = 77.0°F
After setting to 30°C: 30.0°C = 86.0°F
After setting to 32°F: 0.0°C = 32.0°F
Error: Temperature cannot be below absolute zero
```
