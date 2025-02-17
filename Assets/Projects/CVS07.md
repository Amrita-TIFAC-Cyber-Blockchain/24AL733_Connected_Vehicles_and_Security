# 24AL733 - Connected Vehicles and Security

![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange)

## CVS#07 - Role of 5G in Vehicle-to-Everything (V2X) Communication

![](https://img.shields.io/badge/Member-Shashank_R-gold) <br/>
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/>
![](https://img.shields.io/badge/Reviewed-17th_Feb_2025-brown)

### Problem Statement

The integration of 5G technology into Vehicle-to-Everything (V2X) communication is revolutionizing the landscape of connected and automated mobility. Traditional systems, such as Dedicated Short-Range Communication (DSRC) and LTE-based networks, have struggled with limitations in scalability, latency, and security, which hinder their ability to meet the growing demands of modern V2X applications. As vehicular networks become more data-intensive and time-sensitive, these systems fail to provide the required efficiency, particularly in high-density urban environments where communication channels are easily congested. 5G addresses these challenges with its advanced capabilities, offering low-latency, high-bandwidth, and highly reliable communication solutions that enable seamless data exchange and support real-time decision-making in critical scenarios.

---

### Literature Survey

1. 5G MEC-Enabled Vehicle Discovery Service for Streaming-Based CAM Applications
    * Authors: Gorka Velez, Josu Perez, Angel Martin
    * Source: Multimedia Tools and Applications, 2022
    * Focus: This study highlights the use of Multi-access Edge Computing (MEC)  to optimize vehicle discovery in connected and automated mobility (CAM) applications. The proposed Vehicle Discovery Service (VDS) employs a centralized MEC system to efficiently identify and connect vehicles within a geographical Region of Interest (ROI). This avoids the inefficiencies of traditional broadcast-based discovery methods, particularly in dense urban environments.
    * Contributions:
      * Developed a novel architecture using WebRTC for low-latency streaming.
      * Evaluated spatial accuracy and end-to-end latency for applications like See-Through video streaming.
      * Demonstrated scalability and reduced communication delays using real-world vehicular datasets.
  
2. A Group-Based Multicast Service Authentication and Data Transmission Scheme for 5G-V2X
   * Authors: Ruhui Ma, Jin Cao, Yinghui Zhang, et al.
   * Source: IEEE Transactions on Intelligent Transportation Systems, 2022
   * Focus: This paper introduces a secure and efficient group-based authentication scheme tailored for 5G-V2X multicast services. The model ensures seamless and secure data transmission for a large number of vehicles while addressing issues such as signaling congestion and mobility challenges.
   * Contributions:
     * Introduced a group authentication process to reduce signaling overhead during multicast service access.
     * Proposed dual-key technology for secure and efficient key distribution.
     * Formal verification showed robustness against protocol attacks, ensuring data privacy, anonymity, and unlinkability.
     * Demonstrated superior computational and communication efficiency compared to existing methods.

3. On 5G-V2X Use Cases and Enabling Technologies: A Comprehensive Survey
   * Authors: Ahmad Alalewi, Iyad Dayoub, Soumaya Cherkaoui
   * Source: IEEE Access, 2021
   * Focus: This survey comprehensively reviews V2X use cases, 5G enabling technologies, and their applications in vehicular communication. It maps the requirements of V2X applications to 5G capabilities, such as ultra-reliable low-latency communication (URLLC) and massive machine-type communication (mMTC).
   * Contributions:
     * Provided a detailed classification of V2X use cases into safety, traffic efficiency, and infotainment.
     * Discussed enabling technologies like edge computing, network slicing, full-duplex communication, and artificial intelligence.
     * Highlighted challenges such as resource management, interoperability, and integration of advanced communication protocols.
     * Identified research gaps, including low-latency communication for safety-critical scenarios and efficient spectrum utilization.
4. Toward 5G Edge Computing for Enabling Autonomous Aerial Vehicles
   * Authors: Gerasimos Damigos, Tore Lindgren, George Nikolakopoulos
   * Source: IEEE Access, 2023
   * Focus: This paper explores the use of 5G-enabled edge computing to support time-critical control operations in unmanned aerial vehicles (UAVs). The study emphasizes the role of edge servers in reducing latency for closed-loop control systems, using real-world 5G networks.
   * Contributions:
     * Proposed a 5G-enabled architecture for offloading computationally intensive tasks to edge servers.
     * Evaluated round-trip latency, jitter, and system behavior in high-load scenarios.
     * Experimentally validated the impact of 5G edge computing on UAV performance, including trajectory tracking and obstacle navigation.
     * Identified unexplored areas for optimization, such as path planning and network resource allocation.

---

### Proposed Work

Based on the insights from the literature, the proposed work aims to design and implement a comprehensive 5G-enabled framework for V2X communication. This framework will address the challenges of low-latency data processing, secure communication, and efficient resource utilization in dense and dynamic vehicular environments. The proposed work also integrates real-world testing and simulation to validate the system's performance and reliability.

---

### Implementation Details

The development and optimization of 5G-V2X systems rely heavily on advanced simulation and testing tools. Traffic simulation platforms like SUMO (Simulation of Urban Mobility) integrate vehicular movement dynamics with communication models, enabling researchers to evaluate network performance under realistic scenarios. Network simulators such as OMNeT++ and NS-3 analyze latency, throughput, and signal interference, providing insights into the impact of traffic loads and mobility patterns on communication efficiency.

---

### Mapping to Sustainable Development Goals (SDG)

The proposed 5G-enabled V2X framework aligns with multiple SDGs by addressing critical issues such as road safety, urban sustainability, climate change, and technological innovation. By integrating cutting-edge communication technologies with sustainable practices, this framework contributes to the creation of a smarter, safer, and greener transportation ecosystem. It also establishes a foundation for global partnerships and knowledge exchange, driving progress toward achieving the SDGs

---

### References

[1]. 5G MEC-Enabled Vehicle Discovery Service for Streaming-Based CAM Applications

[2]. A Group-Based Multicast Service Authentication and Data Transmission Scheme for 5G-V2X

[3]. On 5G-V2X Use Cases and Enabling Technologies: A Comprehensive Survey

[4]. Toward 5G Edge Computing for Enabling Autonomous Aerial Vehicles

---
