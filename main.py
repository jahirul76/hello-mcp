from mcp.server.fastmcp import FastMCP
import httpx

brent_collection_text = """Your bin days

Address
    50 East Lane, Wembley, HA9 7NS

Your collections

Please note all collections can take place between 7am – 10pm.
Recycling collection

Frequency
    Every other Thursday 
Next collection
    Thursday, 8th January (In progress) 

A missed collection cannot be reported on the day of collection until the crew have finished their round.
Rubbish collection

Frequency
    Every other Thursday 
Next collection
    Thursday, 15th January 
Last collection
    Friday, 2nd January, at 11:08am (this collection was adjusted from its usual time)

    Not Presented

A missed collection cannot be reported; please see the last collection status above.
Garden waste collection
Warning
Your subscription is soon due for renewal.
Avoid disruption to your service.

Frequency
    Tuesday every 4 weeks 
Next collection
    Tuesday, 13th January 
Last collection
    Tuesday, 16th December, at 7:58am 

Please note that missed collections can only be reported within 2 working days of your scheduled collection.

Subscription
    1 bin
Renewal
    31 March 2026, soon due for renewal.

If you are looking to pay for another garden waste service, please contact our Customer Services Team.
Food waste collection

Frequency
    Every Thursday 
Next collection
    Thursday, 8th January (In progress) 

A missed collection cannot be reported on the day of collection until the crew have finished their round.
Paper and cardboard (blue sacks) collection

Frequency
    Every other Thursday 
Next collection
    Thursday, 15th January 
Last collection
    Friday, 2nd January, at 8:59am (this collection was adjusted from its usual time) 

Please note that missed collections can only be reported within 2 working days of your scheduled collection.
Small items"""


# Initialise FastMCP server
mcp = FastMCP("reliefweb")

@mcp.tool(name="hello", description="A simple hello world tool")
def hello(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool(name="find_council",
          description="Finds the council for a given postcode")
def find_council(postcode: str) -> str:
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['result']['admin_district']
    else:
        return "Unknown Council"

@mcp.tool(name="get_bin_collection_day", 
          description="Fetches bin collection day for a given council")
def get_bin_collection_day(council: str) -> str:

    if council.lower() != "brent":
        return "This tool only supports Brent council."

    # with open('brent_collection_text.txt', 'r') as file:
    #     data = file.read().rstrip()

    return brent_collection_text


def main():
    print("Hello from hello-mcp!")

    # Initialise and run the server
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
