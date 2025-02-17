# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#08 - Secure OTA Updates for Electric Vehicles (EVs)
![](https://img.shields.io/badge/Member-Shriram_Rajaraman-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-14th_Feb_2025-brown) 

### Problem Statement

Modern Electric Vehicles are dependent heavily on embedded software for core functionalities like Battery Management, Motor Control, Advanced Driver Assistance Systems (ADAS), Safety and Infotainment. 
As a result of this dependency, OEMs regularly release updates to fix bugs, add features and enhance security based upon the field issues and consumer feedback. 
Over-the-Air (OTA) updates provides an aspect of convenience in order to distribute these changes without having a physical recall of vehicles or requiring consumers to visit service centres.

Despite their benefits, OTA updates introduce significant cybersecurity challenges:

**i. Risk of Tampering**: An attacker who intercepts or spoofs the update processes could deploy malicious firmware which will effectively lead to compromise of safety-critical systems.

**ii. Battery Constraints**: Large updates or repeated installations can drain the EV’s battery, potentially immobilizing the vehicle.

**iii. Real-Time Operation**: Features like braking and motor control rely on deterministic and time-critical software that must remain uninterrupted during updates.

**iv. Complex Architecture**: Modern EVs have multiple Electronic Control Units (ECUs) with varying resource limitations. Managing secure updates across all these devices adds complexity.

**v. Scalability**: As EV fleets grow, the backend infrastructure may face challenges delivering secure, timely updates to thousands of vehicles simultaneously.

Addressing to these problems is crucial for preserving vehicle safety, consumer trust and overall product reliability in the EV market.

---

### Literature Survey

**1. ISO/SAE 21434 Road Vehicles – Cybersecurity Engineering**: Provides guidelines for incorporating security throughout the lifecycle of automotive systems including OTA updates.

**2. MQTT Protocol & Light-Overhead Communication**: Shin (2024) proposes “MQTree” illustrating a secure OTA protocol that leverages the lightweight MQTT protocol and Merkle trees to verify update integrity.

**3. Trusted Verification of Over-the-Air Software Updates**: Mukherjee (2021) discusses practical approaches to verifying OTA packages on commercial off-the-shelf (COTS) embedded systems highlighting the challenges of limited processing resources.

**4. Security-by-Design for OTA Updates**: Iyieke et al. (2025) emphasize building security into every layer of the update process i.e. from the initial cryptographic signing of firmware to post-update monitoring.

Research also points to delta updates (transmitting only changed portions of firmware) and modular architectures (splitting large software into smaller components) as some useful strategies to reduce bandwidth and battery consumption.


---

### Proposed Work

This project aims to develop and evaluate a secure OTA update mechanism tailored to Electric Vehicles. Key objectives are:

**1. System Architecture Definition:**

Propose an end-to-end framework that covers the OEM backend, communication channel and in-vehicle ECUs. 
Incorporate cryptographic protections such as digital signatures and encryption of update data.

**2. Battery-Aware Update Scheduling**

Designing a mechanism that checks the vehicle’s State of Charge (SOC) before proceeding with large sized updates. 
Avoid update attempts during critical driving states or low battery conditions.

**3. Real-Time Operation Safeguards**

Implement phased updates that update smaller components one at a time.
Provide fail-safe and redundancy strategies so critical systems remain operational if an update stalls or fails.

**4. Hands-On Modelling with MATLAB Simulink**

Use Simulink to model the entire OTA pipeline: from request and download to verification and installation.
Simulate various scenarios (low SOC, network latency, partial update failures) to observe potential impacts on battery consumption and vehicle safety.

By addressing both security and operational aspect of OTA updates, this approach aims to produce a decent solution that can be extended to large EV fleets.


---

### Implementation Details

Below is a high-level plan for implementing the proposed secure OTA system:

***1. Software Tools:***

**(i) MATLAB & Simulink**

Purpose: Create a virtual EV environment (battery model, powertrain, ECU communication flows) and simulate the OTA process.

Usage: Conduct scenario-based tests (e.g. repeated updates under low SOC) and measure performance metrics like time-to-completion.

**(ii) Cryptographic Libraries**

OpenSSL: Generate cryptographic keys, sign firmware images and verify signatures during the simulation.

Role: Secure firmware distribution, ensuring updates remain tamper-proof and authentically sourced. 

***2. Implementation Steps:***

**(i) System Modelling**

Create Simulink blocks for each subsystem: Battery Management System (BMS), motor control, telematics unit and secure OTA manager.

**(ii) Security Layer Integration**

Incorporate hash/checksum verification logic and signature validation into the Simulink model or as external scripts called during simulation.

**(iii) Scenario Testing**

Run simulations under various conditions (e.g. near-empty SOC, tampered firmware) to assess system behaviour.

**(iv) Performance & Security Analysis**

Evaluate how the system responds to replay attacks or unauthorized update attempts.


---


### Mapping to Sustainable Development Goals (SDG)

***SDG 7: Affordable and Clean Energy***

Efficient software updates can help maintain optimal battery performance, extending the driving range and overall energy efficiency of EVs.

***SDG 9: Industry, Innovation, and Infrastructure***

Secure OTA capabilities promote a more innovative automotive industry. 
By reducing the need for physical recalls, manufacturers lower costs, streamline operations and encourage cutting-edge technology adoption.

***SDG 11: Sustainable Cities and Communities***

Widespread adoption of reliable EVs contributes to cleaner transportation in urban environments. Securing OTA updates fosters trust in EV technology, furthering the transition to sustainable mobility.

***SDG 12: Responsible Consumption and Production***

OTA updates reduce waste by eliminating disposable hardware updates and frequent service centre visits, aligning with responsible resource usage.


---

### References

1.	Yunje Shin, “MQTree: Secure OTA Protocol Using MQTT and MerkleTree,” 2024, MDPI.
2.	Anway Mukherjee, “Trusted Verification of Over-the-Air (OTA) Secure Software Updates on COTS Embedded Systems,” 2021, Automotive and Autonomous Vehicle Security.
3.	Victormills Iyieke et al., “An adaptable security-by-design approach for ensuring a secure Over the Air (OTA) update in modern vehicles,” 2025, Elsevier Computers and Security.
4.	MathWorks (MATLAB & Simulink) – https://www.mathworks.com
5.	David Ward, “Automotive Cybersecurity: An Introduction to ISO/ SAE 21434” ,2022, SAE International 
