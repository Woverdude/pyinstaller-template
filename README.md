# pyinstaller-template
A template for creating Python programs that are delivered with a Pyinstaller binary.

--------------------------------------------------------------------------------------

Author: Woverdude
Purpose: So that I don't have to start from scratch every damn time I need to use 

pyinstaller on a project.
Github:

What is Pyinstaller?

http://www.pyinstaller.org/

How do I compile?

Pyinstaller compiles for the environment that your code is being compiled in. So, if 

you compile your code in 64-bit Ubuntu Python 2.7., then the produced binary will run 

properly in environments that meet the same description. For Windows 7 32-bit Python 

3.X, compile in that same environment.

Process:

If in Windows, 'pip-Win_1.8.exe'. Run the following command in the 'Command' box:

	venv -c -i  pyi-env-name 

Then, run pyinstaller with the options that you would like. An example is below:

	pyinstaller example.py -c -F -n PythonTemplate

Result:

Once compiled, look for your binary in the 'dist' directory. Run it as needed.

Useful Options:

-F Put everything into one executable binary file
-D Put everything into one directory
-n Specify binary's filename
-c Compiled code runs within a console that pops up.
-d Compiled code will run in debug mode.

Documentation:

https://pyinstaller.readthedocs.io/en/stable/installation.html#installing-in-windows
https://pyinstaller.readthedocs.io/en/stable/usage.html#options
https://github.com/pyinstaller/pyinstaller/wiki/FAQ
