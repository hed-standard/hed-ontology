# HED ontology development guide

## Overview

### Naming conventions

#### HED classes

- All hed classes have names starting with *Hed*.
- HED classes use upper camel case (all words start with a capital letter). 
- Class names should be singular.

#### HED properties

HED properties use lower camel case (all words except first start with a capital letter). 


#### HED instances of classes

In the HED schema HED tags start with a capital letter and individual words are hyphenated. These are converted upper camel case with underscores and hyphens removed:  

**Example:** The HED tag *Sensory-event* is converted to *SensoryEvent*. 


## Annotation properties

| Property            | Range         | Target         | Description                                                |
|---------------------|---------------|----------------|------------------------------------------------------------|
| *library*           | *xsd:string*  | **HedHeader**  | Indicates the name of the library schema if applicable.    |
| *unmerged*          | *xsd:boolean* | **HedHeader**  | Indicates whether schema is not merged with partner schema. |
| *version*           | *xsd:boolean* | **HedHeader**  | Indicates the semantic version of this schema.             |
| *wikiSchemaSection* | *xsd:string*  | **HedElement** | The section name in Mediawiki format for this element.     |
| *withStandard*      | *xsd:boolean* | **HedHeader**  | Indicates whether schema is not merged with partner schema. |
| *xmlSchemaSection*  | *xsd:string*  | **HedElement** | The section name in XML format for this element.           |


### Mapping rules


- The element (whether class, property, or instance) description (that appears in square brackets in the schema) is mapped to **rdfs:comment**.
- The name the element uses in the HED schema is mapped to **rdfs:label**.

#### Schema attributes

Rules:
- Schema attributes have either *owl:DatatypeProperty* or *owl:ObjectProperty*.
-  *owl:DatatypeProperty* are recognized by having *rdfs:subPropertyOf* value of either *hed:schemaAttributeDatatypeProperty* or *hed:schemaAttributeObjectProperty*,
- Schema attributes are mapped to owl:DatatypeProperty with if 


### Main classes

| Name                                          | subclass                       | Description                                                  |
|-----------------------------------------------|--------------------------------|--------------------------------------------------------------|
| [**HedElement**](#hedelement)                 | owl:Class                      | Superclass for specifying the structure of a HED schema.     |
| [**HedHeader**](#hedheader)                   | owl:Class<br/>**HedElement**   | Specifies the schema header.                                 |
| [**HedNode**](#hednode)                       | owl:Class<br/>**HedElement**   | Specifies HED term or node elements.                         |
| [**HedPlaceholder**](#hedplaceholder)         | owl:Class<br/>**HedNode**      | Specifies HED node placeholders.                             |
| [**HedSchemaAttribute**](#hedschemaattribute) | owl:Class<br/>**HedElement**   | Defines attribute modifiers of other sections of the schema. |
| [**HedUnit**](#hedunit)                       | owl:Class<br/>**HedElement**   | Specifies a HED unit .                                       |
| [**HedUnitClass**](#hedunitclass)             | owl:Class<br/>**HedElement**   | Specifies HED units and unit modifiers.                      |
| [**HedUnitModifier**](#hedunitmodifier)       | owl:Class<br/>**HedUnitClass** | Subclass of **HedUnitClass** defining unit modifiers.        |
| [**HedValueClass**](#hedvalueclass)           | owl:Class<br/>**HedElement**   | Defines the types of value classes.                          |

## HedElement
**HedElement** is the superclass for all structure of the HED schema.


## HedHeader

## HedNode

**HedNode** is a class representing a HED tag or term. It is a subclass of **HedElement**.

**Rules for instances:**
- each HED tag or term is an instance of **HedNode**.
- every instance of **HedNode** has either the **hasHedParent** or the **isTopLevelTag** property.

## HedPlaceholder
**HedPlaceholder** is a class representing the `#` nodes in the HED schema.

Each `#` in the schema corresponds to an instance of **HedPlaceholder**.

**Rules for instances of HedPlaceholder:**
- must have a **isTakesValue** property of true.
- may have one or more **hasValueClass** property items.
- may have one or more UnitClass instances.
- must have **isExtensionAllowed** property of False.
- must have **isTopLevelTag** property of False.
- must have a **hasHedParent** property.

## HedSchemaAttribute


## HedUnit
**HedUnit** specifies units.

**Rules for instances of HedUnit:**
- Must be an instance of **HedUnit**.
- Must have a **hasUnitClassType** property
- May have the **isSIUnit** property.
- May have a **isUnitSymbol** property.
- May have a **hasConversionFactorValue** property.



## HedUnitClass

**HedUnitClass** specifies the types of HED units and unit modifiers.

**Rules for instances of HedUnitClass:**
- Each type of units such as *accelerationUnits* is an instance of **HedUnitClass**.
- An instance of **HedUnitClass** may have a **hasDefaultUnits** property.

## HedUnitModifier

**HedUnitModifier** is a subclass of **HedUnitClass** that specifies unit modifiers.

**Rules for instances of HedUnitModifier:**
- Must be an instance of **HedUnitModifier**.
- Has either the **isSIUnitModifier** or **isSIUnitSymbolModifier** property.
- Must have the **hasConversionFactor** property.

## HedValueClass
