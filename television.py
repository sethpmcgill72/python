class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Creates a new TV object with attributes status, muted, both set to False,
        and volume and channel, set to MIN_VOLUME and MIN_CHANNEL, respectively.
        """
        self.__status = False #power
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles TV power.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        If powered, toggles TV mute option.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        If powered, increments the current channel by 1. Moves to channel
        MIN_CHANNEL if incrementing results in a channel above MAX_CHANNEL.
        """
        if self.__status:
            self.__channel += 1

            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        If powered, Decrements the current channel by 1. Moves to channel
        MAX_CHANNEL if decrementing results in a channel below MIN_CHANNEL.
        """
        if self.__status:
            self.__channel -= 1

            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        If powered, increases TV volume by 1, up to 2. Unmutes TV if muted.
        """
        if self.__status:
            if self.__muted: #unmute TV to allow volume changing.
                self.mute()

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        If powered, decreases TV volume by 1, down to 0. Unmutes TV if muted.
        """
        if self.__status:
            if self.__muted: #unmute TV to allow volume changing.
                self.mute()

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Displays TV power, channel, and volume information.
        Displays zero volume if TV is muted.
        :return: str
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
