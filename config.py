# Configuration for hot reload server when detect changes on any file

class Config:
    pass


class DevelopConfig(Config):
    DEBUG = True


config = {
    "development": DevelopConfig,
    "default": DevelopConfig
}