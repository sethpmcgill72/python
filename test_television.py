import pytest
from television import Television

def main():
    init_test()
    power_test()
    mute_test()
    channel_up_test()
    channel_down_test()
    volume_up_test()
    volume_down_test()

def init_test():
    tv_init = Television()
    assert tv_init.__str__() == "Power = False, Channel = 0, Volume = 0"

def power_test():
    tv_power = Television()

    #power on
    tv_power.power()
    assert tv_power.__str__() == "Power = True, Channel = 0, Volume = 0"

    #power off
    tv_power.power()
    assert tv_power.__str__() == "Power = False, Channel = 0, Volume = 0"

def mute_test():
    tv_mute = Television()

    #power on, volume 1, mute.
    tv_mute.power()
    tv_mute.volume_up()
    tv_mute.mute()
    assert tv_mute.__str__() == "Power = True, Channel = 0, Volume = 0"

    #unmute
    tv_mute.mute()
    assert tv_mute.__str__() == "Power = True, Channel = 0, Volume = 1"

    #power off
    tv_mute.power()
    assert tv_mute.__str__() == "Power = False, Channel = 0, Volume = 1"

    #power off - unmute does not work.
    tv_mute.mute()
    assert tv_mute.__str__() == "Power = False, Channel = 0, Volume = 1"

def channel_up_test():
    tv_channel_up = Television()

    #power off - channel up does not work.
    tv_channel_up.channel_up()
    assert tv_channel_up.__str__() == "Power = False, Channel = 0, Volume = 0"

    #power on - channel up works
    tv_channel_up.power()
    tv_channel_up.channel_up()
    assert tv_channel_up.__str__() == "Power = True, Channel = 1, Volume = 0"

    #power on, channel wraps down to minimum channel.
    tv_channel_up.channel_up()
    tv_channel_up.channel_up()
    tv_channel_up.channel_up()
    assert tv_channel_up.__str__() == "Power = True, Channel = 0, Volume = 0"

def channel_down_test():
    tv_channel_down = Television()

    #power off - channel down does not work
    tv_channel_down.channel_down()
    assert tv_channel_down.__str__() == "Power = False, Channel = 0, Volume = 0"

    #power on - channel wraps up to maximum channel.
    tv_channel_down.power()
    tv_channel_down.channel_down()
    assert tv_channel_down.__str__() == "Power = True, Channel = 3, Volume = 0"

def volume_up_test():
    tv_volume_up = Television()

    #power off - volume up does not work
    tv_volume_up.volume_up()
    assert tv_volume_up.__str__() == "Power = False, Channel = 0, Volume = 0"

    #power on - volume increases by 1
    tv_volume_up.power()
    tv_volume_up.volume_up()
    assert tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 1"

    #TV is muted, then volume is increased - TV auto
    # unmutes and increases volume to 2 (from 1).
    tv_volume_up.mute()
    tv_volume_up.volume_up()
    assert tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 2"

    #at maximum volume - volume stays constant.
    tv_volume_up.volume_up()
    assert tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 2"

def volume_down_test():
    tv_volume_down = Television()

    #power off - volume down does not work
    tv_volume_down.volume_down()
    assert tv_volume_down.__str__() == "Power = False, Channel = 0, Volume = 0"

    #power on. volume increased to maximum, then decreased to 1.
    tv_volume_down.power()
    tv_volume_down.volume_up()
    tv_volume_down.volume_up()
    tv_volume_down.volume_down()
    assert tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 1"

    #TV is muted, then volume is decreased - TV auto
    #unmutes and decreases volume to 0 (from 1).
    tv_volume_down.mute()
    tv_volume_down.volume_down()
    assert tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 0"

    #at minimum volume - volume stays constant.
    tv_volume_down.volume_down()
    assert tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 0"

if __name__ == "__main__":
    main()

    # import pytest
    # from television import Television
    #
    # class TestTelevision:
    #     def setup(self):
    #         self.tv_init = Television()
    #         self.tv_power = Television()
    #         self.tv_mute = Television()
    #         self.tv_channel_up = Television()
    #         self.tv_channel_down = Television()
    #         self.tv_volume_up = Television()
    #         self.tv_volume_down = Television()
    #
    #         self.init_test()
    #         self.power_test()
    #         self.mute_test()
    #         self.channel_up_test()
    #         self.channel_down_test()
    #         self.volume_up_test()
    #         self.volume_down_test()
    #
    #     def teardown(self):
    #         del self.tv_init
    #         del self.tv_power
    #         del self.tv_mute
    #         del self.tv_channel_up
    #         del self.tv_channel_down
    #         del self.tv_volume_up
    #         del self.tv_volume_down
    #
    #     def init_test(self):
    #         assert self.tv_init.__str__() == "Power = False, Channel = 0, Volume = 0"
    #
    #     def power_test(self):
    #         self.tv_power.power()
    #         assert self.tv_power.__str__() == "Power = True, Channel = 0, Volume = 0"
    #
    #         self.tv_power.power()
    #         assert self.tv_power.__str__() == "Power = False, Channel = 0, Volume = 0"
    #
    #     def mute_test(self):
    #         # power on, volume 1, mute.
    #         self.tv_mute.power()
    #         self.tv_mute.volume_up()
    #         self.tv_mute.mute()
    #         assert self.tv_mute.__str__() == "Power = True, Channel = 0, Volume = 0"
    #
    #         # unmute
    #         self.tv_mute.mute()
    #         assert self.tv_mute.__str__() == "Power = True, Channel = 0, Volume = 1"
    #
    #         # power off
    #         self.tv_mute.power()
    #         assert self.tv_mute.__str__() == "Power = False, Channel = 0, Volume = 1"
    #
    #         # power off - unmute does not work.
    #         self.tv_mute.mute()
    #         assert self.tv_mute.__str__() == "Power = False, Channel = 0, Volume = 1"
    #
    #     def channel_up_test(self):
    #         # power off - channel up does not work.
    #         self.tv_channel_up.channel_up()
    #         assert self.tv_channel_up.__str__() == "Power = False, Channel = 0, Volume = 0"
    #
    #         # power on - channel up works
    #         self.tv_channel_up.power()
    #         self.tv_channel_up.channel_up()
    #         assert self.tv_channel_up.__str__() == "Power = True, Channel = 1, Volume = 0"
    #
    #         # power on, channel wraps down to minimum channel.
    #         self.tv_channel_up.channel_up()
    #         self.tv_channel_up.channel_up()
    #         self.tv_channel_up.channel_up()
    #         assert self.tv_channel_up.__str__() == "Power = True, Channel = 0, Volume = 0"
    #
    #     def channel_down_test(self):
    #         # power off - channel down does not work
    #         self.tv_channel_down.channel_down()
    #         assert self.tv_channel_down.__str__() == "Power = False, Channel = 0, Volume = 0"
    #
    #         # power on - channel wraps up to maximum channel.
    #         self.tv_channel_down.power()
    #         self.tv_channel_down.channel_down()
    #         assert self.tv_channel_down.__str__() == "Power = True, Channel = 3, Volume = 0"
    #
    #     def volume_up_test(self):
    #         # power off - volume up does not work
    #         self.tv_volume_up.volume_up()
    #         assert self.tv_volume_up.__str__() == "Power = False, Channel = 0, Volume = 0"
    #
    #         # power on - volume increases by 1
    #         self.tv_volume_up.power()
    #         self.tv_volume_up.volume_up()
    #         assert self.tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 1"
    #
    #         # TV is muted, then volume is increased - TV auto
    #         # unmutes and increases volume to 2 (from 1).
    #         self.tv_volume_up.mute()
    #         self.tv_volume_up.volume_up()
    #         assert self.tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 2"
    #
    #         # at maximum volume - volume stays constant.
    #         self.tv_volume_up.volume_up()
    #         assert self.tv_volume_up.__str__() == "Power = True, Channel = 0, Volume = 2"
    #
    #     def volume_down_test(self):
    #         # power off - volume down does not work
    #         self.tv_volume_down.volume_down()
    #         assert self.tv_volume_down.__str__() == "Power = False, Channel = 0, Volume = 0"
    #
    #         # power on. volume increased to maximum, then decreased to 1.
    #         self.tv_volume_down.power()
    #         self.tv_volume_down.volume_up()
    #         self.tv_volume_down.volume_up()
    #         self.tv_volume_down.volume_down()
    #         assert self.tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 1"
    #
    #         # TV is muted, then volume is decreased - TV auto
    #         # unmutes and decreases volume to 0 (from 1).
    #         self.tv_volume_down.mute()
    #         self.tv_volume_down.volume_down()
    #         assert self.tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 0"
    #
    #         # at minimum volume - volume stays constant.
    #         self.tv_volume_down.volume_down()
    #         assert self.tv_volume_down.__str__() == "Power = True, Channel = 0, Volume = 0"
    #
    #
    # if __name__.__str__() == "__main__":
    #     print("test")
    #     test = TestTelevision()