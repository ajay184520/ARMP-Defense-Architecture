# --- TERMINAL COLORS ---
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

print(f"{CYAN}=== ARMP PILLAR 4: THE WHISPER SWARM (CONSENSUS) ==={RESET}\n")

# --- 1. SETUP THE NETWORK (50 Servers) ---
TOTAL_SERVERS = 50

# The real cryptographic hash (The truth: The truck was stolen)
REAL_HASH = "8f4e2...[STOLEN]"

# The fake cryptographic hash (The lie: The Admin recalculated the math to say it's safe)
FAKE_HASH = "1a9c7...[CLEAN]"

# --- 2. POPULATE THE SWARM ---
print(f"{YELLOW}[SYSTEM]: Booting up the Distributed Ledger...{RESET}")

# 49 Honest Partner Servers hold the REAL history
network_nodes = [REAL_HASH] * 49

# 1 Rogue Admin Server tries to inject the FAKE history
network_nodes.append(FAKE_HASH)

# --- 3. THE CONSENSUS AUDIT (The Trap) ---
def consensus_audit(nodes):
    print(f"{YELLOW}[SYSTEM]: Initiating Network Audit across {len(nodes)} Servers...{RESET}\n")
    
    # The network counts the votes
    vote_counts = {}
    for node_hash in nodes:
        if node_hash in vote_counts:
            vote_counts[node_hash] += 1
        else:
            vote_counts[node_hash] = 1
            
    # Display the results
    print("--- AUDIT RESULTS ---")
    print(f"Votes for '{REAL_HASH}' : {vote_counts.get(REAL_HASH, 0)}")
    print(f"Votes for '{FAKE_HASH}'  : {vote_counts.get(FAKE_HASH, 0)}\n")
    
    # Find the majority
    max_votes = max(vote_counts.values())
    
    # The Trap triggers if there is a minority lie
    fake_votes = vote_counts.get(FAKE_HASH, 0)
    if fake_votes > 0 and fake_votes < max_votes:
        print(f"{RED}[CRITICAL ALERT]: ROGUE NODE DETECTED!{RESET}")
        print(f"{RED}[ACTION]: Rejecting mathematically valid but fraudulent history '{FAKE_HASH}'.{RESET}")
        print(f"{RED}[ACTION]: Permanently locking Rogue Admin out of the network.{RESET}\n")
        
    print(f"{GREEN}[SUCCESS]: Consensus reached. Official ledger mathematically restored to majority truth.{RESET}")

# Run the simulation
consensus_audit(network_nodes)