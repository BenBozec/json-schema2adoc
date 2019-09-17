'''
schemaAdocGenerator.py

Script used to produce AsciiDoc files from Json Schemas

usage: schemaAdocGenerator.py input output-directory
'''

import os
import argparse
import json

def main():
    """Entry Point for the script"""

    # Set up CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="The json schema file to parse", type=str)
    parser.add_argument("output-directory", help="The directory to ouput file to")
    args = parser.parse_args()

    # Open input file
    with open(args.input, encoding='utf-8') as jsonFile:
        json_object = json.loads(jsonFile.read())
        adoc_name = os.path.splitext(jsonFile.name)[0] + '.adoc'

    # Build the document
    if json_object:
        document = build_document(json_object)

        # Ouput document to file
        with open(adoc_name, 'w') as outputFile:
            for line in document:
                outputFile.write(line+'\n')


def build_document(json_schema: dict) -> list:
    """
    Returns a list of lines to generate a basic adoc file, with the format:

    Title

    A table for the data properties

    A table for the data attributes and nested attributes if any
    """

    lines = []

    """
    Title and description of schema
    """
    title = get_json_attribute(['title'], json_schema)
    description = get_json_attribute(['description'], json_schema)

    """
    Id and required properties of object
    """
    data = get_json_attribute(['properties', 'data'], json_schema)
    data_required = get_json_attribute(['required'], data)
    data_properties = get_json_attribute(['properties'], data)

    """
    Attributes of object
    """
    attributes = get_json_attribute(['attributes'], data_properties)
    required = get_json_attribute(['required'], attributes)
    attribute_properties = get_json_attribute(['properties'], attributes)

    """
    Relationships of object
    """
    relationships = get_json_attribute(['relationships', 'properties'], data_properties)

    """
    Cleans up properties table
    """
    data_type = get_json_attribute(['type', 'const'], data_properties)

    if 'type' in data_properties:
        data_properties.update({'type': {'type': str(data_type)}})
    
    if 'relationships' in data_properties:
        del data_properties['relationships']

    del data_properties['attributes']

    """
    Sets title, description, and tables
    """
    lines.append(get_adoc_title(title, 2))

    if description:
        lines.append(description+'\n')

    if data_properties:
        lines.extend(get_adoc_table('Properties', ['Type', 'Description'], data_properties, data_required))

    if attributes:
        lines.extend(get_adoc_table('Attributes', ['Type', 'Description'], attribute_properties, required))
        lines.append('\n')

    if relationships:
        lines.extend(get_adoc_table('Relationships', ['Type', 'Description'], relationships, ''))

    return lines


def get_adoc_table(title, columns: list, items: dict, required: list) -> list:
    """
    Returns a list of lines to generate a asciidoc table with a given title, columns, 
    and items to populate the table.

    A name column will be added to the table by default and will reference the keys 
    of the given items.
    """
    if not items:
        return []
    lines = []
    lines.append('.'+title)
    lines.append('|===')
    columns.insert(0, 'Name')
    lines.append(' '.join('|'+col for col in columns) + '|Required?')
    for prop in items.keys():
        lines.append('\n|'+prop)
        for col in columns[1:]:
            lines.append('|' + str(get_json_attribute([prop, str(col).lower()], items)))
        lines.append('|X' if prop in required else '|')
    lines.append('|===')
    return lines


def get_adoc_title(title: str, level: int) -> str:
    """Returns a string to generate a ascidoc title with the given title, and level"""

    return " ".join(["="*level, title, '\n'])


def get_json_attribute(path: list, jsonObject: dict):
    """
    Returns a Json element of the given Json Object nested by the given list of 
    attribute paths.
    """

    if not path or not jsonObject:
        return jsonObject
    name = path.pop(0)
    if name in jsonObject:
        return get_json_attribute(path, jsonObject[name])
    else:
        return None


if __name__ == '__main__':
    main()

