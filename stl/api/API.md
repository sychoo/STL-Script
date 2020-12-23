# How to import/invoke the STL API from other modules?

## Temporary Solution
```bash
import sys
sys.path.append("/path/to/STL-Script/directory/")
import stl.api
```
## Permanently Solution

Adding the following line to your shell configuration file (in Unix-based OS). For Mac users, the default shell configuration file is ~/.zshrc

```bash
export PYTHONPATH="/path/to/STL-Script/directory:$PYTHONPATH"
```

Then, execute the following command on the command line (for .zshrc)

```bash
source ~/.zshrc
```
