$RTSPSModule = Join-Path -Path ${env:ProgramFiles(x86)} -ChildPath 'code4ward.net\Royal TS V4\RoyalDocument.PowerShell.dll'
Import-Module $RTSPSModule

$gatewayName = "<gatewayName>"

$store = New-RoyalStore -UserName "<username>"

$doc = Open-RoyalDocument -store $store -FileName "<documentPath>" -password (Read-Host -AsSecureString "Secrets") 

$object = Get-RoyalObject -store $store -type RoyalSecureGateway -name $gatewayName

Write-Output $object.ID

Close-RoyalDocument -document $doc