
from pyasn1.type import univ
from pyasn1.codec.der import encoder as DERencoder, decoder as DERdecoder


from j2735 import *
from Plausability import nmea2deg

import datetime


BSMcounter = 0

def createJ2735BSM(status, nmealatitude,nmealongitude, altitude, speed, vehicleWidth, vehicleLength):
	# - Fixed TemporaryID
	# - Fixed Accuracy
	# - speed in m/s
	# - Fixed Heading
	# - Fixed Angle
	# - Fixed Acceleration
		
	BSM = BasicSafetyMessage()
	BSM.setComponentByName('msgID',2) #basicSafetyMessage
	
	global BSMcounter
	BSM.setComponentByName('msgCnt',BSMcounter)
	BSM.setComponentByName('id',status)
	
	nowTime = datetime.datetime.now()
	timeMS = int(str(nowTime.microsecond)[0:4])
	
	
	#print "[createJ2735BSM]\tConverting to Degrees " +  nmealatitude + " - " + nmealongitude
	newlat = nmea2deg(nmealatitude)
	newlon = nmea2deg(nmealongitude)
	#print "[createJ2735BSM]\tAfter Conversion " +  str(newlat) + " - " + str(newlon) 
	
	#FAZER SPLIT PELO PONTO E FAZER O ENCODE
	newlat = str(newlat).replace(".","")
	newlon = str(newlon).replace(".","")
	
	
	BSM.setComponentByName('secMark',timeMS)	
	BSM.setComponentByName('lat',newlat)
	BSM.setComponentByName('long',newlon)
	BSM.setComponentByName('elev',altitude)
	BSM.setComponentByName('accuracy',"0000")
	
	newSpeed = int(float(speed)*100)
	#newSpeedHex = hex(newSpeed)
	#newSpeedHex = newSpeedHex.split("x")
	
	transAndSpeed = TransmissionAndSpeed()
	transAndSpeed.setComponentByName('state',7)
	transAndSpeed.setComponentByName('speed',newSpeed)
		
	BSM.setComponentByName('speed',transAndSpeed)
	BSM.setComponentByName('heading',0)
	BSM.setComponentByName('angle',"0")
	BSM.setComponentByName('accelSet',"acceler")
	BSM.setComponentByName('brakes',"nn")
	
	vehicleSize = VehicleSize()
	vehicleSize.setComponentByName('width',vehicleWidth)
	vehicleSize.setComponentByName('length',vehicleLength)
	
	BSM.setComponentByName('size',vehicleSize)

	#print(BSM.prettyPrint())
	
	# Increase BSM sequencenumber and Prevent overflow
	BSMcounter = BSMcounter+1 
	if(BSMcounter==127):
		BSMcounter = 0
	
	encodedMessage = DERencoder.encode(BSM)
	return encodedMessage

def createALaCarte(appID,initTS, recvTS, sourceIP, destinationIP, destPort ,content):
	ALC = ALaCarte()	
	ALC.setComponentByName('msgID', 1)
	ALC.setComponentByName('appID',appID)
	ALC.setComponentByName('initTS',initTS)
	ALC.setComponentByName('recvTS',recvTS)
	ALC.setComponentByName('source',sourceIP)
	ALC.setComponentByName('destination',destinationIP)
	ALC.setComponentByName('destPort',destPort)
	ALC.setComponentByName('appData', content)
	encodedMessage = DERencoder.encode(ALC)
	
	return encodedMessage

