import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

def main():
    try:
        with open('data/sample_salaries.json', 'r') as f:
            salary_data = json.load(f)['salaries']
        
        engine = StatEngine(salary_data)
        print("--- STARTUP SALARY ANALYSIS ---")
        print(f"Average Salary: ${engine.get_mean():,.2f}")
        print(f"Median Salary:  ${engine.get_median():,.2f}")
        print(f"Outliers Found: {engine.get_outliers(threshold=2)}")
    except FileNotFoundError:
        print("Error: data/sample_salaries.json not found.")

    print("\n--- SERVER CRASH SIMULATION (Target: 4.5%) ---")
    for days in [100, 1000, 10000, 100000]:
        results = simulate_crashes(days)
        sim_engine = StatEngine(results)
        prob = sim_engine.get_mean()
        print(f"Days: {days:7} | Simulated Probability: {prob:.5f}")

if __name__ == "__main__":
    main()
