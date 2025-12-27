# Configuration for your_plugin_name plugin
from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    ...
    # Add your configuration here


# Get your config by using `get_plugin_config(Config)`

CONFIG = get_plugin_config(Config)
