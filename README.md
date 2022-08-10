# mirthpy
Basic python api for Mirth Connect

> **_NOTE:_**  This api only has Channels, Code Templates, Events, and Users built in. You should still be able to get to the rest, you'll just need to use the ElementTree to navigate.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mirthpy.

```bash
pip install mirthpy
```

## Setup
Config file must match the following: 
```sh
{
    "instanceName": "{instance IP or DNS Name}",
    "credentials": {
        "username": "{username}", 
        "password": "{password}"
    }
}
```

## Usage

```python
import json
import mirthpy

config = json.load(open('config.json'))

service = MirthService(config)
service.open()

# Get a list of channels
channels = service.getChannels({"channelId":"3bb08639-7725-4b1b-a2ac-13687101fe9b"}) 

for channel in channels:
    print(f"{channel.name} - {channel.revision}")

```
