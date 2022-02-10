# Module required to run
pip3 install pytest
pip3 install requests

# Environment variable setup before run in command line
For Windows
SET USER_NAME=<value>
SET PASS_WORD=<value>
For Linux
export USER_NAME=<value>
export PASS_WORD=<value>

# Command to run
Go to directory where python script is available, and run below command
pytest -v
