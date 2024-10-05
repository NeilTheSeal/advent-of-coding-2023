# Advent of Code 2023 Solutions

This repository contains my solutions to the Advent of Code 2023 challenges in Python. Each day's solution is contained in a separate file named `day_<day_number>.py` within the `advent_2023` directory.

## Virtual Environment Setup

To ensure a consistent and isolated environment for the project, it's recommended to use a virtual environment. Here's how to set it up:

1. Install virtualenv if you haven't already:

```
pip install virtualenv
```

2. Navigate to the root directory of this repository and create a virtual environment:

```
virtualenv venv
```

3. Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On macOS/Linux:
```
source venv/bin/activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. You're now ready to run the solutions and tests within the virtual environment. When you're done, you can exit the virtual environment by running:

```
deactivate
```

## Running the Solutions

To view the solutions for each day, navigate to the root directory of this repository and run the following command, which will print the solutions to the console.

```
python3 main.py
```

## Running Tests

The methods for each day's solution are tested using pytest. To run the tests for the solutions, first install the dependencies in the virtual environment, then run the following command:

```
pytest
```

This will execute all the tests in the repository, or run the tests for a specific day by running `pytest tests/test_day_<day_number>.py`.
