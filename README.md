## Investment Growth Calculator

This Python script calculates and visualizes the growth of an investment over a specified number of years with yearly contributions. It also saves a plot and a table of the investment growth.

Please note this is for simple illustration purposes only, expecting a steady projected growth. Markets fluctuate and value of your investment can go up and down. 

### Requirements

- Python 3.x
- Matplotlib

### Usage

1. Clone the repository:
 
    ```bash
    git clone https://github.com/rickzkm/investment-growth-calculator
    ```

2. Navigate to the project directory:
 
    ```bash
    cd investment-growth-calculator
    ```

3. Run the script:

    ```bash
    python investment.py
    ```

### Description

This script calculates the future value of an investment over a specified number of years with yearly contributions, considering an initial investment, annual contribution, and annual interest rate. 

### Parameters

- `initial_investment`: The initial investment amount.
- `annual_contribution`: The yearly contribution amount.
- `annual_interest_rate`: The annual interest rate (in decimal form, e.g., 0.10 for 10%).
- `years`: The number of years for which the investment growth is calculated.

### Output

- The script displays the future value of the investment after the specified number of years with yearly contributions.
- It saves a plot (`investment_growth.png`) illustrating the investment growth over time.

### Example

Consider an initial investment of 100,000 Czech Koruna, with a yearly contribution of 120,000 Czech Koruna and an annual interest rate of 12% over 20 years. Running the script will display the future value of the investment after 20 years and save a plot illustrating the investment growth.

![Investment plot](https://github.com/rickzkm/investment-growth-calculator/blob/main/pictures/graph.png?raw=true)

And additionally a table with each year 

![Investment table](https://github.com/rickzkm/investment-growth-calculator/blob/main/pictures/table.png?raw=true)

### License

- Feel free to change, customise and modify without any limitations.