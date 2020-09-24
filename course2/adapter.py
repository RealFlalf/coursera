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


class MappingAdapter(Light):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, map):
        lmap = []
        omap = []
        for i in range(len(syst.map)):
            try:
                lmap.append((i, syst.map[i].index(1)))
            except ValueError:
                pass
            try:
                omap.append((i, syst.map[i].index(-1)))
            except ValueError:
                pass
        self.adaptee.set_lights(lmap)
        self.adaptee.set_obstacles(omap)
        return self.adaptee.grid
        print(lmap, omap)


if __name__ == '__main__':
    syst = System()
    lmap = []
    omap = []
    for i in range(len(syst.map)):
        try:
            lmap.append((i, syst.map[i].index(1)))
        except ValueError:
            pass
    lght = Light((30, 20))
    # syst.get_lightening(lght)
    adp = MappingAdapter(lght)
    syst.get_lightening(adp)
    print("done")