import time
from dataclasses import dataclass, field
from typing import Callable, ClassVar, Dict, Optional


class TimerError(Exception):
    """Custom excepicional para reportar erros"""


@dataclass
class Timer:
    """    timers = {}

    def __init__(self, name=None, text='Tempo decorrido: {:0.4f} segundos', logger=print):
        self._star_time = None
        self.name = name
        self.text = text
        self.logger = logger

        if name:
            self.timers.setdefault(name, 0)"""
    timers: ClassVar[Dict[str, float]] = {}
    name: Optional[str] = None
    text: str = "Tempo decorrido: {:0.2f} segundos."
    logger: Optional[Callable[[str], None]] = print
    _start_time: Optional[float] = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.name is not None:
            self.timers.setdefault(self.name, 0)

    def start(self) -> None:
        if self._start_time is not None:
            raise TimerError(f'Tempo já em andamento. use Stop() para parar o tempo.')

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        if self._start_time is None:
            raise TimerError(f'O tempo não está correndo. use Start() para começar a contar o tempo.')

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))

        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time


def main():
    t = Timer()
    t.start()
    for contador in range(1000):
        print('Temporazidor...')
    t.stop()


if __name__ == "__main__":
    main()
