#!/usr/bin/env bash
export user_id=423022171
export fsq_id=4e15daa2227165ad03b27dea
export member_expected_points=2250000
export ctyhocn1=ATLAAHH
export ctyhocn2=PRGOTHI
export ctyhocn3=HNLHVHH
export ctyhocn4=SMOPCDT
export ctyhocn5=AUSAHHF
export venue_count=150
export venue_entries=150
export base_path=localhost:8084
echo -e "\n$0 setting base_path set to: ${base_path}\n"
export console_username=admin
export console_password=admin
nose2 -v -c nose2_localhost.cfg --junit-xml
