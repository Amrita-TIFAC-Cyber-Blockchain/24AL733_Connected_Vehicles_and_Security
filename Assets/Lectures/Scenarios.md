# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>

## Scenarios 
### Pedestrian Safety System in a Smart City
A smart city integrates a Pedestrian Safety System (PSS). Smart crosswalks are equipped with IoT sensors, and vehicles receive real-time alerts when pedestrians are detected, reducing accidents. Pedestrians using a mobile app can also notify nearby vehicles when crossing the road.

However, privacy advocates raise concerns about tracking pedestrian movements and collecting personal data. Additionally, researchers discover that an attacker could jam communication signals, causing vehicles to fail in detecting pedestrians, leading to accidents.

#### Questions and Answers:
- **What V2X communication methods are used in the pedestrian safety system?**
  - V2P (Vehicle-to-Pedestrian): Vehicles receive alerts from pedestrian apps and smart crosswalk sensors.
  - V2I (Vehicle-to-Infrastructure): Crosswalk IoT sensors detect pedestrian movement.
- **What are the privacy issues when tracking pedestrian movements?**
  - Unethical tracking of pedestrian movement patterns.
  - Personal data exposure from mobile apps.
  - Risk of surveillance abuse by third parties. 
- **What are the possible cybersecurity threats, and how can they be mitigated?**
  - Mobile App Spoofing → Implement biometric authentication for pedestrian alerts.
- **Discuss the role of Edge AI, IoT security, and Blockchain in securing pedestrian detection.**
  - Edge AI: Real-time pedestrian detection without sending data to the cloud.
  - Blockchain: Decentralized identity management for pedestrians using smart contracts.
- **Propose a privacy-preserving pedestrian detection system that balances security and functionality.**
  - Decentralized Identity (DID) for anonymous pedestrian alerts.
  - Federated Learning AI to train pedestrian detection models without data leaks.

### Connected Vehicle Platooning for Freight Transport
A logistics company deploys connected vehicle platooning, where multiple trucks autonomously follow a lead truck using V2V communication. This system reduces fuel consumption and improves efficiency by maintaining a constant speed and distance.

However, security experts identify a potential risk: if an attacker compromises the lead truck’s communication system, they can cause an accident or force all trucks to stop suddenly. Additionally, concerns arise about sensitive cargo information being leaked to competitors.

#### Questions and Answers:
- **Identify and explain the V2X communication methods in truck platooning.**
  - V2V (Vehicle-to-Vehicle): Trucks in the platoon share real-time data on speed, braking, and distance.
  - V2N (Vehicle-to-Network): Cloud-based traffic management adjusts platoon speeds. 
- **What are the cybersecurity threats if an attacker takes control of the lead truck?**
  - A hacker taking control of the lead truck can stop, crash, or reroute the entire platoon.
  - GPS spoofing could mislead trucks into taking incorrect routes.
  - Jamming V2V signals could break vehicle coordination. 
- **How can end-to-end encryption and authentication prevent unauthorized control of trucks?**
  - Mutual Authentication Mechanisms between platoon members.
  - Hardware Security Modules (HSMs) to prevent unauthorized vehicle firmware modifications.
- **Discuss the privacy risks of tracking cargo movement and how they can be mitigated.**
  - Cargo tracking data should be anonymized before being shared with third parties.
  - Confidential Computing ensures truck data is processed securely in the cloud.
  - Zero-Knowledge Proofs (ZKP) allow freight tracking without revealing sensitive details.
- **Suggest a secure communication protocol for preventing cyberattacks on connected freight vehicles.**
  - Blockchain-based access control to verify which entities can issue control commands.
  - Software-defined perimeter (SDP) to restrict unauthorized network access. 
