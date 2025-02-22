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
These studies underline the need for robust and secure frameworks to ensure reliable and efficient FOTA implementation in intelligent vehicles.
---

### Proposed Work
The proposed solution focuses on designing a secure and efficient FOTA protocol tailored for intelligent vehicles. 
Key features include:

1.Integrity Assurance: Ensures firmware remains unaltered during transmission and installation.

2.Authentication Mechanisms: Verifies the authenticity of firmware sources.

3.Confidentiality Protocols: Protects proprietary firmware from unauthorized access.

4.Freshness Verification: Prevents outdated firmware from being reused.

The framework will leverage lightweight cryptographic methods to address the resource constraints of ECUs, ensuring seamless and secure updates.

---

### Implementation Details
The implementation involves the following steps:
1.	Protocol Design: Develop a secure communication protocol with features like encryption, digital signatures, and secure hash algorithms.
2.	Virtualization for Verification: Implement virtualization within the ECU for trusted execution and validation of firmware.
3.	Testing and Validation: Simulate update processes under various scenarios to evaluate security, efficiency, and reliability.
4.	Deployment: Pilot the solution in a controlled environment, iteratively improving based on performance metrics and feedback.

---


### Mapping to Sustainable Development Goals (SDG)
The proposed work aligns with several UN Sustainable Development Goals:
•	SDG 9 (Industry, Innovation, and Infrastructure): Promotes innovation in the automotive industry, enhancing infrastructure through intelligent vehicles.
•	SDG 11 (Sustainable Cities and Communities): Improves vehicle safety and functionality, contributing to sustainable urban mobility.
•	SDG 13 (Climate Action): Reduces physical interventions and operational inefficiencies, lowering the carbon footprint associated with traditional update methods.

---

### References
1.	Nilsson, D. K., Larson, U. E., "Secure Firmware Updates over the Air in Intelligent Vehicles", Communications Workshops, 2008. ICC Workshops 08. IEEE International Conference on.
2.	Shavit, M., Gryc, A., and Miucic, R., "Firmware Update Over The Air (FOTA) for Automotive Industry", SAE Technical Paper, 2007.
3.	Miucic, R., and Mahmud, S. M., "Wireless Multicasting for Remote Software Upload in Vehicles with Realistic Vehicle Movement," Wayne State University, Tech. Rep., 2005.
