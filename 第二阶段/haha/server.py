from wsgiref.simple_server import make_server
from myapp import myapp
httpd = make_server('', 8000, myapp)
print ("Serving HTTP on port 8000...")
httpd.serve_forever()