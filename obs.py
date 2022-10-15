from ipaddress import ip_address
import simpleobsws
import config

config.initialize()

IP = config.get_ip()
PORT = config.get_port()
PASSWORD = config.get_password()

# Set up OBS websocket
parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False)
ws = simpleobsws.WebSocketClient(url = f"ws://{IP}:{PORT}", password = PASSWORD, identification_parameters = parameters)

# Connect to websocket
async def connect():
    print(f"Attempting to connect to OBS Websocket: ws://{config.get_ip()}:{config.get_port()}")
    await ws.connect() 
    await ws.wait_until_identified()

    # Get version to test connection
    request = simpleobsws.Request('GetVersion')

    ret = await ws.call(request) # Perform the request
    if ret.ok(): # Check if the request succeeded
        print("Connection to OBS Websocket successful!")
    else:
        print("Connection to OBS Websocket failed")