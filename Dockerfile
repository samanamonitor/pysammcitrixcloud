FROM python:3.12
COPY dev-requirements.txt /tmp
RUN <<EOF
pip install -r /tmp/dev-requirements.txt
EOF
WORKDIR /app
ENTRYPOINT /bin/bash