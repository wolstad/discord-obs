from ipaddress import ip_address
from aiohttp import request
import simpleobsws
import config


class OBS():
    @classmethod
    async def create(self, ip, port, password, browser_source):
        # Websocket Config
        parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False)
        self.ip = ip
        self.port = port
        self.password = password
        self.ws = simpleobsws.WebSocketClient(url = f"ws://{ip}:{port}", password = password, identification_parameters = parameters)

        # OBS State
        self.obs_state = {
            "browser_source": browser_source,
            "browser_visible": False
        }

        return self


    # Connect to websocket
    async def connect(self):
        print(f"Attempting to connect to OBS Websocket: ws://{self.ip}:{self.port}")
        await self.ws.connect() 
        await self.ws.wait_until_identified()

        # Get version to test connection
        request = simpleobsws.Request('GetVersion')

        ret = await self.ws.call(request) # Perform the request
        if ret.ok(): # Check if the request succeeded
            print("Connection to OBS Websocket successful!")
        else:
            print("[Error] Connection to OBS Websocket failed")
            return False

        await self.initialize_vars()


    async def initialize_vars(self):
        print("Initializing OBS Variables.")

        check_browser_vis = simpleobsws.Request('GetInputSettings', {'inputName': self.obs_state["browser_source"]})

        ret = await self.ws.call(check_browser_vis) 
        if not ret.ok():
            print("[Error] Function failed to execute.")
            return False
        
        if ret.responseData['inputSettings']['url']:
            self.obs_state["browser_visible"] = True

        print(f"OBS State: {self.obs_state}")


    async def img_toggle(self, img_src):
        # Disable cat
        if self.obs_state["browser_visible"]:
            print("Disabling cat.")
            request = simpleobsws.Request('SetInputSettings', {'inputName': 'Testy', 'inputSettings': {'url': ''}})
        else:
            print("Enabling cat.")
            request = simpleobsws.Request('SetInputSettings', {'inputName': 'Testy', 'inputSettings': {'url': img_src}})

        ret = await self.ws.call(request) 
        if not ret.ok():
            print("[Error] Function failed to execute.")
            return False

        self.obs_state["browser_visible"] = not self.obs_state["browser_visible"]