
from dataclasses import dataclass, field


@dataclass
class Process:
    """Represents an individual process in CPU scheduling."""

    # Input attributes
    pid: int
    burst_time: int
    arrival_time: int = 0
    priority: int = 0

    # Runtime attributes
    remaining_time: int = field(init=False)
    start_time: int | None = field(default=None, init=False)
    completion_time: int | None = field(default=None, init=False)

    def __post_init__(self):
        if not isinstance(self.pid, int) or isinstance(self.pid, bool):
            raise TypeError("PID must be an integer.")
        if self.pid < 1:
            raise ValueError("PID must be positive.")

        if not isinstance(self.burst_time, int) or isinstance(self.burst_time, bool):
            raise TypeError("Burst time must be an integer.")
        if self.burst_time <= 0:
            raise ValueError("Burst time must be positive.")

        if not isinstance(self.arrival_time, int) or isinstance(self.arrival_time, bool):
            raise TypeError("Arrival time must be an integer.")
        if self.arrival_time < 0:
            raise ValueError("Arrival time cannot be negative.")

        if not isinstance(self.priority, int) or isinstance(self.priority, bool):
            raise TypeError("Priority must be an integer.")

        self.remaining_time = self.burst_time

    @property
    def is_completed(self) -> bool:
        return self.remaining_time == 0

    def reset(self):
        """Reset execution state for another scheduling run."""
        self.remaining_time = self.burst_time
        self.start_time = None
        self.completion_time = None

    def clone(self):
        """Create an independent process with fresh execution state."""
        return Process(
            pid=self.pid,
            burst_time=self.burst_time,
            arrival_time=self.arrival_time,
            priority=self.priority
        )
