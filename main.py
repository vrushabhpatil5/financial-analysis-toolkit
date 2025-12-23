import os
import sys
import subprocess

SCRIPTS = {
    "1": ("NPV & IRR Calculator", "npv_irr_calculator.py"),
    "2": ("Ratio Analysis", "ratio_analysis.py"),
    "3": ("DCF Sensitivity (WACC × Growth)", "dcf_sensitivity_wacc_growth.py"),
}

def clear_screen():
    # Works on Windows/macOS/Linux
    os.system("cls" if os.name == "nt" else "clear")

def run_script(script_name: str):
    if not os.path.exists(script_name):
        print(f"\n❌ Cannot find: {script_name}")
        print("Make sure the file exists in the repo root.\n")
        return

    print(f"\n▶ Running: {script_name}\n")
    # Use the current Python interpreter
    result = subprocess.run([sys.executable, script_name])
    if result.returncode != 0:
        print(f"\n❌ Script exited with code {result.returncode}\n")
    else:
        print("\n✅ Done.\n")

def show_menu():
    print("======================================")
    print("   Financial Analysis Toolkit (CLI)")
    print("======================================\n")

    for key, (title, _) in SCRIPTS.items():
        print(f"{key}) {title}")
    print("\n0) Exit\n")

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("\nGoodbye 👋")
            break

        if choice in SCRIPTS:
            _, script = SCRIPTS[choice]
            clear_screen()
            run_script(script)
            input("Press Enter to return to menu...")
        else:
            print("\n❌ Invalid choice. Please select 0–3.\n")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
