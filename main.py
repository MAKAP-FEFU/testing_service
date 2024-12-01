import json

import click

from src.tool import get_data


def save_to_json(filename: str, data: dict | list) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@click.command(
    "get_data",
)
@click.option(
    "-s",
    type=click.Choice(("local", "prod")),
    default="local",
)
def get_data_from_server(server: str):
    result = get_data(server=server)
    save_to_json("files/data.json", result)

    print("Result:")
    print("\n".join([f"{key}: {result[key]}" for key in result]))
