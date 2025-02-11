# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>

## CAN and CAN-FD
![](https://img.shields.io/badge/Date-XX_Feb-blue)

### Comparison of CAN and CAN-FD

| **Parameter**           | **CAN (Classical CAN)**      | **CAN-FD (Flexible Data-Rate)** |
|-------------------------|-----------------------------|---------------------------------|
| **Developed by**        | Bosch (1986)                | Bosch (2012)                   |
| **Max Data Rate**       | 1 Mbps                      | Up to 8 Mbps (2, 5 and 8 Mbps   |
| **Max Payload Size**    | 8 bytes                     | 64 bytes (0, 8, 12, 16, 20, 24, 32, 48, 64) |
| **Bit Rate**            | Fixed throughout frame      | Dual Bit Rate (Higher in data phase) |
| **Frame Structure**     | Standard CAN Frame         | Extended CAN Frame with FD features |
| **Error Handling**      | Standard CRC (15-bit)       | Improved CRC (17-bit or 21-bit)  |
| **Arbitration**         | Non-destructive CSMA/CD     | Non-destructive CSMA/CD         |
| **Efficiency**          | Lower due to smaller payload and fixed bit rate | Higher due to larger payload and flexible bit rate |
| **Compatibility** | Yes (CAN-FD controllers can support classical CAN) | No (Classical CAN controllers cannot process CAN-FD frames) |
| **Use Cases**          | Automotive, Industrial Automation, Medical Devices | High-bandwidth applications in Automotive (ADAS, ECU updates), Aerospace |

### Message Formats
#### CAN

<p align="center">
  <img src="images/CAN_Frame.png" width=600 />
</p>

#### CAN-FD

<p align="center">
  <img src="images/CAN-FD_Frame.png" width=600 />
</p>

#### CAN-XL

<p align="center">
  <img src="images/CAN-XL_Frame.png" width=600 />
</p>

###### Image Source:[HMS-Networks](https://www.hms-networks.com/industrial-iot-blog/blogpost/hms-blog/2024/06/18/can-can-fd-can-xl-what-are-the-differences)
