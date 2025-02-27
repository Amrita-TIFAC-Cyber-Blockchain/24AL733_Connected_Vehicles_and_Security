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
1.	FOTAMOTIVE: Highlights the inefficiencies of traditional update methods and proposes a FOTA solution to address OEM, dealer, and consumer challenges.
2.	Firmware Over The Air (FOTA) and Wireless Diagnostics in Vehicles:
	1. Introduction to FOTA and Wireless Diagnostics
	 Firmware Over The Air (FOTA) updates and wireless diagnostics are emerging as critical technologies in modern automotive systems. With the increasing reliance on electronic control units (ECUs) in 		 vehicles, manufacturers aim to enhance vehicle performance, security, and user convenience by enabling remote software updates. Wireless diagnostics complement this by allowing real-time monitoring and 	 fault detection, reducing maintenance costs and downtime for vehicle owners.
	2. The Need for FOTA in Modern Vehicles
	 Traditional software updates require physical access to the vehicle, often necessitating service center visits, which are both time-consuming and costly for Original Equipment Manufacturers (OEMs). The 	 implementation of FOTA eliminates the need for these visits by allowing seamless updates via wireless communication. The study highlights how this shift can lead to significant cost savings for 	 	 manufacturers and increased convenience for consumers.
	3. Challenges in Implementing FOTA Systems
	 Several challenges need to be addressed when designing and deploying FOTA solutions:
	 •System Architecture: A key issue is ensuring compatibility across various communication protocols such as Controller Area Network (CAN), Local Interconnect Network (LIN), and Automotive Ethernet. The 	  system should support all interfaces to allow smooth integration with different ECUs.
	 •Memory Constraints: Memory allocation for storing firmware updates poses a challenge, as ECUs often have limited flash storage. The study suggests techniques such as external memory buffering and 
	  optimizing software structures to minimize memory usage.
	 •Cost Optimization: While integrating FOTA increases the initial cost of vehicles, long-term savings can be achieved by reducing physical servicing needs. The research explores approaches like reducing 	  internal memory requirements and using supercapacitors for energy efficiency.
	 •Security Concerns: Wireless updates introduce vulnerabilities to cyber threats. The paper outlines the need for encryption mechanisms, authentication protocols, and secure data transmission to prevent 
	  unauthorized access to the vehicle’s software.
	4. Proposed Solutions for Effective FOTA Deployment
	The paper discusses various methodologies to enhance FOTA performance:
	•Architectural Improvements: Implementing a centralized control unit that manages all firmware updates and diagnostic functions.
	•Enhanced Security Mechanisms: Encryption techniques such as CRC32 validation and hardware security keys can prevent malicious interference.
	•Software Optimization: Using universal software modules and compression techniques to reduce update file sizes.
	5. The Future of Wireless Diagnostics and FOTA
	The research emphasizes the potential of FOTA to revolutionize vehicle maintenance by enabling remote diagnostics, predictive maintenance, and enhanced security features. As electric and autonomous 		vehicles gain traction, FOTA will play a crucial role in ensuring their software remains up to date and resilient to cyber threats.
	Conclusion:
	The literature review highlights the significance of FOTA and wireless diagnostics in modern automotive technology. By addressing security risks, optimizing memory usage, and refining communication 		architectures, the industry can unlock the full potential of these technologies. Future advancements in cloud computing and artificial intelligence are expected to further enhance FOTA capabilities.

5.	Self-Verification Framework: Discusses virtualization techniques and hash-based verification protocols to ensure the integrity of firmware installations.
6.	Secure FOTA Protocols: Focuses on security challenges in intelligent vehicles, emphasizing the need for data integrity, authentication, and resilience to packet loss in wireless communications.
7.	AI-Enabled UDS for Secure OTA Updates (IARJSET, 2023):
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
