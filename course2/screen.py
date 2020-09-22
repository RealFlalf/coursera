import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, v):
        self.x = v[0]
        self.y = v[1]

    def __sub__(self, other):
        return Vec2d((self.x - other.x, self.y - other.y))

    def __add__(self, other):
        return Vec2d((self.x + other.x, self.y + other.y))

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __mul__(self, other):
        return Vec2d((self.x * other, self.y * other))

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, v, s):
        self.points.append(Vec2d(v))
        self.speeds.append(Vec2d(s))

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p].x = -self.speeds[p].x
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p].y = -self.speeds[p].y

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (self.points[p_n].int_pair()),
                                 (self.points[p_n + 1].int_pair()), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   p.int_pair(), width)


class Knot(Polyline):
    def __init__(self, count):
        super(Knot, self).__init__()
        self.count = count
        self.knot_points = []

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(self.get_points())
            print(res)
        return res

    def get_points(self):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(i * alpha))
        return res

    def get_point(self, alpha, deg=None):
        if deg is None:
            deg = len(self.points) - 1
        if deg == 0:
            return self.points[0]
        return self.points[deg] * alpha + self.get_point(alpha, deg - 1) * (1 - alpha)

    def add_point(self, v, s):
        super(Knot, self).add_point(v, s)
        self.knot_points = self.get_knot()

    def set_points(self):
        super(Knot, self).set_points()
        self.knot_points = self.get_knot()

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.knot_points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (self.knot_points[p_n].int_pair()),
                                 (self.knot_points[p_n + 1].int_pair()), width)

        elif style == "points":
            for p in self.knot_points:
                pygame.draw.circle(gameDisplay, color,
                                   p.int_pair(), width)


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    main_knot = Knot(steps)
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    main_knot = Knot(steps)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    main_knot.count += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    main_knot.count -= 1 if main_knot.count > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                main_knot.add_point(event.pos, (random.random() * 2, random.random() * 2))
                # points.append(event.pos)
                # speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        main_knot.draw_points()
        main_knot.draw_points("line", 3, color)
        # draw_points(get_knot(points, steps), "line", 3, color)
        if not pause:
            main_knot.set_points()
            # set_points(points, speeds)
        # if show_help:
        #     draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
