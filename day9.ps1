#region foreach
$servers = @('localhost','SRV2','SRV3','SRV4')

#Iterating over each element in the array and running some code for "for each" item
foreach($server in $servers) {
    write-Host "Im processing server $server rightnow..."
}

$servers.Count

##Useful for smaller arrays to use the pipeline
$servers | ForEach-Object {
    write-Host "Im processing server $_ right now..."
}

##the foreach( method () a method on an array: fastest)
$servers.forach({Write-Host "Im processing server $_ right now..."})

