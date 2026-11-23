from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os, webbrowser
os.chdir(Path(__file__).resolve().parent)
server = ThreadingHTTPServer(('127.0.0.1', 0), SimpleHTTPRequestHandler)
url = 'http://127.0.0.1:%s/index.html' % server.server_port
print('Journal Tutorial:', url, flush=True)
webbrowser.open(url)
try: server.serve_forever()
except KeyboardInterrupt: pass
