import asyncio
import asyncpg
import time

# Postgres database details:
host = "localhost"
db_name = "northwind"
port = "55432"
username = "postgres"
password = "postgres"
schema = "public"

PINK = '\033[38;5;205m'
TEAL = '\033[38;5;31m'
GREEN = '\033[32m'
RESET = '\033[0m'

def print_pink(msg):
    print(f"{PINK} {time.ctime()} - {msg} {RESET}" )
    
def print_teal(msg):
    print(f"{TEAL} {time.ctime()} - {msg} {RESET}" )
    
def print_green(msg):
    print(f"{GREEN} {time.ctime()} - {msg} {RESET}" )

def print_in_color(msg, color):
    if color == 'green':
        print_green(msg)
    elif color == 'teal':
        print_teal(msg)
    else:
        print_pink(msg)

async def asyncpg_async_get_monitors_many_calls(color="green", id="ALFKI"):
    print_in_color(f"Openning connection", color=color)
    conn = await asyncpg.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=db_name,
        server_settings={'search_path': schema}
        )
    rows = await conn.fetch(f"""SELECT (SUM((1 - order_details.discount) * order_details.unit_price * order_details.quantity))::NUMERIC::MONEY AS totalamount FROM orders JOIN order_details ON (orders.order_id=order_details.order_id) JOIN customers ON (customers.customer_id=orders.customer_id) WHERE customers.customer_id = '{id}'""")
    for row in rows:
        print_in_color(dict(row), color=color)
        endquery = time.monotonic()
        print_in_color(f"time on id '{id}' is {endquery - start} seconds" , color=color)

    await conn.close()

async def main():
    await asyncio.gather(
        asyncpg_async_get_monitors_many_calls(color='green', id='ALFKI'),
        asyncpg_async_get_monitors_many_calls(color='pink', id='ANATR'),
        asyncpg_async_get_monitors_many_calls(color='teal', id='BERGS')
    )

if __name__ == "__main__":
    start = time.monotonic()
    asyncio.run(main())
    end = time.monotonic()
    print(f"total time {end - start} seconds")

# [32m Wed Aug  9 13:57:38 2023 - Openning connection [0m
# [38;5;205m Wed Aug  9 13:57:38 2023 - Openning connection [0m
# [38;5;31m Wed Aug  9 13:57:38 2023 - Openning connection [0m
# [38;5;31m Wed Aug  9 13:57:38 2023 - {'totalamount': '$24,927.58'} [0m
# [38;5;31m Wed Aug  9 13:57:38 2023 - time on id 'BERGS' is 0.125 seconds [0m
# [38;5;205m Wed Aug  9 13:57:38 2023 - {'totalamount': '$1,402.95'} [0m
# [38;5;205m Wed Aug  9 13:57:38 2023 - time on id 'ANATR' is 0.125 seconds [0m
# [32m Wed Aug  9 13:57:38 2023 - {'totalamount': '$4,273.00'} [0m
# [32m Wed Aug  9 13:57:38 2023 - time on id 'ALFKI' is 0.14100000000325963 seconds [0m
# total time 0.14100000000325963 seconds