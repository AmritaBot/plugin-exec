from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent

# Register your commands here
your_plugin_name = on_command("your_plugin_name")


@your_plugin_name.handle()
async def handle_function(event: MessageEvent):
    await your_plugin_name.finish("Hello from your_plugin_name!")
