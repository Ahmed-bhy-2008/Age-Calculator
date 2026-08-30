# Age Calculator Application 📅

A simple, lightweight command-line interface (CLI) application built with Python. It calculates a user's exact age in years and remaining days by taking their birthdate details and comparing them against the current live calendar date.

## 🚀 Features

- **Interactive CLI:** Prompt-driven interface for easy user inputs.
- **Real-Time Accuracy:** Leverages Python's built-in `datetime` library to always calculate against today's exact date.
- **Precise Breakdown:** Outputs the final calculation cleanly in total years and days.

## 📋 Prerequisites

To run this project, you only need Python installed on your machine. No external third-party libraries are required.

- Python 3.x or higher

## 🛠️ How to Run

1. **Clone the repository** (or download the source script):
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the directory**:
   ```bash
   cd age-calculator
   ```
3. **Execute the script**:
   ```bash
   python age_calculator.py
   ```

## 💻 Sample Output

```text
--- welcome to the age calculator application ---
Enter birth year (YYYY): 2000
Enter birth month (1-12): 05
Enter birth day (1-31): 15
Your exact age is: 26 years old and 107 day.
```

## 🔧 Future Improvements

Potential features to implement next:
- [ ] Add input validation to prevent crashes from invalid dates (e.g., Month 13).
- [ ] Break down the age calculation further to include exact months.
- [ ] Account for exact leap year shifts dynamically.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
