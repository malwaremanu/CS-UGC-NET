RAID (Redundant Array of Independent Disks) is a method of combining multiple physical disks into a single logical unit to improve performance, increase fault tolerance, or balance both, and questions on its concepts, levels, and calculations are common in exams like UGC NET, GATE, DSSSB, KVS, and NVS. Different RAID levels (0, 1, 2, 3, 4, 5, 6, 10) vary in how they distribute data, parity, and redundancy, which directly affects storage efficiency, reliability, and I/O speed—these differences are frequently targeted in conceptual and application-based MCQs.[1][2][3][4][5][6]

## Core idea of RAID  

RAID groups several disks so that the operating system sees them as one logical drive, allowing parallel I/O and redundancy mechanisms to close the speed gap between CPU and disk and to keep data available if a disk fails. The main exam points are: definition of RAID, motivations (performance + fault tolerance), and how redundancy (mirroring/parity) lets the system keep running despite hardware failures.[7][2][3][1]

## Key standard RAID levels  

- RAID 0: Block-level striping without redundancy; gives maximum storage efficiency and high read/write throughput but if any disk fails, all data is lost, so no fault tolerance.[4][8][1]
- RAID 1: Mirroring; data is duplicated on two or more disks, giving excellent fault tolerance and improved read performance, but only about 50% of raw capacity is usable.[2][8][4]
- RAID 2/3/4: Use striping plus dedicated parity or error-correction disks—bit/byte or block-level striping with a separate parity disk—conceptually important for theory and matching questions but rarely used in modern practical systems.[9][10][1]
- RAID 5: Block-level striping with distributed parity; tolerates one disk failure, offers good read speed and better storage efficiency than pure mirroring, but writes are slower due to parity overhead.[11][1][4]
- RAID 6: Similar to RAID 5 but with double distributed parity; can tolerate any two disk failures at the cost of extra parity overhead and slower writes.[12][8][4]
- RAID 10 (1+0): Data is mirrored and then striped; effectively uses half of the disks for usable capacity, but delivers very high performance and strong fault tolerance, so it is used for critical servers and databases.[13][14][4]

## Performance and fault tolerance  

Performance comes mainly from striping (parallel reads/writes), while fault tolerance comes from redundancy via mirroring or parity. Typical exam contrasts include: RAID 0 is fastest but least reliable, RAID 1 is most reliable but space-inefficient, RAID 5/6 provide a balance with parity, and RAID 10 gives both high speed and high availability at 50% capacity efficiency.[5][8][1][2][4]

## Storage efficiency, redundancy, speed, use cases  

RAID levels differ in usable capacity fraction, number of tolerated disk failures, and relative speed; these relationships often appear in numerical and assertion–reason questions. The table below summarizes commonly asked levels (assuming N disks, N ≥ minimum for that level).[15][4][13]

| RAID level | Storage efficiency (approx.) | Fault tolerance | Relative speed (read/write) | Typical use cases |
|-----------|------------------------------|-----------------|-----------------------------|-------------------|
| RAID 0    | N/N = 100% (all capacity usable) [4] | 0 disk failures; any failure loses array [4] | Very high / very high (no parity overhead) [1][8] | Scratch disks, video editing, temporary or non-critical data where speed matters more than safety [4][8] |
| RAID 1    | N/2N ≈ 50% (mirroring) [4] | Can lose up to N−1 disks as long as each mirrored pair has one surviving disk [2] | High read (can read from either mirror), normal write [2][8] | OS partitions, critical small data sets, system volumes needing high availability [2][4] |
| RAID 5    | (N−1)/N (one disk worth of parity) [4] | Tolerates 1 disk failure [4][12] | High read, moderate write (parity calculation penalty) [1][11] | File servers, general-purpose storage, read-heavy workloads where capacity and redundancy must be balanced [12][8] |
| RAID 6    | (N−2)/N (two disks for parity) [4] | Tolerates 2 disk failures [4][12] | High read, lower write than RAID 5 (double parity) [12][8] | Large-capacity arrays, archival and backup systems where rebuild window risk is high [12][16] |
| RAID 10   | N/2N ≈ 50% (striped mirrors) [4][13] | Multiple disk failures tolerated if no mirrored pair loses both disks [4][13] | Very high read and write (mirroring + striping) [13][14] | High-transaction databases, web/email servers, mission-critical workloads needing both speed and resilience [4][8] |

For calculations, exams often give number of disks and RAID level and ask usable capacity (e.g., RAID 5 usable = \((N-1)\times\)disk size, RAID 6 = \((N-2)\times\)disk size, RAID 1/10 ≈ 50% of raw), or ask which level wastes least space for given fault tolerance. Conceptual questions also test understanding of which levels offer mirroring, which use dedicated vs distributed parity, and what happens to system availability when one or two disks fail in each configuration.[10][6][1][9][4][12]

[1](https://www.geeksforgeeks.org/dbms/raid-redundant-arrays-of-independent-disks/)
[2](https://www.techtarget.com/searchstorage/definition/RAID)
[3](https://www.geeksforgeeks.org/operating-systems/redundant-array-of-independent-disks-raid-set-2/)
[4](https://www.prepressure.com/library/technology/raid)
[5](https://www.techtarget.com/searchstorage/answer/RAID-types-and-benefits-explained)
[6](https://edurev.in/t/186799/RAID--Redundant-Arrays-of-Independent-Disks-)
[7](https://www.studocu.com/en-gb/messages/question/13256035/discuss-the-concept-of-raid-redundant-array-of-independent-disks-and-its-various-levels)
[8](https://www.liquidweb.com/blog/raid-level-1-5-6-10/)
[9](https://www.slideshare.net/slideshow/introduction-to-raid-38639172/38639172)
[10](https://www.scribd.com/document/222263382/RAID-Level-Comparison-Table)
[11](https://www.trentonsystems.com/en-au/blog/raid-levels-0-1-5-6-10-raid-types)
[12](https://phoenixnap.com/kb/raid-levels-and-types)
[13](https://www.diskinternals.com/raid-recovery/raid-5-vs-raid-6-vs-raid-10/)
[14](https://www.trentonsystems.com/en-us/resource-hub/blog/raid-levels-0-1-5-6-10-raid-types)
[15](https://docs.oracle.com/cd/E19045-01/blade.x6450/820-4708-13/appendixa.html)
[16](https://www.ibm.com/docs/POWER6/arebj/raidlevelsummary.htm)
[17](https://github.dev/malwaremanu/CS-UGC-NET)
[18](https://jetstor.com/news/raid-levels-fault-tolerance)
[19](https://testbook.com/question-answer/which-of-the-following-raid-redundant-array-of-in--61653e9ef0f735d30611844b)
[20](https://www.scribd.com/document/795299224/RAID-Redundant-Arrays-of-Independent-Disks-GeeksforGeeks)
[21](https://www.youtube.com/watch?v=4J7iSumiJNk)