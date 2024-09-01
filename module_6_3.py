class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.dx = dx
        self.x_distance = self.x_distance + self.dx
        return self.x_distance


class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.dx = dy
        self.y_distance = self.y_distance + self.dx
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        return self.run(dx), self.fly(dy)

    def voice(self):
        print(self.sound)




p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
#
p1.voice()