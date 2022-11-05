import logging

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from nicos.clients.base import NicosClient, ErrorResponse

from nicos.clients.http.backend.src import devices, detectors, setups
from nicos.clients.base import ErrorResponse, NicosClient, ConnectionData

log = logging.getLogger(__name__)


# class HttpClient(NicosClient):
#
#     def connect_to_daemon(self, hostname, port, user, *args) :
#         NicosClient.connect(self, ConnectionData(hostname, port, user, args))
#
#     def signal(self, name, *args):
#         log.debug(f'{name} -- {args}')
#
#     def ask(self, command, *args, **kwds):
#         """Execute a command that generates a response, and return the response.
#
#         The arguments are the command and its parameter(s), if necessary.
#
#         A *quiet=True* keyword can be given if no error should be generated if
#         the client is not connected.  When not connected, you can give a
#         *default* keyword to return.
#         """
#
#         try:
#             with self.lock:
#                 self.transport.send_command(command, args)
#                 success, data = self.transport.recv_reply()
#                 if not success:
#                     if not kwds.get('noerror', False):
#                         raise ErrorResponse(data)
#                     return kwds.get('default')
#                 return data
#         except (Exception, KeyboardInterrupt) as err:
#             log.error(err)
#             return args[1]

#
# conndata = ConnectionData('localhost', 1301, 'guest', '')
# client = HttpClient(log)
# client.connect(conndata)


# class HttpClient(NicosClient):
#     def signal(self, name, *args):
#         log.debug(f'{name} -- {args}')
#
#     def ask(self, command, *args, **kwds):
#         """Execute a command that generates a response, and return the response.
#
#         The arguments are the command and its parameter(s), if necessary.
#
#         A *quiet=True* keyword can be given if no error should be generated if
#         the client is not connected.  When not connected, you can give a
#         *default* keyword to return.
#         """
#         try:
#             with self.lock:
#                 self.transport.send_command(command, args)
#                 success, data = self.transport.recv_reply()
#                 if not success:
#                     if not kwds.get('noerror', False):
#                         raise ErrorResponse(data)
#                     return kwds.get('default')
#                 return data
#         except (Exception, KeyboardInterrupt) as err:
#             log.error(err)
#             return args[1]


app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(devices.router)
app.include_router(setups.router)
app.include_router(detectors.router)


@app.get("/")
async def root():
    return {"message": "Hello, NICOS!"}






