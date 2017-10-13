FROM alpine:3.6
RUN apk add --no-cache python curl docker py-pip

RUN pip install --upgrade --user awscli

# Add AWS CLI to PATH
ENV PATH="/root/.local/bin:${PATH}"

COPY build-docker-images /root/.local/bin/
COPY push-docker-images /root/.local/bin/
