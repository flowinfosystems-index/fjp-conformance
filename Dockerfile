# FJP-CONF static site — Railway build.
# Official Caddy image; serves landing page at root and spec at canonical path.
FROM caddy:2.8-alpine

# Config
COPY Caddyfile /etc/caddy/Caddyfile

# Landing page at root
COPY web/landing.html /srv/index.html

# Spec page at canonical path
COPY web/index.html /srv/conformance/v0.1/index.html

# Railway sets $PORT; the Caddyfile binds :{$PORT}. No EXPOSE needed.
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
