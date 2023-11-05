# auto-audio
A program made to help gaming with music on.
## First time setup
Run the file called "run_with_dependencies.py" the first time you use the app.<br>
You can get Process ID from Task Manager > Details<br>
After first use you can just run "main.py".<br>
## How it works
Using OCR it scans zones on screen to test for certain static text elements. If those static elements are found then the program knows what state the game is in. The game state is mapped to a louder/quieter value. The value can be changed for each game and each app.
## Configs
To change which app's volume is controlled change the Process ID stored in app.json<br>
Check app_region_presets.json to adjust scanning zones. The zones are stored in the following format: \[x, y, width, height\]<br>
To change volume values check app_settings.json. They are sorted by game>application>volume.<br>
Theoretically this program is quite easily scalable and you should be able to semi-easily add support for any game/games that are not already supported.<br>
## Currently supported games:
Fortnite
## Game Support WIP
Valorant<br>
Counter-Strike 2
