# Operating System - Lecture 08: Deadlocks

## Overview
Deadlock is a situation where a set of processes cannot proceed because each waits for a resource held by another. Understanding deadlock causes, detection, prevention, and recovery is essential for robust OS design.

## 1. Deadlock Definition and Conditions

### Deadlock Definition
- A set of processes is deadlocked if each process waits for an event
- The event can only be triggered by another process in the set
- No process can proceed, no resources released
- Permanent stall unless external intervention

### Four Necessary Conditions
All four must hold simultaneously:

1. **Mutual Exclusion**
   - At least one resource is non-shareable
   - Only one process can use resource at a time
   - Process holds exclusive access

2. **Hold and Wait**
   - Process holds at least one resource
   - Waits to acquire additional resources
   - Does not release held resources

3. **No Preemption**
   - Resources cannot be forcibly taken from process
   - Only process can release its resources
   - No external preemption mechanism

4. **Circular Wait**
   - Circular chain of processes exists: P1→P2→...→Pn→P1
   - Each process waits for resource held by next
   - Forms cycle in wait-for graph

## 2. Resource Allocation Graph

### Nodes
- **Process Nodes**: Represent processes (circles)
- **Resource Nodes**: Represent resources (squares)

### Edges
- **Request Edge**: P→R (process requests resource)
- **Assignment Edge**: R→P (resource assigned to process)

### Deadlock Detection
- Cycle in graph = potential deadlock
- If each resource has one instance: cycle = deadlock
- If each resource has multiple instances: cycle = possible deadlock

## 3. Deadlock Prevention

Break one of four necessary conditions:

### 1. Prevent Mutual Exclusion
- Make resources shareable
- Not always possible (e.g., printer)
- Limited applicability

### 2. Prevent Hold and Wait

**Option A: Pre-allocate**
- Process requests all resources before execution
- Releases all at once
- Wasteful: Resources idle if not immediately needed
- Low resource utilization

**Option B: Request then Release**
- Process must release current resources before requesting new ones
- Complex to implement
- Potential data inconsistency

### 3. Prevent No Preemption

**Allow Preemption:**
- Take resources from process
- Process restart with preempted resources
- Requires rollback capability
- For CPUs: Context switching acceptable
- For other resources: Often impossible

### 4. Prevent Circular Wait

**Resource Ordering (Numbering):**
- Number all resources: R1, R2, ..., Rn
- Process can request resources in increasing order only
- Cannot request lower-numbered resource after higher
- Prevents cycles
- Must be imposed by OS
- Easy to implement
- No resource wastage

## 4. Deadlock Avoidance

Allow conditions but avoid unsafe states

### Safe State
- State where no deadlock exists
- Sequence of processes can complete
- Resource available to first process
- After first completes, resources available to second
- Etc.

### Unsafe State
- May lead to deadlock
- Not necessarily in deadlock
- Risk of deadlock if requests made

### Banker's Algorithm

**Process:**
1. Assume request granted
2. Check if resulting state safe
3. If safe: grant request
4. If unsafe: delay request

**Data Structures:**
- Available: Available resources of each type
- Maximum: Maximum claim of each process
- Allocated: Resources currently allocated
- Need: Additional resources needed

**Complexity:** O(n²m) - expensive

## 5. Deadlock Detection

Allow deadlock to occur, then detect and recover

### Detection Algorithms
- Similar to avoidance but no pre-checking
- Run periodically
- Resource allocation graph: Check for cycle
- O(n²) complexity

### When to Run
- Frequently: High overhead, quick detection
- Rarely: Low overhead, longer undetected
- When CPU utilization low: Resource waiting likely
- Trade-off between overhead and detection time

## 6. Deadlock Recovery

### Options
1. **Inform Operator**
   - Manual intervention
   - Restart system
   - Last resort

2. **Process Termination**
   - Abort all deadlocked processes
   - Or abort one at a time
   - Loss of work
   - Data inconsistency possible

3. **Resource Preemption**
   - Take resources from processes
   - Restart with preempted resources
   - Select victim minimizing cost
   - Complex to implement

### Victim Selection
- Choose process with least cost to kill
- Consider: Execution time, output produced, resources held
- Preempt and restart process
- Risk: Starvation of same process

## 7. Comparison of Approaches

| Approach | Prevention | Avoidance | Detection |
|----------|-----------|-----------|----------|
| **Allows Deadlock** | No | No | Yes |
| **Overhead** | Medium-High | Very High | Medium |
| **Resources Used** | Wasteful | Moderate | Efficient |
| **Recovery** | N/A | N/A | Required |
| **Practical** | Limited | Moderate | Common |

## 8. Key Concepts

| Term | Meaning |
|------|----------|
| **Deadlock** | Permanent stall of processes |
| **Safe State** | Sequence exists to complete all processes |
| **Unsafe State** | May lead to deadlock |
| **Banker's Algorithm** | Avoidance algorithm for resource allocation |
| **Wait-for Graph** | Graph of process waiting relationships |

---

**Last Updated**: November 28, 2025
**Difficulty Level**: Advanced
**GATE/NET Relevance**: Very High