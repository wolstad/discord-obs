import json
import os
import sys

class Config():

    ############################
    # Read and Write Functions #
    ############################

    # Create config file if it does not exist
    def initialize(self):
        # Define config
        config = {}
        config['bot'] = {
            'token': '',
            'command_prefix': '.',
            'image_channel': None
        }
        config['obs'] = {
            'ip': '',
            'port': '',
            'pass': '',
            'browser_source': ''           
        }

        # Check if file exists
        exists = os.path.isfile('config.json')

        # Check for existing values in config
        if exists:
            with open('config.json') as json_file:
                config_f = json.load(json_file)

                for outer_key in config.keys():
                    for inner_key in config[outer_key].keys():     
                        # Check if key currently exists and set it
                        try:
                            config[outer_key][inner_key] = config_f[outer_key][inner_key]
                        except KeyError:
                            pass # Do nothing
                        
        self.update(config)

    # Update config file
    def update(self, config):
        with open("config.json", "w") as json_file:
            json.dump(config, json_file, indent=4, sort_keys=False)


    ##################
    # Set Functions #
    ##################

    def set_image_channel(self, channel):
        config = self.get_config()
        config['bot']['image_channel'] = channel.id
        self.update(config)

    ####################
    # Access Functions #
    ####################


    def get_config(self):
        with open('config.json') as json_file:
            config = json.load(json_file)
            return config


    def get_token(self):
        config = self.get_config()
        token = config['bot']['token']
        # Exit bot if token is not defined
        if len(token)<=0:
            print("[Error] Please define a token in config.json")
            sys.exit()
        return token

    def get_ip(self):
        config = self.get_config()
        ip = config['obs']['ip']
        # Exit bot if token is not defined
        if len(ip)<=0:
            print("[Error] Please define a websocket IP in config.json")
            sys.exit()
        return str(ip)

    def get_port(self):
        config = self.get_config()
        port = config['obs']['port']
        # Exit bot if token is not defined
        if len(port)<=0:
            print("[Error] Please define a websocket port in config.json")
            sys.exit()
        return str(port)

    def get_password(self):
        config = self.get_config()
        password = config['obs']['pass']
        # Exit bot if token is not defined
        if len(password)<=0:
            print("[Error] Please define a websocket password in config.json")
            sys.exit()
        return str(password)

    def get_command_prefix(self):
        config = self.get_config()
        return config['bot']['command_prefix']

    def get_image_channel(self):
        config = self.get_config()
        return config['bot']['image_channel']

    def get_browser_source(self):
        config = self.get_config()
        return config['obs']['browser_source']