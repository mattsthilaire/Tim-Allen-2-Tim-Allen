from pathlib import Path
import pickle


# you can replace this with your local path if needed
DATA_PATH = Path(__file__).parents[1] / "data"

GRAPH_PATH = DATA_PATH / "tim_allen_graph_2.pkl"
ACTOR_LOOKUP = DATA_PATH / "actor_lookup.pickle"
ACTOR2ID = DATA_PATH / "actor2id.pickle"

with open(GRAPH_PATH, "rb") as f:
    GRAPH = pickle.load(f)

with open(ACTOR_LOOKUP, "rb") as f:
    ACTOR_LOOKUP = pickle.load(f)

with open(ACTOR2ID, "rb") as f:
    ACTOR2ID = pickle.load(f)
