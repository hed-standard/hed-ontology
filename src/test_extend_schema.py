import hed
from rdflib import Graph, RDF, RDFS, Namespace, Literal, URIRef

ADD_ONLY_A_FEW_ENTRIES = True
HED = Namespace("https://purl.org/hed#")

# Create a new graph and load your ontology
g = Graph()
g.parse("hedschema_data.ttl", format="turtle")

for prefix, ns in g.namespaces():
    print(f"{prefix}: {ns}")

# Ones I verified work/mostly work
handled_attributes = {"suggestedTag", "relatedTag", "deprecatedFrom", "unitClass", "valueClass",
                      "defaultUnits", "conversionFactor"}
float_attributes = {"conversionFactor"}
def write_attributes(entry_uri, entry):
    for attribute, value in entry.attributes.items():
        is_bool = entry.attribute_has_property(attribute, "boolProperty")
        if attribute not in handled_attributes and not is_bool:
            print(f"Make sure {is_bool} {attribute} is handled")

        if is_bool:
            g.add((entry_uri, HED[attribute], Literal(True)))

        elif attribute in float_attributes:
            # todo: this isn't handled correctly right now
            g.add((entry_uri, HED[attribute], Literal(value.replace("^", "e"))))
        else:
            # Todo: further develop this if needed or merge into base tools
            values = value.split(",")
            for val2 in values:
                # Can't write ^ to files
                # Todo: Add more robust character checks.
                clean_value = val2.replace("^", "e")
                attribute_uri = HED[clean_value]
                g.add((entry_uri, HED[attribute], attribute_uri))


# Todo: make sure we properly handle unit classes/value classes with multiple values
def add_entry(tag_name, label, comment, in_schema_section, parent=None, entry=None, tag_type=HED.HedTag, unit_class=None):
    is_takes_value = entry.has_attribute("takesValue")
    if is_takes_value:
        tag_type = HED.HedPlaceholder
        tag_name = entry.short_tag_name + "-Placeholder"

    # Patch for now to never write out spaces
    # degree Celsius and m-per-s^2
    tag_name = tag_name.replace("^", "e").replace(" ", "-")
    uri = f"https://purl.org/hed#{tag_name}"
    hed_tag_uri = URIRef(uri)

    g.add((hed_tag_uri, RDF.type, tag_type))
    g.add((hed_tag_uri, RDFS.label, Literal(label)))
    g.add((hed_tag_uri, RDFS.comment, Literal(comment)))
    if parent is not None:
        parent_uri = HED[parent]
        g.add((hed_tag_uri, HED.hasHedParent, parent_uri))
    if unit_class is not None:
        unit_class_uri = HED[unit_class]
        g.add((hed_tag_uri, HED.unitClass, unit_class_uri))
    section_uri = HED[in_schema_section]
    g.add((hed_tag_uri, HED.inSchemaSection, section_uri))
    write_attributes(hed_tag_uri, entry)


from hed import load_schema_version

schema = load_schema_version()

# Add just one tag(Agent-action) to the schema for saving
skip_tags = ["event", "event/sensory-event"]
total_count = 0
for tag, entry in schema.tags.items():
    total_count += 1
    if ADD_ONLY_A_FEW_ENTRIES and total_count > 4:
        break

    tag_name = entry.short_tag_name
    parent = entry.parent
    if parent:
        parent = parent.short_tag_name
    label = tag_name
    comment = entry.description
    add_entry(
        tag_name=tag_name,
        label=tag_name,
        comment=comment,
        in_schema_section="StartSchemaSection",
        parent=parent,
        entry=entry
    )

for unit_class, class_entry in schema.unit_classes.items():
    uri = f"https://purl.org/hed#{unit_class}"
    # todo: extend this to dump everything when unifying
    unit_class_uri = URIRef(uri)
    g.add((unit_class_uri, RDF.type, HED.HedUnitClass))
    write_attributes(unit_class_uri, class_entry)
    for unit, entry in class_entry.units.items():
        comment = entry.description
        add_entry(
            tag_name=unit,
            label=unit,
            comment=comment,
            in_schema_section="UnitClassSection",
            unit_class=unit_class,
            entry=entry,
            tag_type=HED.HedUnit
        )
        pass

for unit_modifier, entry in schema.unit_modifiers.items():
    comment = entry.description
    add_entry(
        tag_name=unit_modifier,
        label=unit_modifier,
        comment=comment,
        in_schema_section="UnitModifierSection",
        entry=entry,
        tag_type=HED.HedUnitModifier
    )

# Save the updated graph
g.serialize("updated_hedschema_data.ttl", format="turtle")
g.parse("hedschema.ttl", format="turtle")

g.serialize("updated_hedschema_combined.ttl", format="turtle")
