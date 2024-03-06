import matplotlib.pyplot as plt

def future_value_with_contributions(initial_investment, annual_contribution, annual_interest_rate, years):
    future_values = [initial_investment]
    print("Year\tFuture Value (CZK)")
    print("---------------------------------")
    for year in range(1, years + 1):
        future_value = future_values[-1] * (1 + annual_interest_rate) + annual_contribution
        future_values.append(future_value)
        print(f"{year}\t{future_value:,.2f}")
    return future_values

def plot_investment_growth(years, future_values, initial_investment):
    plt.plot(range(years + 1), future_values, marker='o', linestyle='-')
    plt.scatter([0, years], [initial_investment, future_values[-1]], color='red', zorder=5)
    plt.xlabel('Years')
    plt.ylabel('Future Value (CZK)')
    plt.title('Investment Growth Over Time')
    plt.grid(True)
    plt.annotate('Initial Investment', xy=(0, initial_investment), xytext=(-50, 20),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'))
    plt.annotate('Final Value', xy=(years, future_values[-1]), xytext=(20, 10),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'))

def main():
    # Given values
    initial_investment = 100000  # Initial investment in CZK
    annual_contribution = 120000  # Annual contribution in CZK
    annual_interest_rate = 0.12  # Annual interest rate (12%)
    years = 20  # Number of years

    # Calculate future values
    future_values = future_value_with_contributions(initial_investment, annual_contribution, annual_interest_rate, years)

    # Plot and save the graph
    plot_investment_growth(years, future_values, initial_investment)
    plt.savefig('investment_growth.png')
    plt.show()

    # Format the future value with spaces as thousands separators
    formatted_future_value = "{:,.2f}".format(future_values[-1]).replace(",", " ")
    print(f"Future value of the investment after {years} years with yearly contributions: {formatted_future_value} CZK")

if __name__ == "__main__":
    main()