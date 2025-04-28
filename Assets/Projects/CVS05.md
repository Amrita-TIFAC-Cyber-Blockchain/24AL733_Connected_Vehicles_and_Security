# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#05 - Authentication Mechanism and Workflow using CISCO Packet Tracer
![](https://img.shields.io/badge/Member-Pathan_Zubair_Khan-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-26_Apr-brown)

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
This section outlines the detailed implementation steps carried out to simulate Vehicle-to-Infrastructure (V2I) authentication mechanisms using CISCO Packet Tracer.
#### Tools Used
CISCO Packet Tracer v8.2+
Wireless LAN (WLAN) protocols
WPA2 PSK Authentication Mechanism
PC (Vehicle) Simulation Nodes
Wireless Routers (for RSU and Cloud Access Points)
Servers (to simulate cloud services)
##### Authentication Flow chart:

<p align="center">
  <img src="https://github.com/user-attachments/assets/bd638764-4c0c-4404-adfd-75b1010d591b" width=600 />
</p


##### Vehicular Authentication Flow:
Step 1: Vehicle initiates authentication with the cloud server.<br>
Step 2: Cloud server verifies the vehicle’s identity using certificate-based authentication.<br>
Step 3: A session key is generated using symmetric cryptography for secure communication.<br>
Step 4: Data integrity is verified for every packet exchanged during the session.<br>


#### Implementation and Simulation
##### Step 1: Initial Setup
Open CISCO Packet Tracer.
Create two PC devices representing two connected vehicles (e.g., Vehicle1 and Vehicle2).
Add a Wireless Router (e.g., RSU-Router).
Add a Server representing the cloud infrastructure.

![](CVS05/images/Screenshot%202025-03-23%20155315.png) <br/> 

##### Step 2: Configure the Wireless Router (RSU)
Set SSID to a custom name (e.g., ConnectedVehiclesNet).
Enable Wireless Security:
Security Mode: WPA2-PSK
Set a strong Pre-Shared Key (Password), e.g., SecureV2X2025
Assign a DHCP Server role to the router to automatically allocate IP addresses to connected vehicles.
Configure basic router settings (LAN IP address, default gateway, etc.).

##### Step 3: Configure Vehicles (PC Devices)
Enable Wireless Interface on each PC (select the appropriate NIC card).
Search for available networks and connect to ConnectedVehiclesNet.
Enter the correct password SecureV2X2025 when prompted.

![ ](CVS05/images/Screenshot%202025-04-26%20151541.png)

##### Network Design in CISCO Packet Tracer:
Create a network model with end devices(HPC in an automotive vehicle), routers, and cloud servers.<br>
Configure secure communication channels using cryptographic protocols.<br>

![](CVS05/images/Screenshot%202025-03-23%20164716.png)

Image showing the established connection.
---


### Mapping to Sustainable Development Goals (SDG)
The security of connected vehicle ecosystems plays a crucial role in building a smarter, safer, and more efficient transportation system. This research contributes to several United Nations Sustainable Development Goals (SDGs) by ensuring secure communication, protecting user data, and supporting innovation in intelligent transportation.


| **SDG** | **Goal Focus** | **Research Contribution** |
|:-------:|:--------------|:---------------------------|
| **SDG 9: Industry, Innovation, and Infrastructure** | Build resilient infrastructure, promote sustainable industrialization, and foster innovation. | Developed a secure authentication framework for Vehicle-to-Cloud (V2C) and Vehicle-to-Everything (V2X) communications. Strengthened cybersecurity of intelligent transport systems. Integrated lightweight cryptographic techniques to promote efficient, scalable security solutions. |
| **SDG 11: Sustainable Cities and Communities** | Make cities inclusive, safe, resilient, and sustainable. | Secured connected vehicle communications to prevent cyber threats like hijacking and data breaches. Enabled safe and efficient real-time data exchange to improve traffic management, reduce congestion, and lower emissions. Supported development of smarter, cleaner urban mobility systems. |
| **SDG 16: Peace, Justice, and Strong Institutions** | Promote peaceful, inclusive societies and build strong institutions. | Ensured data integrity, user privacy, and cybersecurity in smart transportation systems. Strengthened digital governance and regulatory compliance by preventing unauthorized access and identity theft. Fostered trust and transparency in connected vehicle ecosystems. |


By ensuring secure communication in cloud-based connected vehicle ecosystems, this research contributes to a more sustainable, efficient, and resilient transportation network that aligns with global efforts to build smarter cities and protect digital infrastructure.


### Conclusion
The simulation and experimentation conducted using CISCO Packet Tracer successfully demonstrated the importance of authentication mechanisms in securing Vehicle-to-Everything (V2X) communication networks.

Through various scenarios, it was observed that simple security measures, such as WPA2-PSK authentication at the wireless access point level, can effectively prevent unauthorized access attempts and ensure that only trusted entities (vehicles) can participate in the network. Authentication not only validated the legitimacy of each vehicle’s connection request but also served as the first line of defense against common cyber-attacks such as spoofing and man-in-the-middle (MITM) attacks.

The project reinforced several key takeaways:

Authentication is foundational to V2X security: Without verifying the identity of communicating vehicles and infrastructure, the entire network remains vulnerable to malicious actors.

Even basic authentication mechanisms provide significant protection: By simply enforcing password-based access control, many attack vectors are blocked before they can impact critical systems.

Real-world V2X security needs multi-layered defenses: Beyond password authentication, real deployments would benefit from Public Key Infrastructure (PKI), digital certificates, blockchain-based authentication, and cryptographic session management to achieve comprehensive security.

The practical implementation using Packet Tracer also highlighted the simulation tool’s strength in providing a safe, flexible, and educational environment for modeling, testing, and visualizing connected vehicle security architectures before real-world deployment.

In conclusion, secure authentication workflows are not optional but essential for the future of connected and autonomous vehicles. As vehicles become increasingly intelligent and interconnected, building trust in vehicular networks through strong, scalable, and efficient authentication mechanisms will be key to realizing the vision of safe, reliable, and cyber-resilient intelligent transportation systems.


---

### References
- IEEE. (2016). IEEE standard for wireless access in vehicular environments--security services for applications and management messages (IEEE Std 1609.2-2016, Revision of IEEE Std 1609.2-2013). https://doi.org/10.1109/IEEESTD.2016.7426684<br>

- Hasan, S. S. U., Ghani, A., Daud, A., Akbar, H., & Khan, M. F. (2025). A review on secure authentication mechanisms for mobile security. Sensors, 25(3), 700. https://doi.org/10.3390/s25030700<br>

- Mugunthan, S., Sureshkumar, V., Saravanan, P., & Amin, R. (2024). VAuth: Robust lightweight mutual authentication protocol preserving user’s anonymity for VANET with FPGA implementation. IEEE Transactions on Intelligent Transportation Systems, 25(12), 21097–21106. https://doi.org/10.1109/TITS.2024.3461838<br>

- Abbasinezhad-Mood, D., & Ghaemi, H. (2024). Dual-signature blockchain-based key sharing protocol for secure V2V communications in multi-domain IoV environments. IEEE Transactions on Intelligent Transportation Systems, 25(10), 13407–13416. https://doi.org/10.1109/TITS.2024.3410114<br>

- Aljumaili, A., Trabelsi, H., Jerbi, W., & Hazim, R. (2024). Implementing cryptographic mechanisms with IRS for enhancing an internet of vehicles. 2024 IEEE 7th International Conference on Computer and Communication Engineering Technology (CCET), Beijing, China, 185–194. https://doi.org/10.1109/CCET62233.2024.10837706

