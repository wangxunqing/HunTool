import click
from flask.cli import FlaskGroup

from hun_tool.app import create_app


def create_hun_tool(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_hun_tool)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from hun_tool.extensions import db
    from hun_tool.models import User
    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create user")
    user = User(
        username="admin",
        email="benge@163.com",
        password="123456",
        active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
