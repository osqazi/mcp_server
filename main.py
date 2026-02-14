# First install mcp serever with cli using:  uv add "mcp[cli]"

from typing import Any
from mcp.server.fastmcp import FastMCP


mcp = FastMCP[Any](
    name="hello-server",
    stateless_http=True # set true for no handshake 
)

@mcp.tool()
def hello(name: str) -> str:
    return f"hello, {name}!"

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is Sunny"



mcp_app = mcp.streamable_http_app()


# how to run mcp server : uv run uvicorrn main:mcp_app --reload


#how to send request to mcp: localhost:8000/mcp along with json rpc, method, params and id.

# A Developer Tool/inspector server for mcp server: mcp dev main.py
