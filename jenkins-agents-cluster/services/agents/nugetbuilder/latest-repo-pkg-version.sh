getLatestPackage () {
    nuget list $1
    latestPackage=$?
    return $latestPackage | cut -d' ' -f2
}
getLatestPackage $1