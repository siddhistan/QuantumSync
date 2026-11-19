# QuantumSync
 
QuantumSync is a CPU scheduling simulation and benchmarking framework designed to implement, evaluate, and compare traditional scheduling algorithms alongside research-based adaptive scheduling approaches.
 
The project investigates how different scheduling strategies behave under diverse workload conditions, examining their efficiency, responsiveness, fairness, and scheduling overhead.
 
Building upon an earlier CPU scheduling implementation, QuantumSync aims to evolve into a comprehensive experimental framework that combines algorithm implementation, configurable workload generation, automated benchmarking, and performance visualization.
 
## Project Objectives
 
The primary objective is not simply to identify the fastest scheduling algorithm, but to understand how different algorithms perform under different workloads, where they excel, and what trade-offs they introduce.
 
- Implement and evaluate six traditional CPU scheduling algorithms.
- Reproduce and integrate advanced scheduling approaches proposed in research literature.
- Design configurable workload generators to simulate different process execution patterns.
- Conduct controlled experiments by executing multiple scheduling algorithms on identical workloads.
- Evaluate scheduling performance across efficiency, responsiveness, fairness, and overhead metrics.
- Develop an interactive visualization interface featuring Gantt charts, performance tables, and comparative graphs.
- Identify performance trade-offs and determine the workload conditions under which particular scheduling strategies perform better.
 
## Traditional Scheduling Algorithms
 
The framework incorporates classical CPU scheduling techniques as baseline implementations for comparative evaluation.
 
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Priority Scheduling
- Round Robin (RR)
- Additional traditional scheduling variants
 
The complete set of six algorithms will be documented alongside their respective implementation details.
 
## Research-Based Scheduling Algorithms
 
In addition to traditional scheduling approaches, QuantumSync investigates advanced scheduling strategies proposed in academic research.
 
| Algorithm | Description |
|---|---|
| Modified Priority Preemptive (MPP) | A modified priority-based preemptive scheduling approach |
| Agent-Based Adaptive Dynamic Round Robin (AADRR) | An agent-based scheduling approach incorporating adaptive time quantum selection |
 
These algorithms will be studied and implemented based on their respective research methodologies, with particular attention to their scheduling mechanisms, decision-making strategies, and underlying assumptions.
 
Additional research-based approaches may be explored as the project evolves.
 
## Benchmarking Framework
 
A major component of QuantumSync is its experimental benchmarking framework.
 
Rather than evaluating algorithms using a single fixed dataset, the system aims to generate configurable workloads representing different process execution conditions.
 
### Workload Scenarios
 
Planned workload scenarios include:
 
- **Uniform Workloads:** Processes with similar burst times.
- **Variable Workloads:** Processes with significantly different CPU burst requirements.
- **Dynamic Arrival Workloads:** Processes arriving at different points in time.
- **Priority-Driven Workloads:** Processes with varying priority levels.
- **High-Load Workloads:** Large numbers of competing processes.
- **Starvation-Prone Workloads:** Scenarios designed to investigate fairness and indefinite waiting.
- **Mixed Workloads:** Combinations of different arrival times, burst times, and priorities.
 
All scheduling algorithms will be evaluated against identical process datasets to ensure fair and reproducible comparisons.
 
## Performance Metrics
 
QuantumSync evaluates scheduling algorithms across multiple performance dimensions.
 
| Metric | Purpose |
|---|---|
| Average Waiting Time | Measures the average time processes spend waiting in the ready queue |
| Maximum Waiting Time | Identifies processes experiencing prolonged waiting |
| Average Turnaround Time | Measures the average time from process arrival to completion |
| Average Response Time | Measures how quickly processes receive their first CPU allocation |
| CPU Utilization | Measures the percentage of time the CPU remains busy |
| Throughput | Measures the number of completed processes per unit time |
| Context Switches | Evaluates scheduling overhead |
| Waiting Time Variance | Measures the distribution of waiting times |
| Turnaround Time Variance | Examines variations in process completion times |
| Jain's Fairness Index | Quantifies fairness in CPU resource allocation |
 
These metrics provide a multidimensional view of scheduling performance rather than relying on a single efficiency indicator.
 
## Experimental Capabilities
 
The benchmarking framework aims to automate the execution and evaluation of scheduling algorithms across configurable workloads.
 
Planned capabilities include:
 
- Running multiple scheduling algorithms on identical process datasets.
- Generating comparative performance tables.
- Visualizing performance differences using graphs.
- Analysing efficiency and fairness trade-offs.
- Investigating starvation and maximum waiting times.
- Studying how algorithm performance changes with increasing workload sizes.
- Identifying workload-specific strengths and weaknesses.
 
The emphasis is on experimental analysis rather than assuming that one scheduling algorithm is universally superior.
 
## Visualization
 
QuantumSync aims to provide an interactive interface for exploring CPU scheduling behaviour.
 
Planned visualization features include:
 
- Interactive Gantt charts representing process execution timelines.
- Process-level scheduling information.
- Comparative performance tables.
- Graphical metric comparisons across algorithms.
- Workload configuration and experiment execution.
- Exportable experimental results and reports.
 
## Architecture
 
The project is organized around three primary components:
 
1. **Scheduling Engine:** Contains the implementations of traditional and research-based CPU scheduling algorithms.
2. **Benchmarking Engine:** Handles workload generation, experiment execution, metric calculation, and comparative evaluation.
3. **Visualization Layer:** Presents scheduling timelines, performance metrics, and experimental results through an interactive interface.
 
## Research Foundation
 
The project draws upon academic literature covering traditional, hybrid, priority-based, and adaptive CPU scheduling techniques.
 
Selected research papers include:
 
- Agent-Based Adaptive Dynamic Round Robin (AADRR) Scheduling Algorithm (2025).
- Study and Evaluation of CPU Scheduling Algorithms (2024).
- A New Hybrid CPU Scheduling Algorithm: SJF with Round Robin (2020).
- Optimised Round Robin with Virtual Runtime for CPU Scheduling (2024).
- Optimizing Task Execution: The Impact of Dynamic Time Quantum and Priorities on Round Robin Scheduling (2023).
 
Additional references and implementation-specific research papers are maintained in the `docs/` directory.
 
## Team
 
| Member | Role |
|---|---|
| Siddharth Jain | Development, algorithm implementation, benchmarking and comparative analysis |
| Nishant Bisht | Development, algorithm implementation, system design and experimentation |
 
## Current Status
 
Currently evolving from an existing CPU scheduling implementation into a comprehensive benchmarking and experimental analysis framework.
 
The project is being expanded through additional algorithm implementations, research reproduction, workload generation, automated benchmarking, and visualization capabilities.
 
## Vision
 
QuantumSync aims to provide an experimental environment for understanding the behaviour of CPU scheduling algorithms beyond theoretical descriptions.
 
By combining established scheduling techniques with research-based adaptive approaches and systematic performance evaluation, the project seeks to explore an important question:
 
> Under what workload conditions do adaptive and hybrid CPU scheduling algorithms outperform traditional approaches, and what trade-offs do they introduce?
 
