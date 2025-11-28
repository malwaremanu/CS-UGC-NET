# Operating System - Lecture 03: CPU Scheduling

## Overview
This lecture covers CPU scheduling algorithms, which determine which process runs on the CPU at any given time. It discusses different scheduling algorithms, their criteria, and their performance metrics.

## 1. CPU Scheduling Basics

### Definition
CPU Scheduling is the process of deciding which process in the ready queue gets to run on the CPU.

### Goals of Scheduling
- **Maximize CPU Utilization**: Keep CPU as busy as possible
- **Maximize Throughput**: Complete maximum number of processes per unit time
- **Minimize Turnaround Time**: Minimize time from process submission to completion
- **Minimize Waiting Time**: Minimize time process spends in ready queue
- **Minimize Response Time**: Minimize time from process request to first response
- **Fair CPU Allocation**: Distribute CPU fairly among processes

## 2. Scheduling Criteria

**CPU Burst**: Period when process is using CPU
**I/O Burst**: Period when process is waiting for I/O

### Performance Metrics

1. **CPU Utilization**: Percentage of time CPU is busy (0-100%)
   - Goal: Keep as high as possible (70-90% ideal)

2. **Throughput**: Number of processes completed per unit time
   - Goal: Maximize throughput

3. **Turnaround Time**: Time from process submission to completion
   - TAT = Completion Time - Arrival Time
   - Goal: Minimize TAT

4. **Waiting Time**: Time process spends in ready queue
   - WT = TAT - Burst Time
   - Goal: Minimize WT

5. **Response Time**: Time from submission to first response
   - Goal: Minimize RT

## 3. Scheduling Algorithms

### 1. First Come First Served (FCFS)

**Characteristics**:
- Simplest scheduling algorithm
- Non-preemptive
- Processes served in order of arrival
- Uses FIFO queue

**Advantages**:
- Simple to implement
- Fair allocation

**Disadvantages**:
- Can have long average waiting time
- Convoy effect (short processes wait for long processes)
- Not suitable for interactive systems

### 2. Shortest Job Next (SJN)

**Characteristics**:
- Non-preemptive
- Selects process with shortest CPU burst
- Minimizes average waiting time

**Advantages**:
- Minimizes average waiting time
- Good throughput

**Disadvantages**:
- Cannot predict future burst times
- Can lead to starvation of longer processes
- Not suitable for interactive systems

### 3. Shortest Remaining Time (SRT)

**Characteristics**:
- Preemptive version of SJN
- Preempts if new process has shorter remaining time

**Advantages**:
- Further reduces average waiting time

**Disadvantages**:
- More overhead due to context switching
- Can starve longer processes

### 4. Priority Scheduling

**Characteristics**:
- Each process has priority
- Highest priority process runs next
- Can be preemptive or non-preemptive

**Issues**:
- **Starvation**: Low priority processes may never run
- **Solution**: Aging - gradually increase priority over time

### 5. Round Robin (RR)

**Characteristics**:
- Preemptive
- Each process gets fixed time quantum (time slice)
- After quantum expires, process goes to end of ready queue
- Suitable for interactive systems

**Time Quantum Effects**:
- Small quantum: More context switches, more overhead
- Large quantum: Becomes FCFS
- Optimal: 80% processes finish within 1 time quantum

**Advantages**:
- Fair allocation
- Good response time
- Prevents starvation

**Disadvantages**:
- Context switching overhead
- Average waiting time not best

### 6. Multilevel Queue Scheduling

- Separate queues for different process types
- Each queue has own scheduling algorithm
- Scheduler must decide which queue gets CPU
- Can use fixed or variable time allocation

### 7. Multilevel Feedback Queue

- Process can move between queues
- Initially enters highest priority queue
- If uses full time quantum, moves to lower priority queue
- Promotes responsiveness and prevents starvation

## 4. Scheduling Algorithm Comparison

| Algorithm | Preemptive | Avg WT | Starvation | Overhead |
|-----------|-----------|---------|-----------|----------|
| FCFS | No | High | No | Low |
| SJN | No | Low | Yes | Low |
| SRT | Yes | Very Low | Yes | Medium |
| Priority | Both | Medium | Yes | Medium |
| RR | Yes | Medium | No | High |

## 5. Context Switching Overhead

- Time to save current process state
- Time to load next process state
- Time to update memory management structures
- Loss of CPU cache efficiency

## 6. Key Concepts

| Term | Definition |
|------|------------|
| **Burst Time** | Time process needs CPU |
| **Arrival Time** | When process enters ready queue |
| **Completion Time** | When process finishes |
| **Turnaround Time** | Completion - Arrival time |
| **Waiting Time** | TAT - Burst time |
| **Response Time** | First execution - Arrival time |
| **Quantum** | Fixed time slice in RR |

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Intermediate
**GATE/NET Relevance**: High