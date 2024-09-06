class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://posts:iti@localhost:5432/postlab2"


config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig,
}
