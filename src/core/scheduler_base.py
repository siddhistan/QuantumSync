
from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.core.process import Process
from src.core.timeline import Timeline


class SchedulerBase(ABC):
    """Base class for all CPU scheduling algorithms."""

    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Scheduler name must be a non-empty string.")

        self.name = name

    def schedule(self, processes: Sequence[Process]) -> Timeline:
        """
        Validate processes, execute the scheduling algorithm,
        and return the resulting CPU timeline.
        """

        # Validate the input collection.
        if not isinstance(processes, Sequence):
            raise TypeError("Processes must be a list or tuple.")

        processes = list(processes)

        # Validate individual process objects.
        for process in processes:
            if not isinstance(process, Process):
                raise TypeError("All elements must be Process objects.")

        # Ensure process IDs are unique.
        pids = [process.pid for process in processes]

        if len(pids) != len(set(pids)):
            raise ValueError("Process IDs must be unique.")

        # Ensure all processes are in their initial execution state.
        for process in processes:
            if (
                process.remaining_time != process.burst_time
                or process.start_time is not None
                or process.completion_time is not None
            ):
                raise ValueError(
                    f"Process P{process.pid} is not in its initial state. "
                    "Use reset() or clone() before scheduling."
                )

        # Create a fresh timeline for this scheduling run.
        timeline = Timeline()

        # Handle an empty workload safely.
        if not processes:
            return timeline

        # Execute the algorithm-specific scheduling logic.
        self._execute(processes, timeline)

        return timeline

    @abstractmethod
    def _execute(
        self,
        processes: list[Process],
        timeline: Timeline
    ) -> None:
        """
        Implement the actual scheduling logic in child classes.

        Each scheduling algorithm must:
        1. Decide which process executes next.
        2. Update process runtime attributes.
        3. Record CPU execution using the supplied timeline.
        """
        pass
