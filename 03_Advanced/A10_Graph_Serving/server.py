"""Loopback-only teaching endpoint. python server.py --port 8124"""
import argparse
import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from app import graph

class Handler(BaseHTTPRequestHandler):
    def respond(self,status,payload):
        body=json.dumps(payload).encode()
        self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
    def do_GET(self):
        self.respond(200,{'ready':True}) if self.path=='/health' else self.respond(404,{'error':'not found'})
    def do_POST(self):
        if self.path!='/invoke':self.respond(404,{'error':'not found'});return
        try:
            size=int(self.headers.get('Content-Length','0'))
            if not 0<size<=8000:raise ValueError('Request size must be 1–8000 bytes.')
            value=json.loads(self.rfile.read(size))
            if not isinstance(value,dict) or set(value)!={'request'}:raise ValueError('Supply exactly one request field.')
            result=graph.invoke({'request':value['request']})
        except (ValueError,TypeError,KeyError):self.respond(400,{'error':'invalid request'});return
        self.respond(200,result)
    def log_message(self,*args):pass

def serve(port):
    with ThreadingHTTPServer(('127.0.0.1',port),Handler) as server:
        print(json.dumps({'port':server.server_address[1]}),flush=True)
        server.serve_forever()

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--port',type=int,default=8124);args=parser.parse_args();serve(args.port)
