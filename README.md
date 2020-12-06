# Buzz! controller web app
Simple web app app to simulate key presses to feed into PCSX2 when playing Buzz! games. Tested in conjunction with the [USBqemu-wheel plugin](https://github.com/jackun/USBqemu-wheel) plugin to emulate the Buzz! controllers.

## Requirements
1. Set the WEB_SERVER_URL environment variables (including protocol), e.g. https://myserver.com/.
2. Set up certificates in the root of the repository with names 'cert.pem' and 'key.pem'.

Install dependencies
```
pip install flask pyautogui
```

## Run
```
python .\main.py
```
