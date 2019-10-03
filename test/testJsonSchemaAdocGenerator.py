import unittest
import logging
import json
import json_schema2adoc.jsonSchemaAdocGenerator

class TestSchemaAdocGenerator(unittest.TestCase):

    def test_build_document(self):
        with open('test/TestJsonSchema.json', encoding='utf-8') as json_file:
             json_object = json.loads(json_file.read())
             asciiDocOutput = json_schema2adoc.jsonSchemaAdocGenerator.build_document(json_object)
        self.assertTrue(asciiDocOutput[0].startswith('=='))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

