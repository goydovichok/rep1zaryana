gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        dx = obj.x - body.x
        dy = obj.y - body.y
        r = (dx ** 2 + dy ** 2) ** 0.5
        if r == 0:
            continue
        F = gravitational_constant * body.m * obj.m / (r ** 2)
        body.Fx += F * dx / r
        body.Fy += F * dy / r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    body.x = ax * dt
    body.Vx = body.Vx * dt
    ay = body.Fy / body.m
    body.y += ay * dt
    body.Vy += body.Vy * dt


# solar_physics.py (дополняем в конец файла)

def calculate_angular_velocity(body, central_body):
    """Вычисляет угловую скорость тела относительно центрального."""
    rx = body.x - central_body.x
    ry = body.y - central_body.y
    r = (rx ** 2 + ry ** 2) ** 0.5

    if r == 0:
        return 0

    # Перпендикулярная составляющая скорости
    V_perp = (body.Vx * (-ry) + body.Vy * rx) / r

    return V_perp / r


def check_kepler_second_law(body, central_body, dt):
    """Проверяет второй закон Кеплера."""
    x0, y0 = body.x, body.y
    Vx0, Vy0 = body.Vx, body.Vy

    calculate_force(body, [central_body])
    move_space_object(body, dt)

    # Площадь треугольника
    area = 0.5 * abs((x0 - central_body.x) * (body.y - central_body.y)-(body.x - central_body.x) * (y0 - central_body.y))

    body.x, body.y = x0, y0
    body.Vx, body.Vy = Vx0, Vy0

    print(area)
    return area


if __name__ == "__main__":
    print("This module is not for direct call!")

    sun = Star()
    sun.m = 1.0e30
    sun.x = sun.y = 0

    planet = Planet()
    planet.m = 1.0e24
    planet.x = 1.0e11
    planet.y = 0
    planet.Vx = 0
    planet.Vy = 3.0e4

    angular_vel = calculate_angular_velocity(planet, sun)
    area = check_kepler_second_law(planet, sun, 86400)

    print(angular_vel)
    print(area)


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")