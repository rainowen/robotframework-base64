*** Settings ***
Library             Base64Library
Library             OperatingSystem
Library             String
Library             Collections

*** Variables ***
${hello}    hello_world

*** Test Cases ***

Check functions
    Log    ${hello}
    ${rsp2} =    BASE64_ENCODING    ${hello}
    Log     ${rsp2}
    ${rsp3} =    BASE64_DECODING    ${rsp2}
    Log    ${rsp3}
    Should Be Equal As Strings    ${hello}    ${rsp3}

