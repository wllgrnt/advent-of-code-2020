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
if __name__ == "__main__":

    with open("input.txt") as flines:
        bag_rules = [line.strip() for line in flines]

    # We have to generate a directed bag graph, then find the number of paths that lead to "shiny gold".

    G = nx.DiGraph()
    # Start by parsing the edges - format is {colour_id} bags contain {number} {colour_id} bag(s) (, {number colour_id} bag(s))... \.
    for rule in bag_rules:
        source, target = rule.split(" bags contain ")
        # print(rule)
        matches =re.findall(r"[0-9]+.*?(?= bag)", target)
        if matches:
            # generate an edge
            for match in matches:
                edge_weight = match.split(" ")[0]
                match_name = " ".join(match.split(" ")[1: ])
                G.add_edge(source, match_name, weight=edge_weight)

    matches = 0
    bag_colours = []
    for node in G.nodes():
        if node != "shiny gold" and nx.has_path(G, node, "shiny gold"):
            matches += 1
            bag_colours.append(node)

    print(bag_colours)
    print(matches)
    #  
     