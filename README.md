# what
## Description
Python Package to help look up coding errors.
Simply type "what" after getting an error from a piece of code and a Google or StackOverflow search will appear with your error.
## How to run
```
$git clone 
$cd what
```
If you don't have virtualenv for python installed, run this command.
```
$pip install virtualenv
```
Next,
```
$virtualenv -p python3 venv
$source venv/bin/activate
$pip install -e .
```
You are now ready to use what.
## Example
```
$python 
/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python: can't open file 'main.py': [Errno 2] No such file or directory
$what
```
This will pull up a google search with the error.
