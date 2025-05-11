from http.server import SimpleHTTPRequestHandler, HTTPServer

# Configuração do servidor
host = "localhost"
port = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"POST request received!")

    def do_PUT(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"PUT request received!")
        
    def do_DELETE(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"DELETE request received!")

# Inicializando o servidor
server = HTTPServer((host, port), MyHandler)
print(f"Servidor rodando em http://{host}:{port}")
server.serve_forever()
