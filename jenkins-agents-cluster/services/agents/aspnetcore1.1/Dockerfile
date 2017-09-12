FROM microsoft/aspnetcore-build:1.1
WORKDIR /app

# Install Python PIP
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

# Install AWS CLI
RUN pip install --upgrade --user awscli

# Install ECS Deploy command
RUN pip install ecs-deploy

# Add AWS CLI to PATH
ENV PATH="~/.local/bin:${PATH}"

# Install docker
RUN curl -sSL https://get.docker.com/ | sh