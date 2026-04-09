class Television:
    def __init__(self):
        self.MIN_VOLUME = 0
        self.MAX_VOLUME = 2
        self.MIN_CHANNEL = 0
        self.MAX_CHANNEL = 3

        self.__status = False #power
        self.__muted = False
        self.__volume = 0
        self.__channel = 0

    def power(self):
        """
        Toggles TV power.
        :return: None
        """
        self.__status = not self.__status

    def mute(self):
        """
        Toggles TV mute option.
        :return: None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increments the current channel by 1. Moves to channel
        0 if incrementing results in a channel above 3.
        :return: None
        """
        if self.__status:
            self.__channel += 1

            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        Decrements the current channel by 1. Moves to channel
        3 if decrementing results in a channel below 0.
        :return: None
        """
        if self.__status:
            self.__channel -= 1

            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        Increases TV volume by 1, up to 2.
        :return: None
        """
        if self.__status:
            if self.__muted: #unmute TV to allow volume changing.
                self.mute()

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        If powered, unmutes TV and decreases volume by 1, down to 0.
        :return: None
        """
        if self.__status:
            if self.__muted: #unmute TV to allow volume changing.
                self.mute()

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Displays TV power, channel, and volume information.
        Displays zero volume if TV is muted.
        :return: str
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
