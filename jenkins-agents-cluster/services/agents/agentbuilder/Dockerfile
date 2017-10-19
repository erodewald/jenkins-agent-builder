FROM alpine:3.6
RUN apk update
RUN apk add python curl docker py-pip bash

RUN pip install --upgrade --user awscli

# Add AWS CLI to PATH
ENV PATH="/root/.local/bin:${PATH}"

COPY build-docker-images /root/.local/bin/
COPY push-docker-images /root/.local/bin/
COPY increment-version /root/.local/bin/
COPY generate-version /root/.local/bin/

RUN curl -sSL https://raw.githubusercontent.com/moul/docker-diff/master/docker-diff > /root/.local/bin/docker-diff
RUN chmod +x /root/.local/bin/docker-diff