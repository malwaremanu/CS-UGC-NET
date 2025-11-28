# Operating System - Lecture 05: File System Management

## Overview
The file system is a critical OS component that manages how data is stored, organized, and accessed on storage devices. It provides abstraction from hardware details and enforces security and efficiency.

## 1. File Concepts

### File Definition
- Named collection of related records stored on secondary storage
- Permanent storage unit for data and programs
- Persists after process termination

### File Attributes
- Name, Type, Location, Size
- Creation time, Modification time, Access time
- Owner, Permissions (read, write, execute)
- File descriptor/inode number

### File Types
- Regular files: Text, Binary, Executable
- Directories: Collections of files
- Special files: Devices, Pipes

## 2. File Operations

- **Create**: Allocate space on disk
- **Read**: Retrieve data from file
- **Write**: Store data in file
- **Append**: Add data at end
- **Delete**: Remove file and free space
- **Seek**: Reposition file pointer
- **Truncate**: Reduce size to zero

## 3. Directory Structure

### Single Level Directory
- All files in one directory
- Simple but limited

### Two Level Directory
- One directory per user
- File names must be unique within user directory

### Tree/Hierarchical Directory
- Most common: folders containing folders
- Absolute and relative paths
- Root directory (/)

### Acyclic-Graph Directory
- Allows sharing of subdirectories
- More complex but flexible

## 4. File Allocation Methods

### Contiguous Allocation
- Files stored in contiguous blocks
- **Pros**: Fast access, simple
- **Cons**: External fragmentation, must know size

### Linked Allocation
- Each block has pointer to next block
- **Pros**: No external fragmentation, dynamic growth
- **Cons**: Slow access, pointer overhead

### Indexed Allocation
- Index block contains pointers to file blocks
- **Pros**: Efficient access, supports dynamic size
- **Cons**: Index overhead

## 5. Free Space Management

- **Bit Vector**: Each bit represents free/used block
- **Linked List**: Linked list of free blocks
- **Grouping**: Index block points to free blocks
- **Counting**: Store block address and count of free blocks

## 6. Disk Scheduling (Brief)

Determines order of disk read/write requests:
- **FCFS**: First Come First Served
- **SSTF**: Shortest Seek Time First
- **SCAN**: Elevator algorithm
- **C-SCAN**: Circular SCAN

## 7. Key Concepts

| Term | Meaning |
|------|----------|
| **Inode** | Data structure storing file metadata |
| **Block** | Smallest disk allocation unit |
| **File Descriptor** | Process-specific file reference |
| **File Table** | OS tracks open files |
| **Fragmentation** | Free space scattered or files split |

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Intermediate
**GATE/NET Relevance**: High