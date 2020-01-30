# briansimulator.org

## Installing

```
    conda create --name nikola python=3
    conda activate nikola
    pip install Nikola[extras]
```

## Building the website locally
```
    conda activate nikola
    nikola build
```

Depending on your configuration, you might have to set an environment variable
to avoid conflicts over the jupyter configuration. E.g. on Windows:
```
    conda activate nikola
    set JUPYTER_CONFIG_DIR=.
    nikola build
```

To serve the website locally:
```
    nikola serve -b
```

Alternatively, you can use the following command to develop locally, it will
build and serve the website, and rebuild it whenever a file changes:
```
    nikola auto
```

## Deploy the website
```
    nikola github_deploy
```

## Writing articles

Articles are jupyter notebook files. By default, a special header is added to
their rendering on the website. This header contains an automatically generated
"launch binder" badge, and a link to the general "Notes on Notebooks" article.
Note that this header is only included on the website, it will not be shown on
binder or when downloading the notebook.

If you do not want this header to be added, set `hide_notebook_header` to `true`
in the notebook's metadata.
