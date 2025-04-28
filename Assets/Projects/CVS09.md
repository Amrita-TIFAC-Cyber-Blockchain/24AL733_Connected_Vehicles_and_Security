# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>
![](https://img.shields.io/badge/Lecture-3-orange) ![](https://img.shields.io/badge/Credits-3-orange) 

## CVS#09 - DevOps/CICD with OTA
![](https://img.shields.io/badge/Member-Syed_Ameenul-gold) <br/> 
![](https://img.shields.io/badge/SDG-TBD-darkgreen) <br/> 
![](https://img.shields.io/badge/Reviewed-26_Apr-brown) 

### Problem Statement
  In the rapidly evolving automotive industry, software-defined vehicles need reliable and seamless software update deployment systems to ensure customer satisfaction, security, and functionality. However, the traditional method of updating automotive software requires
a lot of manual labor, which increases costs, lengthens downtime, and could delay the delivery of crucial updates.

  Furthermore, the lack of a standardized framework for efficiently deploying and testing new features in automotive ECUs (Electronic Control Units) makes it difficult for Original Equipment Manufacturers (OEMs) and developers to maintain high software quality and responsiveness.

---

### Literature Survey

**Paper-1:** Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices.<br/>
**Name Of Journal:** IEEE ACCESS.<br/>
**Summary:** This paper has the details about the best practices for ci/cd implementations, challenges in ci/cd implementation and classification of ci/cd. The best tools required for ci/cd implementation are also mentioned here.<br/>
**Research Gap:** The gap found here is lack of security and real world considerations.<br/>

**Paper-2:** Scalable Python Tools for Managing OTA Updates in Automotive Systems.<br/>
**Name Of Journal:** International Journal of Scientific Research and Management (IJSRM).<br/>
**Summary:** By making it possible to remotely update software in cars and provide enhanced functionality, security patches, and bug fixes without the need for physical intervention, over-the-air (OTA) updates have completely transformed the automotive sector. Python offers a promising framework for creating scalable tools to effectively manage OTA updates in automotive systems because of its adaptability and robust ecosystem. This study examines existing research and highlights the benefits, drawbacks, and potential avenues for future study of several Python-based frameworks, tools, and approaches for OTA update implementation and management in automotive systems.<br/>
**Research Gap:** Real world considerations.<br/>

**Paper-3:** Creation of Continuous Integration Continuous Deployment pipeline using cloud<br/>
**Name Of Journal:** 2024 5th International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV).<br/>
**Summary:** The document's suggested concept is to use cloud-based tools to build a strong Continuous Integration and Continuous Deployment (CI/CD) pipeline. In the automotive industry, where software-defined vehicles need regular updates and bug fixes, the objective is to expedite the development, testing, and deployment processes for software in vehicles. Software updates will be delivered to vehicles—including ones that are currently in use—in a timely and secure manner thanks to this CI/CD pipeline, which will also automate several development stages and minimize manual interventions.<br/>
**Research Gap:** Real world considerations, Security & Practical implementation<br/>

**Paper-4:** Investigation And Implementation of Jenkins Pipelines into Raspberry Pi For Automated Control Units.<br/>
**Name Of Journal:** III International Scientific and Practical Conference.<br/>
**Summary:** To design and execute a Raspberry Pi-based automated Jenkins pipeline for controlling block units (such as motors, temperature sensors, and other appliances) for contemporary industrial applications. The solution combines the Raspberry Pi with Jenkins, a potent automation tool, to support continuous integration and delivery (CI/CD) procedures and provide flexible and effective control over a variety of devices.<br/>
**Research Gap:** Real world considerations & Security.<br/>

---

### Proposed Work
  This project explores how DevOps approaches and CI/CD pipelines can be integrated in the automotive industry through the creation and deployment of a feature for cars. The feature is implemented using a Raspberry Pi board, which functions as an Electronic Control Unit (ECU) in a mock car setup. The project incorporates continuous integration to ensure code quality and continuous deployment for a seamless delivery to the Raspberry Pi ECU in compliance with DevOps best practices. This setup simulates real-world automotive scenarios using OTA update mechanisms, highlighting how DevOps enables software-defined vehicles to have scalable, reliable, and quick software updates. This approach demonstrates the benefit of CI/CD pipelines in automotive innovation by promoting improved collaboration between development and operations teams and ensuring adherence.<br/>

**Tools & Technologies**<br/>
**Hardware:** Raspberry Pi and Related Sensors & Actuators.<br/>
**Software**Python, Linux OS{Raspbian Os), Repository (Github), CICD (Github actions), Encryption (Cython), Configuration (YAML), Containerization (Docker).<br/>

---
### Methodology
The design and implementation approach for creating the safe OTA deployment pipeline for Software Defined Vehicles (SDVs) is described in this section. Using open-source tools, the method incorporates DevSecOps principles to enable automated, secure, and reproducible deployment workflows for edge hardware like Raspberry Pi.<br/>

**A. System Overview:** <br/>
The proposed system comprises the following key components:<br/>
• A GitHub repository hosting application source code and workflow configurations.<br/>
• A Docker-based build environment targeting arm64 to match the Raspberry Pi’s architecture.<br/>
• PyArmor for runtime code obfuscation, ensuring intellectual property protection.<br/>
• A GitHub Actions workflow that orchestrates code obfuscation, Docker image creation, image pushing, and remote deployment.<br/>
• A Tailscale-powered VPN that enables secure, IP independent SSH access to the target device for deployment.<br/>

**B. Code Obfuscation with PyArmor** <br/>
To ensure protection against reverse engineering and maintain code confidentiality:<br/>
• PyArmor is installed in a Docker container running arm64v8/python:3.11 to match the Raspberry Pi’s architecture.<br/>
• The pyarmor gen app.py command obfuscates the source file, creating a new app.py and a pyarmorruntime000000/ directory containing a runtime .so file.<br/>
• Only these files are included in the final Docker image, ensuring the original source is never exposed.<br/>

**C. Docker-Based Containerization**<br/>
The application is containerized to ensure consistency and platform independence:<br/>
• A Dockerfile is created using arm64v8/python:latest as the base image.<br/>
• The obfuscated app.py and PyArmor runtime files are copied into the container.<br/>
• All required Python dependencies are installed via requirements.txt.<br/>
• The container is built and tagged using docker buildx, targeting the linux/arm64 architecture.<br/>
• The final image is pushed to Docker Hub under a versioned tag.<br/>

**D. CI/CD Pipeline using GitHub Actions**<br/>
The GitHub Actions workflow (app-deploy.yml) is responsible for:<br/>
• Checking out the code from the repository.<br/>
• Obfuscating the application code with PyArmor inside an ARM64 container.<br/>
• Building the Docker image using buildx and pushing it to Docker Hub.<br/>
• Install and authenticate Tailscale with a GitHub secret (TAILSCALE_AUTHKEY ).<br/>
• Setting up SSH access using a securely stored private key (SSH_PRIVATE_KEY ).<br/>
• Remotely accessing the Raspberry Pi using its Tailscale IP and deploying the container using docker run.<br/>

**E. Remote Deployment with Tailscale**<br/>
Given that Raspberry Pi may operate in dynamic or NATed networks:<br/>
• Tailscale is used to create a secure mesh VPN, enabling direct access to the Raspberry Pi using a constant virtual IP.<br/>
• The GitHub runner connects to the Raspberry Pi using SSH over Tailscale.<br/>
• The deployment script logs in to Docker Hub, pulls the latest image, stops any existing container, and runs the new container with the –privileged flag.<br/>

**F. Summary Workflow**<br/>
• Developer pushes code to the main branch.<br/>
• GitHub Actions initiates:<br/>
  1. PyArmor obfuscation<br/>
  2. Docker build (ARM64)<br/>
  3. Docker push<br/>
  4. Tailscale login<br/>
  5. SSH deployment<br/>
• Raspberry Pi pulls and runs the updated container.<br/>
• Logs and failures are tracked via GitHub Actions dashboard.<br/>
![image](https://github.com/user-attachments/assets/ea04f7b7-480a-48f7-b517-5732c4b16964)

<p align="center">
  
</p>

---

### Implementation Details

  <img src="https://github.com/user-attachments/assets/b098e9ea-e7ef-49ad-a826-9558c46d3dc4" width=800/>



---

### Results & Discussion
To demonstrate the process, the ”Autonomous Emergency
Braking System for EV” application has been implemented.
1) Create a GitHub repository with all files, including a .YML file, to trigger GitHub actions.
![image](https://github.com/user-attachments/assets/9a4f210d-254e-42f8-99eb-ff81bb1dcec6)

---
### Demo Videos


---

### Mapping the Project to Relevant Sustainable Development Goals (SDGs)

| SDG        | Alignment                                                                         |
|:-----------|:----------------------------------------------------------------------------------|
| *Goal 3 - Good Health and Well-Being*  | Reduces delays caused by traffic congestion, improving response times and lowering fatalities from accidents. Enhances universal access to timely emergency medical care. |
| *Goal 9 - Industry, Innovation, and Infrastructure* | Supports sustainable and resilient infrastructure through the integration of IoT for emergency medical services. Advances innovation in IoT-enabled emergency response systems. |


---

### References
[1] MOJTABA SHAHIN, L. Z., MUHAMMAD ALI BABAR. (2017). Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices. IEEE Access.<br/>
[2] Ayush Ankit, M. J., K Nimala. (2024). Creation of continuous integration continuous deployment pipeline using cloud. 2024 5th International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV).<br/>
[3] Karthikeyan Palanichamy. (2023). Scalable Python Tools for Managing OTA Updates in Automotive Systems. International Journal of Scientific Research and Management (IJSRM).<br/>
[4] Volodymyr Havran, Maria Orynchak. (2022). Investigation And Implementation of Jenkins Pipelines into Raspberry Pi For Automated Control Units. Education and science of today: intersectoral issues and development of sciences.<br/>
