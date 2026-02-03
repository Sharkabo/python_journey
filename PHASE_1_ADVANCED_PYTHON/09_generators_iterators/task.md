# Task: Build Data Processing Pipeline with Generators

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Data Reading Generator
Create a generator function `read_sensor_data(count)` that:
- Simulates reading sensor data (you can use random numbers or incrementing values)
- Yields dictionaries with keys: `timestamp`, `temperature`, `humidity`
- Generates `count` number of readings
- Example: `{"timestamp": 1234567890, "temperature": 22.5, "humidity": 65}`

## Goal 2: Create Filtering Generator
Create a generator function `filter_high_temperature(data_stream, threshold)` that:
- Takes a generator of sensor data as input
- Yields only readings where temperature exceeds the threshold
- Preserves all data in the original dictionary

## Goal 3: Create Data Transformation Generator
Create a generator function `convert_to_fahrenheit(data_stream)` that:
- Takes a generator of sensor data
- Converts temperature from Celsius to Fahrenheit
- Formula: `F = C * 9/5 + 32`
- Yields modified dictionaries with temperature in Fahrenheit

## Goal 4: Build Complete Pipeline
Create a function `analyze_data()` that:
- Chains the generators together: read → filter → convert
- Collects results into a list
- Returns statistics: count, average temperature, max temperature

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Reading sensor data...
Filtering high temperatures (>25C)...
Converting to Fahrenheit...

Results:
Total high-temp readings: 15
Average temperature: 80.5 F
Max temperature: 95.0 F

Sample readings:
{"timestamp": 1001, "temperature": 77.0, "humidity": 60}
{"timestamp": 1002, "temperature": 82.4, "humidity": 55}
{"timestamp": 1003, "temperature": 86.0, "humidity": 70}
```
