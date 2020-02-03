# infoAssignment2

so we have to add student id when agent is to be able to start crowling 
i already added mine


-------------------------------------
guys i had a hard time getting the enviroment setup but it turned out it only works on openalab to be able
to download the dependency so the only way to work on this assignment is on openlab.

i follow this instruction and it helped me to run the program




# curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"

# python get-pip.py

 

At this point, you should get a warning message about where you pip package lives:

WARNING: The scripts pip, pip2 and pip2.7 are installed in '/home/wvan/.local/bin' which is not on PATH

 

* My user is [wvan], change yours to fit *

Check the version of Pip that is installed (should mention 20.0.2):

# /home/wvan/.local/bin/pip -V

 

Finish up by running: 
	 NOTE: i didnt have master so i just used cd ~/spacetime-crawler4py/packages

# cd ~/spacetime-crawler4py-master/packages

# /home/wvan/.local/bin/pip install -r requirements.txt



 Try the following steps as per the professor's orientation:
 
	NOte: i think i did cd .. to go back to previous directory to install the rest, not remember 

install dependencies:  

pip3 install --user packages/spacetime-2.1.1-py3-none-any.whl
pip3 install --user -r packages/requirements.txt
pip3 install --user lxml

 

Now, configure your config.ini

launch it: python3 launch.py

It should try to run, but return: ConnectionRefusedError: [Errno 111] Connection refused

This just means that the server is still down.



