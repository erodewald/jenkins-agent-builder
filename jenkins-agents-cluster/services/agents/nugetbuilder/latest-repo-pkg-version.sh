response=$(mono /root/nuget.exe list $1 -Source https://nexus.fod247.io/repository/nuget-hosted/| head -n 1)
if [ "$response" == "No packages found." ]; then
    echo 0.0.0
else
    echo "$response" | cut -d' ' -f2
fi
