// In SecurityModule.cc
void SecurityModule::handleMessage(cMessage* msg) {
    EmergencyAlert* alert = check_and_cast<EmergencyAlert*>(msg);

    if (!verifySignature(alert->getSignature(), publicKey)) {
        sendSecurityAlert("INVALID_SIGNATURE", alert->getSenderAddress());
        delete msg;
        return;
    }

    // Forward valid messages
    send(msg, "out");
}
