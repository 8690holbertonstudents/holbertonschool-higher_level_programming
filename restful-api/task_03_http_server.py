#!/usr/bin/python3
"""
    Python class to Develop a simple API
    using Python with the "http.server" module.
"""
import http.server
import socketserver
import json
HOST = "localhost"
PORT = 8000


class MyFirstServer(http.server.BaseHTTPRequestHandler):
    """
        Subclass of http.server.BaseHTTPRequestHandler named MyFirstServer.
    """

    def do_GET(self):
        """
        Method to handle GET requests.

        Returns:
            Status code: 200 = OK / 404 = Not found.
            /data endpoint return a simple dataset
            /status endpoint return OK.
            others returns err 404.
        """
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))
        else:
            self.send_error(404, "Not Found")


if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), MyFirstServer) as httpd:
        print(f"Server started on {HOST}:{PORT}")
        httpd.serve_forever()
