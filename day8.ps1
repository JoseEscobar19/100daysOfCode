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

#to set a variable to be constant and anti change you do the 
Set-Variable -Name 'color' -Value 'green' -Option Constant
#this tells the variable named color, that has value green, to be a contant and anti chnage
$color
#if you try to change it to blue from the current green
$color = 'blue'
#itll give an error


# to run two commands at the same time you can use the ; semicolo
#this allows for the console to run two commands

ping.exe 127.0.0.1 -n 1 ; $LastExitCode

#objects in powershell




$serviceName = 'wauserv
Get-Service -Name $ServiceName
