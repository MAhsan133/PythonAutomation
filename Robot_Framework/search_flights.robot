*** Settings ***
Library         page_steps.py  Chrome
Suite Setup     Open
Suite Teardown  Close

*** Test Cases ***
The user can search for flights
    Select Departure City   Paris
    Select Destination City    London
    Search For Flights
    @{flights}=     Get Found Flights
    Should Not Be Empty     ${flights}