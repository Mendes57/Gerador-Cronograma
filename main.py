from static.funcoes.coletaDadosEChecaErros import coletaDadosEChecaErros
from static.funcoes.printaCrono import printaCrono
from static.funcoes.geraCrono import geraCrono
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


# printaCrono(geraCrono(coletaDadosEChecaErros()))



if __name__ == "__main__":
    # Configurando para host='0.0.0.0' e port=8080
    server_address = ('0.0.0.0', 8080)
    httpd = TCPServer(server_address, SimpleHTTPRequestHandler)

    print(printaCrono(geraCrono(coletaDadosEChecaErros())))
    httpd.serve_forever()