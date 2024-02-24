import typing
from abc import ABC, abstractmethod


class RaptorQEngine(ABC):

    @abstractmethod
    def get_decoder(self, symbol_count: int, symbol_size: int, data_size: int):
        ...

    @abstractmethod
    def may_try_decode(self, decoder) -> bool:
        ...

    @abstractmethod
    def add_symbol(self, decoder, symbol_id: int, symbol_data: bytes) -> bool:
        ...

    @abstractmethod
    def try_decode(self, decoder) -> typing.Optional[bytes]:
        ...

    @abstractmethod
    def destroy_decoder(self, decoder):
        ...

    @abstractmethod
    def get_encoder(self, data: bytes, symbol_size: int):
        ...

    @abstractmethod
    def gen_symbol(self, encoder, symbol_id: int) -> bytes:
        ...

    @abstractmethod
    def destroy_encoder(self, encoder):
        ...
