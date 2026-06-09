import urllib.request
import json
import os
import ssl

packages = ["pyttsx3", "pyobjc", "pyobjc-core", "pyobjc-framework-Cocoa"]
dest_dir = "./wheels"
os.makedirs(dest_dir, exist_ok=True)

user_agent = "curl/7.64.1"
ssl_context = ssl._create_unverified_context()

for pkg in packages:
    print(f"Fetching metadata for {pkg}...")
    url = f"https://pypi.org/pypi/{pkg}/json"
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    try:
        with urllib.request.urlopen(req, context=ssl_context) as response:
            data = json.loads(response.read().decode())
            
            releases = data["urls"]
            wheel_url = None
            filename = None
            
            for release in releases:
                url_str = release["url"]
                fname = release["filename"]
                packagetype = release["packagetype"]
                
                if packagetype == "bdist_wheel":
                    if "macos" in fname or "macosx" in fname:
                        # Match cp314 wheels for Python 3.14 (Homebrew)
                        if "cp314" in fname and ("arm64" in fname or "universal2" in fname or "any" in fname):
                            wheel_url = url_str
                            filename = fname
                            break
                    elif "none-any" in fname:
                        wheel_url = url_str
                        filename = fname
                        break
            
            if not wheel_url:
                for release in releases:
                    url_str = release["url"]
                    fname = release["filename"]
                    if fname.endswith(".whl") and "none-any" in fname:
                        wheel_url = url_str
                        filename = fname
                        break
                    elif fname.endswith(".tar.gz"):
                        wheel_url = url_str
                        filename = fname
            
            if not wheel_url and releases:
                for release in releases:
                    if release["filename"].endswith(".whl"):
                        wheel_url = release["url"]
                        filename = release["filename"]
                        break
            
            if wheel_url:
                print(f"Downloading {filename} from {wheel_url}...")
                dl_req = urllib.request.Request(wheel_url, headers={'User-Agent': user_agent})
                with urllib.request.urlopen(dl_req, context=ssl_context) as dl_resp:
                    with open(os.path.join(dest_dir, filename), "wb") as f:
                        f.write(dl_resp.read())
                print(f"Successfully downloaded {filename}")
            else:
                print(f"No suitable release found for {pkg}")
                
    except Exception as e:
        print(f"Error processing {pkg}: {e}")
