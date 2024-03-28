import asyncio

async def tcp_echo_client(message):
    #A connection can be opened in asyncio using the asyncio.open_connection() function.
    # Establish a network connection and return a pair of (reader, writer) objects.
    # Which can be used to read/write messages to/from the server.
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Send: {message}')
    writer.write(message.encode())
    #await writer.drain() halts the execution until it is possible to resume writing.
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))