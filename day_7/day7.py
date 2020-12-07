"""
How many bag colours can eventually contain at least one shiny gold bag?

Test input:
```
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
```

Using those rules:

- A bright white bag, which can hold your shiny gold bag directly.
- A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
- A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
- A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4
"""
import re
import networkx as nx

def get_weight_from_edge_data(G, edge):
    return int(G.get_edge_data(edge[0], edge[1])["weight"])

def get_edge_weights(G, node):
    weight = 0
    if G.edges(node):
        for edge in G.edges(node):
            edge_weight = get_weight_from_edge_data(G, edge)
            weight += edge_weight*get_edge_weights(G, edge[1])
    return weight+1  # account for the bag itself with the +1

def solve(input_data):
    # We have to generate a directed bag graph, then find the number of paths that lead to "shiny gold".
    G = nx.DiGraph()
    # Start by parsing the edges - format is {colour_id} bags contain {number} {colour_id} bag(s) (, {number colour_id} bag(s))... \.
    for rule in input_data:
        source, target = rule.split(" bags contain ")
        # print(rule)
        matches =re.findall(r"[0-9]+.*?(?= bag)", target)
        if matches:
            # generate an edge
            for match in matches:
                edge_weight = match.split(" ")[0]
                match_name = " ".join(match.split(" ")[1: ])
                G.add_edge(source, match_name, weight=edge_weight)

    # Part one - how many nodes have a path to "shiny gold"?
    print(len(nx.ancestors(G, "shiny gold")))

    # Part two - how many individual bags are required inside your shiny gold bag?
    print(get_edge_weights(G, "shiny gold") - 1)


if __name__ == "__main__":

    print("Test data:")
    test_data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
    test_bag_rules = [line.strip() for line in test_data.split("\n")]
    solve(test_bag_rules)

    test_data_2 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    test_bag_rules_2 = [line.strip() for line in test_data_2.split("\n")]
    solve(test_bag_rules_2)
    

    with open("input.txt") as flines:
        bag_rules = [line.strip() for line in flines]
    print("Problem:")
    solve(bag_rules)
