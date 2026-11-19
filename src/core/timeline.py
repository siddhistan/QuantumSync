
from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionSegment:
    """Represents one continuous CPU execution interval."""

    pid: int | None
    start_time: int
    end_time: int

    def __post_init__(self):
        if self.pid is not None:
            if not isinstance(self.pid, int) or isinstance(self.pid, bool):
                raise TypeError("PID must be an integer or None.")

            if self.pid < 1:
                raise ValueError("PID must be positive.")

        if not isinstance(self.start_time, int) or isinstance(self.start_time, bool):
            raise TypeError("Start time must be an integer.")

        if not isinstance(self.end_time, int) or isinstance(self.end_time, bool):
            raise TypeError("End time must be an integer.")

        if self.start_time < 0:
            raise ValueError("Start time cannot be negative.")

        if self.end_time <= self.start_time:
            raise ValueError("End time must be greater than start time.")

    @property
    def duration(self) -> int:
        """Return the duration of this execution segment."""
        return self.end_time - self.start_time

    @property
    def is_idle(self) -> bool:
        """Check whether the CPU was idle during this segment."""
        return self.pid is None


class Timeline:
    """Stores the chronological execution history of the CPU."""

    def __init__(self):
        self._segments: list[ExecutionSegment] = []

    def add_segment(
        self,
        pid: int | None,
        start_time: int,
        end_time: int
    ) -> None:
        """Add a process execution or CPU idle segment."""

        segment = ExecutionSegment(
            pid=pid,
            start_time=start_time,
            end_time=end_time
        )

        if self._segments:
            previous_segment = self._segments[-1]

            if segment.start_time < previous_segment.end_time:
                raise ValueError("Execution segments cannot overlap or go backwards.")

        self._segments.append(segment)

    def get_segments(self) -> list[ExecutionSegment]:
        """Return a copy of all recorded execution segments."""
        return self._segments.copy()

    def clear(self) -> None:
        """Remove all recorded execution segments."""
        self._segments.clear()

    @property
    def total_time(self) -> int:
        """Return the total elapsed time covered by the timeline."""
        if not self._segments:
            return 0

        return self._segments[-1].end_time

    @property
    def total_busy_time(self) -> int:
        """Return the total time for which the CPU was executing processes."""
        return sum(
            segment.duration
            for segment in self._segments
            if not segment.is_idle
        )

    @property
    def total_idle_time(self) -> int:
        """Return the total time for which the CPU was idle."""
        return sum(
            segment.duration
            for segment in self._segments
            if segment.is_idle
        )

    def __len__(self) -> int:
        """Return the number of recorded execution segments."""
        return len(self._segments)

    def __repr__(self) -> str:
        return f"Timeline(segments={len(self._segments)})"
