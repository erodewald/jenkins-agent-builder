echo $(mono /root/nuget.exe list $1 -Source https://sonatype-nexus.fod247.io/repository/nuget-hosted/| head -n 1 | cut -d' ' -f2)