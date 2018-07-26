__author__ = 'root'
import yaml
import sys
import os

class Config:
    'Common base class for all employees'
    cfg = None

    def __init__(self, path):
        #with open(os.environ['GAUSSIAN_CONFIG'] + "/config.yml", 'r') as ymlfile:
        with open(path + "/config.yml", 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile)

    def value(self, levels):
        ret = self.cfg[levels[0]]
        for level in levels[1:]:
            ret = ret[level]
        return ret