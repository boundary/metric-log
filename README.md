# LogMe

Simple debugging tool for logging tsp measurements for debugging purposes.

Uses a sqlite3 database for logging measurements created by a Python
script.

**NOTE:** sqlite3 has been included in python since version 2.5.

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

## Instrumenting Code

The steps to instrument the code are as follows:

1. Import the module

    ```python
    import logme
    ```

2. Create an instance of `LogMe`. The construct takes a single argument of `db_path`,
which defaults to `measurement.db`

    ```python
    logdb = LogMe(db_path=<path to database to write measurements>)
    ```

3. Call either the `log` or `log_batch` on the instance with measurements
sent using the TrueSight Pulse measurement API.

    ```python
    timestamp = int(datetime.now().strftime("%s"))
    logdb.log(metric='MY_METRIC', value=42, source='foo', timestamp=timestamp)

    ```
or    

    ```python
    measurements = []
    measurements.append(Measurement(metric='CPU', value=randrange(0, 100) / 100.0,
                                            source='red', timestamp=timestamp))
    measurements.append(Measurement(metric='CPU', value=randrange(0, 100) / 100.0,
                                            source='green', timestamp=timestamp))
    measurements.append(Measurement(metric='CPU', value=randrange(0, 100) / 100.0,
                                            source='blue', timestamp=timestamp))
    logdb.log_batch(measurements)
    ```

## Instrumentation Code Example

A complete instrumented example is shown [here](send_log.py)

## Viewing the Collected Measurements

The collected data can be viewing by the invoking the `sqlite`
command line tool:

```bash
$ sqlite3 <path to database file> 'select * from measurement'
CPU|0.12|foo|1466615494
CPU|0.09|red|1466615494
CPU|0.56|green|1466615494
CPU|0.05|blue|1466615494
CPU|0.44|foo|1466615500
CPU|0.35|red|1466615500
CPU|0.57|green|1466615500
CPU|0.86|blue|1466615500
CPU|0.3|foo|1466617532
CPU|0.41|red|1466617532
CPU|0.82|green|1466617532
CPU|0.53|blue|1466617532
```

## Exporting the Collected Measurements

1. Open the database file by invoking the `sqlite` command tool:

    ```bash
    $ sqlite3 <path to database file>
    ```
    
2. At the sqlite prompt, run the following:

    ```bash
    sqlite> .headers on
    sqlite> .mode csv
    sqlite> .output measurement.csv
    sqlite> select * from measurement;
    sqlite> .output stdout
    ```
    
3. Exit the `sqlite` command line utility

    ```bash
    sqlite> .quit
    ```

4. The export file will be in the directory where you invoked the `sqlite`
command line tool:

    ```bash
    cat measurement.csv
    metric,value,source,timestamp
    CPU,0.12,foo,1466615494
    CPU,0.09,red,1466615494
    CPU,0.56,green,1466615494
    CPU,0.05,blue,1466615494
    CPU,0.44,foo,1466615500
    CPU,0.35,red,1466615500
    CPU,0.57,green,1466615500
    CPU,0.86,blue,1466615500
    CPU,0.3,foo,1466617532
    CPU,0.41,red,1466617532
    CPU,0.82,green,1466617532
    CPU,0.53,blue,1466617532
    ```





