import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("sample_cashflows.csv")
    cash_flows = data["CashFlow"].values

    discount_rate = 0.10

    npv = np.npv(discount_rate, cash_flows)
    irr = np.irr(cash_flows)

    print("Net Present Value (NPV):", round(npv, 2))
    print("Internal Rate of Return (IRR):", round(irr * 100, 2), "%")

if __name__ == "__main__":
    main()
