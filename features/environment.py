from flask import current_app
from controllers import RestController, RancherController, CLIController, AWSController, CLIArgs
from flask_migrate import Config, command
import app, db

def before_all(context):

    context.rest = RestController()
    context.cli = CLIController()
    context.rancher = RancherController()
    context.aws = AWSController()
    context.args = CLIArgs(context.rest)
    # config = Config()
    # config.set_main_option("script_location", "migrations")
    # command.downgrade(config, "base")
    # command.upgrade(config, "head")
    db.db.drop_all()
    db.db.create_all()
    print("hello")



