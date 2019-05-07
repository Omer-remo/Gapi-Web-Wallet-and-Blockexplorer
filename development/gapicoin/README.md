# Welcome to Gapi-Web-Wallet-and-Blockexplorer

It is the most popular and original gapicoin python script. The code is exceptionally portable and has been used successfully on a very broad range of ubuntu systems and hardware.

## Contact

[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/gapicoin.svg?style=social)](https://twitter.com/gapicoin/)
[![GitHub Issues](https://img.shields.io/badge/open%20issues-0-yellow.svg)](https://github.com/Omer-remo/Gapi-Web-Wallet-and-Blockexplorer/issues)


- Report bugs, issues or feature requests using [GitHub issues](issues/new).



## Getting Started

The Gapicoin Documentation site hosts the **[gapicoin homepage](http://gapicoin.com/)**, which
has a Quick Start section.

Operating system | Status
---------------- | ----------
Ubuntu and macOS | [![TravisCI](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://travis-ci.org/gapicoin/gapicoin-github)
Windows          | [![AppVeyor](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://ci.appveyor.com/project/gapicoin/gapicoin-github)


```shell
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install vim -y && sudo apt-get install python-dev -y && sudo apt-get install libevent-dev -y &&  sudo apt-get install python-virtualenv -y && apt-get install git -y
```



## Install python last version..

```shell
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo apt-get install python3.4
sudo apt-get install python3-pip
pip install --upgrade virtualenv
```

## Other configurations..

```shell
virtualenv -p python3 venv
pip install -r requirements.txt
pipenv install requests
```


## After clone our project.

```shell
export DJANGO_SETTINGS_MODULE=gapicoin.settings
```




## Circus: A Process & Socket Manager configurations
The simplest way to install it is to use pip, a tool for installing and managing Python packages:
```shell
pip install circus
pip install circus-web
pip install chaussette
```

example.ini
```shell
[watcher:startserver]
cmd = /opt/venv/bin/gunicorn_start
numprocesses = 1
[watcher:starttcpconnections]
cmd = python /opt/venv/gapicoin/server.py
numprocesses = 1
```

The file is then passed to circusd:
```shell
circusd example.ini
```

You can exist from program if already running.
```shell
circusctl quit --waiting
```

# REST APIs

## GET Endpoints
 * `http://gapicoin.com/api/v1/createnewwallet/` - to create new wallet and private key.

 * `http://gapicoin.com/api/v1/alltransactions/` -  to get all transactions from database.

 * `http://gapicoin.com/api/v1/gettransaction/$transactionID` -  to get transaction details.

 * `http://gapicoin.com/api/v1/getwalletfrompkey/$publicKey` -  to create new wallet and private key.

 * `http://gapicoin.com/api/v1/getpublickeyfromprikey/$privateKEY` -  to get public key from private key.

 * `http://gapicoin.com/api/v1/getbalance/$wallet` -  to get last balance from wallet.

 *  `http://gapicoin.com/api/v1/getwalletdetails/$wallet` -  to get all wallet history.





## POST Endpoints
  * `http://gapicoin.com/api/v1/sendgapicoin/`
  * `sprikey` sender's private key
  * `receiverwallet`  receiver's wallet
  * `amount`  and amount.
  ___


## Donations
  * Project gapicoin Wallet : `GAPI58cde6448cdfec78d0407658c52e5c`

## License

[![License](https://img.shields.io/github/license/ethereum/cpp-ethereum.svg)](LICENSE)

All contributions are made under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html). See [LICENSE](LICENSE).
