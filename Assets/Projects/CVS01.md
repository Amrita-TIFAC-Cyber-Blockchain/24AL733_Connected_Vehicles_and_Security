# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#01 - Implementation of CAN-FD Communication Protocols with Secure Communication Channel
![](https://img.shields.io/badge/Member-Amit_Kumar_Nandi-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-17th_Feb_2025-brown) 

### Problem Statement
  In the Automotive domain, Controller Area Network (CAN) is one of the common and popular communication protocols, which is known for it’s simplicity and ease of implementation. It offers better data speed as compared to LIN. However, with the advancement of Automotive domain, more and more features are getting added, which requires the transfer of vast amounts of data collected through various sensors like RADAR, LIDAR, Ultrasonic Sensor, high-definition Cameras etc. To handle this enormous amount of data, a high-speed data transmission protocol is essential. The traditional CAN having data speed up to 1Mbps and payload of 8 bytes, is inefficient for handling the demands of modern ADAS applications. To accommodate this high-speed data, an improved version of classical CAN, known as Controller Area Network Flexible Data-Rate has been introduced which offers data speed of 10 Mbps with payload capacity of 64 bytes. 
  
Moreover, as neither CAN nor CAN-FD protocol is inherently secured, they are becoming vulnerable to data breaches, tampering, and unauthorized access. 
  
  Therefore, there is a need to implement CAN-FD communication protocol and incorporate security measures like lightweight Encryption protocol and Hashing Algorithm. Also, it's necessary to evaluate the performance of CAN-FD over classical CAN in terms of latency and bandwidth.

 
---

### Literature Survey

Paper [1] discusses the evolution of in-vehicle communication protocols, emphasizing the need for improvements in terms of data speed and payload capacity to meet the increasing demands of modern Advanced Driver Assistance Systems (ADAS). 
The paper gives an in-depth comparative analysis of Classical CAN and CAN-FD protocols, where it has been discussed that classical CAN supports a payload up to 8 bytes, making it unsuitable for heavy data from sensors like RADAR, LIDAR, and high-definition cameras. To overcome this, CAN-FD was introduced, with its support for a higher payload along with data rate and bit rate flexibility; hence, it is suitable for data streaming applications that have a high speed.
            The study demonstrates that with the introduction of CAN-FD, throughput can be increased up to 70% of the data rate and also latency and jitter can be reduced significantly. The paper also talks about the absence of security measures in the CAN or CAN-FD communication protocol which is making them vulnerable to common attacks such as spoofing, tampering, and eavesdropping.

Paper [2] provides a detailed analysis of the performance improvements of CAN-FD over CAN. As CAN supports a data speed of 1 Mbps, it struggles to handle high-speed data for modern automotive applications. CAN-FD addresses the limitation by introducing higher data rates, up to 10 Mbps.
            The study compares both the protocols using real-world and simulated messages. The result shows that CAN-FD reduces bandwidth utilization, message overhead, and worst-case transmission time (WCTT) significantly. It has been shown that at a 500-kbps arbitration rate and a 5 Mbps data rate, CAN-FD reduces WCTT by up to 10.88 times compared to CAN. Also, CAN-FD achieves 2.91 times lower bandwidth utilization as compared to classical CAN.
            Although CAN-FD solves the problem of lower data rate and lower bandwidth, but at the same time it increases challenges such as increased susceptibility to noise at higher bit rates, and the need for enhanced hardware is noted.
	    
Paper [3] describes the evolution of classical CAN protocol and introduction of newer CAN-FD protocol, capable of handling higher data rates and larger payload. Despite this advancement CAN-FD lacks inherent security measures, making them vulnerable to attackers. 
	To solve the problem, the paper suggests AES-128 symmetric encryption algorithm. In this way, AES-128 encrypts the message and ensures that the sensitive data cannot be intercepted or understood by any unauthorized entities. To ensure the authenticity the paper proposed SHA-256 Hashing algorithm, where the Hash value of the encrypted message is calculated and appended with the original message. To ensure data is not tampered in between the Hash value is calculated again and verified.
	The implementation takes advantage of CAN-FD’s larger payload capacity, which allows to accommodate both the Hash value and encrypted value. The paper shows that calculation of these Hash Value and Cipher text has little impact on real-time performance but it enhances data security up to a larger instance.

Paper [4] addresses the security issues of CAN-FD protocol by incorporating different algorithms like lightweight encryption algorithm, digital signature-based authentication mechanism, to ensure confidentiality and authenticity. The paper integrates additional security measures by using Invasion Detection system (IDS), to monitor the network traffic for anomalies, such as unexpected message frequencies or spoofed packets. If there is any unusual behaviour detected IDS system provides defensive actions, such as isolating compromised nodes or alerting the system to suspicious activities. 

  At the receiving end, the receiver takes the message first to decrypt it and verifies the digital signature for the legitimate sender. On the other hand, the IDS system is always running, looking for any anomaly in the network. 
Only if there are no observations of unusual behaviour and the digital signature passes verification is the message allowed to proceed for execution of the intended operation. And after execution of the message at the receiver side an acknowledgement is sent back to the sender over the secure channel. 
	The paper, therefore, shows a multi-layered approach to solve the security issue of CAN-FD, allowing for the methods of encryption, authentication, and anomaly detection mechanisms to be prectically integrated.

---

### Proposed Work

1.	To implement the communication between TCU and BCM using CAN protocol.
2.	Implement the communication between TCU and BCM using the advanced CAN-FD protocol.
3.	Simulate the communication between the TCU and the BCM using the CANoe tool.
4.	Integrate a simple Encryption Algorithm and Hashing Algorithm to secure the communication between different nodes or ECUs.
5.	Provide a comparative study highlighting the strengths and limitations of both protocols in the selected use case. Also the advantages of securing the communication in real world scenario.



---

### Implementation Details

This project focusses on the implementation of a part of Remote Door Lock/Unlock Request. In this use case, the user initiates the remote door lock/unlock request via Mobile App, which communicates with the offboard cloud environment, where the request is verified and forwarded to the onboard ECU, using SOME/IP protocol. Once the request from the offboard server reaches the vehicle, Telematics Control Unit (TCU) performs precondition checks. Upon successful verification of the preconditions, the request is forwarded to the Body Control Module (BCM). The request from the TCU to BCM is sent via CAN protocol. The proposed work aims to establish this CAN communication, between TCU and BCM keeping security aspects in mind. 

The methodology involves several steps, including system design, database file (.dbc) creation, protocol implementation, performance analysis, etc. The following steps outline the detailed process required to design and implement the proposed system: 

•**System Architecture:**  The System architecture is designed to establish a secure communication channel between TCU and BCM.  The operation starts when TCU triggers the request and after checking for the preconditions it sent the request to BCM, which executes the lock/unlock command.

•**Creation of CAN Database File:** The CAN or CAN-FD protocol requires one .dbc (database file), which contains the details about arbitration IDs, data payloads, signal mappings, decoding mechanisms etc. This .dbc file can be created by using CANDB Editor, which then needs to be imported into the CANoE simulation tool.

•**CAN and CAN-FD Implementation:** The implementation of CAN and CAN-FD communication models includes designing communication nodes in the CANoE simulation tool. Where one node (i.e. TCU) is configured to send the Lock, Unlock request and other node i.e. BCM is configured to receive those requests and execute that. 

•**CAPL Scripting:** The behaviour of the TCU and BCM during simulation will be defined through CAPL scripting.  This script manages sending or receiving messages with the correct arbitration ID, payload and Control bits. 

•**Performance Analysis:** Once the communication between TCU and BCM is established using both CAN and CAN-FD protocols, a comparative study of both protocols will be performed. The CAPL scripting supported by CANoE, will be used to write code that will be used to measure the delay and latency of the messages. 

•**Security Integration:** To ensure the confidentiality of data, basic Encryption protocol such as XOR encryption or RC4 encryption will be implemented, considering the computational resources in mind. Some external libraries need to be imported as CAPL does not natively support any encryption algorithm. 

 To ensure integrity, different hashing algorithms such as MD5, SHA-256 can be incorporated. This hashing algorithm enhances the security, but at the same time it needs a lot of computational power, essentially needing high-end processor. 
 Keeping all these into consideration, some basic function or logical operation (like XOR operation, OR operation) can also be performed to generate the Hash value as an alternative in this project. 
 After that, the calculated Hash value will be appended to the original message before transmission. Similarly, at the receiving end, the Hash value will be calculated again, and if both the values match, then the integrity is proved, and it ensures data has not been tampered with in between. 
 And if the values do not match, the receiver discards the message to prevent unauthorized access. 
 
•**Response from the BCM:** After verifying the confidentiality and integrity of the message, the BCM will check for the ‘DoorStatus’ and execute the request from the TCU (essentially from Mobile App). If the vehicle is successfully unlocked, the notification will be sent back to the TCU and the use case ends here.


---

![Screenshot 2025-02-28 200612](https://github.com/user-attachments/assets/565da2a5-94c4-4fd9-8f6d-a120fb35e660)

### Mapping to Sustainable Development Goals (SDG)

This project aligns with the following Sustainable Development Goals:

• SDG 9: Industry, Innovation, and Infrastructure : Enhances automotive communication protocols by implementing CAN-FD, which improves data transmission speed and efficiency. 
		Strengthening vehicle cybersecurity by integrating encryption and authentication mechanisms, ensuring safe and secure communication between electronic control units (ECUs). 

• SDG 11: Sustainable Cities and Communities: Supporting intelligent and connected transportation by ensuring fast and secure data transmission, which is essential for smart city initiatives. Also, contributing to reliable and secure mobility solutions, which are key components of future urban transportation networks.

• SDG 13: Climate Action: Using CAN-FD instead of classical CAN increases the actual useful data-to-transmitted data ratio (efficiency), allowing larger amounts of data to be sent with less overhead. Since more data is transmitted per message frame, the number of frames needed for communication is reduced, leading to lower power consumption in electronic control units (ECUs), which helps to minimize energy usage in vehicle networks.



---

### References

1.	Dhanush M S , Ananthakrinshna T,  'Enhancing In-Vehicle Networks with CAN-FD: A study of Protocol Improvements over Classical CAN', International Conference on Electronics.
2.	Yong Xie, Pengcheng Huang, Wei Liang, 'Comparison between CAN and CAN FD: A Quantified Approach', IEEE International Symposium on Parallel and Distributed Processing.
3.	Farag Mohamed E.Lagnf, Subramaniam Ganesan , ‘Securing CAN FD by implementing AES-128, SHA256, and Message Counter based on FPGA’, IEEE International Conference on Electro Information Technology (EIT).
4.	Jingyi Jia , Yujing Wu, Yinan Xu, ‘Intelligent Connected Vehicle CAN-FD Bus Network Security Protocol’, International Conference on Mobile Internet, Cloud Computing and Information Security (MICCIS).


[Implementation of CAN-FD Communication Protocols with Secure Communication.pdf](https://github.com/user-attachments/files/18924349/Implementation.of.CAN-FD.Communication.Protocols.with.Secure.Communication.pdf)
