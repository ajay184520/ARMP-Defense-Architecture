import hmac
import hashlib
import time

# 1. THE SECRET KEY & TERMINAL COLORS
SECRET_KEY = b"armp_secure_key_2026"
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

def create_seal(message: str) -> str:
    """Creates a cryptographic wax seal (HMAC-SHA256) for the data."""
    seal = hmac.new(SECRET_KEY, message.encode('utf-8'), hashlib.sha256)
    return seal.hexdigest()

# --- TERMINAL SIMULATION START ---
print(f"{CYAN}=== ARMP PILLAR 1: HMAC WAX SEAL (WITH ANTI-REPLAY) ==={RESET}\n")

# 2. THE NORMAL OPERATION (Now with live Timestamp)
current_timestamp = int(time.time())
original_data = f"Truck01 | Speed: 60km/h | Time: {current_timestamp}"
valid_seal = create_seal(original_data)

print(f"[TRUCK]: Sending Data -> {original_data}")
print(f"[TRUCK]: Attached Cryptographic Seal -> {valid_seal[:15]}...\n")

# 3. THE HACKER ATTACK
print(f"{RED}[HACKER]: Intercepting Wi-Fi signal...{RESET}")
print(f"{RED}[HACKER]: Changing truck speed to 0km/h!{RESET}\n")
hacked_data = f"Truck01 | Speed: 0km/h | Time: {current_timestamp}"

# 4. THE SERVER VERIFICATION
print("[SERVER]: Receiving data... checking the seal.")
expected_seal_for_hacked_data = create_seal(hacked_data)

if expected_seal_for_hacked_data == valid_seal:
    print(f"{GREEN}[SERVER STATUS]: Data is Authentic. Accepted.{RESET}")
else:
    print(f"{RED}[SERVER STATUS]: CRITICAL ALERT! WAX SEAL BROKEN!{RESET}")
    print(f"{RED}[SERVER STATUS]: Tampering detected. Rejecting payload.{RESET}")