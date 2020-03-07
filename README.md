# Faking [hubstaff](https://hubstaff.com/) tracking

### Installation
Check versions and current user
```bash
whoami
which python3
python3 -V
pip3 -V
```
Install [pynput](https://pynput.readthedocs.io/en/latest/) library
```bash
pip3 install --user pynput
```
or 
```bash
sudo pip3 install pynput
```


### Usage 
Open terminal window in your IDE.  

```
python3 main.py [options]

Options:
--total, -t         Duration in minutes     [5 min]
--interval, -i      Keypress interval       [10 sec] 
```

Trigger keypress, every 12 seconds, for 30 minutes,  

```bash
python3 main.py --total 30 --interval 12
python3 main.py -t 30 -i 12
```

### Important
Terminal window should always be active, while script is running.