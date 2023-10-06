import requests
from utils import string_utils
from os.path import abspath
from rich.progress import Progress

def download(url:str, file_preffix:str='', extension:str='bin') -> str:
    res:requests.Response = None
    file_name = string_utils.file_name(file_preffix, extension) if file_preffix.isspace() else ""

    if not file_name:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = url.split('/')[-1] # Extract file name using string split
        else:
            print("Error: Unable to retrieve the URL")
    try:
        res = requests.get(url, stream=True)
        total_size = int(res.headers.get('content-length', 0))
        with open(file_name, 'wb') as downloaded_file:
            try:
                progress = Progress()
                task = progress.add_task(f"[cyan]Downloading... {string_utils.cut(url, 30, '')}", total=total_size)
                progress.start()
                for chunk in res.iter_content(chunk_size=4096):
                    if chunk:
                        downloaded_file.write(chunk)
                        progress.advance(task, advance=len(chunk))
                progress.stop()
            except PermissionError:
                print(f"Unable to write into {file_name} due to permission error...")
                return None
            except IOError:
                print(f"Unable to write into {file_name} due to IO error...")
                return None
    
    except requests.ConnectionError as e:
        print(f"Connection error unable to download from url: {url}")
        return None
    except requests.HTTPError as e:
        print(f"Unable to download from url: {url} due to HTTP error: {e.response}")
        return None
    # except:
    #     print(f"Unable to download from url: {url}")
    #     return None
    
    
    try: 
        path = abspath(f'./{file_name}')
        return path
    except:
        return None
    # return abspath(f'./{file_name}')