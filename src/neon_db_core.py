from typing import Dict, Any
class NarrativeNode:
    def __init__(self, node_id, classification):
        self.node_id = node_id
        self.classification = classification
        self.properties = {}
        self.tension_index = 0.0

    def inscribe_truth(self, key, observer, value):
        if key not in self.properties: self.properties[key] = {}
        self.properties[key][observer] = value
