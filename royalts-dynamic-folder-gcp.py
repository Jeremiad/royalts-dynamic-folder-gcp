import json, subprocess, sys, logging

def get_instances(project, account = "", gateway = ""):
    cmd = "gcloud compute instances list --format json --project " + project

    if account != "$CustomProperty.Account$":
        if account != "":
            cmd += " --account " + account

    gcp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (response_json, err) = gcp.communicate()
    exit_code = gcp.wait()

    response = json.loads(response_json)

    connections = []

    for instance in response:
        connection = {}
        public_ip_address = ""
        private_ip_address = ""
        for nics in instance.get("networkInterfaces"):
            if nics.get("accessConfigs") != None:
                for extnic in nics.get("accessConfigs"):
                    if extnic.get("natIP") != None:
                        public_ip_address = extnic.get("natIP")
            private_ip_address = nics.get("networkIP")
        connection["Name"] = instance.get("name")
        if public_ip_address != "":
            connection["ComputerName"] = public_ip_address
        else:
            connection["ComputerName"] = private_ip_address
            if gateway != "$CustomProperty.Gateway$":
                if gateway != "":
                    connection["SecureGatewayID"] = gateway
        connection["Type"] = "TerminalConnection"
        connection["TerminalConnectionType"] = "SSH"
        connection["CredentialsFromParent"] = "true"
        #connection["SecureGatewayFromParent"] = "true"
        connections.append(connection)

    store = {
        "Objects": connections
    }

    return json.dumps(store)

def royalts():
    project = "$CustomProperty.Project$"
    account = "$CustomProperty.Account$"
    gateway = "$CustomProperty.Gateway$"
    print(get_instances(project, account, gateway))

def development():
    try:
        if len(sys.argv) != 1 and len(sys.argv) <= 4:
            print(json.dumps(get_instances(sys.argv[1], sys.argv[2]), indent=2))
    except IndexError:
        print("Index error")
    except TypeError:
        print("Type error")
    except:
        print("General error")

def main():
    royalts()
    #development()

if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    main()