

## Project Overview
This project is a statistical toolkit built from scratch using pure Python. It features a custom `StatEngine` class designed to process numerical data, handle mixed-type noise, and detect outliers. Additionally, it includes a Monte Carlo simulation to demonstrate the **Law of Large Numbers (LLN)** using server crash probabilities.

---

## Mathematical Logic

### 1. Variance Calculation
The engine supports both **Population** and **Sample** variance. To ensure accuracy, we implemented **Bessel's Correction** for sample data:
- **Population Variance ($\sigma^2$):** Divides the sum of squared deviations by $N$.
- **Sample Variance ($s^2$):** Divides by $n - 1$ to correct the bias in estimation.



### 2. Median Logic (Even vs. Odd)
To handle the median constraint:
- If the dataset length ($n$) is **Odd**, we return the middle element at index `n // 2`.
- If the dataset length is **Even**, we calculate the average of the two middle elements at indices `(n // 2) - 1` and `n // 2`.

---

## Setup & Execution
Since this project uses only the Python Standard Library, no external installations (like Pip) are required.

### How to Run:
1. Ensure you have Python 3.x installed.
2. Run the main analysis script:
   ```bash
   python main.py
