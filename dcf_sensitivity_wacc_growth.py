import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    # Load forecast free cash flows
    fcf_df = pd.read_csv("forecast_cashflows.csv")
    fcfs = fcf_df["FCF"].values
    n = len(fcfs)

    # Sensitivity ranges (edit as needed)
    wacc_values = np.arange(0.075, 0.105, 0.005)   # 7.5% to 10.0% (step 0.5%)
    g_values = np.arange(0.00, 0.015, 0.0025)      # 0.0% to 1.25% (step 0.25%)

    def dcf_value(wacc: float, g: float) -> float:
        """
        Simple DCF:
        - PV of forecast FCFs
        - Terminal value using perpetuity growth: TV = FCF_n * (1+g) / (wacc - g)
        - PV of TV discounted back n years
        """
        # PV of forecast cash flows
        pv_fcfs = 0.0
        for t in range(n):
            pv_fcfs += fcfs[t] / ((1 + wacc) ** (t + 1))

        # Terminal value (perpetuity growth)
        if wacc <= g:
            return np.nan  # invalid

        terminal_value = fcfs[-1] * (1 + g) / (wacc - g)
        pv_terminal = terminal_value / ((1 + wacc) ** n)

        return pv_fcfs + pv_terminal

    # Build sensitivity table
    table = pd.DataFrame(
        index=[f"{w * 100:.2f}%" for w in wacc_values],
        columns=[f"{g * 100:.2f}%" for g in g_values]
    )

    for wacc in wacc_values:
        for g in g_values:
            val = dcf_value(wacc, g)
            table.loc[f"{wacc * 100:.2f}%", f"{g * 100:.2f}%"] = (
                round(float(val), 2) if pd.notna(val) else ""
            )

    # Save sensitivity output (CSV for Excel)
    output_csv = "outputs/dcf_sensitivity_wacc_growth_output.csv"
    table.to_csv(output_csv)
    print("Saved sensitivity table:", output_csv)

    # ---- NPV vs WACC chart (holding terminal growth constant) ----
    fixed_g = 0.005  # 0.5% terminal growth
    npv_values = []

    for wacc in wacc_values:
        val = dcf_value(wacc, fixed_g)
        npv_values.append(val)

    plt.figure()
    plt.plot([w * 100 for w in wacc_values], npv_values, marker="o")
    plt.xlabel("WACC (%)")
    plt.ylabel("Net Present Value")
    plt.title("NPV Sensitivity to WACC (g = 0.5%)")
    plt.grid(True)

    output_png = "outputs/npv_vs_wacc.png"
    plt.savefig(output_png, bbox_inches="tight")
    plt.close()

    print("Saved chart:", output_png)

    # Print quick preview
    print("\nDCF Sensitivity (WACC x Growth) preview:\n")
    print(table)


if __name__ == "__main__":
    main()
