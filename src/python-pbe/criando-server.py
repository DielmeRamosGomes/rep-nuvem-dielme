import http.server
import socketserver

PORT = 8000

class MeuHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        mensagem = "Olá do seu servidor Python personalizado!"
        self.wfile.write(mensagem.encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MeuHandler) as httpd:
        print(f"Servindo na porta {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor interrompido.")