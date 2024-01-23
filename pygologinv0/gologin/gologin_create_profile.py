import random
from gologin import GoLogin

def create_profile():
    proxy_list=['us', 'ca', 'uk', 'de', 'in']
    proxy=random.choice(proxy_list)
    print(
        f'Going to use following proxy {proxy}'
    )
    gl = GoLogin({
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZWQzZDQ5MWQ1MzJkMDgzNDZjNDYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWFmZWUzMjI3MmE5ZmI1ZmY5OTlkM2EifQ.t1dVMtPypOcInLeB7GMDeTR19Jtdre8dEtK-kpL-MnA",
        })

    profile_id = gl.create({
        "name": 'profile_mac',
        "os": 'mac',
        "navigator": {
            "language": 'en-US',
            "userAgent": 'random',
            "resolution": '1024x768',
            "platform": 'mac',
        },
        'proxy': {
            'mode': 'gologin', # Specify 'none' if not using proxy
            'autoProxyRegion': proxy
            # "host": '',
            # "port": '',
            # "username": '',
            # "password": '',
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
        },
        "storage": {
            "local":        True,   # Local Storage is special browser caches that websites may use for user tracking in a way similar to cookies. 
                                    # Having them enabled is generally advised but may increase browser profile loading times.
    
            "extensions":   True,   # Extension storage is a special cotainer where a browser stores extensions and their parameter. 
                                    # Enable it if you need to install extensions from a browser interface.
                                
            "bookmarks":    True,   # This option enables saving bookmarks in a browser interface.
                                
            "history":      True,   # Warning! Enabling this option may increase the amount of data required 
                                    # to open/save a browser profile significantly. 
                                    # In the interests of security, you may wish to disable this feature, 
                                    # but it may make using GoLogin less convenient.
                                
            "passwords":    True,   # This option will save passwords stored in browsers.
                                    # It is used for pre-filling login forms on websites. 
                                    # All passwords are securely encrypted alongside all your data.
                                
            "session":      True,   # This option will save browser session. It is used to save last open tabs.
                                
            "indexedDb":    False   # IndexedDB is special browser caches that websites may use for user tracking in a way similar to cookies. 
                                    # Having them enabled is generally advised but may increase browser profile loading times.
        }
    })
    return profile_id
