import argparse

from cfg import ACTOR2ID, ACTOR_LOOKUP, GRAPH as G
from graph_utils import bfs_from_tim, bfs_back_to_tim, find_return_path

def main(args):
    
    actor_name = args.actor_name
    
    # remove excess whitespace
    actor_name = " ".join(actor_name.split())
    
    if actor_name not in ACTOR2ID:
        raise ValueError("Actorname not in Lookup. Are you sure you Spelled it Right?")
    
    actor_id = ACTOR2ID[actor_name]
    
    results = bfs_from_tim(actor_id)
    if not results:
        return
    
    visited, tracking, actor = results
    paths_id_to, paths_name_to, used_actors = find_return_path(actor, "nm0000741", tracking)
    
    results = bfs_back_to_tim(actor, used_actors)
    if not results:
        return
    
    visited, tracking, actor = results
    paths_id_return, paths_name_return, _ = find_return_path("nm0000741", actor_id, tracking)
    
    path2and_from_ids = paths_id_to[:-1] + paths_id_return
    
    for s1,s2 in zip(path2and_from_ids, path2and_from_ids[1:]):
        print(
            f"{ACTOR_LOOKUP[s1]} was in {' OR '.join([v['title'] for k,v in G.get_edge_data(s1, s2).items()])} with {ACTOR_LOOKUP[s2]}")
        
def parse_arguments():
    parser = argparse.ArgumentParser(description="Play the Tim Allen 2 Tim Allen Game")
    parser.add_argument("actor_name")
    args = parser.parse_args()
    
    return args
    
if __name__ == "__main__":
    
    args = parse_arguments()
    main(args)
