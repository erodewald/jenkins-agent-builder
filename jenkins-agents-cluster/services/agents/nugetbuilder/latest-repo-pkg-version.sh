echo $(mono /root/nuget.exe list $1 -Source https://sonatype-nexus.fod247.io/repository/nuget-hosted/| head -n 1 | cut -d' ' -f2)

# getLatestPackage () {
#     latestPackage=$(mono /root/nuget.exe list $1 -Source https://api.nuget.org/v3/index.json | head -n 1 | cut -d' ' -f2) #sed -n -e 1p
    
#     echo "$latestPackage"
# }
# getLatestPackage $1