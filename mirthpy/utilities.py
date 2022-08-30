from typing import Callable, List
from xml.etree.ElementTree import Element


def getSafeText(self : Element, prop:str):
    return self.find(prop).text if self.find(prop) != None else None

def build_encoded_url_params(**kwargs):
    params = []

    for key, value in kwargs.items():
        if type(value) == list or type(value) == tuple:
            for x in value:
                params.append(f"{key}={x}")
        elif type(value) == bool:
            if value:
                params.append(f"{key}=true")
            else:
                params.append(f"{key}=false")
        else:
            params.append(f"{key}={value}")
    
    return '?' + '&'.join(params)
 