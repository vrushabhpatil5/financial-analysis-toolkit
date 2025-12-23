# Financial Analysis Toolkit

A Python-based toolkit applying core financial analysis and valuation concepts
using clean, data-driven models and Excel-friendly outputs.

This project bridges traditional finance theory with real-world
decision-making, focusing on clarity, structure, and practical usability.

---

## Modules
- **NPV & IRR Calculator** (Python + CSV inputs, CSV outputs)
- **Ratio Analysis** (profitability, liquidity, leverage)
- **DCF Sensitivity Analysis** (WACC × Terminal Growth)
- **NPV vs WACC Sensitivity Chart** (visual valuation insight)

---

## Project Structure
((( 
financial-analysis-toolkit/
│
├── npv_irr_calculator.py
├── ratio_analysis.py
├── dcf_sensitivity_wacc_growth.py
├── main.py
│
├── sample_cashflows.csv
├── sample_financials.csv
├── forecast_cashflows.csv
│
├── outputs/
│ ├── npv_irr_results.csv
│ ├── ratio_analysis_results.csv
│ ├── dcf_sensitivity_wacc_growth_output.csv
│ └── npv_vs_wacc.png
│
├── requirements.txt
└── README.md
)))
---

## How to Run

### 1) Install dependencies
```bash
pip install -r requirements.txt
````

### 2) Run the toolkit menu
```bash
python main.py
````

### 3) Or run individual modules
```bash
python npv_irr_calculator.py
python ratio_analysis.py
python dcf_sensitivity_wacc_growth.py
````
