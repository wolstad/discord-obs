from ipaddress import ip_address
from aiohttp import request
import simpleobsws
import config

# Set up OBS websocket
IP = config.get_ip()
PORT = config.get_port()
PASSWORD = config.get_password()

ws = None
parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False)

# Media variables
BROWSER_SOURCE = 'Testy'
browser_visible = False

# Connect to websocket
async def connect():
    global ws
    ws = simpleobsws.WebSocketClient(url = f"ws://{IP}:{PORT}", password = PASSWORD, identification_parameters = parameters)
    print(f"Attempting to connect to OBS Websocket: ws://{IP}:{PORT}")
    await ws.connect() 
    await ws.wait_until_identified()

    # Get version to test connection
    request = simpleobsws.Request('GetVersion')

    ret = await ws.call(request) # Perform the request
    if ret.ok(): # Check if the request succeeded
        print("Connection to OBS Websocket successful!")
    else:
        print("[Error] Connection to OBS Websocket failed")
        return False

    await initialize_vars()


async def initialize_vars():
    print("Initializing OBS Variables.")

    global browser_visible

    request = simpleobsws.Request('GetInputSettings', {'inputName': BROWSER_SOURCE})

    ret = await ws.call(request) 
    if not ret.ok():
        print("[Error] Function failed to execute.")
        return False
    
    if ret.responseData['inputSettings']['url']:
        browser_visible = True

    print(f"Browser Visible: {browser_visible}")


async def img_toggle(img_src):
    global browser_visible

    # Disable cat
    if browser_visible:
        print("Disabling cat.")
        request = simpleobsws.Request('SetInputSettings', {'inputName': 'Testy', 'inputSettings': {'url': ''}})
    else:
        print("Enabling cat.")
        request = simpleobsws.Request('SetInputSettings', {'inputName': 'Testy', 'inputSettings': {'url': img_src}})

    ret = await ws.call(request) 
    if not ret.ok():
        print("[Error] Function failed to execute.")
        return False

    browser_visible = not browser_visible