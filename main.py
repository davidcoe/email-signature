#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List

import jsonpickle
from jinja2 import Environment, FileSystemLoader, select_autoescape

Url = str


@dataclass
class Social:
    """A social media personal link and an icon"""
    link: Url
    icon: Url


@dataclass
class Signature:
    """All the information contained in a signature"""
    name: str
    title: str
    phone: str
    website_link: Url
    website_text: str
    avatar_link: Url
    avatar_img: Url
    avatar_description: str
    socials: List[Social]


def main():
    with open('signature.json', 'r') as f:
        signature = jsonpickle.decode(f.read())

    env = Environment(
        loader=FileSystemLoader(searchpath='./templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('signature.html')
    print(template.render(signature=signature))


if __name__ == '__main__':
    main()
