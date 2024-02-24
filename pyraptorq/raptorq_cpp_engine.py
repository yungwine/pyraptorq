import base64
import ctypes
import typing

from .engine import RaptorQEngine


class RaptorQCppEngine(RaptorQEngine):

    def __init__(self, path_to_lib: str):
        self.lib = ctypes.CDLL(path_to_lib)
        assert self.lib.test_link(1, 2) == 3, 'Invalid library'

        # Define signatures
        self.lib.get_decoder.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.lib.get_decoder.restype = ctypes.c_void_p

        self.lib.may_try_decode.argtypes = [ctypes.c_void_p]
        self.lib.may_try_decode.restype = ctypes.c_bool

        self.lib.add_symbol.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
        self.lib.add_symbol.restype = ctypes.c_bool

        self.lib.try_decode.argtypes = [ctypes.c_void_p]
        self.lib.try_decode.restype = ctypes.c_char_p

        self.lib.destroy_decoder.argtypes = [ctypes.c_void_p]
        self.lib.destroy_decoder.restype = None

        self.lib.get_encoder.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
        self.lib.get_encoder.restype = ctypes.c_void_p

        self.lib.gen_symbol.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.lib.gen_symbol.restype = ctypes.c_char_p

        self.lib.destroy_encoder.argtypes = [ctypes.c_void_p]
        self.lib.destroy_encoder.restype = None

    def get_decoder(self, symbol_count: int, symbol_size: int, data_size: int):
        return self.lib.get_decoder(symbol_count, symbol_size, data_size)

    def may_try_decode(self, decoder) -> bool:
        return self.lib.may_try_decode(decoder)

    def add_symbol(self, decoder, symbol_id: int, symbol_data: bytes) -> bool:
        return self.lib.add_symbol(decoder, symbol_id, len(symbol_data), symbol_data)

    def try_decode(self, decoder) -> typing.Optional[bytes]:
        res = self.lib.try_decode(decoder)
        if res is not None:
            res = base64.b64decode(res)
        return res

    def destroy_decoder(self, decoder):
        self.lib.destroy_decoder(decoder)

    def get_encoder(self, data: bytes, symbol_size: int):
        res = self.lib.get_encoder(data, len(data), symbol_size)
        if res is None:
            raise Exception('Failed to create encoder')
        return res

    def gen_symbol(self, encoder, symbol_id: int) -> bytes:
        res = self.lib.gen_symbol(encoder, symbol_id)
        if res is None:
            raise Exception('Failed to generate symbol')
        return base64.b64decode(res)

    def destroy_encoder(self, encoder):
        self.lib.destroy_encoder(encoder)

    @classmethod
    def default(cls):
        import pkg_resources
        import platform

        arch = platform.system().lower()
        machine = platform.machine().lower()
        name = f'libpyraptorq.{machine}'
        if arch == 'darwin':
            name += '.dylib'
        elif arch == 'linux':
            name += '.so'
        elif arch == 'windows':
            name += '.dll'
        else:
            raise Exception('Unsupported platform')

        if not pkg_resources.resource_exists('pyraptorq', f'distlib/{arch}/{name}'):
            raise Exception('No binaries found')
        return cls(pkg_resources.resource_filename('pyraptorq', f'distlib/{arch}/{name}'))
