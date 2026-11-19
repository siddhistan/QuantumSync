
from src.core.scheduler_base import SchedulerBase
from src.core.process import Process
from src.core.timeline import Timeline


class FCFSScheduler(SchedulerBase):
    """First Come, First Served CPU scheduling algorithm."""

    def __init__(self):
        super().__init__("FCFS")

    def _execute(
        self,
        processes: list[Process],
        timeline: Timeline
    ) -> None:
        """
        Execute processes in order of arrival time.

        FCFS is non-preemptive, meaning each process
        executes until its burst time is completed.
        """

        # Sort processes by arrival time.
        # Python's sorting is stable, so processes with
        # identical arrival times retain their input order.
        sorted_processes = sorted(
            processes,
            key=lambda process: process.arrival_time
        )

        # Track the current CPU time.
        current_time = 0

        # Execute each process in arrival order.
        for process in sorted_processes:

            # Handle CPU idle time if the next process
            # has not arrived yet.
            if current_time < process.arrival_time:

                timeline.add_segment(
                    pid=None,
                    start_time=current_time,
                    end_time=process.arrival_time
                )

                current_time = process.arrival_time

            # Record the process's starting time.
            process.start_time = current_time

            # Calculate when the process will finish.
            process.completion_time = (
                current_time + process.burst_time
            )

            # FCFS executes the entire process without interruption.
            process.remaining_time = 0

            # Record the execution interval in the timeline.
            timeline.add_segment(
                pid=process.pid,
                start_time=process.start_time,
                end_time=process.completion_time
            )

            # Move the CPU clock forward.
            current_time = process.completion_time
