# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#10 - AI-Powered Secure OTA Updates for Electric Vehicles (EVs)
![](https://img.shields.io/badge/Member-Mani_Shankar_Molleti-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement
Modern vehicles increasingly rely on Electronic Control Units (ECUs) to manage critical functions such as braking, infotainment, and safety systems. These ECUs require frequent firmware updates to address software bugs, enhance performance, and strengthen cybersecurity. Traditionally, firmware updates are carried out manually at service centers through wired connections. This approach is inefficient, costly, and time-consuming, leading to vehicle downtime and inconvenience for users.
To overcome these limitations, the automotive industry is shifting towards Over-the-Air (OTA) firmware updates, allowing remote software updates without requiring physical access to the vehicle. While OTA updates offer convenience and cost savings, their large-scale implementation presents several technical and security challenges, including:
1.	Cybersecurity Vulnerabilities: Hackers may exploit weaknesses in the update process to inject malicious firmware, which can compromise vehicle control systems and endanger passenger safety.
2.	Network Reliability Issues: Inconsistent or poor network conditions can lead to incomplete or corrupted updates, causing ECU malfunctions or failures.
3.	Legacy ECU Compatibility: Many older vehicle models lack the hardware and software capabilities required for secure, high-speed OTA updates, making integration difficult.
4.	Update Optimization: Blindly pushing updates without analyzing vehicle conditions can lead to inefficient updates, increased power consumption, and potential system instability.

Proposed Solution:
To address these challenges, this project proposes an AI-driven Secure OTA Firmware Update System, integrating Artificial Intelligence (AI) and Ethernet/IP-based Unified Diagnostic Services (UDS). The solution offers:
•	AI-Powered Predictive Maintenance: AI analyzes real-time vehicle health data to determine the optimal timing for updates, minimizing operational disruptions.
•	Enhanced Cybersecurity: The system employs end-to-end encryption and intrusion detection systems (IDS) to prevent unauthorized access and firmware tampering.
•	Efficient Data Transmission: Leveraging Ethernet/IP communication, the system ensures faster, more reliable OTA updates, reducing the risks associated with poor network conditions.
•	Legacy Vehicle Support: The solution includes backward-compatible encryption protocols and adaptive data transfer mechanisms to support older ECUs.
By combining AI-driven diagnostics, robust cybersecurity, and efficient communication protocols, the proposed system enhances OTA firmware updates' security, reliability, and efficiency. This approach reduces vehicle downtime, improves cybersecurity resilience, and ensures a seamless update process for modern and legacy vehicles alike.

---

### Literature Survey
1.	Title: Firmware Over the Air for Automotive (FOTAMOTIVE)

	Name of Journal: Published in IEEE Xplore (2014)

	Summary: The paper presents FOTAMOTIVE, a cloud-based Firmware Over-the-Air (FOTA) system for automotive ECUs. It addresses challenges in traditional firmware update methods, which require physical access, 		leading to high recall costs and inconvenience. The proposed system enables wireless updates through a cloud-server mechanism, where OEMs can deploy updates remotely to vehicle ECUs. This enhances efficiency, 	scalability, and cost-effectiveness. The paper also highlights potential security risks, connectivity challenges, and safety concerns associated with remote firmware updates.
	
	Research Gap:
	•	Post-Installation Verification: The study focuses on secure transmission but lacks a mechanism to verify firmware integrity after installation.
	•	Security Measures: While it mentions cybersecurity risks, it does not propose a detailed security framework to mitigate unauthorized firmware modifications.
	•	Real-World Implementation: The paper relies on simulations, and real-world validation in automotive environments is missing.
	•	Rollback & Recovery: There is no discussion on rollback strategies in case of a failed update, which is crucial for vehicle safety.

3.	Title:Firmware Over The Air (FOTA) and Wireless Diagnostics in Vehicles:
	
	Name of Journal:Proceedings of the XXIX International Scientific Conference Electronics - ET2020, IEEE, September 16-18, 20

	Summary:This paper explores the architecture and challenges of Firmware Over The Air (FOTA) systems and wireless vehicle diagnostics. The increasing reliance on Electronic Control Units (ECUs) in modern 	vehicles necessitates frequent firmware updates to fix software bugs, enhance cybersecurity, and optimize performance. Traditionally, firmware updates require service center visits, which are costly and 	time-consuming. FOTA technology eliminates this need by enabling wireless updates, thereby improving efficiency and reducing downtime.

	Research Gap:While the paper provides a broad overview of FOTA and wireless diagnostics, it lacks insights into AI-driven predictive maintenance, advanced security measures (e.g., IDS, man-in-the-middle 	attack prevention), legacy vehicle compatibility, and network reliability issues affecting OTA update success. Addressing these gaps is crucial for a secure and efficient FOTA deployment.

4.	Self-Verification Framework: Discusses virtualization techniques and hash-based verification protocols to ensure the integrity of firmware installations.

5.	Title: AI-Enabled Unified Diagnostic Services: Ensuring Secure and Efficient OTA Updates Over Ethernet/IP
	
	Name of Journal: International Advanced Research Journal in Science, Engineering, and Technology (IARJSET), Vol. 10, Issue 10, October 2023

	Summary: The paper introduces an Ethernet/IP-based Unified Diagnostic Service (UDS) architecture to enhance OTA firmware updates in vehicles. It addresses bandwidth, latency, and security limitations of 	traditional CAN/LIN-based OTA methods. Key features include non-interference with runtime services, enhanced cybersecurity (secure boot, authentication), and ISO-14229 UDS standardization for OEM and 	aftermarket compatibility. The system is tested under various network conditions, demonstrating improved reliability, security, and update speed over existing methods.

	Research Gap :
	The study lacks AI-driven predictive maintenance for ECU failure detection, intrusion detection systems (IDS) for enhanced cybersecurity, and legacy ECU compatibility with Ethernet/IP updates. It also 	does not address scalability and network reliability challenges for large-scale deployment.

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
The proposed work aligns with several UN Sustainable Development Goals:\
• SDG 7 (Affordable and Clean Energy): Optimizes energy management in EVs, reducing battery drain and improving efficiency.\
• SDG 9 (Industry, Innovation, and Infrastructure): Promotes innovation in the automotive industry, enhancing infrastructure through intelligent vehicles.\
• SDG 11 (Sustainable Cities and Communities): Improves vehicle safety and functionality, contributing to sustainable urban mobility.\
• SDG 13 (Climate Action): Reduces physical interventions and operational inefficiencies, lowering the carbon footprint associated with traditional update methods.

---

### References
1.	Nilsson, D. K., Larson, U. E., "Secure Firmware Updates over the Air in Intelligent Vehicles", Communications Workshops, 2008. ICC Workshops 08. IEEE International Conference on.
2.	Shavit, M., Gryc, A., and Miucic, R., "Firmware Update Over The Air (FOTA) for Automotive Industry", SAE Technical Paper, 2007.
3.	Miucic, R., and Mahmud, S. M., "Wireless Multicasting for Remote Software Upload in Vehicles with Realistic Vehicle Movement," Wayne State University, Tech. Rep., 2005.
4.	Ravi, A., Surabhi, M. D., & Shah, C. V. (2023). AI-Enabled Unified Diagnostic Services: Ensuring Secure and Efficient OTA Updates Over Ethernet/IP. International Advanced Research Journal in Science, Engineering and       Technology (IARJSET). DOI: 10.17148/IARJSET.2023.101019​
