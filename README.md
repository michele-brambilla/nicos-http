# NICOS-HTTP

An HTTP REST API client for NICOS.


## Requirements 

### API client

- the NICOS source code
- fastapi
- uvicorn


## Installation

Clone or copy the repository in the folder

```
nicos/clients/
```

of the NICOS source code. Rename the folder `"nicos-http" -> "http"` and install the necessary packages (both NICOS and nicos-http).

## Usage

Launch the REST API client with

```
uvicorn nicos.clients.http.backend.app:app --reload --host 0.0.0.0 --port 5000
```

(the service assume that NICOS is running on the local machine and accepts the `guest` account with no password).

### List the devices, detectors, setups

- get informations about all the devices
`curl -X 'GET' 'http://localhost:5000/devices' -H 'accept: application/json'`
- get informations about a specific device
`curl -X 'GET' 'http://localhost:5000/device/<device name>' -H 'accept: application/json'`
- get informations about all the setups
`curl -X 'GET' 'http://localhost:5000/setups' -H 'accept: application/json'`
- get informations about all the detectors
`curl -X 'GET' 'http://localhost:5000/detectors' -H 'accept: application/json'`


### Add/remove devices and setups

- create a device
`curl -X 'POST' 'http://localhost:5000/devices/<device name>' -H 'accept: application/json' -d ''`
- remove a device
`curl -X 'DELETE' 'http://localhost:5000/devices/<device name>' -H 'accept: application/json'`
- load a setup
`curl -X 'POST' 'http://localhost:5000/setups/<setup name>' -H 'accept: application/json' -d ''`
- unload a device
`curl -X 'DELETE' 'http://localhost:5000/setups/<setup name>' -H 'accept: application/json'`

### Move a device or set a parameter

```
curl -X 'PATCH' \
  'http://localhost:5000/devices/T' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "param": "target",
  "value": 200
}'
```

where `param` can be `target` in case of a `maw` command or the name of the parameter.

### Count command
```
curl -X 'PATCH' \
  'http://localhost:5000/detectors/det' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "preset": "t",
  "value": 10
}'
```

