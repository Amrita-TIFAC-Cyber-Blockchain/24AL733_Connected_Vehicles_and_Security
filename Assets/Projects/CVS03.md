# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#03 - IDS and IPS for CAN in Connected Vehicles
![](https://img.shields.io/badge/Member-Pratiksha_Mahalingpure-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-15th_Feb_2025-brown) 

### IDS and IPS for CAN in Connected Vehicles
Pratiksha Mahalingpure<br>
Department of ECE,<br>
Amrita Vishwa Vidyapeetham, Coimbatore<br>
24AL733: Connected Vehicles and Security 


### Problem Statement
The increased connectivity in vehicles through different communication protocols like CAN, Ethernet, LIN, FlexRay, MOST introduces different cyber security attacks and raises concern regarding safety and security concerns.
1.	Physical Attacks: Attackers connect to the vehicle On-Board Diagnostics (OBD-II) port to gain access to the CAN bus. Tampering with Internal Wiring. Attackers can gain unauthorized access to a vehicle’s network by physically connecting to the On-Board Diagnostics (OBD-II) port, which serves as a gateway to the CAN bus
2.	Spoofing Attacks: Cybercriminals inject fabricated messages into the CAN bus, imitating legitimate commands from vehicle components. CAN protocol lacks built-in message authentication, it affectes by these types of attacks.
3.	Frame Fuzzification: Frame fuzzification involves sending random or framed CAN messages to the network, which can trigger unexpected behaviors in vehicle functions. This technique disrupts the normal operation of the ECUs, leading to unpredictable responses, system crashes, or safety-critical failures.
4.	Denial-of-Service (DoS) Attacks: A DoS attack floods the vehicle’s communication network with an excessive volume of CAN messages, overloading the system and causing actual messages to be delayed or dropped. This can result in the failure of critical vehicle functions, such as braking or steering causing safety risk.
5.	Remote Attacks via Infotainment Systems: As modern vehicles are equipped with infotainment systems that offer connectivity through USB ports, Bluetooth, and Wi-Fi, they become vulnerable to remote attacks.
6.	Malware Injection: Malware can be introduced into a vehicle’s network through commonly used access points such as USB drives, SD cards, or Over-The-Air (OTA) software updates. Once the malicious software is installed, it can compromise the vehicle’s ECUs, manipulate sensor data, or disable security systems.<br>

Due to these all kinds of vulnerabilities, it is essential to implement IDS and IPS for CAN which will detect and prevent known and unknown attacks.

---

### Literature Survey
The first paper [1], have used a lightweight multi-stage Intrusion Detection System (IDS) for in-vehicle networks using deep learning. It employs an artificial neural network (ANN) for known attacks and an LSTM-autoencoder for unknown threats. The unsupervised model, which works as an anomaly detection model, is trained solely on normal data, and any samples that deviate significantly from the learned patterns are identified as an anomaly or an unseen attack. Once the unsupervised model detects malicious traffic, it is flagged for further investigation. Any anomalies detected by the unsupervised model that are later confirmed as threats will have a new attack label generated. For broader applicability, the proposed IDS can learn the legitimate CAN IDs and normal behavior for each vehicle at design time and monitor the network to detect any attacks during operational runtime. The system has integrated hierarchical federated learning for privacy and achieving high accuracy and low false alarm rates. Utilizing FL allows the IDS to benefit from various driving scenarios, enhances its resilience against new and unseen attacks, and enables continuous learning without compromising the privacy and security of the training data.<br>
In paper [2], discussed different IDPS methodology mostly focused on hybrid detection system using anomaly-based and signature-based detection mechanism. It also introduces SNORT which is a free open-source intrusion detection system. It is one of the Signature based Intrusion Detection and Prevention System. This tool lies with the formation of rules.  Rules can be created/designed to block traffic or to merely send alerts, alerts can be logged to a log file, can be sent to the console or displayed on the screen.  They can be configured to send an email to someone or they can be logged to database. Various options can be used for the formation of rules. Snort basically works on the three modes: Sniffer mode, Packet logger mode and NIDS mode. this system may provide a good model for the realization of the intrusion detection system. This paper includes the reference to the structure of snort and NTOP, and proposes a new design idea of combining Snort with NTOP, which is validated by the experiment. The results of experiment prove that intrusion behaviour can be detected by this system.  This system works well and has been successfully tested.<br>
In paper [3], analyses intrusion detection systems (IDS) for automotive Ethernet networks, challenges, methodologies, and solutions for securing in-vehicle communications. It highlights the importance of using IDS against cyberattacks, compares existing IDS architectures, and proposes future research directions, including blockchain, machine learning, and edge computing for enhanced security and scalability.<br>
In paper [4], it proposes an embedded intrusion detection system (IDS) for connected vehicles using a two-step algorithm. It analyses CAN-Bus traffic with spatial-temporal methods and Bayesian networks to identify attacks like DoS and Frame Fuzzification. A Bayesian network is a probabilistic graph that predicts the dependency relationships between a set of random variables through a probabilistic inference process. Once the threat model and the risks associated with it have been identified, a system is devised to mitigate these dangers and test them. Using a two-step detection algorithm that exploits both the variation of the status parameters of the various ECUs over time and the Bayesian networks, it can identify a possible attack. First of all, we have to analyze the domain to understand the parameters and their related ECUs that must be taken into consideration to map the vehicle and all the possible cyber risks associated with it. To obtain the actual conditions of a possible attack on the vehicle, the conditions were defined in which one can be in the presence of a specific attack. In particular, as we will see in the next section, the parameters that, combined, can identify a possible attack situation. This system may provide a good model for the realization of the intrusion detection system. 

---

### Proposed Work
The proposed Intrusion Detection System (IDS) employs a hybrid, multi-stage approach to detect cyber threats within in-vehicle networks. The hybrid IDS integrates both signature-based and anomaly-based detection methodologies.<br>
1.	Signature-Based Intrusion Detection System:<br>
•	Monitoring all packets within the network.<br>
•	Detect known attacks based on previous data.<br>
•	For Signature -Based IDS and IPS supervised algorithm is suitable to detect known attacks.<br>
•	Snort is a free open-source intrusion detection system which is one of the Signature based Intrusion Detection and Prevention System. It not only detects but also prevent attack by reject, drop and blocking the communication.<br>

2.	Anomaly-Based Intrusion Detection System:<br>
•	Identifies anomalous unknown threats.<br>
•	The unsupervised model, which works as an anomaly detection model, is trained solely on normal data, and any samples that deviate significantly from the learned patterns are identified as an anomaly or an unseen attack.<br>
•	Any anomalies detected by the unsupervised model that are later confirmed as threats will have a new attack label generated.<br>

Targeted Network: CAN

---

### Implementation Details
The proposed IDS implementation involves the following steps:<br>
1.	Data Collection:<br>
•	Gathering data from in-vehicle networks such as CAN which contains both normal and malicious activities.<br>
2.	Data Preprocessing:<br>
•	Converting data into a format suitable for use by deep neural networks.<br>
•	Data cleaning and normalization of raw data from different sources.<br>
•	Features extraction for analysis and ensuring compatibility with deep learning models.<br>
3.	Model Training and Testing:<br>
•	Training the supervised model using labelled datasets to recognize known attacks.<br>
•	Validating the model using cross-validation techniques.<br>
•	Using SNORT to detect and prevent the known attacks in first layer.<br>
•	Training the unsupervised model with normal data to identify patterns and variations.<br>
4.	Hybrid IDS Deployment:<br>
•	Deploying the multi-stage IDS in an in-vehicle environment.<br>
•	Integrate SIDS to monitor known attack patterns.<br>
•	Incorporating the anomaly-based system to detect unknown threats in real time.<br>
5.	Performance Evaluation:<br>
•	Assess detection accuracy, false-positive rates.<br>
•	Continuously updating models to adapt to new threats.<br>
---

### Mapping to Sustainable Development Goals (SDG)
**SDG 9: Industry, Innovation, and Infrastructure**: Encourages building smarter, more secure vehicle systems by detecting cyber risks in communication protocols like CAN, Ethernet, and others. Solutions like IDS/IPS will help make vehicles more safer and reliable.<br>
**SDG 11: Sustainable Cities and Communities**: Secure vehicle networks improves trust in smart transportation systems, making cities safer and better connected for everyone.<br>
**SDG 12: Responsible Consumption and Production**: Designing vehicles with built-in detection and prevention system against cyberattacks ensures better, safer use of technology over time, reducing risks and improving reliability.<br>
**SDG 13: Climate Action**: By solving cybersecurity issues, more people will trust connected and autonomous vehicles, supporting the shift to environmentally friendly transportation.<br>
**SDG 16: Peace, Justice, and Strong Institutions**: Protecting vehicles from hacking and data theft builds trust in technology, keeps personal information safe, and reduces cybercrimes.

---

### Architecture Model
Architecture Model for IDS and IPS in Connected Vehicles<br>
1. Data Collection Layer: Continuous real-time data collection from vehicle networks.<br>
•	Sources: CAN Bus, OBD-II Port, Infotainment Systems, External Communication Interfaces (Wi-Fi, Bluetooth, USB, etc.).<br>
2. Preprocessing Layer<br>
•	Data Cleaning & Normalization: Filling missing values, and standardizing data.<br>
•	Feature Extraction: Extracting essential CAN IDs, and payload for analysis.<br>
3. Detection Engine<br>
a. Signature-Based IDS (SIDS)<br>
•	 Tool: SNORT<br>
•	Mechanism: Predefined attack signatures (e.g., DoS, spoofing). Rule-based filtering and blocking.<br>
•	Deployment Mode: NIDS mode for monitoring and IPS mode for active prevention.<br>
b. Anomaly-Based IDS (AIDS)<br>
•	Model: LSTM-Autoencoder trained on normal CAN traffic.<br>
•	Mechanism: Detect deviations from normal behaviour. Identifies novel or zero-day attacks.<br>
4. Decision Layer<br>
•	Threat Classification: Known threats are detected.<br>
•	Real-Time Response: Drop malicious packets.<br>
6. Monitoring & Visualization Layer<br>
•	Dashboard: Real-time threat visualization, alerts, and performance analytics.<br>
7. Evaluation & Feedback Loop <br>
•	Performance Metrics: Detection rate, false positives/negatives, response time.<br>
•	Continuous Improvement: Update threat databases, refine ML models, and adapt to new attack vectors.<br>



### References
[1] https://www.sciencedirect.com/science/article/pii/S2214209624001128<br>
[2] https://www.researchgate.net/publication/329716671_Intrusion_Detection_Prevention_System_using_SNORT<br>
[3] https://ieeexplore.ieee.org/document/10463660<br>
[4] https://www.mdpi.com/2079-9292/10/15/1765<br>
[5]https://www.researchgate.net/publication/334583725_Intrusion_detection_system_for_automotive_Controller_Area_Network_CAN_bus_system_a_review
