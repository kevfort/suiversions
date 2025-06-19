import requests
# TODO iterate releases
# # TODO Robust if mainnet not found... fatal error.
def get_version_number(owner, repo_name):
    endpoint = "https://api.github.com/repos/{owner}/{repo_name}/releases"
    response = requests.get(endpoint.format(owner=owner,repo_name=repo_name))
    version_types = {
        "testnet": None,
        "devnet": None,
        "mainnet": None
    }
    if response.status_code == 200:
        data = response.json()
        for release in data:
            
            if version_types["testnet"] is None:
                if "testnet" in release["tag_name"]:
                    version_types["testnet"] = release["tag_name"]

            elif version_types["devnet"] is None:
                if "devnet" in release["tag_name"]:
                    version_types["devnet"] = release["tag_name"]

            elif version_types["mainnet"] is None:
                if "mainnet" in release["tag_name"]:
                    version_types["mainnet"] = release["tag_name"]

            else:
                print("All versions found")
                break

    elif response.status_code == 404:
        return("Not Found")

    if list(version_types.values()).count(None) == 0:
        return(version_types) 
    
    else:
        raise Exception("1")
        #return("1") #One or more of the versions were not found

print(get_version_number("MystenLabs", "sui"))

page_content = """
<!DOCTYPE html>
<html>
<p>sui testnet version:{testnet_ver}</p>
<p>sui devnet version:{devnet_ver}</p>
<p>sui mainnet version:{mainnet_ver}</p>
</html>
"""
versions = get_version_number("MystenLabs", "sui")
with open("index.html", "w") as file:
    file.write(page_content.format(testnet_ver=versions["testnet"],
                                   devnet_ver=versions["devnet"], 
                                   mainnet_ver=versions["mainnet"]))


    