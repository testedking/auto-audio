# auto-audio
A program made to help gaming with music on.
## First time setup
Run the file called "run_with_dependencies.py" the first time you use the app.
You can get Process ID from Task Manager > Details
After first use you can just run "main.py".
## How it works
Using OCR it scans zones on screen to test for certain static text elements. If those static elements are found then the program knows what state the game is in. The game state is mapped to a louder/quieter value. The value can be changed for each game and each app.
## Configs
To change which app's volume is controlled change the Process ID stored in app.json
Check app_region_presets.json to adjust scanning zones. The zones are stored in the following format: \[x, y, width, height\]
To change volume values check app_settings.json. They are sorted by game>application>volume.
Theoretically this program is quite easily scalable and you should be able to semi-easily add support for any game/games that are not already supported.
## Currently supported games:
Fortnite
## Game Support WIP
Valorant
Counter-Strike 2
