import shlex

from amrita.plugins.chat.API import (
    FunctionDefinitionSchema,
    FunctionParametersSchema,
    FunctionPropertySchema,
    ToolContext,
    on_tools,
)

from . import container_exec
from .config import CONFIG
from .main import permission_docker

TOOL_DATA = FunctionDefinitionSchema(
    name="command_exec",
    description="Execute a command in the shell",
    parameters=FunctionParametersSchema(
        type="object",
        properties={
            "command": FunctionPropertySchema(
                type="string", description="Command to execute"
            )
        },
        required=["command"],
    ),
)


@on_tools(
    data=TOOL_DATA,
    custom_run=True,
    strict=True,
    show_call=True,
    enable_if=lambda: CONFIG.enable_in_tool,
)
async def _(ctx: ToolContext) -> str:
    if not await permission_docker(ctx.event._nbevent):
        return "User permission denied."
    cmd_text = ctx.data["command"]
    cmd_parts = shlex.split(cmd_text)

    logs, exit_code = await container_exec.execute_in_docker(*cmd_parts)
    return f"exit_code: {exit_code}\n执行结果：\n\n```text{logs}\n```"
