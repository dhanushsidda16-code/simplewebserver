from http.server import HTTPServer, BaseHTTPRequestHandler

htmlcontent = '''
<!doctype html>
<html>
<head>
<title> localhost</title>
</head>

<body>
    <center><font color="blue" face="Lucida Handwriting" size="100">
    <b>List of protocols in TCP/IP Mdel</b>
    </center></font>
        <h2>
         <br>Application Layer - HTTP,FTP,DNS,TELNET & SSH</br>
         <br>Transport Layer - HTTP,FTP,TCP</br>
         <br>Network Layer - IPV4/IPV6</br>
        Link Layer - Ethernet
    </h2>
        
    </font>
</body>
</html>
     '''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(htmlcontent.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()