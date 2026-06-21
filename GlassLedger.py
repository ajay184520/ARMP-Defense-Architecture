import hashlib

# --- TERMINAL COLORS ---
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def hash_data(data: str, previous_hash: str) -> str:
    """Creates a cryptographic block linking this data to the previous block."""
    block_content = data + previous_hash
    return hashlib.sha256(block_content.encode('utf-8')).hexdigest()

print(f"{CYAN}=== ARMP PILLAR 2: THE GLASS-LEDGER ==={RESET}\n")

# 1. THE NORMAL OPERATION (Building the Chain)
print(f"{YELLOW}[SYSTEM]: Building secure ledger...{RESET}")
log_1 = "08:00 AM | Truck01 leaves facility"
hash_1 = hash_data(log_1, "000000") # Genesis block

log_2 = "09:00 AM | Truck01 stops at Checkpoint Bravo"
hash_2 = hash_data(log_2, hash_1) # Mathematically linked to Log 1

log_3 = "10:00 AM | Truck01 arrives at destination"
hash_3 = hash_data(log_3, hash_2) # Mathematically linked to Log 2

# The official Ledger stored in the system
ledger = [
    {"log": log_1, "hash": hash_1, "prev_hash": "000000"},
    {"log": log_2, "hash": hash_2, "prev_hash": hash_1},
    {"log": log_3, "hash": hash_3, "prev_hash": hash_2}
]

print(f"{GREEN}[SYSTEM STATUS]: Ledger secured. 3 Blocks chained together.{RESET}\n")

# 2. THE INSIDER THREAT (Corrupt Admin Attack)
print(f"{RED}[CORRUPT ADMIN]: Logging into database with valid credentials...{RESET}")
print(f"{RED}[CORRUPT ADMIN]: Changing Log 2 to hide an unauthorized stop!{RESET}\n")
ledger[1]["log"] = "09:00 AM | Truck01 NEVER STOPPED (HACKED)"

# 3. THE SYSTEM AUDIT (The Defense)
print(f"{YELLOW}[SYSTEM]: Running daily Glass-Ledger audit...{RESET}")
tampering_detected = False

for i in range(1, len(ledger)):
    current_block = ledger[i]
    previous_block = ledger[i-1]
    
    # Recalculate what the hash SHOULD be based on the data and previous hash
    expected_hash = hash_data(current_block["log"], previous_block["hash"])
    
    if expected_hash != current_block["hash"]:
        print(f"{RED}[CRITICAL ALERT]: BROKEN CHAIN DETECTED AT BLOCK {i+1}!{RESET}")
        print(f"{RED}[CRITICAL ALERT]: The data was secretly altered by an insider.{RESET}")
        tampering_detected = True
        break

if not tampering_detected:
    print(f"{GREEN}[SYSTEM STATUS]: Audit passed. Ledger is 100% authentic.{RESET}")