import http.server
import cgi, random, sys

MESSAGES = [
    "That's as maybe, it's still a frog.",
    "Albatross! Albatross! Albatross!",
    "It's Wolfgang Amadeus Mozart.",
    "A pink form from Reading.",
    "Hello people, and welcome to 'It's a Tree.'"
    "I simply stare at the brick and it goes to sleep.",
  ]


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404, "file not found");
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        try:
            # redirect stdout to client
            stdout = sys.stdout
            sys.stdout = self.wfile
            self.makepage()
        finally:
            sys.stdout = stdout  # restore

    def makepage(self):
        # generate a random msg
        tagline = random.choice(MESSAGES)
        print("<html><title>toast</title><body><p>Today's quote:<i>")
        print (cgi.escape(tagline))
        print("</i></body></html>")
PORT=19019
httpd = http.server.HTTPServer(("", PORT), Handler)
print ("serving at port", PORT)
httpd.serve_forever()