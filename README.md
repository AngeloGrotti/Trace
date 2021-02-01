# Project Trace

I started this project out of bordem that turned into something exciting. 

I am by no means a master coder. 

This Project listens for a CDP packet then parses information that is wanted plus more and sends that information over to a web interface which inturn converts it into a SQL Query in a backend database

Please replace the the following fields in the code on line 69 :
servername
filename

You may also want to change on what interface the program listens for the CDP packet on line 24.

Install Modules :
pip install scapy, requests

Run :
python3 trace.py
