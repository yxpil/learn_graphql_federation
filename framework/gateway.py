"""GraphQL Federation: multiple subgraph services each own part of the schema.
A gateway combines them into one graph and routes query parts to the right service."""


class UserSubgraph:
    def resolve(self, field, args):
        if field == "user":
            return {"id": args["id"], "name": "Alice", "email": "alice@x.com"}
        return None


class ProductSubgraph:
    def resolve(self, field, args):
        if field == "product":
            return {"id": args["id"], "title": "Wireless Headphones", "price": 99.0}
        return None


class FederationGateway:
    def __init__(self):
        self.subgraphs = {}

    def register(self, name, subgraph, fields):
        self.subgraphs[name] = {"service": subgraph, "fields": fields}

    def query(self, parts):
        """parts: list of (field, args). Gateway routes each to the owning subgraph."""
        result = {}
        for field, args in parts:
            for _, sub in self.subgraphs.items():
                if field in sub["fields"]:
                    result[field] = sub["service"].resolve(field, args)
                    break
        return result
