# Command Line Interface for Synology DiskStation Manager (DSM)
A simple command line interface for Synology's NAS Systems

## How to use it

1. Clone this repository
2. Authenticate (you can pass a Session Name or let it generate one at random):

```
python ./synocli.py login -u myUser -p "myPassword" -r "http://192.168.1.40:5000"
python ./synocli.py login -u myUser -p "myPassword" -r "http://192.168.1.40:5000" -s DevDSM
```

3. Check CLI Help to look at available Commands:

```
python ./synocli.py -h
```

4. Check CLI Help to look at available subcommands for a given command:

```
python ./synocli.py auth -h
```

5. Check CLI Help to look at available parameters for a given subcommand:
```
python ./synocli.py auth login -h
```

## Things to know:

Before you can run any of the commands, you need to **authenticate** using *python ./synocli.py auth login*:

```
python ./synocli.py login -u myUser -p "myPassword" -r "http://192.168.1.40:5000"
```

The **authentication token** along with the **URL** and DSM Version passed in the authentication call are **stored locally** and **do not need to be passed as parameters beyond the first authentication call**.

The **Session Name** needs to be passed in all calls (it serves to retrieve the URL and Authentication Token dynamically)

Apart from the initial authentication call, each call should contain **at least 1 option**: **-s** (**-s** is used to specify the **Session Name**.)

The output format can be set to CSV, DF (DataFrame) or JSON (Default) by using the -f option in addition to the -s option


## Commands & Subcommands Currently Available:

* auth
  * login: authenticate to DSM
  * logout: logout of DSM
  * list: list existing Sessions
* network
  * show: show network information
* packages
  * list
  * start
  * stop
* download station (dsm)
  * list

## Examples
```
# Authenticate
./synocli.py auth login -u myUser -p "myPassword" -r "http://192.168.1.100:5000"
```


```
# List Download Station entries (and display as a Dataframe)
./synocli.py -s OrangeCat -f DF dsm list
```

```
# List Download Station entries (and display as a CSV)
./synocli.py -s OrangeCat -f CSV dsm list
```

```
# List Download Station entries (and display as JSON)
./synocli.py -s OrangeCat dsm list
```
## TO DO

add a list of python dependencies
