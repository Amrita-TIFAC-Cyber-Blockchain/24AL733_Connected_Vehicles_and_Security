// In AccidentDetector.cc
void AccidentDetector::handleMessage(cMessage* msg) {
    if (isCollisionDetected()) {
        EmergencyAlert* alert = new EmergencyAlert("ACCIDENT_ALERT");
        alert->setPosition(getCurrentPosition());
        send(alert, "out");

        // Trigger SUMO emergency response
        TraCICommandInterface::Vehicle vehicle = getTraCI()->vehicle(getExternalId());
        vehicle.setSpeed(0);
    }
}
