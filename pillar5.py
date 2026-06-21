import time

def layer_5_hydra_protocol(last_heartbeat_timestamp):
    print("\n========================================================")
    print("LAYER 5: HYDRA PROTOCOL (Hardware Air-Gap Initiated)")
    print("========================================================")
    print("[SYSTEM] Monitoring cryptographic heartbeat from Edge Oracle...")
    
    # Simulating the current time in the system
    current_time = time.time()
    
    # Calculate the decay window (time since the last secure signal)
    signal_decay_window = current_time - last_heartbeat_timestamp
    
    print(f"[METRIC] Time since last valid key: {signal_decay_window:.2f} seconds")
    
    # If the signal drops for more than 0.5 seconds (Simulating the physical destruction of the computer)
    if signal_decay_window > 0.5:
        print("[CRITICAL ALERT] Heartbeat derivative has dropped to zero (dH/dt = 0).")
        print("[CRITICAL ALERT] Main computer compromised or destroyed!")
        print("[ACTION] Severing digital connections. Triggering mechanical fuel line lockdown...")
        print("[STATUS] Truck is now completely immobilized. Layer 5 Defense Successful.")
        return "LOCKED"
    else:
        print("[STATUS] Cryptographic heartbeat is stable. Fuel lines remain open.")
        return "SECURE"

# --- Test the Layer 5 Code ---
if __name__ == "__main__":
    # Test 1: Normal Operation (Heartbeat received 0.1 seconds ago)
    print("\n--- SCENARIO 1: NORMAL DRIVING ---")
    simulated_safe_time = time.time() - 0.1
    layer_5_hydra_protocol(simulated_safe_time)
    
    time.sleep(2) # Pausing for 2 seconds to simulate time passing
    
    # Test 2: Attack Scenario (Cartel rips out the computer, heartbeat stops for 2 seconds)
    print("\n--- SCENARIO 2: CARTEL ATTACKS MAIN COMPUTER ---")
    simulated_attack_time = time.time() - 2.0
    layer_5_hydra_protocol(simulated_attack_time)