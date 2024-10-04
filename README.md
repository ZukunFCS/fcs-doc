# FCS User manual
This repository stores the user manual of all public versions of FCS. 
You can directly view the [hosted version here](https://zukunfcs.github.io/fcs-doc/latest/en/index.html)

## Build locally
If you require an offline manaul please feel free to build it yourself. 

### HTML
```
cd doc
python build_docs.y
```
You should find all documents in `doc/_build/html` after the script finishes. 


### PDF


----
## Contributing
If you were so kind to contribute, please feel free to do so. 

### Update translations
```
cd doc
make gettext
sphinx-intl update -p _build/gettext -l en
```