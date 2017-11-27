FROM microsoft/aspnetcore-build:2.0.0
USER root

RUN apt-get update && apt-get -y install curl
RUN apt-get -y install mono-complete
RUN wget https://dist.nuget.org/win-x86-commandline/latest/nuget.exe -P /root

#add our source for debugging scripts
#RUN mono /root/nuget.exe sources Add -Name "nexus" -Source https://sonatype-nexus.fod247.io/repository/nuget-hosted/

ENV PATH="/root:/root/.local/bin:${PATH}"

COPY latest-repo-pkg-version.sh /root/.local/bin/
COPY version-compare.sh /root/.local/bin/

RUN chmod 755 /root/.local/bin/latest-repo-pkg-version.sh
RUN chmod 755 /root/.local/bin/version-compare.sh