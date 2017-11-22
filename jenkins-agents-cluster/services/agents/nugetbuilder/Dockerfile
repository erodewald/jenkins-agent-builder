FROM microsoft/aspnetcore-build:2.0.0
USER root

RUN apt-get update && apt-get -y install curl
RUN apt-get -y install mono-complete
RUN wget https://dist.nuget.org/win-x86-commandline/latest/nuget.exe -P /root
RUN mono /root/nuget.exe install

ENV PATH="/root:/root/.local/bin:${PATH}"

RUN echo $PATH

COPY latest-repo-pkg-version.sh /root/.local/bin/
COPY version-compare.sh /root/.local/bin/

RUN chmod 755 /root/.local/bin/latest-repo-pkg-version.sh
RUN chmod 755 /root/.local/bin/version-compare.sh