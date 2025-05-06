# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>


## CVS#02 - CAN and CAN-FD Vulnerability Analysis
![](https://img.shields.io/badge/Member-Boomika_K_T-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown)  ![](https://img.shields.io/badge/Final_Review-28th_Apr_2025-darkgreen) 

### Problem Statement
Modern connected vehicles heavily rely on communication protocols like Controller Area Network (CAN) and CAN-FD (Flexible Data-rate) to facilitate the exchange of critical information between Electronic Control Units (ECUs) and sensors. These protocols are essential for vehicle operations, from managing engine performance to ensuring the functionality of safety systems.

However, CAN and CAN-FD protocols lack built-in security features, making them vulnerable to various threats, including:
1. Unauthorized access to sensitive vehicle data.
2. Manipulation or falsification of sensor data, leading to inaccurate decisions. 
3. Replay attacks, where attackers reuse valid messages to manipulate the system.
4. Eavesdropping on communications, raising significant privacy concerns.
   
As technologies like Vehicle-to-Everything (V2X) systems become more widespread, securing communication between ECUs and external sensors (such as radar, LiDAR, cameras, and environmental sensors) is increasingly important. Without effective security measures, connected vehicles face serious risks to safety and privacy.

---

### Literature Survey

Several methods have been explored in the literature to mitigate the vulnerabilities associated with CAN and CAN-FD communication protocols. These methods aim to enhance the security and integrity of the vehicle network, ensuring safe and reliable operation:

1. **Device Authentication:**  
   Device authentication mechanisms are proposed to ensure that only authorized devices can access the network. This prevents unauthorized access and protects the         system from unverified data exchanges, reducing the risk of malicious attacks.

2. **Message Authentication (HMAC):**
   The use of Hash-based Message Authentication Code (HMAC) is suggested as a way to verify the integrity and authenticity of messages. This ensures that messages have    not been tampered with during transmission, offering protection against potential data manipulation.

3. **Encryption (AES):** 
   Advanced Encryption Standard (AES) is often recommended for encrypting messages. AES ensures that the data remains confidential, preventing unauthorized access and     safeguarding against eavesdropping during communication.

4. **Enhanced Error Detection (CRC & Extended CRC):**  
   The implementation of Cyclic Redundancy Check (CRC) and its extended version in CAN-FD improves error detection capabilities. These techniques help identify and        discard corrupted or tampered messages, thereby maintaining the integrity of the data exchanged within the network.

5. **Replay Attack Prevention (Timestamps & Sequence Numbers):**  
   To defend against replay attacks, literature suggests adding timestamps and sequence numbers to messages. This approach ensures that only current and valid data is     processed, blocking the retransmission of previously captured messages and preventing manipulation of the system.

6. **Bit Rate Monitoring (for CAN-FD):**  
   Bit-rate monitoring in CAN-FD is another proposed method to detect and prevent exploits. By controlling the bit-rate switching process, it is possible to identify     and mitigate issues such as timing mismatches that could disrupt the communication flow.

7. **Network Isolation and Gateway Security:**  
   Implementing network isolation within the vehicle’s internal network, combined with firewalls and gateway security, can block unauthorized external access. This        approach protects the system from external threats and ensures that only trusted communication is allowed.

8. **Packet Filtering and Intrusion Detection (for CAN-FD):**  
   The use of packet filtering and intrusion detection systems (IDS) has been explored as a means to protect CAN-FD networks. These methods help identify and block        suspicious or abnormal traffic, thus defending the system against malicious activities.

---

### Proposed Work
This project focuses on enhancing the security of CAN-FD networks by detecting and mitigating Message Tampering, Malicious Injection, and Denial-of-Service (DoS) attacks. The following key phases and methods will be employed:

1. **CAN-FD Network Simulation:**  
   A CAN-FD network will be simulated, consisting of multiple ECUs exchanging messages within the system.

2. **Attack Simulation:**  
   - Message Tampering: Unauthorized modification of messages.  
   - Malicious Injection: Injection of unauthorized commands into the network.  
   - DoS Attack: Overloading the network with excessive messages, disrupting communication.

3. **Intrusion Detection System (IDS):**  
   A real-time IDS will monitor the network traffic, detect anomalies, and identify security threats through message integrity and frequency analysis.

4. **AES-128 Encryption:** 
   All CAN-FD messages will be encrypted using AES-128, ensuring data confidentiality and integrity, preventing tampering, and unauthorized access.

5. **Defensive Measures:**  
   - Rate-Monitoring: To detect DoS attacks by tracking message rate and identifying potential overload situations.  
   - Firewall-Based Filtering: Blocks unauthorized messages and filters out malicious traffic.  
   - Secure Transceiver Communication: Authenticates ECUs to ensure that only authorized devices can communicate within the network.

6. **Performance Evaluation:**  
   The performance of security measures will be evaluated by:
   - Accuracy of IDS detection.
   - Latency impact of AES-128 encryption.
   - Response time to security threats.

This approach ensures the development of a secure and resilient CAN-FD communication system, protecting against critical cyber threats and safeguarding vehicle network integrity.

---
### Implementation Details

1. Simulate a CAN-FD network using MATLAB Vehicle Network Toolbox with virtual ECUs communicating over MathWorks Virtual Channel 1.

2. Normal sensor data (temperature) is generated using Random Number and constant sources, packed into CAN-FD messages (Temperature Data Packing1, Packing2).

3. Messages are transmitted using CAN-FD Transmit blocks (CAN-FD Transmit1, CAN-FD Transmit2).

4. An attacker node intercepts and modifies legitimate CAN-FD messages before forwarding.

5. AES-128 encryption is applied to outgoing messages to protect data integrity.

6. SHA-256 hashing is used to generate a Message Authentication Code (MAC) for verifying message authenticity.

7. At the receiver side, incoming messages undergo AES-128 decryption and SHA verification.

8. Intrusion Detection System (IDS) compares received hashes with expected hashes to detect message tampering.

9. Unauthorized messages or tampered packets are filtered and rejected.

10. Flooding/DoS attacks are simulated by randomly generating excessive CAN messages using Random Number and multiple transmitters.

11. Rate-monitoring logic detects abnormal traffic patterns indicative of flooding.

12. Firewall-based packet filtering is applied to drop excessive or malformed packets.

13. Rate-limiting techniques (similar to SYN cookies) prevent the CAN bus from being overwhelmed.

14. System performance is evaluated under normal, tampered, and flood attack scenarios.

---

### Mapping to Sustainable Development Goals (SDG)
This project aligns with:
SDG 9 - Industry, Innovation, and Infrastructure by strengthening automotive cybersecurity.\
SDG 11 - Sustainable Cities and Communities by ensuring safer vehicle communication.\
SDG 16 - Peace, Justice, and Strong Institutions by protecting automotive networks from cybercrime.

---

### References
1. Addressing Vulnerabilities in CAN-FD: An Exploration and Security Enhancement Approach ;  by Naseeruddin Lodge, Nahush Tambe and Fareena Saqib
Department of Electrical and Computer Engineering, University of North Carolina at Charlotte, Charlotte.
2. Enhancing In-Vehicle Networks with CAN-FD: A study of Protocol Improvements over Classical CAN; Dhanush M S; Ananthakrinshna T;  2024 International Conference on Electronics, Computing, Communication and Control Technology (ICECCC)
3. Intelligent Connected Vehicle CAN-FD Bus Network Security Protocol; Jingyi Jia; Yihu Xu; Yujing Wu; Yinan Xu; Yiming Fan; Dandan Zhang; 2023 International Conference on Mobile Internet, Cloud Computing and Information Security (MICCIS)
