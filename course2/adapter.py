class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, map_):
        dim = (len(map_[0]), len(map_))
        self.adaptee.set_dim(dim)
        lmap = []
        omap = []
        for i in range(dim[0]):
            for j in range(dim[1]):
                if map_[j][i] == 1:
                    lmap.append((i, j))
                elif map_[j][i] == -1:
                    omap.append((i, j))
        self.adaptee.set_obstacles(omap)
        self.adaptee.set_lights(lmap)
        return self.adaptee.generate_lights()

