from .engine import RaptorQEngine
from .raptorq_cpp_engine import RaptorQCppEngine


class Decoder:

    def __init__(
            self,
            symbol_count,
            symbol_size,
            data_size,
            raptorq_engine: RaptorQEngine = None
    ):
        self.symbol_count = symbol_count
        self.symbol_size = symbol_size
        self.data_size = data_size
        if raptorq_engine is None:
            raptorq_engine = RaptorQCppEngine.default()
        self.raptorq_engine = raptorq_engine
        self.decoder = self.raptorq_engine.get_decoder(
            symbol_count,
            symbol_size,
            data_size
        )

    def add_symbol(self, symbol_id, symbol_data):
        return self.raptorq_engine.add_symbol(
            self.decoder,
            symbol_id,
            symbol_data
        )

    def may_try_decode(self):
        return self.raptorq_engine.may_try_decode(self.decoder)

    def try_decode(self):
        return self.raptorq_engine.try_decode(self.decoder)

    def __del__(self):
        self.raptorq_engine.destroy_decoder(self.decoder)
