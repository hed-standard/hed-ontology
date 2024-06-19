import os


def merge_list(onto_files, out_path):
    """ Write a list of text ontology files as a single file

    Parameters:
        onto_files (list):  Full paths of the files to be merge
        out_path (str):  Full path of the output file

    """

    with open(out_path, 'w') as outfile:
        for f_name in onto_files:
            with open(f_name, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')


if __name__ == '__main__':
    schema_version = 'HED8.3.0'
    base_schema = os.path.realpath('../ontology/base/hed_schema.omn')
    base_structure = os.path.realpath('../ontology/HED8.3.0/HED8.3.0_BaseStructure.omn')
    onto_list = ['_AnnotationProperty.omn', '_AttributeProperty.omn',
                 '_DataProperty.omn', '_ObjectProperty.omn', '_Structure.omn',
                 '_Tag.omn', '_Unit.omn', '_UnitClass.omn', '_UnitModifier.omn',
                 '_ValueClass.omn']
    version_path = '../ontology/' + schema_version + '/generated_omn'
    output_path = os.path.realpath(os.path.join('../ontology', schema_version, schema_version + '-merged.omn'))
    onto_paths = [os.path.realpath(os.path.join(version_path, schema_version+filename)) for filename in onto_list]
    onto_paths = [base_schema] + [base_structure] + onto_paths
    merge_list(onto_paths, output_path)
    print(output_path)
    print(str(onto_paths))
