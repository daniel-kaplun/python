class Television:
    """Represents a television with power, volume, channel, and mute controls"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initializes the television with power off, unmuted, at minimum volume, and on the minimum channel."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggles television's power"""
        self.__status = not self.__status
    
    def mute(self) -> None:
        """Mutes and unmutes television when television is on"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Switches channels upwards, wrapping to minimum when necessary"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Switches channels downwards, wrapping to maximum when necessary"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase volume and unmute if necessary"""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease volume and unmute if necessary"""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the television's power, channel, and volume status"""
        volume = Television.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"