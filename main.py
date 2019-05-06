import os
from enum import Enum

import pandas as pd

from constant import CHARACTERS
from constant import EXPORT
from constant import EXPORT_FOLDER
from constant import WEBSITE


class TableType(Enum):
    normals = 1
    specials = 0


if not os.path.exists(EXPORT_FOLDER):
    os.makedirs(EXPORT_FOLDER)

for character in CHARACTERS:

    url = WEBSITE.format(character)
    print("Loading: " + url)
    tables = pd.read_html(url)

    for index, table, in enumerate(tables):
        if index == TableType.specials.value:
            table_part = '_specials'
        elif index == TableType.normals.value:
            table_part = '_normals'
        else:
            table_part = '_ERROR'

        export_file_name = EXPORT.format(character + table_part)
        table.to_csv(export_file_name, ',')
        print("Exported: " + export_file_name)

    print()
