#Install-Module -Name RoyalDocument.PowerShell
Import-Module RoyalDocument.PowerShell

$store = New-RoyalStore -UserName $args[1]

$gatewayName = $args[2]

$doc = Open-RoyalDocument -store $store -FileName $args[3] -password (Read-Host -AsSecureString "Secrets") 

$object = Get-RoyalObject -store $store -type RoyalSecureGateway -name $gatewayName

Write-Output $object.ID

Close-RoyalDocument -document $doc