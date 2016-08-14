# coding: utf-8

# $Id: $
from fffw.graph.base import VIDEO, AUDIO, Dest, Source, Node
from fffw.wrapper import BaseWrapper

__all__ = [
    'VideoCodec',
    'AudioCodec'
]


class BaseCodec(BaseWrapper, Node):
    codec_type = None

    @property
    def enabled(self):
        return True

    def render(self, namer, id=None, partial=False):
        return []

    def __init__(self, **kw):
        super(BaseCodec, self).__init__(**kw)
        self.map = None

    def connect(self, dest):
        assert isinstance(dest, Dest), "Codec connects to Dest"
        self.map = '[%s]' % dest.id

    def __repr__(self):
        return "<%s>(%s)" % (
            self.codecname,
            ','.join('%s=%s' % (k, self._args[k]) for k in self._key_mapping
                     if self._args[k])
        )

    def connect_edge(self, edge):
        src = edge.input
        assert isinstance(src, Source), "Codec connect edge only from Source"
        assert src.id, "Source file has not stream of desired type"
        self.map = src.id

    @property
    def codecname(self):
        return self._args['codec']


class VideoCodec(BaseCodec):
    codec_type = VIDEO
    arguments = [
        ('map', '-map '),
        ('vbsf', '-bsf:v '),
        ('vcodec', '-c:v '),
        ('pass', '-pass '),
        ('pix_fmt', '-pix_fmt '),
        ('preset', '-preset '),
        ('tune', '-tune '),
        ('flags', '-flags '),
        ('force_key_frames', '-force_key_frames '),
        ('vprofile', '-profile:v '),
        ('level', '-level '),
        ('crf', '-crf '),
        ('minrate', '-minrate '),
        ('maxrate', '-maxrate '),
        ('bufsize', '-bufsize '),
        ('gop', '-g '),
        ('vrate', '-r '),
        ('vbitrate', '-b:v '),
        ('vaspect', '-aspect '),
        ('reframes', '-refs '),
        ('mbd', '-mbd '),
        ('trellis', '-trellis '),
        ('cmp', '-cmp '),
        ('subcmp', '-subcmp '),
        ('x265', '-x265-params '),
    ]

    def __init__(self, **kw):
        kw.setdefault('map', '0:v')
        super(VideoCodec, self).__init__(**kw)

    @property
    def codecname(self):
        return self._args['vcodec']


class AudioCodec(BaseCodec):
    codec_type = AUDIO
    arguments = [
        ('map', '-map '),
        ('absf', '-bsf:a '),
        ('acodec', '-c:a '),
        ('aprofile', '-profile:a '),
        ('abitrate', '-b:a '),
        ('arate', '-ar '),
        ('achannels', '-ac '),
    ]

    def __init__(self, **kw):
        kw.setdefault('map', '0:a')
        super(AudioCodec, self).__init__(**kw)

    @property
    def codecname(self):
        return self._args['acodec']
