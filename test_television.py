import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv_init = Television()
        self.tv_power = Television()
        self.tv_mute = Television()
        self.tv_channel_up = Television()
        self.tv_channel_down = Television()
        self.tv_volume_up = Television()
        self.tv_volume_down = Television()

    def teardown_method(self):
        del self.tv_init
        del self.tv_power
        del self.tv_mute
        del self.tv_channel_up
        del self.tv_channel_down
        del self.tv_volume_up
        del self.tv_volume_down

    def test_init(self):
        assert self.tv_init.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv_power.power()
        assert self.tv_power.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv_power.power()
        assert self.tv_power.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        # power on, volume 1, mute.
        self.tv_mute.power()
        self.tv_mute.volume_up()
        self.tv_mute.mute()
        assert self.tv_mute.__str__() == "Power = True, Channel = 0, Volume = 0"

        # unmute
        self.tv_mute.mute()
        assert self.tv_mute.__str__() == "Power = True, Channel = 0, Volume = 1"

        # power off
        self.tv_mute.power()
        assert self.tv_mute.__str__() == "Power = False, Channel = 0, Volume = 1"

        # power off - unmute does not work.
        self.tv_mute.mute()
        assert self.tv_mute.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        # power off - channel up does not work.
        self.tv_channel_up.channel_up()
        assert self.tv_channel_up.__str__() == "Power = False, Channel = 0, Volume = 0"

        # power on - channel up works
        self.tv_channel_up.power()
        self.tv_channel_up.channel_up()
        assert self.tv_channel_up.__str__() == "Power = True, Channel = 1, Volume = 0"

        # power on, channel wraps down to minimum channel.
        self.tv_channel_up.channel_up()
        self.tv_channel_up.channel_up()
        self.tv_channel_up.channel_up()
        assert self.tv_channel_up.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        # power off - channel down does not work
        self.tv_channel_down.channel_down()
        assert self.tv_channel_down.__str__() == "Power = False, Channel = 0, Volume = 0"

        # power on - channel wraps up to maximum channel.
        self.tv_channel_down.power()
        self.tv_channel_down.channel_down()
        assert self.tv_channel_down.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        # power off - volume up does not work
        self.tv_volume_up.volume_up()
        assert self.tv_volume_up.__str__() == "Power = False, Channel = 0, Volume = 0"

        # power on - volume increases by 1
        self.tv_volume_up.power()
        self.tv_volume_up.volume_up()
        assert self.tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 1"

        # TV is muted, then volume is increased - TV auto
        # unmutes and increases volume to 2 (from 1).
        self.tv_volume_up.mute()
        self.tv_volume_up.volume_up()
        assert self.tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 2"

        # at maximum volume - volume stays constant.
        self.tv_volume_up.volume_up()
        assert self.tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        # power off - volume down does not work
        self.tv_volume_down.volume_down()
        assert self.tv_volume_down.__str__() == "Power = False, Channel = 0, Volume = 0"

        # power on. volume increased to maximum, then decreased to 1.
        self.tv_volume_down.power()
        self.tv_volume_down.volume_up()
        self.tv_volume_down.volume_up()
        self.tv_volume_down.volume_down()
        assert self.tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 1"

        # TV is muted, then volume is decreased - TV auto
        # unmutes and decreases volume to 0 (from 1).
        self.tv_volume_down.mute()
        self.tv_volume_down.volume_down()
        assert self.tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 0"

        # at minimum volume - volume stays constant.
        self.tv_volume_down.volume_down()
        assert self.tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 0"
