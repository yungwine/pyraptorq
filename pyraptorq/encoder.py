from .engine import RaptorQEngine
from .raptorq_cpp_engine import RaptorQCppEngine


class Encoder:

    def __init__(
            self,
            data: bytes,
            symbol_size,
            raptorq_engine: RaptorQEngine = None
    ):
        self.data = data
        self.symbol_size = symbol_size
        if raptorq_engine is None:
            raptorq_engine = RaptorQCppEngine.default()
        self.raptorq_engine = raptorq_engine
        self.encoder = self.raptorq_engine.get_encoder(
            data,
            symbol_size,
        )

    def gen_symbol(self, symbol_id):
        return self.raptorq_engine.gen_symbol(self.encoder, symbol_id)

    def __del__(self):
        self.raptorq_engine.destroy_encoder(self.encoder)
