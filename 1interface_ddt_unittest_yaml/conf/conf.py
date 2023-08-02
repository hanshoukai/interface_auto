import configparser
import pathlib

file = pathlib.Path(__file__).parents[0].resolve() / 'conf.ini'
# print(file)  # D:\PythonWork\api_demo\conf\conf.ini


def read(section, option):
    conf = configparser.ConfigParser()
    conf.read(file)
    values = conf.get(section=section, option=option)
    # print(values)
    return values


# read(section="servers", option="test")  # http://shop-xo.hctestedu.com/index.php


def write(section, option, value):
    conf = configparser.ConfigParser()
    conf.read(file)
    if not conf.has_section(section=section):
        conf.add_section(section)
    conf.set(section, option, value)
    with open(file, "w")as f:
        conf.write(f)

