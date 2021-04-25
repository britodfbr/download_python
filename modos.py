import requests
import pathlib


def modo1(url: str, filename: (str, pathlib.Path))->bool:
    """ Download content web 
    :: url: url for download
    :: filename: output download content

    :: return: True if writed file with success
    """
    myfile = requests.get(url, allow_redirects=True)
    pathlib.Path(filename).expanduser().write_bytes(myfile.content)
    return True


def modo2(url, filename)->bool:
    """ Download content web and create path if necessary
    :: url: url for download
    :: filename: output download content

    :: return: True if writed file with success else raise
    """
    req = requests.get(url, allow_redirects=True, stream=True)
    myfile = pathlib.Path(filename).expanduser().resolve()
    myfile.parent.mkdir(parents=True, exist_ok=True)
    myfile.write_bytes(req.content)
    return True


def modo3(url: str, filename: (str, pathlib.Path)) -> str:
    """ Download content web and create path if necessary
    :: url: url for download
    :: filename: output download content

    :: return: True if writed file with success else raise
    """
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        filename = pathlib.Path(filename).expanduser().resolve()
        filename.parent.mkdir(parents=True, exist_ok=True)
        filename.write_bytes(resposta.content)
        print("Download finalizado. Salvo em: {}".format(filename))
    else:
        resposta.raise_for_status()