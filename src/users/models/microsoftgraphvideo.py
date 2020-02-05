# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Microsoftgraphvideo(Model):
    """video.

    :param audio_bits_per_sample:
    :type audio_bits_per_sample: int
    :param audio_channels:
    :type audio_channels: int
    :param audio_format:
    :type audio_format: str
    :param audio_samples_per_second:
    :type audio_samples_per_second: int
    :param bitrate:
    :type bitrate: int
    :param duration:
    :type duration: long
    :param four_cc:
    :type four_cc: str
    :param frame_rate:
    :type frame_rate: float
    :param height:
    :type height: int
    :param width:
    :type width: int
    """

    _validation = {
        'audio_bits_per_sample': {'maximum': 2147483647, 'minimum': -2147483648},
        'audio_channels': {'maximum': 2147483647, 'minimum': -2147483648},
        'audio_samples_per_second': {'maximum': 2147483647, 'minimum': -2147483648},
        'bitrate': {'maximum': 2147483647, 'minimum': -2147483648},
        'height': {'maximum': 2147483647, 'minimum': -2147483648},
        'width': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'audio_bits_per_sample': {'key': 'audioBitsPerSample', 'type': 'int'},
        'audio_channels': {'key': 'audioChannels', 'type': 'int'},
        'audio_format': {'key': 'audioFormat', 'type': 'str'},
        'audio_samples_per_second': {'key': 'audioSamplesPerSecond', 'type': 'int'},
        'bitrate': {'key': 'bitrate', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'long'},
        'four_cc': {'key': 'fourCC', 'type': 'str'},
        'frame_rate': {'key': 'frameRate', 'type': 'float'},
        'height': {'key': 'height', 'type': 'int'},
        'width': {'key': 'width', 'type': 'int'},
    }

    def __init__(self, audio_bits_per_sample=None, audio_channels=None, audio_format=None, audio_samples_per_second=None, bitrate=None, duration=None, four_cc=None, frame_rate=None, height=None, width=None):
        super(Microsoftgraphvideo, self).__init__()
        self.audio_bits_per_sample = audio_bits_per_sample
        self.audio_channels = audio_channels
        self.audio_format = audio_format
        self.audio_samples_per_second = audio_samples_per_second
        self.bitrate = bitrate
        self.duration = duration
        self.four_cc = four_cc
        self.frame_rate = frame_rate
        self.height = height
        self.width = width
