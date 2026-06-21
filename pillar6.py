import time

def layer_6_ghost_protocol(duress_code_entered, current_speed):
    print("\n========================================================")
    print("LAYER 6: GHOST PROTOCOL (Phantom Compliance Initiated)")
    print("========================================================")
    
    if duress_code_entered:
        print("[DURESS DETECTED] Driver entered silent panic code!")
        print("[ILLUSION ACTIVE] Dashboard glowing GREEN. Displaying: 'SYSTEM UNLOCKED. ROUTE APPROVED.'")
        print("[ACTION] Protecting driver... Engaging transmission slow-bleed protocol.")
        print("--------------------------------------------------------")
        
        # The while loop slowly chokes the engine to safely stop the truck
        while current_speed > 0:
            print(f"   -> Phantom Execution: Engine artificially choking... Speed dropping to {current_speed} km/h")
            current_speed -= 10
            time.sleep(1) # Simulates time passing on the highway
            
        print("--------------------------------------------------------")
        print("[SYSTEM HALT] Speed is 0 km/h. Truck safely immobilized on public road.")
        print("[LOCKDOWN] Cargo doors permanently locked. Local authorities notified.")
        return "IMMOBILIZED"
    else:
        print("[STATUS] Driver biometrics and inputs normal. Standard route tracking active.")
        return "ACTIVE"

# --- Test the Layer 6 Code ---
if __name__ == "__main__":
    # Test 1: Normal Operation (No duress code entered at checkpoint)
    print("\n--- SCENARIO 1: NORMAL CHECKPOINT ---")
    layer_6_ghost_protocol(duress_code_entered=False, current_speed=60)
    
    time.sleep(2) # Pausing to separate the tests
    
    # Test 2: Attack Scenario (Hijacker forces driver to unlock the truck at gunpoint)
    print("\n--- SCENARIO 2: HOSTAGE SITUATION (GUNPOINT) ---")
    layer_6_ghost_protocol(duress_code_entered=True, current_speed=40)