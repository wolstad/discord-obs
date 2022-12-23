# discord-obs

discord-obs functions as a Discord Bot that allows Discord users to control elements of OBS. This bot interacts with OBS using the websocket plugin. The primary purpose of this bot is to allow users to display images in a browser source on screen (MediaGrabber).

## Configuration
1. Upon downloading the source, the bot can be started with `discord-obs.py`. This will generate the `config.json` file. The bot will exit until the neccessary parameters have been set in the config.
2. Set the bot token and neccessary OBS websocket parameters in `config.json`.
3. Create an empty browser source in the OBS scene of your choice. Input the name of this source in `config.json`.
4. Run `discord-obs.py` and the bot should start normally.
5. Define the Discord channel you would like to use with the bot using `.mg_set_channel`

## Commands
- `.img <time>` Display an image in the OBS browser source of `time` seconds. If no time is defined, the bot will default to 15 seconds. This command requires that an image be attached to the Discord command message.
- `.clear_browser` Clears the current browser source.
- `.mg_set_channel` Sets the Discord channel for use with MediaGrabber.

## Future Plans/Features
