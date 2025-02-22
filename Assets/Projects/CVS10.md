# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#10 - AI-Powered Secure OTA Updates for Electric Vehicles (EVs)
![](https://img.shields.io/badge/Member-Mani_Shankar_Molleti-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement
Modern vehicles rely heavily on Electronic Control Units (ECUs) to control essential functions such as engine performance, braking, infotainment, and safety systems. These ECUs require frequent firmware updates to fix software bugs, improve performance, and enhance cybersecurity. Traditionally, these updates are performed manually at service centers using wired connections, which is costly, time-consuming, and inefficient. As vehicle technology advances, manufacturers are shifting toward Over-the-Air (OTA) firmware updates, allowing vehicles to receive software updates remotely. However, implementing OTA updates at scale introduces several security and technical challenges that must be addressed.

One of the biggest concerns with OTA updates is cybersecurity risks. Hackers may exploit vulnerabilities in the update process to inject malicious firmware, potentially compromising vehicle safety. Additionally, unreliable network conditions can result in incomplete or corrupted updates, leading to ECU failures. Another major issue is legacy ECU compatibility, as older vehicle models may not support modern encryption protocols or high-speed data transmission, making secure OTA updates difficult to implement. These challenges necessitate a secure, efficient, and intelligent OTA update system that ensures vehicles receive updates safely and seamlessly.

To address these challenges, this project proposes an AI-driven Secure OTA Firmware Update System, integrating Artificial Intelligence (AI) and Ethernet/IP-based Unified Diagnostic Services (UDS). AI enhances predictive maintenance by analyzing vehicle health data to determine the best time for updates while also identifying potential security threats in real time. End-to-end encryption and intrusion detection systems (IDS) protect the firmware from unauthorized modifications. By leveraging AI-powered diagnostics, secure encryption, and high-speed Ethernet/IP communication, this solution ensures safer, more efficient, and reliable OTA firmware updates, reducing downtime, improving cybersecurity, and enhancing overall vehicle performance.

---

### Literature Survey
1.	FOTAMOTIVE: Highlights the inefficiencies of traditional update methods and proposes a FOTA solution to address OEM, dealer, and consumer challenges.
2.	Self-Verification Framework: Discusses virtualization techniques and hash-based verification protocols to ensure the integrity of firmware installations.
3.	Secure FOTA Protocols: Focuses on security challenges in intelligent vehicles, emphasizing the need for data integrity, authentication, and resilience to packet loss in wireless communications.
4.	AI-Enabled UDS for Secure OTA Updates (IARJSET, 2023):
    •	Proposes an Ethernet/IP-based Unified Diagnostic Service (UDS) for secure OTA updates.
    •	Uses AI for anomaly detection, ensuring real-time threat mitigation.
    •	Implements secure boot, authentication, and multi-domain security to prevent cyber threats.
    •	Limitation: Requires high computational power and Ethernet/IP infrastructure, limiting applicability in all vehicles.
5.LoRaWAN & Blockchain for Secure OTA Updates (IEEE QRS-C 2024)
    •	Introduces LoRaWAN for long-range, low-power OTA updates in connected vehicles.
    •	Uses blockchain for integrity verification and IPFS for decentralized storage to prevent tampering.
    •	Simulation results show efficient energy usage but limited bandwidth affects large updates.
    •	Limitation: Blockchain transaction costs and latency can impact real-time updates.
---

### Proposed Work
This project aims to develop an AI-Powered Secure OTA Update System for Electric Vehicles (EVs) to enhance the security, efficiency, and reliability of firmware updates. The proposed system integrates Artificial Intelligence (AI), blockchain technology, and Ethernet/IP-based Unified Diagnostic Services (UDS) to address security vulnerabilities, network reliability issues, and compatibility challenges in modern EVs.
Key Features of the Proposed System:
1.	AI-Driven Predictive Update Scheduling:
  •	AI analyzes vehicle health data (battery status, ECU performance, network stability) to schedule updates at optimal times.
  •	Machine learning models predict potential firmware failures and recommend preemptive updates.
2.	Blockchain-Based Firmware Integrity Verification:
  • Ensures tamper-proof firmware updates using a blockchain ledger to store hash values of valid firmware.
  • Smart contracts authenticate updates before installation.
3.	Secure Ethernet/IP-Based OTA Communication:
  • High-speed Ethernet/IP connectivity for real-time firmware updates, ensuring low latency and secure data transfer.
  • Implements end-to-end encryption (AES-256, TLS 1.3) to protect OTA data packets.
4.	Intrusion Detection & Security Protocols:
   • Uses AI-based anomaly detection to identify potential cyberattacks during the update process.
   • Implements multi-factor authentication (MFA) and secure boot mechanisms to prevent unauthorized firmware modifications.
5.	Adaptive Update Mechanism for Legacy ECUs:
   • Supports differential updates (only sending modified parts of firmware to reduce bandwidth usage).
	 • Implements fallback recovery system to restore firmware in case of update failure.

---

### Implementation Details
1. System Architecture:
•	Vehicle ECUs & Sensors → Collect vehicle health data
•	AI Processing Unit → Predict update schedules & detect anomalies
•	Blockchain Ledger → Verify firmware integrity
•	OTA Management Server → Handles firmware deployment & update authentication
•	Ethernet/IP & LoRaWAN Communication → Secure data transfer
2. AI-Based Firmware Update Optimization:
•	Input: ECU diagnostics, battery health, network strength
•	Process: AI model determines optimal update timing
•	Output: Update is either scheduled or delayed to prevent failures
3. Security Measures:
•	Secure Boot & Authentication: Ensures only verified firmware is installed.
•	Blockchain Verification: Hash values of firmware stored on-chain for validation.
•	End-to-End Encryption: Protects OTA data from interception.
4. Communication Protocols:
•	Ethernet/IP for High-Speed OTA Updates
•	LoRaWAN for Low-Power Long-Range Updates (backup method for critical updates)
5. Testing & Validation:
•	Simulation Environment: Test firmware deployment under different network conditions.
•	Attack Scenarios: Test resilience against MITM (Man-in-the-Middle) attacks, DoS (Denial of Service), and firmware tampering.
•	Performance Metrics: Update time, energy consumption, security validation, failure recovery rate.
---


### Mapping to Sustainable Development Goals (SDG)
The proposed work aligns with several UN Sustainable Development Goals:
• SDG 7 (Affordable and Clean Energy): Optimizes energy management in EVs, reducing battery drain and improving efficiency.
•	SDG 9 (Industry, Innovation, and Infrastructure): Promotes innovation in the automotive industry, enhancing infrastructure through intelligent vehicles.
•	SDG 11 (Sustainable Cities and Communities): Improves vehicle safety and functionality, contributing to sustainable urban mobility.
•	SDG 13 (Climate Action): Reduces physical interventions and operational inefficiencies, lowering the carbon footprint associated with traditional update methods.

---

### References
1.	Nilsson, D. K., Larson, U. E., "Secure Firmware Updates over the Air in Intelligent Vehicles", Communications Workshops, 2008. ICC Workshops 08. IEEE International Conference on.
2.	Shavit, M., Gryc, A., and Miucic, R., "Firmware Update Over The Air (FOTA) for Automotive Industry", SAE Technical Paper, 2007.
3.	Miucic, R., and Mahmud, S. M., "Wireless Multicasting for Remote Software Upload in Vehicles with Realistic Vehicle Movement," Wayne State University, Tech. Rep., 2005.
4.	Ravi, A., Surabhi, M. D., & Shah, C. V. (2023). AI-Enabled Unified Diagnostic Services: Ensuring Secure and Efficient OTA Updates Over Ethernet/IP. International Advanced Research Journal in Science, Engineering and       Technology (IARJSET). DOI: 10.17148/IARJSET.2023.101019​
