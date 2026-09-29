#!/usr/bin/env python3
"""Server web blog Edukasi Praktis (publik, tanpa sandi) - port 8094."""
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class BlogServer(ThreadingHTTPServer):
    # Cloudflare Tunnel butuh banyak koneksi; antrean default 5 terlalu kecil.
    request_queue_size = 128
    daemon_threads = True
    allow_reuse_address = True


AKAR = "/home/server/blog-cuan/public"


class Blog(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _kirim(self, kode, isi, tipe="text/html; charset=utf-8"):
        self.send_response(kode)
        self.send_header("Content-Type", tipe)
        self.send_header("Content-Length", str(len(isi)))
        self.send_header("Cache-Control", "public, max-age=600")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(isi)

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        jalur = self.path.split("?")[0].split("#")[0]
        if jalur == "/":
            jalur = "/index.html"
        # Cegah keluar dari folder
        bersih = os.path.normpath(jalur).lstrip("/")
        if bersih.startswith(".."):
            return self._kirim(404, b"<h1>404</h1>", "text/html; charset=utf-8")
        berkas = os.path.join(AKAR, bersih)
        # Folder -> index.html
        if os.path.isdir(berkas):
            berkas = os.path.join(berkas, "index.html")
        # Tanpa ekstensi -> coba .html
        if not os.path.exists(berkas) and not os.path.splitext(berkas)[1]:
            if os.path.exists(berkas + ".html"):
                berkas += ".html"
        if not os.path.exists(berkas):
            galat = os.path.join(AKAR, "404.html")
            if os.path.exists(galat):
                with open(galat, "rb") as f:
                    return self._kirim(404, f.read())
            return self._kirim(404, b"<h1>404</h1>", "text/html; charset=utf-8")
        tipe = "text/html; charset=utf-8"
        if berkas.endswith(".css"):
            tipe = "text/css; charset=utf-8"
        elif berkas.endswith(".js"):
            tipe = "application/javascript; charset=utf-8"
        elif berkas.endswith(".xml"):
            tipe = "application/xml; charset=utf-8"
        elif berkas.endswith(".json"):
            tipe = "application/json; charset=utf-8"
        elif berkas.endswith(".svg"):
            tipe = "image/svg+xml"
        elif berkas.endswith((".png",)):
            tipe = "image/png"
        elif berkas.endswith((".jpg", ".jpeg")):
            tipe = "image/jpeg"
        elif berkas.endswith(".webp"):
            tipe = "image/webp"
        elif berkas.endswith(".ico"):
            tipe = "image/x-icon"
        elif berkas.endswith(".txt"):
            tipe = "text/plain; charset=utf-8"
        with open(berkas, "rb") as f:
            isi = f.read()
        self._kirim(200, isi, tipe)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8094
    s = BlogServer(("0.0.0.0", port), Blog)
    print(f"Blog jalan di port {port}", flush=True)
    s.serve_forever()
