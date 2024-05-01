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
    onto_list = ['Base_schema.omn', 'Standard_AnnotationProperty.omn', 'Standard_AttributeProperty.omn',
                 'Standard_DataProperty.omn', 'Standard_ObjectProperty.omn', 'Standard_Structure.omn',
                 'Standard_Tag.omn', 'Standard_UnitClass.omn', 'Standard_Unit.omn', 'Standard_UnitModifier.omn',
                 'Standard_ValueClass.omn']
    generated_path = '../ontology/generated'
    output_path = os.path.realpath(os.path.join('../ontology', 'hed-merged.omn'))
    onto_paths = [os.path.realpath(os.path.join(generated_path, filename)) for filename in onto_list]
    merge_list(onto_paths, output_path)
