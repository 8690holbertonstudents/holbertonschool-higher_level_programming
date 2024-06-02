#!/usr/bin/python3
"""
    Python class to Develop a simple API
    using Python with the "http.server" module.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
        Subclass of http.server.BaseHTTPRequestHandler
        named SimpleHTTPRequestHandler.
    """

    def do_GET(self):
        """
        Method to handle GET requests.

        Returns:
           The good output for define endpoints,
           error 404 with message for the others.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"version": "1.0",
                       "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(dataset).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not found")


if __name__ == "__main__":
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    print("serving at port", 8000)
    httpd.serve_forever()
