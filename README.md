# Bee Pi
> 🔧 **NOTE: This project is currently under development. Features and documentation may be incomplete and subject to change without notice.**


## Description
A raspberry pi device to connected to [BEEMINDER](www.beeminder.com) API to build habits. Press the button every time you complete a task and the device will automatically update your BEEMINDER goal. At random intervals the device will also instruct you to reward yourself with a treat.

## Parts
- 3D Printed Case
- Raspberry Pi Zero W
- LED Display
- Python script (connect to BEEMINDER API)
- Other circuitry parts

## Setup
Create a .env file in the root directory with the following format:
```bash
# .env
BEEMINDER_AUTH_TOKEN='<BEEMINDER_AUTH_TOKEN>'
BEEMINDER_USER='<BEEMINDER_USER>'
```

## TODO
- [ ] Add a display screen and related script
- [ ] Design and print a case
- [ ] Move circuit from breadboard to more permanent solution
- [ ] Add "setup" to README.md along with parts list and costs