#
# Sample application on how to encode/decode use J2735 messages with python
#
from J2735Decoders import *
import time
from decimal import Decimal


print("### Starting J2735 test")

# Random NMEA coordinates (Degrees.Minutes)
Latitude = "5231.453"
Longitude= "01323.658"
Altitude = "10"
Speed = "33.33"
VehicleWidth = "200"
VehicleLength = "400"
vehicleStatus = "ACCI" # available temporary status: ACCI, NORM, EMER

print("---")
print("# Generating Basic Safety Message")
encodedBSM = createJ2735BSM(vehicleStatus,Latitude,Longitude,Altitude, Speed, VehicleWidth, VehicleLength)
originalBSM = decodeJ2735BSM(encodedBSM)

print("Encoded: " + getMessageType(encodedBSM))
print(encodedBSM)
print("")
print("Decoded")
print(originalBSM)


# Random Safety application example
appID = "POI"
initTS = str(Decimal(repr(time.time()))) # random timestamp
print(initTS)
recvTS = ""
sourceIP = "192.168.1.66"
destinationIP = "192.168.1.124"
destPort = "8000"
content = "anybyteencodedcontentgoeshere"


print("---")
print("# Generating A La Carte message")
encodedALC = createALaCarte(appID,initTS, recvTS, sourceIP,destinationIP, destPort, content)
originalALC = decodeJ2735ALC(encodedALC)

print("Encoded: " + getMessageType(encodedALC))
print(encodedALC)
print("")
print("Decoded")
print(originalALC)
