class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []
        self.has_free_seats = True
        self.seats = {}
    
    def board(self, *surnames):
        for surname in surnames:
            if len(self.passengers) < self.max_seats:
                self.passengers.append(surname)
                self.seats[len(self.passengers)] = surname
                self.has_free_seats = len(self.passengers) < self.max_seats
    
    def disembark(self, *surnames):
        for surname in surnames:
            if surname in self.passengers:
                self.passengers.remove(surname)
                for seat_num, pass_name in list(self.seats.items()):
                    if pass_name == surname:
                        del self.seats[seat_num]
                self.has_free_seats = len(self.passengers) < self.max_seats
    
    def increase_speed(self, value):
        self.speed = min(self.max_speed, self.speed + value)
    
    def decrease_speed(self, value):
        self.speed = max(0, self.speed - value)
    
    def __contains__(self, surname):
        return surname in self.passengers
    
    def __iadd__(self, surname):
        self.board(surname)
        return self
    
    def __isub__(self, surname):
        self.disembark(surname)
        return self
