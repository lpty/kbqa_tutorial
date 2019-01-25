from SPARQLWrapper import SPARQLWrapper, JSON

url = "http://localhost:3030/kg_demo_movie/query"

sparql = SPARQLWrapper(url)

query = """
    PREFIX : <http://www.kbqa.com#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX vocab: <http://localhost:2020/resource/vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX map: <http://localhost:2020/resource/#>
    PREFIX db: <http://localhost:2020/resource/>

    SELECT ?n WHERE {
      ?s rdf:type :Person.
      ?s :personName '巩俐'.
      ?s :hasActedIn ?o.
      ?o :movieTitle ?n.
      ?o :movieRating ?r.
    FILTER (?r >= 7)
    }
"""
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["n"]["value"])
