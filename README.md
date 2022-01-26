find_unused_import
==================
Yet another solution to **find_unused_import** 

General Info
============
  - My solution to **find_unused_import** problem of python.
  - One day I got an idea to recursively iterate over the ast tree and made this. 
  - Actually, the iteration should be handled with ast.NodeVisiter (which is used by autoflake8 and several others to remove unused import ) which I was not awareof.
  - The whole point of making this is using a naive approch to solve the find_unused_imports problem of python
  - I have zero to minimal design experience so any suggestions on design are welcome.
  - I hope I must have missed to parse some node from ast Like node related to Match of latest python release  
  - Play around with it and help me improve it.
 

How to Use
==========
 - Install the package using `sudo python setup.py install` and run
 - find_unused_imports --name=file_path
