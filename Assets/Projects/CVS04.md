# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#04 - OTA Update Strategies for SDV using CI/CD
![](https://img.shields.io/badge/Member-Mohit_Joshi-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement

Title: OTA Update Strategies for Software-Defined Vehicles (SDVs)

The arrival of Software-Defined Vehicles (SDVs) has caused a shift in perspective in the automotive industry. Unlike conventional vehicles, which are essentially hardware-driven, SDVs relies significantly on software for crucial tasks. These vehicles provide exceptional flexibility by allowing updates, feature enhancements, and new capabilities to be introduced throughout their lives. Mobility is undergoing a digital transformation towards connected, autonomous, shared, and electric (CASE).
Vehicles will be data driven so with so much data flowing around the vehicle, it has challenge, because it has to manage all that data and on the other hand it’s an opportunity to create valuable Services potentially monetization and so on.
New software methodologies and technologies, and this is where the automotive industry can borrow from other industries such as cell phone development, cloud development and deployment, and use CICD continuous integration continuous delivery methodologies using Jenkins to actually have agile development and deployment of software- defined function in a vehicle.
Cloud Native Technologies:
Cloud native are methodologies, technologies, and tooling, for the development of software application in cloud instances.
This involve methodologies such as CI/CD which allows for continuous Integration continuous deployment of software (eg. cloud instances). This also involve breaking down the software into smaller pieces called "micro services", which can then be more easily developed and deployed using these cloud native tooling and technologies. Cloud technologies like container.
Over the Air Updates (OTA) Updates: 
Wireless updates to vehicles that are secure and authenticated. Similar to the smartphones device which receive update and autonomous vehicles can download remotely with OTA updates. These are many benefits life bug fixes, security patches and new features can be added in the upgrades. OTA updates. OTA Updates are crucial for autonomous vehicles because they enable ongoing system maintenance and updations. 
To ensure user pleasure and safety, Software-Defined Vehicles (SDVs) depend on Over-the-Air (OTA) updates to improve performance, address faults, and add new features. Reducing downtime and preserving smooth operations depend on effective OTA update tactics. Agility is further improved by integrating DevOps principles, which guarantees reliable and timely updates.

---

### Literature Survey

1. Introduction:
   Software-Defined Vehicles (SDVs) rely on Over-the-Air (OTA) updates to enhance functionality, security, and performance. Integrating Continuous Integration/Continuous Deployment (CI/CD) pipelines into OTA updates ensures seamless, automated, and efficient software deployment while reducing downtime and security risks.
  
3. Literature Survey:
   The adoption of OTA updates in SDVs has been extensively studied in recent research. El Jaouhari and Bouvet (2022) discuss the importance of secure firmware updates for IoT devices, highlighting various threats and challenges such as integrity verification, authentication, and efficient update mechanisms. Their work emphasizes the role of trust chains and cryptographic security in OTA updates. Another study on OTA updates in connected vehicles provides a comprehensive survey of methodologies, security concerns, and best practices (Secure Over-the-Air Software Updates in Connected Vehicles, 2022). The research outlines strategies such as modular updates, real-time monitoring, and fail-safe rollback mechanisms. These studies collectively provide insights into the evolution of OTA mechanisms and the growing necessity for integrating CI/CD pipelines to enhance automation and security.

---

### Proposed Work

Proposed work in leturature: 
Proposed Solution:
  To address the challenges identified in the literature, auther propose a secure, automated OTA update mechanism utilizing a CI/CD pipeline integrated with security frameworks like Uptane. This solution includes the following key aspects:
•	Automated Update Validation: Before deployment, software updates undergo rigorous testing using virtual SDV environments.
•	Incremental and Delta Updates: Instead of full firmware replacements, only modified portions of the software are updated, reducing bandwidth and time requirements.
•	Staged Rollouts with Monitoring: The updates are first deployed to a small subset of vehicles before full-scale distribution.
•	Rollback and Recovery Mechanisms: Dual-bank storage ensures that vehicles can revert to a previous version if an update fails.
•	Secure Transmission: Encrypted update packages are distributed through cloud-based IoT platforms.

Tools and Methodology: Approach involves a DevOps-driven CI/CD pipeline for efficient OTA updates. The following tools are used:
•	Jenkins/GitLab CI/CD: Automates build, test, and deployment processes.
•	Uptane Framework: Ensures security by verifying authenticity and preventing man-in-the-middle attacks.
•	AWS IoT Core / Azure IoT Hub: Manages and distributes OTA updates securely.
•	Docker/Kubernetes: Provides containerization for deployment consistency across vehicle platforms.
•	CANoe/DSPACE: Simulates vehicle behavior, ensuring that the updates do not introduce new issues.

The methodology follows these steps:
1.	Code Integration and Testing: Developers commit changes to a version control system like Git, triggering an automated CI/CD pipeline.
2.	Build and Test Automation: The pipeline runs unit tests, integration tests, and security scans.
3.	Packaging and Staging: Updates are packaged into secure containers and deployed to a test fleet for validation.
4.	Incremental Rollout and Monitoring: Updates are gradually released while monitoring vehicle telemetry for any anomalies.
5.	Rollback Strategy: If issues are detected, a rollback mechanism is triggered to restore the last stable version.

Research Review and Identified Gaps:

Despite significant advancements in OTA update strategies for SDVs, several gaps remain in existing research:
Security Challenges: While Uptane provides robust security, real-time threat detection and adaptive security frameworks require further development.
Scalability Issues: Research on CI/CD pipelines for large-scale vehicle networks is limited, especially in handling diverse hardware configurations
Edge Computing for OTA: Few studies explore the use of edge computing to process updates locally within vehicles before cloud-based deployment.
AI-Driven Update Optimization: Predictive AI models for proactive update scheduling remain an emerging field, with limited real-world implementations.

---

### Implementation Details

Steps for Deployment with Jenkins
1.	Installed Jenkins
•	Download and install Jenkins from Jenkins.io.
2.	Set Up pf Jenkins Job
•	Created a pipeline project for the OTA deployment pipeline.
•	Defined project-specific configurations.
3.	Integrate with Source Control
•	Linking Jenkins to GitHub with MATLAB is in progress.

Please find Architecture Diagram of project:
![Architecture_Diagram_v1](https://github.com/user-attachments/assets/080b0225-23aa-4534-9a54-5d00c68125a2)
![Architecture_Diagram_v1](https://github.com/user-attachments/assets/16f74a30-f5f1-4af5-ba55-4bdab512822c)

---


### Mapping to Sustainable Development Goals (SDG)

The integration of OTA update strategies with CI/CD pipelines aligns with several United Nations Sustainable Development Goals (SDGs):
SDG 9: Industry, Innovation, and Infrastructure – Enhancing vehicle connectivity and software efficiency contributes to the advancement of smart transportation infrastructure.
SDG 11: Sustainable Cities and Communities – Reducing vehicle downtime and improving safety through real-time updates ensures more sustainable urban mobility.
SDG 12: Responsible Consumption and Production – Efficient software updates minimize electronic waste by extending the lifecycle of vehicle components.
SDG 13: Climate Action – Optimized vehicle software reduces fuel consumption and emissions, contributing to environmentally friendly transportation.

---

### References

el Jaouhari, S., & Bouvet, E. (2022). Secure firmware Over-The-Air updates for IoT: Survey, challenges, and discussions. In Internet of Things (Netherlands) (Vol. 18). Elsevier B.V. https://doi.org/10.1016/j.iot.2022.100508

Secure Over-the-Air Software Updates in Connected Vehicles: A Survey. (2022).
