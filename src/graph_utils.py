from collections import deque
from typing import Any, Dict, List, Set, Tuple
from cfg import ACTOR_LOOKUP, ACTOR2ID, GRAPH as G

def bfs_from_tim(target: str, tim: str = "nm0000741"):
    
    q = deque([tim])
    visited = set([tim])
    tracking = {}

    while q:

        curr = q.popleft()

        for neighbor in G.neighbors(curr):
            if neighbor == target:
                visited.add(neighbor)
                tracking[neighbor] = curr
                return visited, tracking, neighbor

            if neighbor not in visited:
                q.append(neighbor)
                tracking[neighbor] = curr
                visited.add(neighbor)

    return None


def bfs_back_to_tim(src: str, used: Set[str], tim: str = "nm0000741"):

    q = deque([src])
    visited = used
    tracking = {}

    while q:

        curr = q.popleft()

        for neighbor in G.neighbors(curr):
            if neighbor == tim:
                tracking[neighbor] = curr
                return visited, tracking, neighbor

            if neighbor not in visited:
                q.append(neighbor)
                tracking[neighbor] = curr
                visited.add(neighbor)

    return None


def find_return_path(src: str, target: str, tracking_path: Dict[str, str]) -> Tuple[List[str], List[str]]:

    path_from_names = []
    path_from_ids = []

    curr = src
    used_actors = set()
    while True:
        if curr == target:
            path_from_ids.append(curr)
            path_from_names.append(ACTOR_LOOKUP[curr])
            return path_from_ids[::-1], path_from_names[::-1], used_actors

        path_from_ids.append(curr)
        path_from_names.append(ACTOR_LOOKUP[curr])
        used_actors.add(curr)
        curr = tracking_path[curr]