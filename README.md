# canScan

CANopen active scanner atop Christian Sandberg's
[https://github.com/christiansandberg/canopen](CANopen for Python). canScan
watches for CAN arbitration IDs, CANopen node IDs (as determined through
NMT/SDO analysis), and CANopen PDOs. canScan can scan the Object Dictionary
of a specified (or discovered) CANopen node using SDO Receive.

canScan has been developed/tested against Python 2.7 and 3.7.
