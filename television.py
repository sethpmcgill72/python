class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = 0
        self.__channel = 0

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel += 1

            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1

            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
