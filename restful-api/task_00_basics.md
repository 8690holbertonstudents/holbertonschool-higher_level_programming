<h4>0. Basics of HTTP/HTTPS</h4>

<h5>1. A brief summary explaining the differences between HTTP and HTTPS.</h5>

**HTTP** : For *"**H**yper**T**ext **T**ransfer **P**rotocol"*, is the basical web langage. he's written to exchange data between servers and browsers.
Typical use : Web pages (informations, blog)

**HTTPS** : For *"**H**yper**T**ext **T**ransfer **P**rotocol **S**ecure"*, is the secure "side" of HTTP, using **TLS** encryption *(**T**ransport **L**ayer **S**ecurity)*.
It's harder for eavesdroppers to steal data.
Typical use : e-commerce, online-bank, website requesting a login.

<h5>2. A depiction or outline of the structure of an HTTP request and response.</h5>

**Request :** The browser send a request to the web server. this request contains an *"HTTP method"*, the request target (usually URL), and the *"HTTP version"*.
it can contains optional like *"headers"* and *"body"*.
<div>(example: GET http://www.w3.org/pub/WWW/TheProject.html HTTP/1.1:)</div><br>

**Response :** The start line of response, called *"status line"* contains:
The protocol version, a status code, and a status text.
<div>(example: HTTP/1.1 404 Not Found)</div><br>

<h5>3. Lists of common HTTP methods and status codes with their descriptions and possible use cases.</h5>

**Method:**
- **GET :** Retrieves data from a server.(Fetching a web page)
- **POST :** Submits data to a server.(Submitting a form)
- **PUT :** Updates data on a server.(Updating a user profile)
- **DELETE :** Deletes data from a server. (Deleting an email)
  
**Status code:**
- **404 :** Not found. (Requested page not on server)
- **200 :** OK. (Request sucessfull)
- **403 :** Forbidden. (No or bad access rights)
- **400 :** Bad Request. (Server couldn't interpret the request)
- **500 :** Internal Server Error. (An unexpected error occurred on the server)
