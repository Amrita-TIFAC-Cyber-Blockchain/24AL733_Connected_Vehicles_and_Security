# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#04 - OTA Update Strategies for SDV using CI/CD
![](https://img.shields.io/badge/Member-Mohit_Joshi-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement

The arrival of Software-Defined Vehicles (SDVs) has caused a shift in perspective in the automotive industry. Unlike conventional vehicles, which are essentially hardware-driven, SDVs relies significantly on software for crucial tasks. These vehicles provide exceptional flexibility by allowing updates, feature enhancements, and new capabilities to be introduced throughout their lives. Mobility is undergoing a digital transformation towards connected, autonomous, shared, and electric (CASE).
Vehicles will be data driven so with so much data flowing around the vehicle, it has challenge, because it has to manage all that data and on the other hand it’s an opportunity to create valuable Services potentially monetization and so on
New software methodologies and technologies, and this is where the automotive industry can borrow from other industries such as cell phone development, cloud development and deployment, and use CICD continuous integration continuous delivery methodologies using Jenkins to actually have agile development and deployment of software- defined function in a vehicle.
Cloud Native Technologies:
Cloud native are methodologies, technologies, and tooling, for the development of software application in cloud instances.
This involve methodologies such as CI/CD which allows for continuous Integration continuous deployment of software (eg. cloud instances). This also involve breaking down the software into smaller pieces called "micro services", which can then be more easily developed and deployed using these cloud native tooling and technologies. Cloud technologies like container.
Over the Air Updates (OTA) Updates: 
Wireless updates to vehicles that are secure and authenticated. Similar to the smartphones device which receive update and autonomous vehicles can download remotely with OTA updates. These are many benefits life bug fixes, security patches and new features can be added in the upgrades. OTA updates. OTA Updates are crucial for autonomous vehicles because they enable ongoing system maintenance and updations. 
To ensure user pleasure and safety, Software-Defined Vehicles (SDVs) depend on Over-the-Air (OTA) updates to improve performance, address faults, and add new features. Reducing downtime and preserving smooth operations depend on effective OTA update tactics. Agility is further improved by integrating DevOps principles, which guarantees reliable and timely updates.

---

### Literature Survey

Below are the few points of Literature survey considered from journals of OTA
Secure OTA Systems:
•	OTA updates involve three main components: backend cloud servers, in-vehicle ECUs, and communication networks (e.g., cellular or Wi-Fi).
•	Uptane Framework: Developed to address automotive-specific security issues, it uses image repositories, director repositories, and time servers to protect against attacks like replay, freeze, and mix-and-match attacks. Uptane ensures authenticity and integrity of updates through cryptographic signatures.
Threat Assessment and Security Testing:
•	Mahmood et al. employed systematic threat modeling approaches like STRIDE and attack trees to identify vulnerabilities in OTA systems. They highlighted key threats such as data flow sniffing, unauthorized downloads, and denial-of-service attack.
•	The use of model-based security testing (MBST) facilitates the automated derivation of security test cases, ensuring robustness against potential exploits.
Cost and Efficiency Considerations:
•	Traditional update mechanisms, like physical recalls, result in high operational costs. OTA technology is projected to save automakers billions by reducing physical intervention and allowing seamless remote updates.
Proposed Solutions in considered Literature:
•	Blockchain-based architectures: Ensure the confidentiality and integrity of updates through distributed ledgers but face challenges like high latency and resource consumption.
•	Cryptographic and steganographic methods: Enhance security by embedding update data within encrypted images, though performance concerns remain due to increased processing times.

---

### Proposed Work

1.	End-to-End CI/CD Pipeline for OTA Updates
•	Developing a CI/CD pipeline using Jenkins to automate the entire OTA update lifecycle, from code integration to deployment in SDVs.
•	Ensure a modular pipeline structure that integrates development, testing, security validation, and deployment phases.
2.	Integration with Version Control Systems
•	Automate update build processes by integrating Jenkins with GitHub or GitLab for real-time tracking of changes in the source code repository.
•	Also will try to enable webhook-triggered builds for continuous development.
3.	Security-First OTA Deployment
•	Embed security testing at every stage of the pipeline:
•	Use one of the strategies for authenticity and integrity checks.
•	Integrate automated penetration testing tools to detect vulnerabilities.
•	Apply multi-factor authentication for Jenkins deployments.
4.	Progressive Rollouts with Jenkins Pipelines
•	Design pipelines to support testing and phased deployments:
•	Roll out updates to a small subset of vehicles first.
•	Implement rollback strategies in case of update failures.
5.	Simulation Environment for Testing
•	Establish a virtual environment using Raspberry Pi devices to simulate SDV software behaviors during updates.
•	Test update scenarios, such as interrupted downloads, version conflicts, and rollback processes, in the CI/CD pipeline.

---

### Implementation Details

Steps for Deployment with Jenkins
1.	Installed Jenkins
•	Download and install Jenkins from Jenkins.io.
2.	Set Up pf Jenkins Job
•	Created a pipeline project for the OTA deployment pipeline.
•	Defined project-specific configurations.
3.	Integrate with Source Control
•	Linking Jenkins to GitHub is in progress.


---


### Mapping to Sustainable Development Goals (SDG)

TBU
---

### References

Mahmood, S., Nguyen, H. N., & Shaikh, S. A. (2022). Systematic threat assessment and security testing of automotive over-the-air (OTA) updates. Vehicular Communications, 35. https://doi.org/10.1016/j.vehcom.2022.100468

el Jaouhari, S., & Bouvet, E. (2022). Secure firmware Over-The-Air updates for IoT: Survey, challenges, and discussions. In Internet of Things (Netherlands) (Vol. 18). Elsevier B.V. https://doi.org/10.1016/j.iot.2022.100508
