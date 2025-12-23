import pandas as pd
import numpy as np

# Load forecast free cash flows
fcf_df = pd.read_csv("forecast_cashflows.csv")
fcfs = fcf_df["FCF"].values
n = len(fcfs)

# Sensitivity ranges (edit as needed)
wacc_values = np.arange(0.075, 0.105, 0.005)   # 7.5% to 10.0%
g_values = np.arange(0.00, 0.015, 0.0025)     # 0.0% to 1.25%

def dcf_value(wacc: float, g: float) -> float:
    """
    Simple DCF:
    - PV of forecast FCFs
    - Terminal value using perpetuity growth: TV = FCF_n * (1+g) / (wacc - g)
    - PV of TV discounted back n years
    """
    # PV of forecast cash flows
    pv_fcfs = sum(fcfs[t] / ((1 + wacc) ** (t + 1)) for t in range(n))

    # Terminal value (perpetuity growth)
    if wacc <= g:
        return np.nan  # invalid (would blow up)

    terminal_value = fcfs[-1] * (1 + g) / (wacc - g)
    pv_terminal = terminal_value / ((1 + wacc) ** n)

    return pv_fcfs + pv_terminal

# Build sensitivity table
table = pd.DataFrame(index=[f"{w*100:.2f}%" for w in wacc_values],
                     columns=[f"{g*100:.2f}%" for g in g_values])

for wacc in wacc_values:
    for g in g_values:
        val = dcf_value(wacc, g)
        table.loc[f"{wacc*100:.2f}%", f"{g*100:.2f}%"] = round(val, 2) if pd.notna(val) else ""

# Save output for Excel
output_file = "dcf_sensitivity_wacc_growth_output.csv"
table.to_csv(output_file)

print("Saved:", output_file)
print("\nDCF Sensitivity (WACC x Growth) preview:\n")
print(table)
