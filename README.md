# LogMe

Simple debugging tool for logging tsp measurements for debugging purposes.

Uses a sqlite3 database for logging measurements created by a Python
script.

## Installation

1. Download the following python module:

    ```
    $ wget https://raw.githubusercontent.com/jdgwartney/metric-log/master/logme.py
    ```

2. Place file with existing python files

3. Import the module

4. Initialize an instance optionally specifying the path to the
sqlite3 database

3. Instrument code (see section on nstrumenting code)

## Instrumenting code

The steps to instrument the code are as follows:

1. Import the module

    ```python
    import logme
    ```

2. Create an instance of `LogMe`. The construct takes a single argument of `db_path`,
which defaults to `measurement.db`

    ```python
    log = LogMe(db_path=<path to database to write measurements>)
    ```

3. Call either the `log` or `logbatch` on the instance with measurements
sent using the TrueSight Pulse measurement API.

## Example

A completed example is shown [here](send_log.py)



