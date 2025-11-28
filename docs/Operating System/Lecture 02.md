# Operating System - Lecture 02: Process Concept and Process States

## Overview
This lecture introduces the concept of processes, one of the fundamental abstractions provided by operating systems. It covers process definition, process states, process control blocks, and transitions between process states.

## 1. What is a Process?

### Definition
A **Process** is:
- An instance of a program in execution
- A dynamic entity that has a state and uses resources
- The unit of work (or execution) in an operating system
- Different from a program (which is passive/static)

### Program vs Process
- **Program**: Passive entity, code stored on disk
- **Process**: Active entity, program loaded in memory and executing
- One program can have multiple processes executing simultaneously
- Each process has its own memory space and resources

## 2. Process Memory Layout

A process in memory consists of several sections:

1. **Text Section**: Program code (instructions)
2. **Data Section**: Global and static variables
3. **Heap Section**: Dynamically allocated memory (grows upward)
4. **Stack Section**: Local variables, function parameters, return addresses (grows downward)

## 3. Process Control Block (PCB)

### Definition
The **Process Control Block** is a data structure that contains all information about a process that the OS needs to manage it.

### PCB Contains:

**1. Process Identification**
- Process ID (PID): Unique identifier
- Parent process ID (PPID)
- User ID

**2. Processor State Information**
- Program Counter (PC): Address of next instruction
- Registers: CPU register values
- Processor status word

**3. Process Control Information**
- Process state: Running, Ready, Blocked, etc.
- Priority: Process scheduling priority
- Scheduling information: Queue pointers

**4. Memory Management Information**
- Base and limit registers
- Page tables
- Segment tables
- Virtual memory information

**5. I/O Status Information**
- List of open files
- List of I/O devices allocated
- Buffering information

**6. Accounting Information**
- CPU time used
- Memory usage
- I/O operations performed
- Time limits

## 4. Process States

A process transitions through various states during its lifecycle:

### Five-State Process Model

**1. New State**
- Process is being created
- OS is allocating resources
- PCB is created
- Memory is being allocated

**2. Ready State**
- Process is prepared to run
- Has all necessary resources
- Waiting for CPU assignment
- Multiple processes can be in ready state
- Processes are kept in Ready Queue

**3. Running State**
- Process is currently executing on CPU
- CPU executing process instructions
- Only one process can be running (on single CPU system)
- Process has obtained CPU from scheduler

**4. Blocked (Waiting) State**
- Process cannot proceed further until some event occurs
- Waiting for I/O operation to complete
- Waiting for signal or message from another process
- Waiting for timer to expire
- Process voluntarily gives up CPU
- Processes are kept in Blocked/Wait Queue

**5. Terminated State**
- Process has finished execution
- All resources released
- Exit code is returned
- PCB is kept temporarily for parent process

### State Transitions

**Admitted**: New → Ready (when resource allocation completes)

**Dispatch**: Ready → Running (when scheduler assigns CPU)

**Running → Ready**: 
- Time slice expires (preemption)
- Higher priority process arrives

**Event Request**: Running → Blocked (process requests I/O or waits)

**Event Completion**: Blocked → Ready (I/O completes or event occurs)

**Exit**: Running → Terminated (process completes)

## 5. Process Queues

The OS maintains queues to organize processes in various states:

**1. Job Queue**
- Contains all processes in the system
- Includes processes in all states

**2. Ready Queue**
- Contains all processes ready to execute
- Waiting for CPU assignment
- Implemented as linked list or priority queue

**3. Device Queue (I/O Queue)**
- Contains processes waiting for specific I/O device
- Separate queue for each device
- Processes move here when requesting I/O

**4. Wait Queue (Event Queue)**
- Contains processes waiting for specific event
- Can have queues for different types of events

## 6. Process Scheduling

### Context Switch
**Context Switching** is the mechanism where:
1. CPU stops executing current process
2. State of current process saved in PCB
3. PCB of next process loaded into CPU registers
4. CPU begins executing next process

**Context Switch Overhead**:
- Time spent switching = pure overhead (no useful work)
- Modern systems: tens to hundreds of microseconds
- Can become significant bottleneck if too frequent

### Scheduling Decision Points

**Non-preemptive Scheduling**:
- Process keeps CPU until it blocks or terminates
- Context switches only occur on I/O or exit

**Preemptive Scheduling**:
- Process can be interrupted by OS/scheduler
- Context switches on timer interrupt, I/O completion, or signal
- More common in modern OS

## 7. Process Hierarchies

### Parent-Child Relationship
- When process creates another process: parent-child relationship
- Child process inherits resources from parent
- Child may be able to create own children
- Forms process tree structure

### Process Termination

**Cascading Termination**:
- When parent terminates, usually all children terminate
- Prevents orphan processes
- On Unix: init process becomes parent of orphans

## 8. Process Operations

**Create**: Fork/CreateProcess system calls
- Creates new PCB
- Allocates memory
- Initializes PCB
- Adds to ready queue

**Execute**: Exec system calls
- Replaces process memory with new program
- Reuses same PID and PCB
- Commonly follows fork (fork-exec model)

**Terminate**: Exit system call
- Returns exit status
- Releases resources
- Notifies parent process

## 9. Key Concepts

| Term | Meaning |
|------|----------|
| **PCB** | Data structure containing all process info |
| **PID** | Unique process identifier |
| **Context Switch** | Saving/restoring process state |
| **Ready State** | Process waiting for CPU |
| **Blocked State** | Process waiting for event/I/O |
| **Process Queue** | List of processes in particular state |
| **Dispatcher** | Component that assigns CPU to process |

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Intermediate
**GATE/NET Relevance**: High