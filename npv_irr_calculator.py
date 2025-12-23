import os
import pandas as pd
import numpy_financial as npf

def main():
    os.makedirs("outputs", exist_ok=True)

    data = pd.read_csv("sample_cashflows.csv")
    cash_flows = data["CashFlow"].values

    discount_rate = 0.10

    npv = npf.npv(discount_rate, cash_flows)
    irr = npf.irr(cash_flows)

    print("Net Present Value (NPV):", round(float(npv), 2))
    print("Internal Rate of Return (IRR):", round(float(irr) * 100, 2), "%")

    output_file = "outputs/npv_irr_results.csv"
    pd.DataFrame([{
        "discount_rate": discount_rate,
        "npv": round(float(npv), 2),
        "irr_percent": round(float(irr) * 100, 2)
    }]).to_csv(output_file, index=False)

    print("\nSaved results to:", output_file)

if __name__ == "__main__":
    main()
