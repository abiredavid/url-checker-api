# url-checker-api Node version

URL Checker API is an API that take a URL as an input and validates against it's database to see if it is safe to access or unsafe URL.

## Setup Requirements
- Node version v14
## Setup

- Clone the repository https://github.com/abiredavid/url-checker-api
- Change directory into the already cloned repo
```
$ cd url-checker-api/node
```
- Install project dependencies
```
$ npm install
```
- Start the application
```
$ npm start
```
The application should start on a default port of 8000. To modify the port during startup, set the environment variable PORT or start the application with the following command
```
PORT=8002 npm start
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
- **description**: This is string that describes the reason the url is consider unsafe or just information that the site is safe to access.

In a case where the url does not exist in the API's database, the API returns an error message and HTTP_404;

- Node
```
ERROR: hostname "funnypage.ore" does not exist in the database
```

- Python

**Example**
- Check for a safe URL `uncanny.com:8002/foo/?sortBy=dependency&order=asc&page=1&perPage=500` 
```
$ curl http://localhost:8000/urlinfo/1/uncanny.com:8002/foo/?sortBy=dependency&order=asc&page=1&perPage=500

{"url":"uncanny.com","isSafe":true,"description":"Url is safe to access"}
```
- Check for an unsafe URL `coldpage.com:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500`
```
$ curl http://localhost:8000/urlinfo/1/coldpage.com:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500

{"url":"coldpage.com","isSafe":true,"description":"Url is safe to access"}
```
- Check for a URL that does not exist in the API database `coldpage.se:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500`
```
$ curl http://localhost:8000/urlinfo/1/coldpage.se:8001/foo/?sortBy=dependency&order=asc&page=1&perPage=500

ERROR: hostname "coldpage.se" does not exist in the database
```
