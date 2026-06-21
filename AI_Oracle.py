# --- TERMINAL COLORS ---
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

print(f"{CYAN}=== ARMP PILLAR 3: THE AI ORACLE ==={RESET}\n")

# --- CONFIGURE THE THRESHOLDS (The Rules) ---
# The truck is only authorized to move between 6 AM and 8 PM (20:00)
ALLOWED_START_HOUR = 6
ALLOWED_END_HOUR = 20

# The approved highway route (The Geofence Box)
MIN_LAT = 17.0
MAX_LAT = 18.5
MIN_LON = 78.0
MAX_LON = 79.5

def ai_oracle_check(telemetry_data):
    print(f"{YELLOW}[SYSTEM]: Ingesting telemetry for {telemetry_data['id']}...{RESET}")
    
    # 1. Cryptography Check
    if not telemetry_data['crypto_valid']:
        return f"{RED}[REJECTED]: Bad Cryptography{RESET}"
    
    # 2. Behavioral Trap 1: The Time Window
    current_hour = telemetry_data['hour']
    if current_hour < ALLOWED_START_HOUR or current_hour > ALLOWED_END_HOUR:
        print(f"{RED}[BEHAVIORAL ANOMALY]: Vehicle active outside authorized hours! ({current_hour}:00){RESET}")
        return f"{RED}[THIEF DETECTED]: INITIATING ENGINE SHUTDOWN...{RESET}"

    # 3. Behavioral Trap 2: The Geofence
    lat = telemetry_data['gps_lat']
    lon = telemetry_data['gps_lon']
    if not (MIN_LAT <= lat <= MAX_LAT and MIN_LON <= lon <= MAX_LON):
        print(f"{RED}[BEHAVIORAL ANOMALY]: Vehicle has breached the approved Geofence!{RESET}")
        return f"{RED}[THIEF DETECTED]: INITIATING ENGINE SHUTDOWN...{RESET}"

    # If it passes all behavioral checks:
    return f"{GREEN}[STATUS]: Driver Behavior Normal. Route Authorized.{RESET}"

# ==========================================
# --- THE SIMULATION ---
# ==========================================

# Scenario 1: The Real Driver 
print("--- SCENARIO 1: NORMAL OPERATIONS ---")
driver_telemetry = {
    "id": "Truck01",
    "crypto_valid": True,  # The keys are real
    "hour": 14,            # 2:00 PM (Authorized time)
    "gps_lat": 17.5,       # Inside the Geofence
    "gps_lon": 78.5
}
print(ai_oracle_check(driver_telemetry), "\n")


# Scenario 2: The Physical Thief 
print("--- SCENARIO 2: PHYSICAL THEFT ---")
thief_telemetry = {
    "id": "Truck01",
    "crypto_valid": True,  # The math is perfect because they stole the real keys!
    "hour": 3,             # 3:00 AM (Unauthorized time)
    "gps_lat": 19.2,       # Driving off-route to a black market
    "gps_lon": 80.1
}
print(ai_oracle_check(thief_telemetry), "\n")