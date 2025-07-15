import math

class EngineeringComputationEngine:
    def __init__(self):
        self.scientific_constants = {
            "speed_of_light": 299792458,       
            "acceleration_of_gravity": 9.8066, 
            "planck_constant": 6.62607e-34,    
            "avogadro_number": 6.02214e23,     
            "universal_gas_constant": 8.3144   
        }
        
        self.functional_operators = {
            "sine": lambda theta: math.sin(math.radians(theta)),
            "cosine": lambda theta: math.cos(math.radians(theta)),
            "logarithm": lambda x: math.log10(x) if x > 0 else "Execution Error: Domain Violation",
            "square_root": lambda x: math.sqrt(x) if x >= 0 else "Execution Error: Imaginary Root"
        }

    def resolve_constant(self, key_identifier):
        return self.scientific_constants.get(key_identifier, "Error: Unknown Key")

    def execute_computation(self, operational_mode, numerical_input):
        calculation_logic = self.functional_operators.get(operational_mode)
        if not calculation_logic:
            return "Error: Unsupported Operational Mode"
        return calculation_logic(numerical_input)

    def calculate_relativistic_energy(self, mass_kg):
        c = self.resolve_constant("speed_of_light")
        return mass_kg * (c ** 2)

# =====================================================================
# RUNTIME INTERACTIVE DRIVER
# =====================================================================
if __name__ == "__main__":
    engine = EngineeringComputationEngine()
    print("=" * 65)
    print("            HIGH-PRECISION MATH & ENGINEERING ANALYSIS          ")
    print("=" * 65)
    
    print("\nAvailable constants: speed_of_light, acceleration_of_gravity, avogadro_number")
    const_name = input("Enter a constant key to query database: ")
    const_val = engine.resolve_constant(const_name)
    
    print("\n[MASS-ENERGY EQUATION RESOLVER (E=mc²)]")
    input_mass = float(input("Enter object mass in kilograms: "))
    calculated_energy = engine.calculate_relativistic_energy(input_mass)
    
    print("\n[FUNCTION ALGORITHM EXECUTION]")
    op_mode = input("Select math function (sine, cosine, logarithm, square_root): ")
    num_in = float(input("Enter input value: "))
    op_result = engine.execute_computation(op_mode, num_in)

    print("\n" + "=" * 65)
    print(" MATHEMATICAL ANALYSIS ENGINE LOG RUNTIME")
    print("=" * 65)
    print(f" [DATABASE QUERY] {const_name} value: {const_val}")
    print(f" [EQUATION SOLVER] Mass Parameter      : {input_mass} kg")
    print(f" [EQUATION RESULT] Calculated Energy (E): {calculated_energy} Joules")
    print(f" [ALGORITHM RUN]  {op_mode}({num_in}) evaluated: {op_result}")
    print("=" * 65)
