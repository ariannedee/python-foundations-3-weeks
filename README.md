# Hands-on Python Foundations in 3 Weeks

This is the code for the *O'Reilly Live Training* - **Hands-on Python Foundations in 3 Weeks** presented by Arianne Dee

Before the class, please follow these instructions:

1. [Install Python](#1-install-python-36-or-higher)
2. [Install PyCharm](#2-download-pycharm-community-edition)
3. [Install Git](#3-install-git)
4. [Clone the code](#4-clone-the-course-repository)
5. [Make sure that you can run Python in PyCharm](#5-make-sure-that-you-can-run-python-in-pycharm)

## Set up instructions

### 1. Install Python 3.6 or higher

Go to https://www.python.org/downloads/

<img width="60%" src="docs/img/python_download.png">

**Mac/Linux**: Follow the prompts and install using the default settings.

**Windows**:

- You're installing Python now - [instructions](docs/WININSTALL.md)

- You've already installed Python - [instructions](docs/WINSETPATH.md)

### 2. Download PyCharm CE

Download the free, community edition
https://www.jetbrains.com/pycharm/download/

Install, open, and use the default settings.

### 3. Install Git

Follow your operating system instructions if you don't already have Git installed: 
[Git install instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 4. Clone the course repository 

Get the code for this course using Git.

**Option 1**

If you aren't familiar with Git, you can use PyCharm to clone a Git repository.

In PyCharm, when choosing which project to open, choose "Get from VCS" (clone from Git, which is a **v**ersion **c**ontrol **s**ystem)

[See full instructions](docs/PYCHARM_GIT_CLONE.md)

**Option 2**

If you know Git, clone the repository and then open the `python-foundations-3-weeks` folder in PyCharm.

### 5. Make sure that you can run Python in PyCharm

With the `python-foundations-3-weeks` folder open in Pycharm:

1. In the left panel, navigate to `examples/example_1_first_code.py` and double click to open it in the editor

2. On the open file, right click and select **Run 'example_1_first_code'**

3. In the Run tab on the bottom, you should see
   `Process finished with exit code 0`

4. Otherwise, if you got an error (exit code 1 in red), follow the instructions for setting your Python version in PyCharm below

### If you received an error running example_1_first_code, set your Python version in PyCharm

On a Mac:

- Go to **PyCharm** > **Preferences**

On a PC:

- Go to **File** > **Settings**

Once in Settings:

- Go to **Project: python-foundations-3-weeks** > **Project Interpreter**
- Look for your Python version in the Project Interpreter dropdown and select it. Please use Python 3.6 or higher.
- If you found it, click OK and try running `example_1_first_code` again
- Otherwise, if your version wasn't there, click **gear icon** > **Add...**
- In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
- If it's not there, click the **...** button and navigate to your Python location
- **Note:** For this last step, you may have to search the internet for where Python gets installed by default on your operating system

If you are having trouble configuring your Python version, you can find visual instructions
here: [Python interpreter setup](docs/PYCHARM_INTERPRETER.md)

## FAQs

### Can I use Python 2?

No, Python 2 is out of date. Please download a version that is at least Python 3.6.

### Can I use a different code editor besides PyCharm?

Yes, but it is only recommended if you are already know it and are comfortable navigating to different files and running commands in the command line.
If it has syntax highlighting for Python, that is ideal.

If you are using VS Code, make sure the Python plugin is installed.

### PyCharm can't find Python 3

Follow the instructions for [Python interpreter setup](docs/PyCharm_interpreter.md)
