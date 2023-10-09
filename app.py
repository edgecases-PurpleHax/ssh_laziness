from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/')
def get_params():
    config = {}
    with open('hosts.json', 'r') as f:
        config.update(json.load(f))
    host = request.args.get("host")
    ip = request.args.get("ip")
    config[host] = ip
    with open('hosts.json', 'w') as f:
        f.write(json.dumps(config))
    with open('ssh_config', 'w') as f: # Change filename to the location of your ssh config, normally /home/$USER/.ssh/config
        f.write("""
        copy your ssh config here, change the Hostname field to {config['host']} and change this to an f string 
        (add f before the triple quotes)"
""")
    return "200"


if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0") #change debug=False
