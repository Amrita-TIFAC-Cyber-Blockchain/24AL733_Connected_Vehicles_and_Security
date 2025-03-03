# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#05 - Authentication Mechanism and Workflow using CISCO Packet Tracer
![](https://img.shields.io/badge/Member-Pathan_Zubair_Khan-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement
<div style="text-align: justify">
As connected vehicle ecosystems continue to evolve, secure and reliable Vehicle-to-Cloud (V2C) and Vehicle-to-Everything (V2X) communication is essential for enabling real-time data exchange and enhancing smart mobility services. However, these communication systems are highly vulnerable to cyber threats, including unauthorized access, data breaches, and identity spoofing, which can compromise both safety and privacy. To address these challenges, robust mutual authentication mechanisms are required to ensure secure access control, data integrity, and trust in vehicular networks. Anyhow, the security of these communications is paramount and as a necessary result, authentication mechanisms to prevent unauthorized access and ensure data integrity. This project work focuses on Authentication Mechanism and Workflow of cloud-based connected vehicle ecosystems and will be demonstrated by a simulation with the help of CISCO Packet Tracer. 
</div>

---

### Literature Survey

With the growing adoption of Vehicle-to-Cloud (V2C) and Vehicle-to-Everything (V2X) communication, secure authentication mechanisms are critical to preventing cyber threats such as unauthorized access, data tampering, and replay attacks. Various authentication strategies have been proposed to enhance security in connected vehicle ecosystems.
##### Certificate-Based Authentication (PKI)
The IEEE 1609.2 Standard outlines a Public Key Infrastructure (PKI)-based authentication framework for securing vehicular communication through digital certificates, encryption, and message integrity mechanisms (IEEE, 2016).
##### Symmetric and Lightweight Authentication protocols
Recent studies have explored lightweight authentication mechanisms to reduce computational overhead while maintaining security. Hasan et al. (2025) reviewed various mobile security authentication mechanisms, emphasizing the importance of low-latency cryptographic approaches tailored for resource-constrained vehicular systems. Mugunthan et al. (2024) proposed VAuth, a lightweight mutual authentication protocol designed for VANETs, ensuring user anonymity while being efficient enough for FPGA-based implementations.

##### Cloud-Based Authentication
Centralized cloud servers authenticate vehicles and manage session keys. Abbasinezhad-Mood et al. (2024) introduced a dual-signature blockchain-based key-sharing protocol for secure vehicle-to-vehicle (V2V) authentication. This protocol is tailored for multi-domain Internet of Vehicles (IoV) environments, addressing security risks in cross-domain authentication scenarios.

---

### Proposed Work
This project work is to design and demonstrate an efficient authentication mechanism workflow that resembles a cloud-based connected vehicle ecosystem. The key objectives are to:

Develop a secure mutual authentication mechanism that ensures low latency and scalability for V2C and V2X systems.
Create a workflow model for managing authentication between vehicles, cloud servers, and edge devices.
Simulate and demonstrate the mechanism using CISCO Packet Tracer, enabling practical evaluation and validation.

---

### Implementation Details
#### Development and Simulation Tools
Simulation Platform: CISCO Packet Tracer will be used to simulate the communication workflows between vehicles and the cloud.
Cryptographic Components: Lightweight cryptography (ECC, AES) and hash-based integrity checks (HMAC) will be incorporated into the simulation.
Protocol Stack: Implementation of key protocols such as HTTPS, MQTT, or CoAP for secure communication.
#### Workflow Simulation
##### Network Design in CISCO Packet Tracer:
Create a network model with end devices(HPC in an automotive vehicle), routers, and cloud servers.<br>
Configure secure communication channels using cryptographic protocols.<br>

##### Authentication Flow chart:

![image](https://github.com/user-attachments/assets/bd638764-4c0c-4404-adfd-75b1010d591b)


##### Vehicular Authentication Flow:
Step 1: Vehicle initiates authentication with the cloud server.<br>
Step 2: Cloud server verifies the vehicle’s identity using certificate-based authentication.<br>
Step 3: A session key is generated using symmetric cryptography for secure communication.<br>
Step 4: Data integrity is verified for every packet exchanged during the session.<br>


---


### Mapping to Sustainable Development Goals (SDG)
The security of connected vehicle ecosystems plays a crucial role in building a smarter, safer, and more efficient transportation system. This research contributes to several United Nations Sustainable Development Goals (SDGs) by ensuring secure communication, protecting user data, and supporting innovation in intelligent transportation.

SDG 9 (Industry, Innovation, and Infrastructure) focuses on building resilient and sustainable infrastructure. By developing a secure authentication framework for Vehicle-to-Cloud (V2C) and Vehicle-to-Everything (V2X) communication, this research helps strengthen the security of intelligent transportation systems. A reliable authentication mechanism ensures trustworthy data exchange, preventing cyber threats and unauthorized access. Additionally, integrating lightweight cryptographic techniques makes these security solutions efficient and scalable, fostering innovation in autonomous driving, smart mobility, and intelligent traffic management.

SDG 11 (Sustainable Cities and Communities) emphasizes the need for safe and efficient urban mobility. Cyber threats such as vehicle hijacking, data breaches, and unauthorized access pose serious risks to smart transportation systems. A secure authentication mechanism helps mitigate these risks, making connected vehicles and smart city mobility solutions safer and more resilient. Furthermore, secure real-time data exchange improves traffic management, reduces congestion, and lowers carbon emissions, contributing to a cleaner and more sustainable urban environment.

SDG 16 (Peace, Justice, and Strong Institutions) highlights the importance of strong digital governance and cybersecurity. The proposed authentication framework ensures data integrity, privacy, and protection against cyber threats, reinforcing trust in connected vehicle ecosystems. By preventing digital identity theft and unauthorized system access, this research supports transparent and secure smart mobility governance. Strengthening cybersecurity in transportation systems also contributes to better regulatory compliance and the development of strong digital security policies.

By ensuring secure communication in cloud-based connected vehicle ecosystems, this research contributes to a more sustainable, efficient, and resilient transportation network that aligns with global efforts to build smarter cities and protect digital infrastructure.

---

### References
IEEE. (2016). IEEE standard for wireless access in vehicular environments--security services for applications and management messages (IEEE Std 1609.2-2016, Revision of IEEE Std 1609.2-2013). https://doi.org/10.1109/IEEESTD.2016.7426684<br>

Hasan, S. S. U., Ghani, A., Daud, A., Akbar, H., & Khan, M. F. (2025). A review on secure authentication mechanisms for mobile security. Sensors, 25(3), 700. https://doi.org/10.3390/s25030700<br>

Mugunthan, S., Sureshkumar, V., Saravanan, P., & Amin, R. (2024). VAuth: Robust lightweight mutual authentication protocol preserving user’s anonymity for VANET with FPGA implementation. IEEE Transactions on Intelligent Transportation Systems, 25(12), 21097–21106. https://doi.org/10.1109/TITS.2024.3461838<br>

Abbasinezhad-Mood, D., & Ghaemi, H. (2024). Dual-signature blockchain-based key sharing protocol for secure V2V communications in multi-domain IoV environments. IEEE Transactions on Intelligent Transportation Systems, 25(10), 13407–13416. https://doi.org/10.1109/TITS.2024.3410114<br>

Aljumaili, A., Trabelsi, H., Jerbi, W., & Hazim, R. (2024). Implementing cryptographic mechanisms with IRS for enhancing an internet of vehicles. 2024 IEEE 7th International Conference on Computer and Communication Engineering Technology (CCET), Beijing, China, 185–194. https://doi.org/10.1109/CCET62233.2024.10837706

