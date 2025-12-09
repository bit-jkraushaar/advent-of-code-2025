# Day 8: Playground

## Part 1

Connect junction boxes in 3D space using a minimum spanning tree approach. Given positions of junction boxes, connect the 1000 closest pairs and find the product of the three largest circuit sizes.

**Approach**: Use Union-Find (Disjoint Set Union) to track circuits as we connect junction boxes.
- Parse 3D coordinates from input
- Calculate all pairwise distances (using squared distances to avoid sqrt)
- Sort pairs by distance
- Attempt to connect the 1000 closest pairs using Union-Find
- Track circuit sizes and multiply the three largest

## Part 2

[To be released]

## Notes

- This is a classic Minimum Spanning Tree problem variant
- Union-Find with path compression and union by size provides efficient circuit tracking
- When attempting connections, some pairs may already be in the same circuit (skip these)
- The problem asks to *attempt* the first N connections, not make N successful connections

