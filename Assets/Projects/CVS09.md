# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#09 - DevOps/CICD with OTA
![](https://img.shields.io/badge/Member-Syed_Ameenul-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-TBD-brown) 

### Problem Statement
  In the rapidly evolving automotive industry, software-defined vehicles need reliable and seamless software update deployment systems to ensure customer satisfaction, security, and functionality. However, the traditional method of updating automotive software requires
a lot of manual labor, which increases costs, lengthens downtime, and could delay the delivery of crucial updates.

  Furthermore, the lack of a standardized framework for efficiently deploying and testing new features in automotive ECUs (Electronic Control Units) makes it difficult for Original Equipment Manufacturers (OEMs) and developers to maintain high software quality and responsiveness.



---

### Literature Survey

**Paper-1:** Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices
**Name Of Journal:** IEEE ACCESS
**Summary:** This paper has the details about the best practices for ci/cd implementations, challenges in ci/cd implementation and classification of ci/cd. The best tools required for ci/cd implementation are also mentioned here.
**Research Gap:** The gap found here is lack of security and real world considerations.

**Paper-2:** Scalable Python Tools for Managing OTA Updates in Automotive Systems.
**Name Of Journal:** International Journal of Scientific Research and Management (IJSRM)
**Summary:** By making it possible to remotely update software in cars and provide enhanced functionality, security patches, and bug fixes without the need for physical intervention, over-the-air (OTA) updates have completely transformed the automotive sector. Python offers a promising framework for creating scalable tools to effectively manage OTA updates in automotive systems because of its adaptability and robust ecosystem. This study examines existing research and highlights the benefits, drawbacks, and potential avenues for future study of several Python-based frameworks, tools, and approaches for OTA update implementation and management in automotive systems.
**Research Gap:** Real world considerations.

**Paper-3:** Creation of Continuous Integration Continuous Deployment pipeline using cloud
**Name Of Journal:** 2024 5th International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV)
**Summary:** The document's suggested concept is to use cloud-based tools to build a strong Continuous Integration and Continuous Deployment (CI/CD) pipeline. In the automotive industry, where software-defined vehicles need regular updates and bug fixes, the objective is to expedite the development, testing, and deployment processes for software in vehicles. Software updates will be delivered to vehicles—including ones that are currently in use—in a timely and secure manner thanks to this CI/CD pipeline, which will also automate several development stages and minimize manual interventions.
**Research Gap:** Real world considerations, Security & Practical implementation

**Paper-4:** Investigation And Implementation of Jenkins Pipelines into Raspberry Pi For Automated Control Units
**Name Of Journal:** III International Scientific and Practical Conference
**Summary:** To design and execute a Raspberry Pi-based automated Jenkins pipeline for controlling block units (such as motors, temperature sensors, and other appliances) for contemporary industrial applications. The solution combines the Raspberry Pi with Jenkins, a potent automation tool, to support continuous integration and delivery (CI/CD) procedures and provide flexible and effective control over a variety of devices.
**Research Gap:** Real world considerations & Security.


---

### Proposed Work
  This project explores how DevOps approaches and CI/CD pipelines can be integrated in the automotive industry through the creation and deployment of a feature for cars. The feature is implemented using a Raspberry Pi board, which functions as an Electronic Control Unit (ECU) in a mock car setup. The project incorporates continuous integration to ensure code quality and continuous deployment for a seamless delivery to the Raspberry Pi ECU in compliance with DevOps best practices. This setup simulates real-world automotive scenarios using OTA update mechanisms, highlighting how DevOps enables software-defined vehicles to have scalable, reliable, and quick software updates. This approach demonstrates the benefit of CI/CD pipelines in automotive innovation by promoting improved collaboration between development and operations teams and ensuring adherence

**Tools & Technologies**
**Hardware:** Raspberry Pi and Related Sensors & Actuators.
**Software:** Python, Linux OS{Raspbian Os), Repository (Github), CICD (Github actions), Encryption (Cython), Configuration (YAML), Containerization (Docker).
---

### Implementation Details
![image](https://github.com/user-attachments/assets/aa01f82b-fcdc-4d07-b803-2442f4df1562)



---


### Mapping to Sustainable Development Goals (SDG)


---

### References
[1] MOJTABA SHAHIN, L. Z., MUHAMMAD ALI BABAR. (2017). Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices. IEEE Access.
[2] Ayush Ankit, M. J., K Nimala. (2024). Creation of continuous integration continuous deployment pipeline using cloud. 2024 5th International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV).
[3] Karthikeyan Palanichamy. (2023). Scalable Python Tools for Managing OTA Updates in Automotive Systems. International Journal of Scientific Research and Management (IJSRM).
[4] Volodymyr Havran, Maria Orynchak. (2022). Investigation And Implementation of Jenkins Pipelines into Raspberry Pi For Automated Control Units. Education and science of today: intersectoral issues and development of sciences.
