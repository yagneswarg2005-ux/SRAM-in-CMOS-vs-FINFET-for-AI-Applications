# 6T-SRAM Array Architecture

## Overview
A hierarchical multi-cell SRAM array implementation using standard 6-transistor cell design with distributed pre-charge and address decoding.

## Array Configuration

### Physical Layout
- **Dimensions**: 4 rows × 4 columns (4×4 array)
- **Total Cells**: 16 SRAM cells
- **Cell Type**: 6T cross-coupled inverter pair
- **Technology**: GPDK090 (90nm)

### Hierarchical Organization
```
┌─────────────────────────────────┐
│     6T-SRAM Array (4x4)         │
├─────────────────────────────────┤
│  WL1 ──┬──┬──┬──┬──┐           │
│        │  │  │  │  │ 6T Cell  │
│  WL2 ──┼──┼──┼──┼──┤           │
│        │  │  │  │  │           │
│  WL3 ──┼──┼──┼──┼──┤           │
│        │  │  │  │  │           │
│  WL4 ──┼──┼──┼──┼──┤           │
│        │  │  │  │  │           │
│        └┬─┴──┴──┴──┘           │
│         │  Pre-charge Circuits │
│        BL    BLB               │
└─────────────────────────────────┘
```

## Signal Hierarchies

### Word Lines (Row Selection)
- **WL1, WL2, WL3, WL4**: Four horizontal word lines
- Each selects one complete row of 4 cells
- Driven by address decoder
- Active high (logic 1 = selected)

### Bit Lines (Column Data)
- **BL**: Primary bit line (column-wise)
- **BLB**: Complementary bit line (column-wise)
- Shared across all 4 rows in each column
- Connected to sense amplifier and write driver

### Pre-charge Circuits
- **Location**: Bottom of array (I7, I8, I9, I20)
- **Count**: 4 pre-charge blocks (one per column pair)
- **Function**: Charge BL and BLB to VDD
- **Control**: Single PR (pre-charge) signal

### Ground Distribution
- **GND**: Distributed ground nodes
- **Network**: Low-impedance ground grid
- **Connections**: Every cell connects to ground rails

## Cell Array Details

### Individual Cell Configuration
```
WL ───[Pass Transistors]─── BL, BLB
         │
      [Latch]
      Q ─ Q_bar
         │
        GND
```

### Cell Connections Per Row
- **Row 1 (WL1)**: Cells connect to BL1, BLB1 through pass transistors
- **Row 2 (WL2)**: Cells connect to BL1, BLB1 through separate pass transistors
- **Row 3 (WL3)**: Cells connect to BL1, BLB1 through separate pass transistors
- **Row 4 (WL4)**: Cells connect to BL1, BLB1 through separate pass transistors

### Shared Bit Line Access
- All cells in a column share same BL and BLB
- Only selected row (WL=1) conducts during access
- Unselected rows isolate through pass transistor stack

## Decoder and Address Logic

### Address Decoding
- 2-bit address input (A[1:0])
- Selects one of 4 word lines
- Typical decoder implementation:
  - AND/NAND gates for decoding
  - One word line goes high per address
  - Other word lines remain low

### Address-to-Word Line Mapping
| Address | Word Line Selected |
|---------|-------------------|
| 00 | WL1 |
| 01 | WL2 |
| 10 | WL3 |
| 11 | WL4 |

## Pre-charge Circuits in Array

### Circuit Blocks (I7, I8, I9, I20)
- **I7, I8**: Pre-charge for columns 1-2
- **I9, I20**: Pre-charge for columns 3-4
- Each block contains 2-3 PMOS transistors
- Controlled by PR signal (active low)

### Pre-charge Operation
1. PR goes low before memory cycle
2. All bit lines charge to VDD (~1.9V)
3. Equalization between complementary lines
4. Settling time: ~2-3ns
5. Ready for access

## Connectivity Summary

| Component | Count | Description |
|-----------|-------|-------------|
| Cells | 16 | 6T SRAM cells |
| Word Lines | 4 | Row selectors |
| Bit Line Pairs | 2 | Column data paths |
| Pre-charge Blocks | 4 | Initialization circuits |
| Instances Total | 20 | All circuit elements |
| Nets | 46 | Signal interconnections |
| External Pins | 14 | Array I/O |

## Operation Sequence

### Read Cycle (Example: Access cell at WL2, Column BL1)
1. **Pre-charge**: PR = 0V → BL, BLB charge to ~1.9V (2-3ns)
2. **Address Select**: A[1:0] = 01 → WL2 goes high
3. **Cell Access**: Stored data pulls one bit line down (1-2ns)
4. **Sense**: Small differential voltage (~50mV) on bit lines
5. **Amplify**: Sense amplifier detects and amplifies (1-2ns)
6. **Output**: Q or Q_bar reaches rail voltage (~1.8V)

### Write Cycle
1. **Pre-charge**: Initialize bit lines
2. **Address Select**: WL goes high
3. **Drive Data**: Write driver forces data onto BL/BLB
4. **Force Store**: Pass transistors force new state into latch
5. **Settle**: New state latches into cell (5-10ns)

## Array Scaling

This 4×4 architecture can scale to:
- **8×8 Array**: 64 cells, 8 word lines, 4 bit line pairs
- **16×16 Array**: 256 cells, 16 word lines, 8 bit line pairs
- **32×32 Array**: 1024 cells with hierarchical decoding

### Scaling Considerations
- Decoder complexity increases (log N for N rows)
- Bit line capacitance increases (more cells per column)
- Pre-charge time increases with bit line length
- Sense amplifier noise margin decreases
- May require hierarchical bit lines for large arrays

## Power Distribution
- **VDD Rail**: Distributed horizontally
- **GND Rail**: Distributed horizontally
- **Grid Spacing**: Every 2-3 cells
- **Impedance**: Minimized for large arrays

## Performance Metrics

| Metric | Value | Unit |
|--------|-------|------|
| Access Time | 10-12 | ns |
| Cycle Time | 15-20 | ns |
| Data Valid | >8 | ns |
| Setup Time | <2 | ns |
| Hold Time | <1 | ns |
| Array Power | <100 | µW |
