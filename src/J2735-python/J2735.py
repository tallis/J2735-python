from pyasn1.type import univ, namedtype, namedval, constraint, tag, char


# DSRCmsgID ::= ENUMERATED
class DSRCmsgID(univ.Enumerated):
    namedValues = namedval.NamedValues(
        ('reserved', 0),
        ('alaCarteMessage', 1),
        ('basicSafetyMessage', 2),
        ('basicSafetyMessageVerbose', 3),
        ('commonSafetyRequest', 4),
        ('emergencyVehicleAlert', 5),
        ('intersectionCollisionAlert', 6),
        ('mapData', 7),
        ('nmeaCorrections', 8),
        ('probeDataManagement', 9),
        ('probeVehicleData', 10),
        ('roadSideAlert', 11),
        ('rtcmCorrections', 12),
        ('signalPhaseAndTimingMessage', 13),
        ('signalRequestMessage', 14),
        ('signalStatusMessage', 15),
        ('travelerInformation', 16)
    )
    subtypeSpec = univ.Enumerated.subtypeSpec + constraint.SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                                                                 12, 13, 14, 15, 16)


# MsgCount ::= INTEGER (0..127)
class MsgCount(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(0, 127)


# TemporaryID ::= OCTET STRING (SIZE(4))
class TemporaryID(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(4, 4)


# DSecond ::= INTEGER (0..65535)
class DSecond(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(0, 65535)


# Latitude ::= INTEGER (-900000000..900000001)
class Latitude(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(-900000000, 900000001)


# Longitude ::= INTEGER (-1800000000..1800000001)
class Longitude(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(-1800000000, 1800000001)


# Elevation ::= OCTET STRING (SIZE(2))
#   -- 1 decimeter LSB (10 cm) 
#   -- Encode elevations from 0 to 6143.9 meters 
#   -- above the reference ellipsoid as 0x0000 to 0xEFFF.  
#   -- Encode elevations from -409.5 to -0.1 meters, 
#   -- i.e. below the reference ellipsoid, as 0xF001 to 0xFFFF
#   -- unknown as 0xF000 
class Elevation(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(2, 2)


# PositionalAccuracy ::= OCTET STRING (SIZE(4)) 
#   -- And the bytes defined as folllows

#   -- Byte 1: semi-major accuracy at one standard dev 
#   -- range 0-12.7 meter, LSB = .05m
#   -- 0xFE=254=any value equal or greater than 12.70 meter
#   -- 0xFF=255=unavailable semi-major value 

#   -- Byte 2: semi-minor accuracy at one standard dev 
#   -- range 0-12.7 meter, LSB = .05m
#   -- 0xFE=254=any value equal or greater than 12.70 meter
#   -- 0xFF=255=unavailable semi-minor value 

#   -- Bytes 3-4: orientation of semi-major axis 
#   -- relative to true north (0~359.9945078786 degrees)
#   -- LSB units of 360/65535 deg  = 0.0054932479
#   -- a value of 0x0000 =0 shall be 0 degrees
#   -- a value of 0x0001 =1 shall be 0.0054932479degrees 
#   -- a value of 0xFFFE =65534 shall be 359.9945078786 deg
#   -- a value of 0xFFFF =65535 shall be used for orientation unavailable 
#   -- (In NMEA GPGST)
class PositionalAccuracy(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(4, 4)


# TransmissionState ::= ENUMERATED {
#    neutral         (0), -- Neutral, speed relative to the vehicle alignment
#    park            (1), -- Park, speed relative the to vehicle alignment
#    forwardGears    (2), -- Forward gears, speed relative the to vehicle alignment
#    reverseGears    (3), -- Reverse gears, speed relative the to vehicle alignment 
#    reserved1       (4),      
#    reserved2       (5),      
#    reserved3       (6),      
#    unavailable     (7), -- not-equipped or unavailable value,
#    }
class TransmissionState(univ.Enumerated):
    namedValues = namedval.NamedValues(
        ('neutral', 0),
        ('park', 1),
        ('forwardGears', 2),
        ('reverseGears', 3),
        ('reserved1', 4),
        ('reserved2', 5),
        ('reserved3', 6),
        ('unavailable', 7)
    )
    subtypeSpec = univ.Enumerated.subtypeSpec + constraint.SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7)


# Speed ::= INTEGER (0..8191) -- Units of 0.02 m/s
#           -- The value 8191 indicates that 
#           -- speed is unavailable
class Speed(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(0, 8191)


# TransmissionAndSpeed ::= OCTET STRING (SIZE(2))
# ADAPTATION :: USED AS A SEQUENCE 
#     -- Bits 14~16 to be made up of the data element
#     -- DE_TransmissionState 
#     -- Bits 1~13 to be made up of the data element
#     -- DE_Speed
class TransmissionAndSpeed(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('state', TransmissionState()),
        namedtype.NamedType('speed', Speed())
    )


# Heading ::= INTEGER (0..28800)
#    -- LSB of 0.0125 degrees
#    -- A range of 0 to 359.9875 degrees
class Heading(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(0, 28800)


# SteeringWheelAngle ::= OCTET STRING (SIZE(1))
#     -- LSB units of 1.5 degrees.  
#     -- a range of -189 to +189 degrees
#     -- 0x01 = 00 = +1.5 deg
#     -- 0x81 = -126 = -189 deg and beyond
#     -- 0x7E = +126 = +189 deg and beyond
#     -- 0x7F = +127 to be used for unavailable
class SteeringWheelAngle(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(1, 1)


# AccelerationSet4Way ::= OCTET STRING (SIZE(7))
#    -- composed of the following:
#    -- SEQUENCE {
#    --    long Acceleration,          -x- Along the Vehicle Longitudinal axis
#    --    lat  Acceleration,          -x- Along the Vehicle Lateral axis
#    --    vert VerticalAcceleration,  -x- Along the Vehicle Vertical axis
#    --    yaw  YawRa
#    --    }
class AccelerationSet4Way(univ.OctetString):
    # TODO Data Frame to implement
    subtypeSpec = constraint.ValueSizeConstraint(7, 7)


# BrakeSystemStatus ::= OCTET STRING (SIZE(2))
# -- Encoded with the packed content of:
# -- SEQUENCE {
# --   wheelBrakes        BrakeAppliedStatus,
# --                      -x- 4 bits
# --   wheelBrakesUnavailable  BOOL
# --                      -x- 1 bit (1=true)
# --   spareBit
# --                      -x- 1 bit, set to zero
# --   traction           TractionControlState,
# --                      -x- 2 bits
# --   abs                AntiLockBrakeStatus,
# --                      -x- 2 bits
# --   scs                StabilityControlStatus,
# --                      -x- 2 bits
# --   brakeBoost         BrakeBoostApplied,
# --                      -x- 2 bits
# --   auxBrakes          AuxiliaryBrakeStatus,
# --                      -x- 2 bits
# --   }
class BrakeSystemStatus(univ.OctetString):
    # TODO
    subtypeSpec = constraint.ValueSizeConstraint(2, 2)


# VehicleWidth ::= INTEGER (0..1023) -- LSB units are 1 cm
class VehicleWidth(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(0, 1023)


# VehicleLength ::= INTEGER (0..16383) -- LSB units are 1 cm
class VehicleLength(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(0, 16383)


# VehicleSize ::=  SEQUENCE {
#    width     VehicleWidth,
#    length    VehicleLength
#  }  -- 3 bytes in length
class VehicleSize(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('width', VehicleWidth()),
        namedtype.NamedType('length', VehicleLength()),
    )


# MsgCRC ::= OCTET STRING (SIZE(2))
class MsgCRC(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(2, 2)


# Adaptation by Rui
# VADMApplicationData ::= OCTET STRING (MAXSIZE(1..1000))
class VADMApplicationData(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(0, 1000)


# VADMApplicationData ::= OCTET STRING ((0..30))		
class VADMApplicationName(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(0, 30)


class VADMinitTS (univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(0, 19)


class VADMrecvTS(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(0, 19)


class VADMsourceIP(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(0, 16)


class VADMdestinationIP(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(0, 16)


class VADMdestinationPort(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(0, 6)


#####
## SAE J2735 DSRC standard message sets
#####
class BasicSafetyMessage(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('msgID', DSRCmsgID()),
        namedtype.NamedType('msgCnt', MsgCount()),
        namedtype.NamedType('id', TemporaryID()),
        namedtype.NamedType('secMark', DSecond()),
        namedtype.NamedType('lat', Latitude()),
        namedtype.NamedType('long', Longitude()),
        namedtype.NamedType('elev', Elevation()),
        namedtype.NamedType('accuracy', PositionalAccuracy()),
        namedtype.NamedType('speed', TransmissionAndSpeed()),
        namedtype.NamedType('heading', Heading()),
        namedtype.NamedType('angle', SteeringWheelAngle()),
        namedtype.NamedType('accelSet', AccelerationSet4Way()),
        namedtype.NamedType('brakes', BrakeSystemStatus()),
        namedtype.NamedType('size', VehicleSize())
    )


class ALaCarte(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('msgID', DSRCmsgID()),
        namedtype.NamedType('appID', VADMApplicationName()),
        namedtype.NamedType('initTS', VADMinitTS()),
        namedtype.NamedType('recvTS', VADMrecvTS()),
        namedtype.NamedType('source', VADMsourceIP()),
        namedtype.NamedType('destination', VADMdestinationIP()),
        namedtype.NamedType('destPort', VADMdestinationPort()),
        namedtype.NamedType('appData', VADMApplicationData()),
        namedtype.OptionalNamedType('crc', MsgCRC())
    )
