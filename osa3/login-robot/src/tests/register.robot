*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle!  kalle123
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  ka
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekallekalle
    Output Should Contain  Password must contain at least one non-letter character