#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    from django.core.management import execute_from_command_line

    # This allows easy placement of apps within the interior
    # mtg_deckbuilder directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "mtg_deckbuilder"))

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
