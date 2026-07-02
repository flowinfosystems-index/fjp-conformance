# FJP-CONF static site — Railway build.
# Official Caddy image; copy the single spec page to the canonical path.
FROM caddy:2.8-alpine

# Config
COPY Caddyfile /etc/caddy/Caddyfile

# The one static asset, placed exactly where the Caddyfile serves it:
#   GET /conformance/v0.1/  ->  /srv/conformance/v0.1/index.html
COPY web/index.html /srv/conformance/v0.1/index.html

# Railway sets $PORT; the Caddyfile binds :{$PORT}. No EXPOSE needed —
# Railway maps the port from the running process.
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
