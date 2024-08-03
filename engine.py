import asyncio
import json

# class Engine:
    # def __init__(self, host: str, port: int, username: str, password: str):
    #     self.host = host
    #     self.port = port
    #     self.username = username
    #     self.password = password

class Engine:
    host: str = None
    port: int = None
    username: str = None
    password: str = None

async def send_data(host: str, port: int, string: str):
    resp = None
    try:
        reader, writer = await asyncio.open_connection(host, port)
        writer.write(string + b"\n")
        await writer.drain()
        try:
            resp = await asyncio.wait_for(reader.read(), timeout=120)
            resp = resp.decode()
            try:
                if resp.isdigit():
                    resp = int(resp)
                elif resp == "":
                    resp = None
                else:
                    resp = json.loads(resp.replace("'", '"'))

            except:
                pass
        except asyncio.TimeoutError:
            resp = "Operation timed out"
        writer.close()
        await writer.wait_closed()
    except:
        resp = "Connection refused"
    return resp

# async def send_data(self, command):
#     resp = None
#     try:
#         reader, writer = await asyncio.open_connection(self.host, self.port)
#         writer.write(command + b"\n")
#         await writer.drain()
#         try:
#             resp = await asyncio.wait_for(reader.read(), timeout=120)
#             resp = resp.decode()
#             try:
#                 if resp.isdigit():
#                     resp = int(resp)
#                 elif resp == "":
#                     resp = None
#                 else:
#                     resp = json.loads(resp.replace("'", '"'))

#             except:
#                 pass
#         except asyncio.TimeoutError:
#             resp = "Operation timed out"
#         writer.close()
#         await writer.wait_closed()
#     except:
#         resp = "Connection refused"
#     return resp