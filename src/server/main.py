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

# Inicializando o servidor
server = HTTPServer((host, port), MyHandler)
print(f"Servidor rodando em http://{host}:{port}")
server.serve_forever()
