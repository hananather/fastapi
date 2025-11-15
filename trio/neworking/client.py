# echo-client.py

import sys
import trio

# arbitrary, but:
# - must be in between 1024 and 65535
# - can't be in use by some other program on your computer
# - must match what we set in our echo server
PORT = 12345


async def sender(client_stream):
    print("sender: started!")
    while True:
        # sender sends data to the server (4)
        data = b"async can sometimes be confusing, but I believe in you!"
        print(f"sender: sending {data!r}")
        await client_stream.send_all(data)
        await trio.sleep(1)


async def receiver(client_stream):
    # waits for data from the server (5)
    print("receiver: started!")
    async for data in client_stream:
        print(f"receiver: got data {data!r}")
        # 
    print("receiver: connection closed")
    sys.exit()


async def parent():
    # parent opens a TCP conection to the server (2)
    # await pauses until connection is ready
    # create client_stream for communication with the server
    print(f"parent: connecting to 127.0.0.1:{PORT}")
    client_stream = await trio.open_tcp_stream("127.0.0.1", PORT)
    async with client_stream:
        async with trio.open_nursery() as nursery:
            print("parent: spawning sender...")
            # start_soon schedules tasks
            nursery.start_soon(sender, client_stream)

            print("parent: spawning receiver...")
            nursery.start_soon(receiver, client_stream)
            #parent waits here unitl all children finish (sender and receiver) (3)

# trio event loop starts (1)
trio.run(parent)