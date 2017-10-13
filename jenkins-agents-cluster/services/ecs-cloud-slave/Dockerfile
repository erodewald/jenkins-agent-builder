FROM jenkinsci/jnlp-slave:3.10-1

USER root

RUN apt-get -qq update \
   && apt-get -qq -y install \
   curl golang-go

RUN curl -sSL https://get.docker.com/ | sh

RUN usermod -a -G staff,docker jenkins

# Setup gopath folder
RUN mkdir /usr/sbin/go
ENV GOPATH /usr/sbin/go
ENV PATH="$PATH:$GOPATH/bin"

# Install ecr=login credential helper to handle ECR login using IAM Auth
RUN go get -u github.com/awslabs/amazon-ecr-credential-helper/ecr-login/cli/docker-credential-ecr-login

# Configure docker to use ecr-login
RUN mkdir ~/.docker
RUN echo "{\n\"credsStore\": \"ecr-login\"\n}" >> ~/.docker/config.json