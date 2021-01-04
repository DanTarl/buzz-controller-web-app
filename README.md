# Buzz! controller web app
Simple web app to simulate key presses to feed into PCSX2 when playing Buzz! games. Tested in conjunction with the [USBqemu-wheel plugin](https://github.com/jackun/USBqemu-wheel) plugin to emulate the Buzz! controllers.

Can be used to play the game remotely if desired. 720p over Zoom works okay, although there is an expected lag which is noticeable in some rounds (e.g. Pie Fight).

## Requirements
1. Set the WEB_SERVER_URL environment variables (including protocol), e.g. https://myserver.com/
2. Install dependencies
```
pip install flask pyautogui pydirectinput
```

## Run
```
python .\main.py
```

### Configuration
#### USBqemu-wheel
By default, the buzzer buttons are mapped to the below keyboard buttons. These can be edited for each play by updating the files in *button_mappings*.

To configure the plugin:
1. Open the plugin in settings in PCSX2 (Config -> USB -> Plugin Settings)
2. Select "Buzz Device" in "Device type" for each of the Buzz devices you want
3. Select "DInput" for each configured device in "Device API"
4. For each device in "Device API", select configure and work through each buzzer/button with the characters below (or to your own configuration)

| Player   | Buzzer   | Blue   | Orange   | Green   | Yellow   |
| -------- | :------: | :----: | :------: | :-----: | :------: |
| Player 1 | a        | b      | c        | d       | e        |
| Player 2 | f        | g      | h        | i       | j        |
| Player 3 | k        | l      | m        | n       | o        |
| Player 4 | p        | q      | r        | s       | t        |
| Player 5 | u        | v      | w        | x       | y        |
| Player 6 | 1        | 2      | 3        | 4       | 5        |
| Player 7 | 6        | 7      | 8        | 9       | 0        |
| Player 8 | [        | ]      | -        | =       | ,        |

#### PCSX2
Player 1 gets a play/pause symbol displayed on the top right of their buzzer screen. This works best if you disable "Hide window when paused" in the PCSX2 settings (Config -> Emulation Settings -> GS Window).

### Games tested
| Game | Region | State | Verified by |
| --- | --- | --- | --- |
| Buzz! The Mega Quiz | NTSC-U | Working out of the box | [DanTarl](https://github.com/DanTarl) |
| Buzz! The Mega Quiz | PAL | Requires USBqemu-wheel fix to prevent buzzer being constantly pressed ([link to fix](https://github.com/jackun/USBqemu-wheel/issues/31#issuecomment-625177710)) | [DanTarl](https://github.com/DanTarl) |
