import os
import pandas as pd
import numpy_financial as npf

def main():
    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    # Load cash flow data
    data = pd.read_csv("sample_cashflows.csv")
    cash_flows = data["CashFlow"].values

    # Discount rate (edit as needed)
    discount_rate = 0.10

    # Compute NPV and IRR using numpy-financial
    npv = npf.npv(discount_rate, cash_flows)
    irr = npf.irr(cash_flows)

    # Print results
    print("Net Present Value (NPV):", round(float(npv), 2))
    print("Internal Rate of Return (IRR):", round(float(irr) * 100, 2), "%")

    # Save results to CSV (Excel-friendly)
    out = pd.DataFrame([{
        "discount_rate": discount_rate,
        "npv": round(float(npv), 2),
        "irr_percent": round(float(irr) * 100, 2)
    }])

    output_file = "outputs/npv_irr_results.csv"
    out.to_csv(output_file, index=False)
    print("\nSaved results to:", output_file)

if __name__ == "__main__":
    main()
