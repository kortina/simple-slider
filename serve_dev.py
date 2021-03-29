#!/usr/bin/env python3

from http.server import test, SimpleHTTPRequestHandler as RH  # type: ignore


port = 8000
bind = "localhost"
address = f"http://{bind}:{port}/"
print(address)
RH.extensions_map = {k: f"{v};charset=UTF-8" for k, v in RH.extensions_map.items()}
test(RH, port=port, bind=bind)
