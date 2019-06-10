# canScan

CANopen active scanner atop Christian Sandberg's
[CANopen for Python](https://github.com/christiansandberg/canopen). canScan
watches for CAN arbitration IDs, CANopen node IDs (as determined through
NMT/SDO analysis), and CANopen PDOs. canScan can scan the Object Dictionary
of a specified (or discovered) CANopen node using SDO Receive.

canScan has been developed/tested against Python 2.7 and 3.7.

[![Build Status](https://travis-ci.org/dankamongmen/canscan.svg?branch=master)](https://travis-ci.org/dankamongmen/canscan)

# Usage

Two arguments are required: a bus type and a device identifier. The bus types
are due [python-can](https://github.com/hardbyte/python-can), and can be found
in that project's documentation. Device identifier semantics are per-driver.
For virtual devices, use `virtual` and the network device name. Other SocketCAN
devices use `socketcan` and the network device name. The CanalystII uses
`canalystii` and the USB device index.

Default behavior is to perform an SDO scan across the 128 CANopen IDs, then
perform dumps of the entirety of discovered nodes' Object Dictionaries. Both
steps will be periodically repeated. Discovered Object Dictionary entries will
be queried more regularly than failed IDs. The program exits on error or
keyboard interrupt. With the `--oneshot` flag, only an initial set of scans
will be performed, followed by the program's exit.

The `--passive` flag can be provided, in which case no frames will be
transmitted (the driver or hardware might send frames, especially
acknowledgements, on their own).

If the `--scan` argument is provided, it expects a comma-delimited list of
numbers (either decimal, or hex with a prefix of `0x`). These IDs will see
their entire Dictionaries scanned whether they respond to the initial probe or
not.

`--passive` cannot be used with `--scan` or `--oneshot`.

The default local node ID is 64 (0x40), but it may be specified with `--id`.
