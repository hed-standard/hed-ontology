# Hierarchical Event Descriptor Ontology

HED (Hierarchical Event Descriptors) is a standardized vocabulary and supporting infrastructure for 
annotating experimental metadata and mapping it into the experimental timeline.
See [**HED resources**](https://www.hed-resources.org/en/latest/index.html) for more information about the
HED project.

## HED schemas and the HED ontology

HED itself consists of a standard vocabulary the (HED standard schema) and specialized
subfield vocabularies (HED library schemas).
These vocabularies are developed and maintained in the 
[**hed-schemas**](https://github.com/hed-standard/hed-schamas) GitHub repository.

The HED ontology is a representation of the HED schemas as a formal ontology of the HED information space.
Releases of new HED schemas trigger a generation of a new HED ontology 
in this repository ([**hed-ontology**](https://github.com/hed-standard/hed-ontology)), 
and maintainers of this repository do a new release.
The correspondence between the HED schemas and HED ontology is explained more fully in
[**The HED ontology**](https://hed-specification.readthedocs.io/en/latest/08_HED_ontology.html)
chapter of the [**hed-specification](https://githum.com/hed-standard/hed-specification).

## HED namespaces and IRIs

Each HED entity in the HED information space has a globally unique identifier
of the form `HED_xxxxxxx` where `xxxxxxxx` is a 7-digit number.

The identifier namespace is assigned as follows:

| Schema                  | ID Range           | Description                          |  
|-------------------------|--------------------|--------------------------------------| 
| Structure               | 0000001 - 0009999  | Structure elements for HED ontology. | 
| Standard                | 0010001 -  0039999 | Standard annotation of experiments.  |
| Score                   | 0042000-  0059999  | Annotation by clinical neurologists. | 
| Lang | 0062000 -  0079999 | Annotation of language stimuli.      |


## Ontology versions

| Version    | Contains | Files                                                          | Description                       |
|------------| --------|----------------------------------------------------------------|-----------------------------------|
| 2024-06-10 | 8.3.0  | `hed.owl`<br/>`hed-standard.owl` | Contains only the standard schema |


### PURLS
These are the PURL values relative to the 

| PURL                                                                                                          | Relative path                            |  
|---------------------------------------------------------------------------------------------------------------|------------------------------------------|  
| [https://purl.org/hed/hed.owl](https://purl.org/hed/hed.owl)                                                  | `./hed.owl`                              |  
| [https://purl.org/hed/hed-standard.owl](https://purl.org/hed/hed-standard.owl)                                | `./hed-standard.owl`                     |  
| [https://purl.org/hed/releases/2024-06-10/hed.owl](https://purl.org/hed/releases/2024-06-10/hed.owl)          | `./releases/2024-06-10/hed.owl`          |  
| [https://purl.org/hed/releases/2024-06-10/hed.owl](https://purl.org/hed/releases/2024-06-10/hed-standard.owl) | `./releases/2024-06-10/hed-standard.owl` |  


# Contact

In general, posts to our GitHub issue tracker are recommended, however, 
if needed, you can contact the ontology curator by sending an e-mail 
[mailto:hed-maintainers@gmail.com](mailto:hed-maintainers@gmail.com).

# License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
