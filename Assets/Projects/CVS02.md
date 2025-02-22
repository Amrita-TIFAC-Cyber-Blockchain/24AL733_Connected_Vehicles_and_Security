# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#02 - CAN and CAN-FD Vulnerability Analysis
![](https://img.shields.io/badge/Member-Boomika_K_T-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement
Modern connected vehicles rely heavily on communication protocols like the Controller Area Network (CAN) and CAN-FD (Flexible Data-rate) to share critical information between Electronic Control Units (ECUs) and sensors. These protocols are vital for vehicle operations, from managing engine performance to ensuring safety systems function properly. However, since CAN and CAN-FD lack built-in security features, they are vulnerable to threats like data tampering, unauthorized access, message injection, and replay attacks.
As connected vehicle technologies, especially Vehicle-to-Everything (V2X) systems, become more widespread, securing communication between ECUs and external sensors (such as radar, LiDAR, cameras, and environmental sensors) is increasingly important. 
Without effective security measures, these vehicles face significant risks, such as:
1.Unauthorized access to sensitive vehicle data.
2.Manipulation or falsification of sensor data, leading to poor decisions.
3.Replay attacks, where attackers reuse valid messages to manipulate the system.
4.Eavesdropping on communication, which raises serious privacy concerns.



---

### Literature Survey
From the literature survey here are some methods used or can be addressed to over come the CAN and CAN-FD vulnerabilities
1.Device Authentication: Ensures only authorized devices can access the network, preventing unauthorized access and safeguarding the system against unverified data exchanges.
2.Message Authentication (HMAC): Hash-based Message Authentication Code (HMAC) is used to verify the integrity and authenticity of messages, protecting against tampering during transmission.
3.Encryption (AES): Encrypting messages with Advanced Encryption Standard (AES) ensures data confidentiality, preventing unauthorized access and eavesdropping.
4.Enhanced Error Detection (CRC & Extended CRC): CRC (Cyclic Redundancy Check) and its extended version in CAN-FD improve error detection by identifying and discarding corrupted or tampered messages, maintaining data integrity.
5.Replay Attack Prevention (Timestamps & Sequence Numbers): Adding timestamps and sequence numbers to messages ensures only current and valid data is processed, blocking attacks that retransmit previously captured messages.
6.Bit Rate Monitoring (for CAN-FD): Monitors and controls the bit-rate switching process in CAN-FD to detect and prevent exploits like timing mismatches that can disrupt communication.
7.Network Isolation and Gateway Security: Implements internal network isolation along with firewalls and gateway security to block unauthorized external access and protect against external threats.
8.Packet Filtering and Intrusion Detection (for CAN-FD): Uses packet filtering and intrusion detection systems to identify and block suspicious messages or abnormal traffic, protecting the network from malicious activities.


---

### Proposed Work
This project focuses on three major security threats in CAN-FD networks:
Message Tampering – Unauthorized modification of legitimate CAN-FD messages.
Malicious Injection – The attacker injects fake messages into the CAN-FD network.
Denial-of-Service (DoS) Attack – Overloading the CAN-FD network to disrupt communication.
Each attack will be simulated, detected, and mitigated using MATLAB.

### Implementation Details
To address the identified threats, MATLAB will be used to simulate the CAN-FD network, introduce attack scenarios, and implement security mechanisms. The project will be carried out in the following steps:
CAN-FD Network Simulation: A simulated CAN-FD network will be created in MATLAB using the Vehicle Network Toolbox. This will involve setting up multiple Electronic Control Units (ECUs) communicating over a CAN-FD bus. The network will be designed to mimic real-world vehicle communication, with legitimate message exchanges between various ECUs.
Message Tampering Attack Simulation: A normal CAN-FD message transmission scenario will be established. An attacker node will be introduced to intercept and modify legitimate messages before forwarding them. The system will then analyze the impact of these alterations on vehicle functionality.
Detection and Prevention of Message Tampering: A real-time Intrusion Detection System (IDS) will be implemented to monitor message integrity. This will be achieved by comparing incoming messages with expected values. Cryptographic authentication techniques such as AES-128 encryption and HMAC verification will be employed to secure message transmissions and detect unauthorized modifications.
Malicious Injection Attack Simulation: The system will generate normal CAN-FD messages and introduce an attacker node that injects unauthorized messages. This attack will test the vulnerability of the network to unauthorized command execution, such as false brake or acceleration signals.
Detection and Prevention of Malicious Injection: ECU authentication mechanisms will be enforced using Message Authentication Codes (MACs). Messages from unauthorized sources will be filtered out, preventing false commands from affecting the system.
Denial-of-Service (DoS) Attack Simulation: A flooding attack will be simulated, where an attacker node sends an excessive number of messages to overwhelm the CAN-FD bus. The effect of this attack on normal ECU communication and system response times will be analyzed.
Detection and Prevention of DoS Attacks: Rate-monitoring techniques will be implemented to detect abnormal traffic patterns. Firewall-based packet filtering will be used to limit excessive message transmission. Additionally, SYN cookies will be applied to prevent repeated malicious message floods.
Performance Evaluation and Testing: The effectiveness of the implemented security measures will be tested under various attack scenarios. Metrics such as detection rate, false positives, and system response time will be analyzed to evaluate the efficiency of the IDS and cryptographic security mechanisms.


### Mapping to Sustainable Development Goals (SDG)
This project aligns with:
SDG 9 - Industry, Innovation, and Infrastructure by strengthening automotive cybersecurity.
SDG 11 - Sustainable Cities and Communities by ensuring safer vehicle communication.
SDG 16 - Peace, Justice, and Strong Institutions by protecting automotive networks from cybercrime.


### References
1. Addressing Vulnerabilities in CAN-FD: An Exploration and Security Enhancement Approach ;  by Naseeruddin Lodge, Nahush Tambe and Fareena Saqib
Department of Electrical and Computer Engineering, University of North Carolina at Charlotte, Charlotte.
2. Enhancing In-Vehicle Networks with CAN-FD: A study of Protocol Improvements over Classical CAN; Dhanush M S; Ananthakrinshna T;  2024 International Conference on Electronics, Computing, Communication and Control Technology (ICECCC)
3. Intelligent Connected Vehicle CAN-FD Bus Network Security Protocol; Jingyi Jia; Yihu Xu; Yujing Wu; Yinan Xu; Yiming Fan; Dandan Zhang; 2023 International Conference on Mobile Internet, Cloud Computing and Information Security (MICCIS)
