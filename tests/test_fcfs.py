
import pytest

from src.core.process import Process
from src.algorithms.traditional.fcfs import FCFSScheduler


def create_processes(data):
    """Create fresh Process objects from test data."""
    return [
        Process(
            pid=pid,
            arrival_time=arrival,
            burst_time=burst
        )
        for pid, arrival, burst in data
    ]


def test_fcfs_execution_order():
    """Processes should execute in arrival order."""

    processes = create_processes([
        (1, 0, 5),
        (2, 2, 3),
        (3, 4, 2)
    ])

    scheduler = FCFSScheduler()
    timeline = scheduler.schedule(processes)

    segments = timeline.get_segments()

    assert [
        (s.pid, s.start_time, s.end_time)
        for s in segments
    ] == [
        (1, 0, 5),
        (2, 5, 8),
        (3, 8, 10)
    ]


def test_fcfs_handles_idle_time():
    """CPU should remain idle when no process has arrived."""

    processes = create_processes([
        (1, 0, 3),
        (2, 7, 2)
    ])

    scheduler = FCFSScheduler()
    timeline = scheduler.schedule(processes)

    segments = timeline.get_segments()

    assert [
        (s.pid, s.start_time, s.end_time)
        for s in segments
    ] == [
        (1, 0, 3),
        (None, 3, 7),
        (2, 7, 9)
    ]


def test_fcfs_updates_process_attributes():
    """Process runtime attributes should be updated correctly."""

    processes = create_processes([
        (1, 0, 5),
        (2, 2, 3)
    ])

    scheduler = FCFSScheduler()
    scheduler.schedule(processes)

    assert processes[0].start_time == 0
    assert processes[0].completion_time == 5
    assert processes[0].remaining_time == 0

    assert processes[1].start_time == 5
    assert processes[1].completion_time == 8
    assert processes[1].remaining_time == 0


def test_fcfs_preserves_input_order_for_same_arrival():
    """Processes with identical arrival times retain input order."""

    processes = create_processes([
        (3, 0, 2),
        (1, 0, 3),
        (2, 0, 1)
    ])

    scheduler = FCFSScheduler()
    timeline = scheduler.schedule(processes)

    segments = timeline.get_segments()

    assert [s.pid for s in segments] == [3, 1, 2]


def test_fcfs_empty_workload():
    """An empty workload should return an empty timeline."""

    scheduler = FCFSScheduler()
    timeline = scheduler.schedule([])

    assert len(timeline) == 0
    assert timeline.total_time == 0


def test_fcfs_rejects_already_executed_processes():
    """A completed process should not be scheduled again without reset."""

    processes = create_processes([
        (1, 0, 4)
    ])

    scheduler = FCFSScheduler()

    scheduler.schedule(processes)

    with pytest.raises(ValueError):
        scheduler.schedule(processes)
