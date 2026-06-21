# 🛡️ ARMP: Autonomous Route and Mobility Protection
**A 6-Layer Zero-Trust Edge-Consensus Architecture for High-Value Logistics**

`Domain Focus: Critical Infrastructure Security` | `Status: Proof of Concept / Prototype`

---

## 📑 Executive Abstract
ARMP is a localized, autonomous defense framework engineered to neutralize kinetic hijackings, GPS spoofing, and insider corruption within high-value transport chains. By uniting hardware-level Sensor Fusion with decentralized Proof of Authority (PoA) ledgers, ARMP orchestrates defensive execution without relying on vulnerable centralized cloud networks. This architecture utilizes a **6-Layer Defense-in-Depth model**, bridging the gap between digital cybersecurity and physical asset denial.

---

## 🏗️ The 6-Layer Defense Grid

### Layer 1: Cryptographic Geofencing & Route Integrity
*   **Mechanism:** Encrypted spatial polygons and authorized routes are pre-loaded directly onto the vehicle's Edge module prior to dispatch.
*   **Defense:** Breaches of authorized coordinate boundaries trigger local alerts. Operating entirely off-grid prevents attackers from exploiting dead zones, cellular jamming, or server outages to reroute cargo undetected.

### Layer 2: Edge-AI Telemetry Analysis
*   **Mechanism:** Real-time, localized processing of velocity, acceleration, and heading.
*   **Defense:** Neutralizes GPS spoofing. If external GPS coordinates indicate movement, but internal wheel-speed sensors and transmission data report zero velocity, the Edge AI flags the discrepancy and initiates localized lockdown protocols.

### Layer 3: Sensor Fusion & The Hardware Oracle
*   **Mechanism:** The Edge Computer acts as a localized "Oracle," forcing consensus between the GPS module, OBD-II port (engine telemetry), and internal Inertial Measurement Units (IMUs).
*   **Defense:** Eliminates single-point-of-failure vulnerabilities. To bypass the Oracle, an attacker must simultaneously spoof satellite data, compromise the engine control module, and physically manipulate the gyroscope.

### Layer 4: Proof of Authority (PoA) Ledger
*   **Mechanism:** Every critical system event (ignition sequence, route deviation, cargo door unlock) is cryptographically hashed and recorded on a localized Proof of Authority blockchain.
*   **Defense:** Eradicates the "Insider Threat." Neither a compromised driver, a rogue dispatcher, nor an infiltrated cloud server can alter the vehicle's telemetry history. Rogue commands are automatically rejected via multi-signature consensus.

### Layer 5: The "Hydra" Protocol (Distributed Hardware Air-Gap)
*   **Mechanism:** Decentralizes the vehicle's physical mobility via a continuous, encrypted cryptographic heartbeat from the Edge Oracle to micro-controllers on the fuel lines and air brakes. 
*   **Defense:** If an attacker physically destroys the main computer with an EMP or plasma torch, the signal decay is calculated over time window `Δt`. If the derivative drops to zero (`dH/dt = 0`), the fuel lines mechanically sever. The vehicle becomes an immobilized, 20-ton concrete block.

### Layer 6: The "Ghost" Protocol (Phantom Compliance & Hostage Preservation)
*   **Mechanism:** A sub-cognitive psychological defense system triggered by a biometric stress duress code. 
*   **Defense:** If a driver is held at gunpoint, entering the duress code forces the system into "Phantom Compliance." The dashboard glows green, falsely reporting "System Unlocked" to pacify attackers. Simultaneously, the AI engages a slow-bleed transmission protocol, safely choking the engine out over a calculated distance to de-escalate kinetic violence and permanently weld the armored cargo doors shut.

---

## 💻 Technical Implementation
This repository contains the Python-based proof-of-concept (PoC) scripts demonstrating the localized logic for the kinetic defense layers (Layers 5 & 6). 

*   `layer5_hydra.py` - Demonstrates cryptographic signal decay and hardware air-gap triggers.
*   `layer6_ghost.py` - Demonstrates the phantom compliance loop and transmission slow-bleed execution.

*Designed for the advancement of Critical Infrastructure Security.*
