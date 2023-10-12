from rdflib import Graph

g = Graph()
filename = 'hedschema.ttl'
with open(filename, 'r') as f:
  g.parse(f, format='turtle')
print(g.serialize())

owl = g.serialize(format="owl")

print(owl)
# Save the owl file
with open("file.owl", "w") as f:
    f.write(owl)