getLatestPackage () {
    echo $PATH
    mono /root/nuget.exe list $1
    latestPackage=$?
    return $latestPackage | cut -d' ' -f2
}
getLatestPackage $1