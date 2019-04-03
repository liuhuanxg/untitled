import http.server


class RequestHandler(http.server):
    """docstring for RequestHandler(BaseHttpServer.BaseHttpRequestHandler"""


        # page model
    Page = '''\
            <html>
            <body>
            <p>I believe in you, Web!</p>
            </body>
            </html>
            '''

    # deal with a get request


    def do_GET(self):
        # super(RequestHandler(BaseHttpServer.BaseHttpRequestHandler, self).__init__()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)


# -------------colorful Luxuriant lineO(∩_∩)O哈哈~----------

if __name__ == '__main__':
    serverAddress = ('127.0.0.1', 5555)
    server = http.server(serverAddress, RequestHandler)
    server.serve_forever()