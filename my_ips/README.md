# Ip

Simple script to get your private and public IP addresses

## Dependenccies
* Python 3 (this was written with Python 3.5)
* netinterfaces
* requests

## How to use

1. `git clone https://github.com/edjroz/ip.git`
    * Install the dependencies `pip install netinterfaces`
2. Modify the `get_priv()` method with the desired interface if needed
3. Run `python3 get_ip` (use parameters if you don't want the private ip address or want both addresses)

## Recomendations 
* Place the script in a directory linked wih the `/bin` (use a soft link so you dont get your scripts mixed with the systems)
* use `chmod a+x get_ip to make the file executable 
* run it from everywhere 
    
