from mcp.server.fastmcp import FastMCP

# Initialise FastMCP server
mcp = FastMCP("reliefweb")

@mcp.tool(name="hello", description="A simple hello world tool")
def hello(name: str) -> str:
    return f"Hello, {name}!"


def main():
    print("Hello from hello-mcp!")

    # Initialise and run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
