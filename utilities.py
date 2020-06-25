class Graph:
    def __init__(self, art_installations, weighted_connect):
        self.installations = art_installations
        self.adjacency_mtx = weighted_connect
        self.artwork_to_index = {}

        for i, artwork in enumerate(self.installations):
            self.artwork_to_index[artwork] = i
            
    def __str__(self):
        return (str(self.installations) + '\n' + str(self.adjacency_mtx))


class Installation:
    def __init__(self, name, ward, position, indoor):
        self.name = name
        self.ward = ward
        self.position = position
        self.indoor = indoor
        
    def __str__(self):
        return "Installation " + self.name + " in Ward " + str(self.ward)
