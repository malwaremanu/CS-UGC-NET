# Operating System - Lecture 04: Memory Management

## Overview
Memory management is a critical OS function that deals with allocation, de-allocation, and utilization of main memory. It ensures efficient and fair use of memory among competing processes.

## 1. Memory Hierarchy

From fastest/smallest to slowest/largest:
1. **CPU Registers** - Fastest, limited storage
2. **L1, L2, L3 Caches** - Very fast, expensive
3. **Main Memory (RAM)** - Fast, medium cost
4. **Secondary Storage (Disk)** - Slow, cheap, large

## 2. Memory Allocation Schemes

### Contiguous Allocation
- **Single Partition**: One process per partition
- **Multiple Partitions**: Fixed or Variable partitions

### Non-Contiguous Allocation
- **Paging**: Divide memory into fixed-size pages
- **Segmentation**: Divide memory into variable-size segments

## 3. Paging

### Concepts
- Physical memory divided into **frames** (fixed size, e.g., 4KB)
- Logical memory divided into **pages** (same size as frames)
- Process can be scattered across non-contiguous frames
- Page table maps logical pages to physical frames

### Address Translation
- Logical Address = Page Number + Offset
- Physical Address = Frame Number + Offset
- Memory Management Unit (MMU) performs translation

### Advantages
- No external fragmentation
- Simple allocation
- Efficient memory use

### Disadvantages
- Internal fragmentation (wasted space in last frame)
- Page table overhead
- Page table lookup delay

## 4. Segmentation

### Concepts
- Logical memory divided into variable-size segments
- Each segment has base address and limit
- Segment table maps segment numbers to memory locations

### Address Translation
- Logical Address = Segment Number + Offset
- Physical Address = Base + Offset (if Offset < Limit)

### Advantages
- Logical organization of memory
- No internal fragmentation
- Sharing and protection

### Disadvantages
- External fragmentation
- Variable-size allocation complexity

## 5. Virtual Memory

### Concept
- Logical memory larger than physical memory
- Part in RAM, part on disk
- Allows programs larger than RAM

### Demand Paging
- Pages loaded only when needed
- Page fault occurs when page not in memory
- OS fetches page from disk
- Increases program execution time

### Page Replacement Algorithms
1. **FIFO**: First In First Out
2. **LRU**: Least Recently Used
3. **Optimal**: Fewest page faults (theoretical)
4. **Clock Algorithm**: Approximation of LRU

## 6. Fragmentation

### External Fragmentation
- Free memory scattered in small chunks
- Occurs with variable-size allocation
- **Solution**: Memory compaction, Paging

### Internal Fragmentation
- Wasted space within allocated block
- Occurs with fixed-size allocation
- Reduced by smaller page size

## 7. Key Concepts

| Term | Definition |
|------|------------|
| **Page** | Fixed-size logical memory unit |
| **Frame** | Fixed-size physical memory unit |
| **Page Fault** | Access to page not in memory |
| **Page Table** | Mapping of pages to frames |
| **TLB** | Translation Lookaside Buffer (cache) |
| **Thrashing** | Excessive page swapping |

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Intermediate
**GATE/NET Relevance**: Very High