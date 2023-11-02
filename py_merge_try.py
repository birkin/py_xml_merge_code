import logging, sys
from rdflib import Graph, URIRef

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger( __name__ )
log.debug( 'logging working' )

# Initialize two empty RDF graphs
g1 = Graph()
g2 = Graph()

# Parse the JSON-LD files into the graphs
g1.parse( '../source_files/n69528.json', format='json-ld')
g2.parse( '../source_files/nbf078c6402354618a32fd6d897246982.json', format='json-ld')

# Merge the graphs
g1 += g2

# Serialize the merged graph back to JSON-LD
merged_jsonld = g1.serialize(format='json-ld')

# Optionally, save the merged JSON-LD to a file
with open('../output_file/merged_file.json', 'w') as f:
    f.write(merged_jsonld)

## because I do NOT want to try to update anything in VIVO, I'm quitting.
log.debug( 'quitting' )
sys.exit(0)

# # If you want to update a specific URI after merging
# new_uri = URIRef('vivostaging.brown.edu/individual/new_uri')
# old_uri1 = URIRef('vivostaging.brown.edu/individual/nbf078c6402354618a32fd6d897246982')
# old_uri2 = URIRef('vivostaging.brown.edu/individual/n69528')

# # Replace old URIs with the new URI
# for s, p, o in g1.triples((old_uri1, None, None)):
#     g1.add((new_uri, p, o))
#     g1.remove((s, p, o))

# for s, p, o in g1.triples((old_uri2, None, None)):
#     g1.add((new_uri, p, o))
#     g1.remove((s, p, o))
