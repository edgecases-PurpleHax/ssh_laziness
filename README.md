# Quick Check in app for ssh clients that change often

## History

We have several hosts at my current role that we have to ssh into to perform penetration testing. Because of the setup
we are using, I needed a way to get the current host IP prior to logging in for the day. So, I wrote this quick little 
client server app to pull the host and IP and change my ssh config. When I log in, I ssh to the host without worrying
about the new IP if the lease was released or the server was rebooted.

## How to use
1. Install app.py on your machine. The "clients" must be able to reach your machine for this to work. 
2. Run app.py after running `pip install -r requirements.txt`
3. Install the appropriate client app on the hosts you need to check in. Client for unix like systems, client_windows
for MS Windows systems. (Windows clients will need python installed prior to use) run `pip install -r requirements.txt`
on the client. 
4. Generate the hosts.json based on the example_hosts.json 
5. Change main.py per comments 
6. Create a cron job/scheduled task to run client(_windows).py on the clients as appropriate.
7. Make sure to change main.py to point to your ssh config file. 

## Contributing

If you want to contribute, please create a branch called dev_yourusername. Make changes, push to remote, then create the
PR. Thank you :heart: