from enum import Enum


class BSDFType(Enum):
    Light = 0
    Diffuse = 1
    Specular = 2
    Any = 3


class BSDF:

    def __init__(self, description, color):
        self.description = description
        self.color = color
