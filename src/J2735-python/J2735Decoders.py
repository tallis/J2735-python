from pyasn1.codec.der import decoder as DERdecoder
from J2735Encoders import *


def decodeJ2735BSM(encodedBSM):
    decoded = DERdecoder.decode(encodedBSM, asn1Spec=BasicSafetyMessage())
    return decoded[0]


def decodeJ2735ALC(encodedALC):
    decoded = DERdecoder.decode(encodedALC, asn1Spec=ALaCarte())
    return decoded[0]


##
## GETTERS AND SETTERS
##
def getMessageType(encodedJ2735):
    try:
        decoded = DERdecoder.decode(encodedJ2735)

        if str(decoded[0].getComponentByPosition(0)) == "2":
            return "BSM"

        elif str(decoded[0].getComponentByPosition(0)) == "1":
            return "ALC"

    except Exception as err:
        return "STDMSG: " + str(err)


# ALC Getters
def ALCget_appID(encodedALC):
    decodedALC = decodeJ2735ALC(encodedALC)
    return str(decodedALC.getComponentByPosition(1))


def ALCget_initTS(encodedALC):
    decodedALC = decodeJ2735ALC(encodedALC)
    return str(decodedALC.getComponentByPosition(2))


def ALCget_recvTS(encodedALC):
    decodedALC = decodeJ2735ALC(encodedALC)
    return str(decodedALC.getComponentByPosition(3))


def ALCget_source(encodedALC):
    decodedALC = decodeJ2735ALC(encodedALC)
    return str(decodedALC.getComponentByPosition(4))


def ALCget_destination(encodedALC):
    decodedALC = decodeJ2735ALC(encodedALC)
    return str(decodedALC.getComponentByPosition(5))


def ALCget_destport(encodedALC):
    decodedALC = decodeJ2735ALC(encodedALC)
    return str(decodedALC.getComponentByPosition(6))


def ALCget_appData(encodedALC):
    decodedALC = decodeJ2735ALC(encodedALC)
    return str(decodedALC.getComponentByPosition(7))


# ALC SETTERS
def ALCset_source(encodedALC, sourceIP):
    decodedALC = decodeJ2735ALC(encodedALC)
    encodedALC = createALaCarte(decodedALC.getComponentByPosition(1), decodedALC.getComponentByPosition(2),
                                decodedALC.getComponentByPosition(3), sourceIP, decodedALC.getComponentByPosition(5),
                                decodedALC.getComponentByPosition(6), decodedALC.getComponentByPosition(7))
    return encodedALC


def ALCset_recvTS(encodedALC, recvTS):
    decodedALC = decodeJ2735ALC(encodedALC)
    encodedALC = createALaCarte(decodedALC.getComponentByPosition(1), decodedALC.getComponentByPosition(2), recvTS,
                                decodedALC.getComponentByPosition(4), decodedALC.getComponentByPosition(5),
                                decodedALC.getComponentByPosition(6), decodedALC.getComponentByPosition(7))
    return encodedALC
