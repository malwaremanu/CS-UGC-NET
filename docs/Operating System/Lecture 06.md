# Operating System - Lecture 06: I/O Management and Device Drivers

## Overview
I/O management is critical for OS functionality. It handles communication between the computer and peripheral devices (keyboard, printer, disk, network). Device drivers are software programs that enable OS to communicate with hardware devices.

## 1. I/O Subsystem Architecture

### Components
- **CPU**: Initiates I/O operations
- **I/O Controller**: Manages device communication
- **Device Driver**: Software interface to device
- **Device**: Physical hardware (printer, disk, etc.)
- **Interrupts**: Signal completion/error
- **DMA**: Direct Memory Access for bulk transfers

### I/O Devices Classification

**1. Block Devices**
- Access data in fixed-size blocks
- Random access possible
- Example: Hard disk, USB drive

**2. Character Devices**
- Sequential access
- Data stream without structure
- Example: Keyboard, printer, mouse

**3. Network Devices**
- Send/receive data over network
- Specialized protocol handling
- Example: Network interface card

## 2. I/O Operations

### Programmed I/O
- CPU directly controls device
- CPU waits for operation completion
- **Pros**: Simple, no hardware overhead
- **Cons**: CPU wastes cycles, inefficient

### Interrupt-Driven I/O
- Device signals when ready (interrupt)
- CPU continues other tasks
- Interrupt handler processes request
- **Pros**: More efficient CPU use
- **Cons**: Interrupt overhead

### Direct Memory Access (DMA)
- Device controller transfers data directly to/from memory
- No CPU intervention during transfer
- CPU notified when transfer complete via interrupt
- **Pros**: Most efficient, minimal CPU overhead
- **Cons**: Hardware complexity

## 3. Device Driver Functions

### Primary Responsibilities
- **Device Detection**: Identify hardware presence
- **Initialization**: Configure device parameters
- **Command Issuance**: Send commands to device
- **Data Transfer**: Manage data movement
- **Interrupt Handling**: Process device interrupts
- **Error Handling**: Manage device errors
- **Power Management**: Control device power states

### Driver Levels

**1. Kernel Mode Drivers**
- Full hardware access
- Direct memory manipulation
- Performance-critical operations
- Risk: System crash if buggy

**2. User Mode Drivers**
- Limited access, safer
- Isolated from kernel
- Slower performance
- Fault-tolerant

## 4. Interrupt Handling

### Interrupt Process
1. Device signals interrupt request (IRQ)
2. CPU completes current instruction
3. CPU switches to kernel mode
4. CPU saves current state
5. Interrupt handler (ISR) executes
6. CPU restores state and resumes

### Interrupt Priority
- Different devices have different priorities
- Higher priority interrupts can preempt lower
- Prevents critical device delays

### Interrupt Latency
- Time from interrupt signal to handler execution
- Critical for real-time systems
- Affected by ISA length, ISR complexity

## 5. Buffering and Caching

### Buffering
- **Single Buffer**: Process reads from buffer while device fills next
- **Double Buffer**: Device fills one while process uses other
- **Circular Buffer**: Multiple buffers in ring
- Speeds up I/O by hiding device delays

### Caching
- Keep frequently accessed data in memory
- Reduces disk access time
- Write-back cache: Write to cache, later to disk
- Write-through cache: Write to both simultaneously

## 6. I/O Scheduling

### Disk I/O Request Queue
- Requests arrive from processes
- Scheduler orders requests for efficiency
- Different algorithms for optimization

### FCFS (First Come First Served)
- Simple, fair
- Potentially long wait times
- Disk head moves inefficiently

### SSTF (Shortest Seek Time First)
- Minimizes head movement
- Can starve far-away requests
- Good for random access

### SCAN (Elevator Algorithm)
- Head sweeps from one end to other
- Serves all requests in path
- Fair, prevents starvation

### C-SCAN (Circular SCAN)
- Head returns to beginning after sweep
- More uniform wait times
- Slightly better than SCAN

### LOOK Algorithm
- Like SCAN but doesn't go to end
- Only goes as far as last request
- More efficient

## 7. Key Concepts

| Term | Definition |
|------|------------|
| **IRQ** | Interrupt Request signal from device |
| **ISR** | Interrupt Service Routine handler |
| **DMA** | Direct Memory Access |
| **Device Driver** | Software interface to hardware |
| **Interrupt Latency** | Time to process interrupt |
| **Seek Time** | Time to move disk head |
| **Rotational Latency** | Time for sector to reach head |

## 8. Common I/O Devices and Handling

**Keyboard**: Character device, buffered input
**Printer**: Block-oriented, requires buffering
**Disk**: Complex scheduling, critical for performance
**Network**: Packet-based, time-sensitive
**USB**: Hot-plug capable, variable protocols

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Intermediate-Advanced
**GATE/NET Relevance**: Very High