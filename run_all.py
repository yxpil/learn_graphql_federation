"""Demo: federated graph - one query routes to multiple subgraph services."""
from framework.gateway import FederationGateway, UserSubgraph, ProductSubgraph


def main():
    gw = FederationGateway()
    gw.register("users", UserSubgraph(), fields=["user"])
    gw.register("products", ProductSubgraph(), fields=["product"])

    print("--- One query: user + product (routed to two subgraphs) ---")
    result = gw.query([
        ("user", {"id": "u_1"}),
        ("product", {"id": "p_1"}),
    ])
    for field, data in result.items():
        print(f"  {field}: {data}")

    print("\n== all cases done ==")


if __name__ == "__main__":
    main()
