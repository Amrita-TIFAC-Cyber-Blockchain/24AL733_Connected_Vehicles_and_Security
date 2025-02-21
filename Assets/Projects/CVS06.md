# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#06 - Threats in V2I Communications
![](https://img.shields.io/badge/Member-Sakshi_Ganpat_Jadhav-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement
Vehicle-to-Infrastructure (V2I) and broader vehicular communication systems face growing cybersecurity challenges, including risks such as denial-of-service attacks, message tampering, and identity spoofing, which compromise system reliability and user privacy. Current security measures are often insufficient to address the evolving nature of these threats and the increasing complexity of connected and autonomous vehicle networks. With advancements in technologies like quantum computing threatening traditional cryptographic approaches, there is a critical need for scalable and future-proof security frameworks that ensure secure, efficient, and privacy-preserving communication in Intelligent Transportation Systems (ITS)



---

### Literature Survey
Cybersecurity Attacks in Vehicle-to-Infrastructure (V2I) Applications and Their Prevention[1]
This paper addresses the critical vulnerabilities in V2I communication systems, such as Distributed Denial of Service (DDoS) attacks, impersonation, and message alteration, which can disrupt traffic management and safety-critical applications. The study highlights the inadequacy of existing V2I security architectures in mitigating these threats effectively. To address these challenges, the authors propose CVGuard, a novel security architecture combining Edge Computing, Software-Defined Networking (SDN), and Network Functions Virtualization (NFV). CVGuard leverages microboxes at RSUs to monitor data, detect anomalies, and mitigate attacks in real time. The architecture employs a centralized controller for threat analysis and coordination, enabling scalable and flexible protection against a wide range of cyber threats. A case study focusing on a DDoS attack on the Stop Sign Gap Assist (SSGA) application demonstrates CVGuard's effectiveness, reducing vehicle conflicts by 60%. This study emphasizes the importance of integrating emerging technologies to enhance the resilience of V2I systems.<br>Evaluation of Attack Vectors and Risks in Automobiles and Road Infrastructure[2] This paper examines the increasing cybersecurity vulnerabilities in connected and autonomous vehicles and their interaction with road infrastructure. It identifies key problems such as vulnerabilities in the Controller Area Network (CAN) bus, keyless entry systems, and road infrastructure components like smart traffic signs. These systems are susceptible to attacks, including man-in-the-middle, message spoofing, and denial-of-service (DoS), which can compromise vehicle functionality and road safety. To mitigate these risks, the authors recommend implementing secure sensor designs, encryption protocols, and robust authentication mechanisms. Additionally, they emphasize the need for industry-wide collaboration and the adoption of bug bounty programs to proactively identify and address vulnerabilities. The study underscores the importance of securing not just the vehicles but the entire ecosystem of connected infrastructure to ensure overall safety and reliability.<br>
Security Threats in Intelligent Transportation Systems and Their Risk Levels[3] This paper focuses on identifying and evaluating the security threats facing Intelligent Transportation Systems (ITS) using a Threat, Vulnerability, and Risk Analysis (TVRA) framework. The authors address critical threats such as Sybil attacks, impersonation, jamming, and malware propagation, which jeopardize the reliability of ITS. They propose several countermeasures, including encryption, pseudonymous authentication, and digital signatures to ensure data confidentiality and authentication. The study also highlights the potential of blockchain-based routing protocols for ensuring secure communication in ITS. Emerging techniques such as machine learning and reinforcement learning are recommended for real-time threat detection and mitigation. The authors conclude that a multi-layered security framework is essential for protecting ITS against these threats and ensuring safe and efficient transportation networks.<br> Quantum Key Distribution for V2I Communications with Software-Defined Networking[4]
The paper focuses on the increasing vulnerabilities of Vehicle-to-Infrastructure (V2I) communication systems to cyber threats, including quantum-based attacks that can compromise traditional cryptographic systems. With sensitive data like real-time traffic information being exchanged in V2I networks, ensuring the confidentiality, integrity, and resilience of these communications is paramount. Existing cryptographic techniques are inadequate for securing such systems in the post-quantum era.The paper integrates Quantum Key Distribution (QKD) with Software-Defined Networking (SDN) to provide secure and scalable V2I communications. QKD ensures information-theoretic security using Free-Space Optical (FSO) technology, while SDN optimizes resource allocation and key management.<br>A Practical Implementation of Quantum-Derived Keys for Secure Vehicle-to-Infrastructure Communications[5]
This paper highlights the limitations of Public Key Infrastructure (PKI) in securing real-time, safety-critical applications in V2I systems. PKI-based methods are vulnerable to attacks, particularly in the context of future quantum computers, which could easily break current cryptographic protocols. The lack of practical implementations for post-quantum secure V2I communication frameworks is a significant gap. The study implements FSO-QKD to generate quantum-secure encryption keys for V2I systems. It introduces a Zero-Trust Security Protocol (ZAP) to prevent spoofed messages and validates its effectiveness against attack scenarios.<br>
A Privacy Preserving Authentication Protocol Using Quantum Computing for V2I Authentication in Vehicular Ad Hoc Networks[6]
This paper addresses the dual challenges of ensuring both privacy and security in Vehicular Ad Hoc Networks (VANETs). Traditional cryptographic techniques rely on computationally hard problems, which are susceptible to quantum attacks. The need for an authentication protocol that protects against generic and quantum-specific threats while preserving user privacy is a key focus of this study. The paper proposes a QKD-based authentication protocol combined with Classical Identity-Based Authentication to ensure privacy, message unlinkability, and vehicle traceability. Simulations confirm its robustness against quantum attacks and practical applicability.


---

### Proposed Work
The proposed work aims to design a Quantum Machine Learning (QML)-based anomaly detection framework for addressing cybersecurity threats in Vehicle-to-Infrastructure (V2I) communication. Modern V2I systems face significant vulnerabilities, including Distributed Denial of Service (DDoS), message spoofing, and Sybil attacks, which compromise system reliability and traffic safety. Traditional detection methods often lack scalability and efficiency, particularly in real-time scenarios. By leveraging QML algorithms, the proposed framework will enable faster and more accurate threat detection by analyzing vehicular communication patterns.

1.Threat Simulation:<br>
-Model various cyber attacks such as DDoS, Sybil, and Spoofing that can disrupt V2I communication.<br>
-Generate traffic data representing both normal and malicious behavior.<br>
2. Quantum Machine Learning for Threat Detection:<br>
-Train a quantum-based anomaly detection model to classify network traffic as normal or malicious.<br>
-Use traffic patterns, packet logs, and communication anomalies as input features.<br>
-Evaluation Metrics<br>
3. Detection Accuracy:<br>
-Effectiveness of QML in identifying attacks.<br>
-False Positive Rate: Reliability in differentiating real threats from normal traffic.<br>
-Latency Impact: Ensure minimal delay in real-time detection.<br>


---

### Implementation Details
1. Problem Scope<br>
Detect cybersecurity threats in V2I communication using Quantum Machine Learning (QML).<br>
Threats Simulated: DDoS, Message Spoofing, Sybil Attacks.<br>
Data Generation: OMNeT++ simulates normal and malicious V2I communication.<br>

2. Feature Extraction<br>
Extract packet frequency, size, source-destination pairs, and timing from OMNeT++ logs.<br>
Normalize and preprocess data for QML training.<br>

3. QML Model Training<br>
Algorithms: QSVM for binary classification, QNN for multi-class detection.<br>
Framework: Qiskit/PennyLane for quantum circuit-based training.<br>
Evaluation: Accuracy, precision, recall, F1-score.<br>

4. Role of OMNeT++<br>
Simulates normal and attack traffic.<br>
Provides packet-level logs for training data.<br>
Integrates trained QML model for real-time threat detection at RSUs.<br>

5. Detection Framework<br>
Traffic Monitoring: RSUs collect V2I data.<br>
Classification: QML model detects anomalies.<br>
Response: Block threats, send alerts.<br>

6. Performance Evaluation<br>
Metrics: Detection accuracy, false positives, latency, Packet Delivery Ratio (PDR).<br>
Comparison: QML vs. classical ML (SVM, Random Forest).<br>

7. Tools & Resources<br>
OMNeT++ (Simulation), Qiskit/PennyLane (QML), SUMO (Mobility), Python (Feature extraction & integration).<br>

8. Expected Outcomes <br>
High detection accuracy for cyber threats.<br>
Scalability & low latency for real-time applications.<br>


---


### Mapping to Sustainable Development Goals (SDG)
1. SDG 9: Industry, Innovation, and Infrastructure<br>
    Secure Intelligent Transport Systems (ITS): Strengthens V2I communication against cyber threats.<br>
    Resilient Infrastructure: Ensures reliable and safe traffic data exchange.<br>
2. SDG 11: Sustainable Cities and Communities<br>
    Safer Urban Mobility: Reduces accidents and traffic disruptions caused by cyberattacks.<br>
    Efficient Traffic Management: Protects real-time data flow in smart cities.<br>
3. SDG 16: Peace, Justice, and Strong Institutions<br>
    Cybersecurity for Public Safety: Prevents malicious attacks on transport networks.<br>
    Trust in Smart Systems: Ensures integrity and security in intelligent transportation.<br>
4. SDG 13: Climate Action (Indirect Impact)<br>
    Optimized Traffic Flow: Prevents congestion from malicious activities, reducing fuel waste and emissions.<br>


---

### References
https://www.researchgate.net/publication/321375127_Cybersecurity_Attacks_in_Vehicle-to-Infrastructure_V2I_Applications_and_their_Prevention
2.	https://ieeexplore.ieee.org/document/9071073
3.	https://www.mdpi.com/2227-9091/10/5/91
4.	https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/qtc2.12070
5.	https://www.mdpi.com/2624-8921/5/4/86
6.	https://onlinelibrary.wiley.com/doi/10.1155/2022/4280617
