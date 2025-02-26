# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#04 - OTA Update Strategies for SDV using CI/CD
![](https://img.shields.io/badge/Member-Mohit_Joshi-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement

Title: OTA Update Strategies for Software-Defined Vehicles (SDVs)

-SDVs differ from traditional hardware-driven vehicles by relying on software for critical functions. This allows for continuous updates, feature enhancements, and digital transformation towards Connected, Autonomous, Shared, and Electric (CASE) mobility.
-With vast amounts of data being generated, SDVs must efficiently manage and secure it while also leveraging opportunities for service monetization. The automotive industry is adopting software methodologies from cloud and mobile development, using CI/CD pipelines for agile software deployment.
-Cloud-native development enables breaking down software into microservices, making deployment more efficient. CI/CD pipelines (e.g., Jenkins) automate the integration and deployment of vehicle software, enhancing flexibility and scalability through containerization and cloud-based solutions.
-OTA updates provide secure, remote software enhancements, including bug fixes, security patches, and new features, ensuring ongoing system maintenance. Integrating DevOps principles enhances agility, ensuring timely, reliable, and seamless software updates for SDVs.

---

### Literature Survey

1. Introduction:
   Software-Defined Vehicles (SDVs) rely on Over-the-Air (OTA) updates to enhance functionality, security, and performance. Integrating Continuous Integration/Continuous Deployment (CI/CD) pipelines into OTA updates ensures seamless, automated, and efficient software deployment while reducing downtime and security risks.
  
2. Literature Survey:
-The adoption of OTA updates in SDVs has been extensively studied in recent research. El Jaouhari and Bouvet (2022) discuss the importance of secure firmware updates for IoT devices, highlighting various threats and challenges such as integrity verification, authentication, and efficient update mechanisms. Their work emphasizes the role of trust chains and cryptographic security in OTA updates.
-Another study on OTA updates in connected vehicles provides a comprehensive survey of methodologies, security concerns, and best practices (Secure Over-the-Air Software Updates in Connected Vehicles, 2022). The research outlines strategies such as modular updates, real-time monitoring, and fail-safe rollback mechanisms. These studies collectively provide insights into the evolution of OTA mechanisms and the growing necessity for integrating CI/CD pipelines to enhance automation and security.

---

### Proposed Work
 
Proposed Solution:
  To address the challenges identified in the literature, the auther propose a secure, automated OTA update mechanism utilizing a CI/CD pipeline integrated with security frameworks like Uptane e.i., Mender.io. This solution includes the following key aspects:
•	Automated Update Validation: Before deployment, software updates undergo rigorous testing using virtual SDV environments.
•	Incremental and Delta Updates: Instead of full firmware replacements, only modified portions of the software are updated, reducing bandwidth and time requirements.
•	Staged Rollouts with Monitoring: The updates are first deployed to a small subset of vehicles before full-scale distribution.
•	Rollback and Recovery Mechanisms: Dual-bank storage ensures that vehicles can revert to a previous version if an update fails.
•	Secure Transmission: Encrypted update packages are distributed through cloud-based IoT platforms.

The methodology follows these steps:
•	Code Integration and Testing: Developers commit changes to a version control system like Git, triggering an automated CI/CD pipeline.
•	Build and Test Automation: The pipeline runs unit tests, integration tests, and security scans.
•	Packaging and Staging: Updates are packaged into secure containers and deployed to a test fleet for validation.
•	Incremental Rollout and Monitoring: Updates are gradually released while monitoring vehicle telemetry for any anomalies.
•	Rollback Strategy: If issues are detected, a rollback mechanism is triggered to restore the last stable version.

Research Review and Identified Gaps:

Despite significant advancements in OTA update strategies for SDVs, several gaps remain in existing research:
•	Security Challenges: While Uptane provides robust security, real-time threat detection and adaptive security frameworks require further development.
•	Scalability Issues: Research on CI/CD pipelines for large-scale vehicle networks is limited, especially in handling diverse hardware configurations
•	Edge Computing for OTA: Few studies explore the use of edge computing to process updates locally within vehicles before cloud-based deployment.
•	AI-Driven Update Optimization: Predictive AI models for proactive update scheduling remain an emerging field, with limited real-world implementations.

**Tools and Technologies:** Approach involves a DevOps-driven CI/CD pipeline for efficient OTA updates. The following tools are used:
•	Jenkins CI/CD: Automates build, test, and deployment processes.
•	Mender.io: Mender.io – An open-source OTA update management platform.
•	AWS IoT Core / Azure IoT Hub: Manages and distributes OTA updates securely.
•	Docker: Provides containerization for deployment consistency across vehicle platforms.
•	Embedded Linux – For running OTA clients on vehicle ECUs.
•	VMware/VirtualBox – For virtualized test environments before deployment.

Please find the Architecture Diagram of the project:

![Architecture_Diagram_v1](https://github.com/user-attachments/assets/16f74a30-f5f1-4af5-ba55-4bdab512822c)

---

### Implementation Details

Steps for Deployment with Jenkins
1.	Installed Jenkins
•	Download and install Jenkins from Jenkins.io.
2.	Set Up Jenkins Job
•	Created a pipeline project for the OTA deployment pipeline.
•	Defined project-specific configurations.
3.	Integrate with Source Control
•	Linking Jenkins to GitHub with MATLAB is in progress.
4. Virtual box creation in Ubuntu is in progress 

---


### Mapping to Sustainable Development Goals (SDG)

The integration of OTA update strategies with CI/CD pipelines aligns with several United Nations Sustainable Development Goals (SDGs):
-SDG 9: Industry, Innovation, and Infrastructure – Our project leverages CI/CD-driven OTA updates to improve vehicle software management, connectivity, and automation, fostering innovation in smart transportation infrastructure. By ensuring seamless and secure software deployment, it enhances vehicle performance and reliability, supporting the evolution of next-generation mobility solutions.

-SDG 11: Sustainable Cities and Communities – The integration of OTA updates with DevOps methodologies ensures real-time system enhancements, reducing vehicle downtime and improving road safety. By keeping SDVs updated with the latest security patches and performance improvements, our project helps create a more efficient, safer, and sustainable urban transportation ecosystem.

-SDG 12: Responsible Consumption and Production – Our approach to incremental OTA updates ensures that only necessary software components are updated, reducing the need for frequent hardware upgrades. This extends the lifecycle of electronic components in vehicles, minimizing electronic waste and promoting sustainable automotive production and consumption

-SDG 13: Climate Action – Optimized vehicle software reduces fuel consumption and emissions, contributing to environmentally friendly transportation.

---

### References

el Jaouhari, S., & Bouvet, E. (2022). Secure firmware Over-The-Air updates for IoT: Survey, challenges, and discussions. In Internet of Things (Netherlands) (Vol. 18). Elsevier B.V. https://doi.org/10.1016/j.iot.2022.100508

Secure Over-the-Air Software Updates in Connected Vehicles: A Survey. (2022) - (TBD)
