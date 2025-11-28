# Operating System - Lecture 07: Process Synchronization

## Overview
Process synchronization addresses problems arising from concurrent process execution, particularly access to shared resources. It ensures data consistency and prevents race conditions in multi-process/multi-threaded environments.

## 1. The Critical Section Problem

### Race Condition
- Occurs when multiple processes access shared data simultaneously
- Result depends on timing and order of execution
- Leads to unpredictable, incorrect results

### Critical Section
- Code segment where process accesses shared resources
- Only one process should execute critical section at a time
- Entry and exit controlled by synchronization

### Requirements for Solution
1. **Mutual Exclusion**: Only one process in critical section at any time
2. **Progress**: If no process in critical section, any waiting process should enter
3. **Bounded Waiting**: No process waits indefinitely

## 2. Synchronization Primitives

### Locks (Mutual Exclusion)
**Types:**
- **Binary Semaphore**: 0 or 1 value
- **Spinlock**: Busy-wait, checks lock repeatedly
- **Mutex**: Similar to binary semaphore

### Semaphores
- Integer variable accessed by two atomic operations
- `wait(S)`: Decrement S, wait if negative
- `signal(S)`: Increment S, wake waiting process
- Can be binary (0/1) or counting

**Advantages:**
- Simple to use and implement
- Works for multiple resources
- Proven effective

**Disadvantages:**
- Easy to use incorrectly
- No compile-time checking
- Deadlock possible

### Monitors
- High-level synchronization construct
- Collection of procedures and variables
- Compiler ensures only one process active in monitor
- Easier to use than semaphores
- Condition variables for wait/signal

## 3. Classical Synchronization Problems

### Producer-Consumer Problem
- Producer generates data, Consumer uses it
- Buffer between them prevents overwriting/underreading
- Solution requires:
  - Semaphore for empty slots
  - Semaphore for full slots
  - Binary semaphore for mutual exclusion

### Readers-Writers Problem
- Multiple readers can read simultaneously
- Only one writer can write
- Writer needs exclusive access
- Solutions:
  - Readers-preference: Readers never wait for readers
  - Writers-preference: New readers wait for writer
  - Fair solution: FIFO order

### Dining Philosophers Problem
- Five philosophers, five forks
- Each needs two forks to eat
- Potential for deadlock
- Solutions:
  - Resource ordering
  - Arbitrator (waiter)
  - Limited philosophers eating
  - Asymmetric take-up

## 4. Deadlock

### Deadlock Condition
All four conditions must hold:
1. **Mutual Exclusion**: Resources cannot be shared
2. **Hold and Wait**: Process holds resources while waiting for others
3. **No Preemption**: Resources cannot be forcibly taken
4. **Circular Wait**: Circular chain of processes

### Deadlock Prevention
- Break one of four conditions
- Negating mutual exclusion: Not always possible
- Negate hold and wait: Pre-allocate all resources
- Negate no preemption: Allow resource preemption
- Negate circular wait: Impose resource ordering

### Deadlock Avoidance
- Allow only safe states
- Banker's Algorithm: Check if request leads to unsafe state
- Overhead: Significant computation

### Deadlock Detection and Recovery
- Allow deadlock to occur
- Detect using resource allocation graph
- Recover by aborting processes or preempting resources

## 5. Memory Barriers and Memory Models

### Memory Consistency
- Order of memory operations visible to other processes
- Issues in multi-processor systems
- Memory barriers enforce ordering

### Memory Models
- **Strict Consistency**: Any read returns latest write
- **Sequential Consistency**: Appears as if sequential
- **Eventual Consistency**: Eventually all see same state

## 6. Key Concepts

| Term | Meaning |
|------|----------|
| **Race Condition** | Result depends on execution timing |
| **Critical Section** | Code accessing shared resources |
| **Mutual Exclusion** | Only one process in critical section |
| **Semaphore** | Integer for process synchronization |
| **Monitor** | High-level sync construct with conditions |
| **Deadlock** | Circular waiting for resources |
| **Starvation** | Process never gets required resources |

## 7. Best Practices

- Minimize critical sections
- Avoid nested locks (deadlock risk)
- Release locks in reverse order of acquisition
- Use higher-level constructs (monitors) when possible
- Test concurrent code extensively
- Use atomic operations for simple cases

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Advanced
**GATE/NET Relevance**: Very High