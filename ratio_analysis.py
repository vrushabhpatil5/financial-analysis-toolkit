import pandas as pd

# Load sample financials
df = pd.read_csv("sample_financials.csv")
values = dict(zip(df["Metric"], df["Value"]))

revenue = values["Revenue"]
cogs = values["COGS"]
opex = values["Operating_Expenses"]
net_income = values["Net_Income"]
current_assets = values["Current_Assets"]
current_liabilities = values["Current_Liabilities"]
total_assets = values["Total_Assets"]
total_liabilities = values["Total_Liabilities"]
equity = values["Shareholders_Equity"]

# Profitability ratios
gross_profit = revenue - cogs
gross_margin = gross_profit / revenue
net_margin = net_income / revenue

# Liquidity ratios
current_ratio = current_assets / current_liabilities

# Leverage ratios
debt_to_equity = total_liabilities / equity
debt_ratio = total_liabilities / total_assets

print("=== Profitability ===")
print(f"Gross Margin: {gross_margin:.2%}")
print(f"Net Profit Margin: {net_margin:.2%}")

print("\n=== Liquidity ===")
print(f"Current Ratio: {current_ratio:.2f}")

print("\n=== Leverage ===")
print(f"Debt-to-Equity: {debt_to_equity:.2f}")
print(f"Debt Ratio: {debt_ratio:.2f}")
