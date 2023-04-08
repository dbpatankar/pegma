![PEGMA](./pegma_bg.png)

# PEGMA: Package for Exploratory Ground Motion Analysis
This is a package for seismologists and earthquake engineers for exploratory analysis of ground motions. It can help in analyzing and selecting the ground motions based on their characteristics.

# Installation and usage
Installation is straight forward using `pip`. However, I have noticed that sometimes the dependency resolution messes up and need to be resolved manually. Instead, I provide you with a list of commands which will install all the dependencies first and then `pegma`. I also recommend not skipping the optional first step of creating a virtual environment. 

## Linux/Mac

### Create a virtual environment (Optional but highly recommended)
Open terminal and enter following commands
```sh
python -m venv $HOME/trypegma # Give any name of your choice instead of trypegma
source $HOME/trypegma/bin/activate
```
This will create a directory named `trypegma` in your `$HOME` directory and source the new virtual environmant for you to use. Following two steps must be executed in the same terminal instance without closing it (and not in any other terminal instance).

### Install the dependencies
```python
python -m pip install matplotlib numpy scipy pyside6 earthquakepy
```

### Install PEGMA
```python
python -m pip install pegma
```

### Use
Once the installation is successful, you can launch `pegma` using command `pegma`. But every time you should first activate the virtual environment. So you need to use following two commands (if you followed first optional step), or only the second command (if you did **not** follow the first optional step)
```sh
source $HOME/trypegma/bin/activate
pegma
```

## Windows

### Create a virtual environment (Optional but highly recommended)
Open terminal and enter following commands
```sh
python -m venv trypegma # Give any name of your choice instead of trypegma
trypegma\Scripts\activate.bat
```
This will create a directory named `trypegma` in your current working directory and source the new virtual environmant for you to use. The following two steps must be must be executed in the same command prompt instance without closing it (and not in any other command prompt instance).

### Install the dependencies
```python
python -m pip install matplotlib numpy scipy pyside6 earthquakepy
```

### Install PEGMA
```python
python -m pip install pegma
```

### Use
Once the installation is successful, you can launch `pegma` using command `pegma`. But every time you should first activate the virtual environment. So you need to use following two commands (if you followed first optional step), or only the second command (if you did **not** follow the first optional step)
```sh
trypegma\Scripts\activate.bat
pegma
```

# Removing PEGMA
In case you need to remove `PEGMA`, simply delete the `trypegma` directory (if you followed the first optional step) or `pip uninstall pegma` (if you did not follow the first optional step).
