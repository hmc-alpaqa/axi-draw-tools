In order to install the AxiDraw program, start by ensuring you have python3
and git installed on your system. If so, create a parent directory to house
all your AxiDraw related code, here assumed to be `~/Documents/AxiDraw`.

Once you are in the `AxiDraw` directory, start by running

```sh
~/Documents/AxiDraw$ python3 -m venv axi-venv
```

This will create a virtual Python environment which will house the AxiDraw
API. You can replace `axi-venv` with whatever name you want for your virtual
environment.

Next, run `source axi-venv/bin/activate` to activate the virtual environment.
Your shell should now be prefaced with `(axi-venv)` like this:

```sh
(axi-venv) ~/Documents/AxiDraw$
```

Now we will download the source code for the AxiDraw API using
`git clone https://github.com/notpeter/AxiDraw_API`.

Once that has finished downloading, change directories into the API folder
with `cd AxiDraw_API` and then run

```sh
(axi-venv) ~/Documents/AxiDraw/AxiDraw_API$ pip install .
```

This will install the `axicli` engine and `pyaxidraw` in the environment.
You can test to make sure the install has worked by running `axicli -h`,
which should show the help text for the command line tool.

You can now change directories out of the API folder and begin using
the AxiDraw cli and python tools, either in a new folder or in the parent
directory. Remember that you must have the `axi-venv` environment activated
in order to access these tools.

If you want to make it easier to activate the environment from anywhere,
you can add the following bash alias. Start by running `nano ~/.bashrc`
to edit your bash config file, scroll to the very bottom, and then add the
line:

```sh
alias axisetup='source $HOME/Documents/AxiDraw/axi-venv/bin/activate'
```

Now, no matter what directory you are in, if you run `axisetup` you will
automatically activate the virtual environment, giving you access to the
python and cli implementations.
