# J2735-python

Python implementation for SAE J2735 *a la carte* and *basic safety message* Message Set Dictionary. 

## Getting Started
To install dependencies simply run
`python setup.py`

The `src/__init__.pt` contains a basic sample application for encoding and decoding J2735 messages.

## Implementation Notes
For Basic Safety Messages (BSM), a 4-byte representation was used to describe the vehicle temporary status:

| Status  | 4-byte representation |
| ------------- | ------------- |
| Normal  | NORM  |
| Emergency  | EMER  |
| Accident  | ACCI  |


Coordinates are a direct output from NMEA sentencens i.e. expressed in degrees, minutes


## What's SAE J2735?
SAE J2735 - Dedicated Short Range Communications (DSRC) Message Set Dictionary, specifies standard message sets, data frames and data elements for use by applications intended to utilize the 5.9 GHz spectrum.

The complete standard defines several message formats, namely: 
* a la carte message; 
* basic safety message; 
* emergency vehicle alert message; 
* generic transfer message; 
* probe vehicle data message, and; 
* common safety request message. 

The a la carte message (ALC) is composed entirely of message elements determined by the sender, allowing for flexible data exchange. 

The basic safety message (BSM) contains vehicle safety-related information that is periodically broadcast to surrounding vehicles.

### Historical note
This implementation was originaly developed in 2013, when DSRC was pursued as the targe solution for V2X (vehicle-to-anything) networks. Over time, the 5.9 Ghz spectrum availability, V2X technologies, and overall mesh-network standards evolved, possibly deeming the current implementation obsolete.


