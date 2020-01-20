# briansimulator.org

## Installing and building on Windows

The following commands to install:

    conda create --name nikola python=3
    activate nikola
    pip install Nikola[extras]
    pip install jupyter
    
Then to build:

    activate nikola
    set JUPYTER_CONFIG_DIR=.
    nikola build
    
And to serve locally:

    nikola serve -b