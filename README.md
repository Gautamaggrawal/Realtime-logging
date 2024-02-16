# Realtime-logging
Problem statement This problem requires you to implement a log watching solution (similar to the tail -f command in UNIX). However, in this case, the log file is hosted on a remote machine (same machine as your server code). The log file is in append-only mode.
In python django

You have to implement the following:

	1	 A server side program to monitor the given log file and capable of streaming updates that happen in it. This will run on the same machine as the log file. You may implement the server in any programming language. 
	2	 A web based client (accessible via URL like http://localhost/log) that prints the updates in the file as and when they happen and NOT upon page refresh. The page should be loaded once and it should keep getting updated in real-time. The user sees the last 10 lines in the file when he lands on the page. 

Problem Constraints The server should push updates to the clients as we have to be as real time as possible. Be aware that the log file may be several GB, how to optimise for retrieving the last 10 lines? The server should not retransmit the entire file every time. It should only send the updates. The server should be able to handle multiple clients at the same time.

The web page should not stay in loading state post the first load and it should not reload thereafter as well. You may not use off-the-shelf external libraries or tools to read the file or provide tail-like functionalities.

We will be evaluating you for code quality, testability, modularity, corner cases, etc.
