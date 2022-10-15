import json
import os
import sys

############################
# Read and Write Functions #
############################


# Create config file if it does not exist
def initialize():
    exists = os.path.isfile('config.json')
    if not exists:
        config = {}
        config['bot'] = []
        config['bot'].append({
            'token': '',
            'ip': '',
            'port': '',
            'pass': '',
            'command_prefix': '.',
            'image_channel': None,
        })

        update(config)


# Update config file
def update(config):
    with open("config.json", "w") as json_file:
        json.dump(config, json_file, indent=4, sort_keys=True)


##################
# Set Functions #
##################


def set_image_channel(channel):
    config = get_config()
    config['bot'][0]['image_channel'] = channel.id
    update(config)


####################
# Access Functions #
####################


def get_config():
    with open('config.json') as json_file:
        config = json.load(json_file)
        return config


def get_token():
    config = get_config()
    token = config['bot'][0]['token']
    # Exit bot if token is not defined
    if len(token)<=0:
        print("[Error] Please define a token in config.json")
        sys.exit()
    return token

def get_ip():
    config = get_config()
    ip = config['bot'][0]['ip']
    # Exit bot if token is not defined
    if len(ip)<=0:
        print("[Error] Please define a websocket IP in config.json")
        sys.exit()
    return str(ip)

def get_port():
    config = get_config()
    port = config['bot'][0]['port']
    # Exit bot if token is not defined
    if len(port)<=0:
        print("[Error] Please define a websocket port in config.json")
        sys.exit()
    return str(port)

def get_password():
    config = get_config()
    password = config['bot'][0]['pass']
    # Exit bot if token is not defined
    if len(password)<=0:
        print("[Error] Please define a websocket password in config.json")
        sys.exit()
    return str(password)

def get_command_prefix():
    config = get_config()
    return config['bot'][0]['command_prefix']


def get_image_channel():
    config = get_config()
    return config['bot'][0]['image_channel']