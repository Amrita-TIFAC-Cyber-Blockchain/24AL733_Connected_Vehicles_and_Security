# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#03 - IDS and IPS for CAN in Connected Vehicles
![](https://img.shields.io/badge/Member-Pratiksha_Mahalingpure-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-15th_Feb_2025-brown) 

### Problem Statement
The increased connectivity in vehicles through different communication protocols like CAN, Ethernet, LIN, FlexRay, MOST introduces different cyber security attacks and raises concern regarding safety and security concerns.
1.	Physical Attacks: Attackers connect to the vehicle On-Board Diagnostics (OBD-II) port to gain access to the CAN bus. Tampering with Internal Wiring.
2.	Spoofing Attacks: Injecting fabricated messages to control various vehicle functions.
3.	Frame Fuzzification: Sending any random CAN messages to cause unpredictable vehicle behavior.
4.	Denial-of-Service (DoS) Attacks: Transmitting a large volume of messages, which may result in unexpected vehicle system behavior.
5.	Remote Attacks via Infotainment Systems: Attacking USB ports, Bluetooth, and Wi-Fi.
6.	Malware Injection: Malicious software can be introduced through USB drives, SD cards, or OTA updates.<br>

Due to these all kinds of vulnerabilities, it is essential to implement IDS/IPS which will detect and prevent known and unknown attacks.

---

### Literature Survey
The first paper[1], have used a lightweight multi-stage Intrusion Detection System (IDS) for in-vehicle networks using deep learning. It employs an artificial neural network (ANN) for known attacks and an LSTM-autoencoder for unknown threats. The system has integrated hierarchical federated learning for privacy and achieving high accuracy and low false alarm rates.<br>
In paper[2], discussed different IDPS methodology mostly focused on hybrid detection system using anomoly-based and signature-based detection mechanism. It also introduces SNORT which is a free open source intrusion detection system. It is one of the Signature based Intrusion Detection and Prevention System.<br>
In paper[3], analyzes intrusion detection systems (IDS) for automotive Ethernet networks, challenges, methodologies, and solutions for securing in-vehicle communications. It highlights the importance of using IDS against cyberattacks, compares existing IDS architectures, and proposes future research directions, including blockchain, machine learning, and edge computing for enhanced security and scalability.<br>
In paper[4], It proposes an embedded intrusion detection system (IDS) for connected vehicles using a two-step algorithm. It analyzes CAN-Bus traffic with spatial-temporal methods and Bayesian networks to identify attacks like DoS and Frame Fuzzification. Experiments analyzes strong accuracy, highlighting its potential to enhance cybersecurity in modern automotive networks.

---

### Proposed Work
The proposed Intrusion Detection System (IDS) employs a hybrid, multi-stage approach to detect cyber threats within in-vehicle networks. The hybrid IDS integrates both signature-based and anomaly-based detection methodologies.
1.	Signature-Based Intrusion Detection System:<br>
- Monitoring all packets within the network.<br>
- Detect known attacks based on previous data.
2.	Anomaly-Based Intrusion Detection System:<br>
-	Monitors network behaviors such as bandwidth usage, device activity, port usage, and protocol communications.<br>
-	Identifies anomalous unknown threats.<br>
Targeted Networks: CAN, Ethernet
---

### Implementation Details
The proposed IDS implementation involves the following steps:
1.	Data Collection:<br>
-	Gathering data from in-vehicle networks such as CAN, Ethernet which contains bith normal and malicious activities.<br>
2.	Data Preprocessing:<br>
-	Data cleaning and normalization of raw data from different sources.<br>
-	Features extraction for analysis and ensuring compatibility with deep learning models.<br>
3.	Model Training and Testing:<br>
-	Training the supervised model using labeled datasets to recognize known attacks.<br>
-	Validating the model using cross-validation techniques.<br>
-	Training the unsupervised model with normal data to identify patterns and variations.<br>
4.	Hybrid IDS Deployment:<br>
-	Deploying the multi-stage IDS in an in-vehicle environment.<br>
-	Integrate SIDS to monitor known attack patterns.<br>
-	Incorporating the anomaly-based system to detect unknown threats in real time.<br>
5.	Performance Evaluation:<br>
-	Assess detection accuracy, false-positive rates.<br>
-	Continuously updating models to adapt to new threats.

---


### Mapping to Sustainable Development Goals (SDG)
**SDG 9: Industry, Innovation, and Infrastructure**: Encourages building smarter, more secure vehicle systems by detecting cyber risks in communication protocols like CAN, Ethernet, and others. Solutions like IDS/IPS will help make vehicles more safer and reliable.<br>
**SDG 11: Sustainable Cities and Communities**: Secure vehicle networks improves trust in smart transportation systems, making cities safer and better connected for everyone.<br>
**SDG 12: Responsible Consumption and Production**: Designing vehicles with built-in detection and prevention system against cyberattacks ensures better, safer use of technology over time, reducing risks and improving reliability.<br>
**SDG 13: Climate Action**: By solving cybersecurity issues, more people will trust connected and autonomous vehicles, supporting the shift to environmentally friendly transportation.<br>
**SDG 16: Peace, Justice, and Strong Institutions**: Protecting vehicles from hacking and data theft builds trust in technology, keeps personal information safe, and reduces cybercrimes.

---

### References
[1] https://www.sciencedirect.com/science/article/pii/S2214209624001128<br>
[2] https://www.researchgate.net/publication/329716671_Intrusion_Detection_Prevention_System_using_SNORT<br>
[3] https://ieeexplore.ieee.org/document/10463660<br>
[4] https://www.mdpi.com/2079-9292/10/15/1765<br>
[5]https://www.researchgate.net/publication/334583725_Intrusion_detection_system_for_automotive_Controller_Area_Network_CAN_bus_system_a_review
