import sys
import os

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.IdealGas import IdealGas
from src.VanDerWaalsGas import VanDerWaalsGas

def main():
    print("=== Gas Law Comparison: Ideal vs Real ===\n")

    # Parameters
    moles = 100.0
    temp = 300.0 # Kelvin (~27C)
    
    # 1. Create Models
    ideal = IdealGas(moles)
    
    # Nitrogen Parameters (approx)
    # a = 0.1408 Pa m^6 mol^-2
    # b = 3.913e-5 m^3 mol^-1
    nitrogen_real = VanDerWaalsGas(moles, a=0.1408, b=3.913e-5, name="Nitrogen")

    print(f"System: {moles} moles at {temp} K")
    print("-" * 60)
    print(f"{'Volume (L)':<15} | {'Ideal P (kPa)':<15} | {'Real P (kPa)':<15} | {'% Diff':<10}")
    print("-" * 60)

    # 2. Simulate Compression (Reducing Volume)
    # Start at 100L down to 1L
    volumes_liters = [100, 50, 20, 10, 5, 2, 1]

    for v_liter in volumes_liters:
        v_m3 = v_liter / 1000.0 # Convert L to m^3
        
        p_ideal = ideal.pressure(v_m3, temp)
        try:
            p_real = nitrogen_real.pressure(v_m3, temp)
            
            # Convert Pa to kPa
            p_i_kpa = p_ideal / 1000.0
            p_r_kpa = p_real / 1000.0
            
            diff = abs(p_i_kpa - p_r_kpa)
            pct_err = (diff / p_r_kpa) * 100.0
            
            print(f"{v_liter:<15.1f} | {p_i_kpa:<15.2f} | {p_r_kpa:<15.2f} | {pct_err:<10.1f}")
        except ValueError as e:
            print(f"{v_liter:<15.1f} | {p_ideal/1000:<15.2f} | {'CRITICAL':<15} | ---")

    print("-" * 60)
    print("\nObservation: As volume decreases (high pressure), Real Gas deviates significantly from Ideal Gas.")
    print("This is because molecules occupy space (b) and attract each other (a).")

if __name__ == "__main__":
    main()
