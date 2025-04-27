#include <omnetpp.h>
#include "CarModule_m.h"  // Generated message header

using namespace omnetpp;

class CarModule : public cSimpleModule {
  private:
    cMessage *checkTimer;
    double detectionThreshold;
  protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
    void checkForPedestrians();
    double computeDistanceToPedestrian(); // stub function
};

Define_Module(CarModule);

void CarModule::initialize() {
    detectionThreshold = par("detectionThreshold");
    checkTimer = new cMessage("checkTimer");
    scheduleAt(simTime() + 0.1, checkTimer);
}

void CarModule::handleMessage(cMessage *msg) {
    if (msg == checkTimer) {
        checkForPedestrians();
        scheduleAt(simTime() + 0.1, checkTimer);
    }
}

void CarModule::checkForPedestrians() {
    // Here you would normally obtain dynamic positions from the simulation.
    double distance = computeDistanceToPedestrian();
    if (distance < detectionThreshold) {
        EV << "Pedestrian detected at " << distance << " meters away.\n";
        // send alert to sensor module or network broadcast
        send(new cMessage("PedestrianDetectionAlert"), "out");
    }
}

double CarModule::computeDistanceToPedestrian() {
    // In a full implementation, calculate the Euclidean distance
    // between the car's current position and the pedestrian's position.
    // For demonstration, we return a constant value.
    return 3.0; // e.g., 3 meters, triggering an alert
}

void CarModule::checkForAccidents() {
    // This function could be invoked periodically or event-driven
    bool accidentDetected = false;  // Replace with actual collision check
    // For demonstration, trigger an accident alert at a specific simulation time
    if (simTime() > 5 && !accidentDetected) { // condition to trigger once
        accidentDetected = true;
        EV << "Accident detected! Broadcasting accident alert.\n";
        send(new cMessage("AccidentAlert"), "out");
    }
}

