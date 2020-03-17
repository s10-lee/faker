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
--timeout, -t       Duration in minutes             [10 min]
--interval, -i      Event trigger interval          [12 sec]
--path, -p          Wildcard path to source dir     [None]
```

Timeout argument

```bash
python3 run.py --timeout 30 --interval 12
```