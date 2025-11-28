# Operating System - Lecture 09: Types of Operating Systems

## Overview
Operating systems have evolved through different generations and types, each with distinct characteristics and use cases. Understanding these types is crucial for choosing appropriate OS for specific requirements.

## 1. Batch Operating Systems

### Characteristics
- Early OS (1950s-1960s)
- Processes grouped into batches
- User submits jobs on punch cards
- No interactive user interface
- OS processes batch sequentially

### Operation
1. Operator collects similar jobs
2. Groups into batch
3. Submits entire batch to computer
4. Computer processes all jobs
5. Results printed and returned to users

### Advantages
- Simple to implement
- Efficient for bulk processing
- High throughput for certain applications

### Disadvantages
- No user interaction
- Long turnaround time
- Inefficient CPU utilization during I/O
- One bad job halts entire batch

### Examples
- Early IBM mainframes
- UNIVAC, ENIAC

## 2. Multiprogramming Operating Systems

### Characteristics
- Multiple programs in memory simultaneously
- CPU switches between programs
- When one blocks (I/O), CPU executes another
- Improves CPU utilization
- Evolved from batch systems

### Advantages
- Better CPU utilization
- Faster average job completion
- Multiple users served concurrently

### Disadvantages
- No interactive feedback
- Complex resource management
- Potential deadlocks and race conditions

### Example
- IBM OS/360

## 3. Multitasking/Time-Sharing Operating Systems

### Characteristics
- Each user gets time slice (quantum)
- CPU switches between processes rapidly
- User perceives simultaneous execution
- Interactive environment
- Fairness: All processes get CPU time

### Time Quantum
- Fixed time period for each process
- Usually 10-100 milliseconds
- Smaller quantum: More responsiveness, more overhead
- Larger quantum: Less overhead, slower response

### Advantages
- Interactive response
- Fair resource allocation
- Multiple users served
- Better user experience

### Disadvantages
- Context switching overhead
- More complex implementation
- Potential starvation if not managed

### Examples
- UNIX, Linux
- Windows, macOS

## 4. Real-Time Operating Systems (RTOS)

### Characteristics
- Guaranteed response time
- Predictable behavior
- Hard and soft deadlines
- Used in critical applications
- Deterministic scheduling

### Hard Real-Time
- Deadline must be met
- Miss = system failure
- Examples: Pacemaker, Missile guidance

### Soft Real-Time
- Missing deadline undesirable but tolerable
- Performance degradation acceptable
- Examples: Video streaming, Online gaming

### Characteristics
- Priority-based scheduling
- Minimal interrupt latency
- Predictable resource allocation
- Often stripped-down features

### Examples
- QNX, VxWorks
- RTOS-32, RTLinux

## 5. Distributed Operating Systems

### Characteristics
- Multiple independent computers
- Communicate via network
- Appear as single system to users
- Transparent resource sharing
- No single point of failure

### Advantages
- Scalability
- Fault tolerance
- Load sharing
- Global resource pool

### Challenges
- Network communication delays
- Data consistency
- Security and authentication
- Complex synchronization

### Examples
- Google File System
- Hadoop, Spark
- Cloud OS

## 6. Network Operating Systems

### Characteristics
- Multiple autonomous systems
- Each with own OS
- Communicate via network
- Users aware of multiple computers
- Client-server architecture

### Differences from Distributed
- Users know about multiple computers
- Explicit network commands
- Not transparent to users

### Features
- File sharing capabilities
- Remote login
- Network printers
- Email services

### Examples
- Windows Server
- Novell NetWare
- Linux server

## 7. Mobile Operating Systems

### Characteristics
- Designed for mobile devices
- Limited resources (battery, memory)
- Touch-based interface
- Real-time performance
- Security-focused

### Features
- Power management
- Sensor integration
- App ecosystem
- Wireless connectivity
- Security sandboxing

### Examples
- iOS
- Android
- Windows Mobile

## 8. Embedded Operating Systems

### Characteristics
- Dedicated to specific application
- Often single-purpose
- Minimal resources
- Real-time constraints
- Custom design

### Applications
- Home appliances
- Automotive systems
- Industrial control
- IoT devices

### Examples
- FreeRTOS
- RTOS-32
- Custom embedded systems

## 9. Comparison of OS Types

| Type | Users | Interaction | Response | CPU Use | Complexity |
|------|-------|------------|----------|---------|-------------|
| Batch | Sequential | No | Slow | Fair | Low |
| Multi-prog | Multiple | No | Slow | Good | Medium |
| Time-share | Multiple | Yes | Fast | Good | High |
| Real-time | Dedicated | Varies | Guaranteed | Efficient | High |
| Distributed | Multiple | Yes | Variable | Good | Very High |
| Network | Multiple | Yes | Good | Good | High |
| Mobile | Single | Yes | Fast | Efficient | High |
| Embedded | None | N/A | Real-time | Efficient | Medium |

## 10. Evolution Timeline

1. **1950s-60s**: Batch systems (UNIVAC)
2. **1960s-70s**: Multiprogramming (IBM OS/360)
3. **1970s-80s**: Time-sharing (UNIX)
4. **1980s-90s**: Personal computers (DOS, Mac OS)
5. **1990s-2000s**: Internet era (Windows, Linux)
6. **2000s-2010s**: Mobile (iOS, Android)
7. **2010s+**: Cloud, Edge, IoT OS

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Intermediate
**GATE/NET Relevance**: High