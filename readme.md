# Install ampy

``` bash
python3 -m venv .venv
. .venv/bin/activate
pip install adafruit-ampy
.venv/bin/ampy --help
```

# Use with ampy
```bash
# set up for convenient use
export AMPY_PORT=/dev/ttyUSB0
export PATH=.venv/bin:$PATH

# list content
ampy ls
```
