# FJP-CONF static site — Railway build.
FROM caddy:2.8-alpine

COPY Caddyfile /etc/caddy/Caddyfile

# Landing page at root
COPY web/landing.html /srv/index.html

# Post-purchase success page
COPY web/success.html /srv/success.html

# Developer quickstart page
COPY web/quickstart.html /srv/quickstart.html

# Abe (FJP Gate) developer page
COPY web/abe.html /srv/abe.html
COPY web/credits.html /srv/credits.html

# Shared site stylesheet (identical to flowinfo.co src/app/flow-site.css) and logo
COPY web/flow-site.css /srv/flow-site.css
COPY web/flow-mark.png /srv/flow-mark.png

# Crawler and LLM discovery files
COPY web/robots.txt /srv/robots.txt
COPY web/llms.txt /srv/llms.txt
COPY web/sitemap.xml /srv/sitemap.xml

# Spec page at canonical path
COPY web/index.html /srv/conformance/v0.1/index.html

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
