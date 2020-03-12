# Faking [hubstaff](https://hubstaff.com/) tracking

### Requirements
- Python 3.5 
- [Pynput](https://pynput.readthedocs.io/en/latest/) package
```bash
pip3 install --user pynput
```

### Usage 
Open terminal from your IDE

```
python3 run.py [options]

Options:
--timeout, --time, -t   Duration in minutes     [10 min] 
```

Timeout argument

```bash
python3 main.py --timeout 30
```

Then follow the command line prompts
- Min interval  [default: 12 sec]
- Max interval  [default: 20 sec]