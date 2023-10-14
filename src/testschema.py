import io
from rdflib import Graph, plugin
from rdflib.serializer import Serializer
# from rdflib.owl import serialize_owl


g = Graph()
filename = 'hedschema.ttl'
with open(filename, 'r') as f:
  g.parse(f, format='turtle')
print(g.serialize())

# Now try serializing in JSON-LD
output_buffer = io.StringIO()
g.serialize(destination=output_buffer, format='json-ld')
json_ld_data = output_buffer.getvalue()
print(json_ld_data)
# 
# owl = g.serialize(format="owl")
# 
# print(owl)
# # Save the owl file
# with open("file.owl", "w") as f:
#     f.write(owl)