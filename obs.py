from ipaddress import ip_address
import simpleobsws
import config

IP = config.get_ip()
PORT = config.get_port()
PASSWORD = config.get_password()

# Set up OBS websocket
global ws
parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False)

# Connect to websocket
async def connect():
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
        print("Connection to OBS Websocket failed")