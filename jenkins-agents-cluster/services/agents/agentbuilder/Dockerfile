FROM alpine:3.6
RUN apk update
RUN apk add python curl docker py-pip bash git openssh

RUN pip install --upgrade --user awscli

# Add AWS CLI to PATH
ENV PATH="/root/.local/bin:${PATH}"

COPY build-docker-images /root/.local/bin/
COPY push-docker-images /root/.local/bin/
COPY increment-version /root/.local/bin/
COPY generate-version /root/.local/bin/