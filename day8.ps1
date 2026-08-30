# Powershell variables
# to define variables you put $ dollar sign and assign 

$filePath = 'C:\folder\subFolder\file.txt'

#if you close that sessionl it doesnt save the variable
#if you need a permanenet variale you need to use a comdlet

Set-Variable -Name filePath -Value 'C:\folder\subfolder\file.txt'

#now that variable is saved permanently even if you close the session

## automatic variables -read only - you cant change them
# powershell has many options
#for example, the comad $MaximumHistoryCount, 
#this tells how much history of command line history lines are saved
#we can change it because you dont need that much history 

$MaximumHistoryCount 
4096

$MaximumHistoryCount = 200

