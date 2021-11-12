# url-checker-api Python version

URL Checker API is an API that take a URL as an input and validates against it's database to see if it is safe to access or unsafe URL.

## Setup Requirements
- Python 3
## Setup

- Clone the repository https://github.com/abiredavid/url-checker-api
- Change directory into the already cloned repo
```
$ cd url-checker-api/python
```
- Install project dependencies
```
$ pip install -r requirements.txt
```
- Start the application
```
$ python server.py
```
The application should start on a default port of 5000. Navigate to `localhost:5000` and it should take you to the home of the API and you should be greeted with the output 
```
{"Page":"Home","msg":"The URL checker API Home"}
```
## Usage
The applications responds to a Get request that looks like the following:
```
GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}
```
**Parameters**
- **hostname_and_port**: This is the hostname including the port number of the URL to check for. This will typically look like `whereisthatsite.com:8000`
- **original_path_and_query_string**: This is the path of the url and the query strings and will look like `foo/?sortBy=dependency&order=asc&page=1&perPage=500`

**Response**

The API responds with an object that contains the following attributes for hostname that exist in it's database
- **url**: This is the base url for example: `whereisthatsite.com`
- **isSafe**: This is a boolean value that is `true` if the url is safe to access.
- **description**: This is a string that gives a brief description of the safety status of the url.

In a case where the url does not exist in the API's database, the API returns an error message and HTTP 404;

```
{
    "msg": "hostname: whereisthatsite.com does not exist in database.",
    "url": "whereisthatsite.com"
}
```

**Example**
- Check for a safe URL `uncanny.com:8002/foo/?sortBy=dependency&order=asc&page=1&perPage=500` 
```
$ curl http://localhost:5000/urlinfo/1/uncanny.com:8002/foo/?sortBy=dependency&order=asc&page=1&perPage=500

 {"description":"Url is safe to access","isSafe":true,"url":"uncanny.com"}
```
- Check for an unsafe URL `hotpage.com:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500`
```
$ curl http://localhost:5000/urlinfo/1/hotpage.com:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500

{"description":"Contains malware and unsafe to access","isSafe":false,"url":"hotpage.com"}
```
- Check for a URL that does not exist in the API database `coldpage.se:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500`
```
$ curl http://localhost:5000/urlinfo/1/coldpage.se:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500

{"msg":"hostname: coldpage.se does not exist in database.","url":"coldpage.se"}
```
**Some valid hostnames to test with**
- `hotpage.com`
- `coldpage.com`
- `monster.com`
- `works.com`
- `doesnotwork.com`
- `downtown.au`
- `itjustdoesnotwork.edu`
- `iwishthisworks.org`


**Tests**
The test for this service utilizes Pytest and it is also defined in the `requirements.txt` file. 
You can run the tests by simply running the command
```
$ py.test

$ py.test
============================================== test session starts ===============================================
platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /python
collected 7 items

test_server.py .......                                                                                     [100%]

=============================================== 7 passed in 0.26s ================================================
```


**Status Codes**
- HTTP **200** : Successful request
- HTTP **400** : Invalid URL
- HTTP **404** : No information available for the requested URL