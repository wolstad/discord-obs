from ipaddress import ip_address
from aiohttp import request
from timer import Timer
import simpleobsws
import config


class OBS():

    ###################
    # Setup Functions #
    ###################

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

        await self.initialize_vars()


    async def initialize_vars(self):
        print("Initializing OBS Variables.")

        # Browser Source
        check_browser_vis = await self.make_request(simpleobsws.Request('GetInputSettings', {'inputName': self.obs_state["browser_source"]}))
        
        print(check_browser_vis.responseData)

        if check_browser_vis.responseData['inputSettings']['url']:
            self.obs_state["browser_visible"] = True

        print(f"OBS State: {self.obs_state}")


    ##################
    # Manipulate OBS #
    ##################

    # Clear the browser source
    async def clear_browser_source(self):
        request = await self.make_request(simpleobsws.Request('SetInputSettings', {'inputName': self.obs_state["browser_source"], 'inputSettings': {'url': ''}}))
        if request.ok():
            self.obs_state["browser_visible"] = False
            print("Browser source cleared.")
        return request.ok()

    # Set an image for a set amount of time
    async def img_trigger(self, image_src, time):
        # Enabling image
        if self.obs_state["browser_visible"]:
            return False # Media already being displayed
        else:
            print(f"Enabling OBS image for: {time}")

            request = await self.make_request(simpleobsws.Request('SetInputSettings', {'inputName': self.obs_state["browser_source"], 'inputSettings': {'url': image_src}}))
            if request.ok():
                self.obs_state["browser_visible"] = True
            timer = Timer(time, self.clear_browser_source)


    ###########
    # Helpers #
    ###########

    def get_browser_status(self):
        return self.obs_state["browser_visible"]

    async def make_request(self, req):
        ret = await self.ws.call(req) 
        if not ret.ok():
            print(f"[Error] OBS Request Failed: {req}")
            return False
        return ret