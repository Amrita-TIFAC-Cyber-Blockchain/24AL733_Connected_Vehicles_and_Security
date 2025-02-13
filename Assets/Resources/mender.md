# 24AL733 - Connected Vehicles and Security 
![](https://img.shields.io/badge/PG-blue) ![](https://img.shields.io/badge/Subject-CVS-blue) <br/>

## Resources for OTA - Mender
Mender is a 
- professional, purpose-built OTA update solution
- designed by cyber security experts
- complete over-the-air (OTA) update infrastructure for developers and support teams

### Getting Started
- [Signup](https://hosted.mender.io/ui/signup) Here
- Connect up to 10 devices free for 12 months

### Device Configuration (Docker Device)

- Run the below command in Windows Powershell. 
```
docker run -it -p 85:85 `
  -e SERVER_URL="https://eu.hosted.mender.io" `
  -e TENANT_TOKEN="gH1L7HDWkW7Ck2_OcAw8-JZlZFcSH7wCSDNiuPoBs8E" `
  --pull=always mendersoftware/mender-client-qemu
```
<h5 align="center">Docker Device Downloading</h5>
<p align="center">
	<img src="../images/Mender_docker_device_download.png" alt="Docker Device Download" width=650 />
</p>

<h5 align="center">Docker Device Ready</h5>
<p align="center">
	<img src="../images/Mender_docker_device_ready.png" alt="Docker Device Ready" width=650 />
</p>

### Device Authorization 
<h5 align="center">Mender Device Pending Authorization</h5>
<p align="center">
	<img src="../images/Mender_device_pending.png" alt="Device Pending Authorization" width=680 />
</p>

<h5 align="center">Mender Device Pending Authorization (Detailed)</h5>
<p align="center">
	<img src="../images/Mender_device_status_pending.png" alt="Device Pending Authorization" width=680 />
</p>

<h5 align="center">Mender Device Authorization Accept</h5>
<p align="center">
	<img src="../images/Mender_device_accept.png" alt="Device Authorization Accept" width=680 />
</p>

### Deployment
<h5 align="center">Deployment Creation</h5>
<p align="center">
	<img src="../images/Mender_deployment_creation.png" alt="Deployment Creation" width=680 />
</p>

<h5 align="center">Deployment Created</h5>
<p align="center">
	<img src="../images/Mender_deployment_created.png" alt="Deployment Created" width=680 />
</p>

<h5 align="center">Deployment Progress</h5>
<p align="center">
	<img src="../images/Mender_deployment_progress.png" alt="Deployment Progress" width=680 />
</p>

<h5 align="center">Deployment Success</h5>
<p align="center">
	<img src="../images/Mender_deployment_success.png" alt="Deployment Success" width=680 />
</p>
