
from src.core.scheduler_base import SchedulerBase
from src.core.process import Process
from src.core.timeline import Timeline


class SJFScheduler(SchedulerBase):
    """Non-Preemptive Shortest Job First CPU scheduling algorithm."""

    def __init__(self):
        super().__init__("SJF")

    def _execute(
        self,
        processes: list[Process],
        timeline: Timeline
    ) -> None:
        """
        Execute the available process with the shortest burst time.

        SJF is non-preemptive, meaning each selected process
        executes until its burst time is completed.
        """

        # Sort processes by arrival time.
        # Python's stable sorting preserves input order
        # when arrival times are identical.
        sorted_processes = sorted(
            processes,
            key=lambda process: process.arrival_time
        )

        # Maintain the processes that have arrived and are
        # waiting for CPU execution.
        ready_queue = []

        # Track the current position in sorted_processes.
        next_process_index = 0

        # Track the current CPU time.
        current_time = 0

        # Continue until every process has been scheduled.
        while next_process_index < len(sorted_processes) or ready_queue:

            # Add all processes that have arrived by current_time.
            while (
                next_process_index < len(sorted_processes)
                and sorted_processes[next_process_index].arrival_time
                <= current_time
            ):
                ready_queue.append(
                    sorted_processes[next_process_index]
                )

                next_process_index += 1

            # If no process is available, advance time to
            # the next process's arrival.
            if not ready_queue:

                next_arrival = sorted_processes[
                    next_process_index
                ].arrival_time

                # Record CPU idle time.
                if current_time < next_arrival:
                    timeline.add_segment(
                        pid=None,
                        start_time=current_time,
                        end_time=next_arrival
                    )

                current_time = next_arrival

                continue

            # Select the process with the shortest burst time.
            # min() preserves ready_queue order when burst times tie.
            selected_process = min(
                ready_queue,
                key=lambda process: process.burst_time
            )

            # Remove the selected process from the ready queue.
            ready_queue.remove(selected_process)

            # Record the process's starting time.
            selected_process.start_time = current_time

            # Calculate its completion time.
            selected_process.completion_time = (
                current_time + selected_process.burst_time
            )

            # Execute the entire process (non-preemptive).
            selected_process.remaining_time = 0

            # Record its execution in the timeline.
            timeline.add_segment(
                pid=selected_process.pid,
                start_time=selected_process.start_time,
                end_time=selected_process.completion_time
            )

            # Advance the CPU clock.
            current_time = selected_process.completion_time
