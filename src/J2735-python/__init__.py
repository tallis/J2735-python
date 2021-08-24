from J2735Encoders import *
from J2735Decoders import *

print("Starting J2735 test")

currentLatitude = "00917.7729"
currentLongitude= "00917.7729"

fixedAltitude = "F0"
fixedSpeed = "33.33"
fixedVehicleWidth = "200"
fixedVehicleLength = "400"

APPNAME = "RequestAssistance"

encodedBSM = createJ2735BSM("acci",currentLatitude,currentLongitude,fixedAltitude, fixedSpeed, fixedVehicleWidth, fixedVehicleLength)

encodedALC = createALaCarte("GetMusic","00000.0000","recvTS","192.168.0.10","192.168.0.1","8890", "GETTHISMUSIC")

print(getMessageType(encodedBSM))
print(getMessageType(encodedALC))
