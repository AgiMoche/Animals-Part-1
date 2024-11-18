Animals Part 1. OOP basics (224) 
For raw project instructions see: http://syllabus.africacode.net/projects/oop/animals/part1/

## Project Setup

### 1. Environment Setup:
In the instructions below, information is provided to install the necessary tools needed to run the notebook and its dependencies on any capable machine:
- Set up Python on your computer. Refer to: [GETTING SET UP TO WRITE PYTHON ON YOUR COMPUTER](http://syllabus.africacode.net/environment-setup/python-on-computer/index.html).
- Configure Git on your system. Follow the instructions in: [GETTING GIT SET UP](http://syllabus.africacode.net/environment-setup/git/).
- Additional resources: [MORE ABOUT GIT](https://docs.github.com/en/get-started/using-git/about-git).
- To avoid reading and following the above-mentioned instructions on setting up an environment for the project, command prompts can be used in Windows Terminal or Command Prompt as follows:
  1. Create a new virtual environment to run the tests in by using the following command in the terminal window: 
  ~~~
  python -m venv <virtual_environment_name>
  ~~~
  2. Activate the new virtual environment that you just created using the following command:
  ~~~
  <virtual_environment_name>\Scripts\activate
  ~~~
  3. Download all the folders associated with the Animals OOP basics project in the activated virtual environment
  4. Open all the cloned and downloaded folders associated with the Animals OOP basics project in the activated virtual environment
- Once the virtual environment has been set up and activated, you will need to install all the relevant packages for the project in development mode
- The packages will need to be installed in the newly activated virtual environment by running the following command in the Windows Terminal or Command Prompt:
1. Ensure that Setuptools is installed on your machine. If you are unsure that Setuptools is installed on your machine, use the following command in the virtual environment Command Terminal or Windows Terminal to install it:
~~~
pip install setuptools
~~~
2. Once Setuptools has been installed on your machine, the packages will need to be installed in the newly activated virtual environment by running the following command in the Windows Terminal or Command Prompt:
~~~
python setup.py develop
~~~
  
### 2. Cloning the Repository:
In the instructions below, information is provided to clone the repository of the project. Cloning the repository pulls down a full copy of all the repository data associated with the GitHub.com uploads:
- To clone the project repository, check [CLONING THE REPOSITORY](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#creating-remote-repositories) for instructions.
- Link to repository - https://github.com/Umuzi-org/Oageng-Moche-224-animals-part-1-oop-basics-python
- To avoid reading and following the above-mentioned instructions on cloning the project's repository, a command prompt can used in Windows Terminal or Command Prompt as follows: 
~~~
git clone https://github.com/Umuzi-org/Oageng-Moche-224-animals-part-1-oop-basics-python
~~~
  
### 3. Installing the Required Python Packages:
Once the repository has been cloned and the virtual environment has been set up:
1. Navigate to the project directory by using the following command in the virtual environment Command Terminal or Windows Terminal:
~~~
cd Oageng-Moche-224-animals-part-1-oop-basics-python
~~~
2. In the Windows Terminal or Command Prompt of the virtual environment, type in the following command to install the modules required to run the files for the project:
~~~
pip install -r requirements.txt
~~~

### 4. Running the Animals OOP basics project and its test cases:
- After installing the required packages, make sure you are in the project directory 
- If you are not in the project directory or unsure that you are in the project directory, navigate to the project directory by using the following command in the virtual environment Command Terminal or Windows Terminal: 
~~~
cd Oageng-Moche-224-animals-part-1-oop-basics-python
~~~
- To run the tests/test cases of the project, ensure that pytest is installed on your machine. If you are unsure that pytest is installed on your machine, use the following command in the virtual environment Command Terminal or Windows Terminal to install pytest:
~~~
pip install pytest
~~~
- Once pytest has been installed on your machine, to run the tests/test cases of the project, use the following command in the virtual environment Command Terminal or Windows Terminal:
~~~
python -m pytest
~~~

### 5. Deactivating environment setup:
Once the necessary tasks have been completed, deactivate the virtual environment that was set up to run the tasks by typing the following command in the Windows Terminal or Command Prompt:
~~~
deactivate
~~~
