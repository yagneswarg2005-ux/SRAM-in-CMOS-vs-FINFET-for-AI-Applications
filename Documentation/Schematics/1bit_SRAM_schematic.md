# 1-bit SRAM Cell - Block Diagram Schematic

## Overview
This document describes the complete 1-bit SRAM cell architecture designed for efficient read/write operations.

## Architecture Components

### Main Building Blocks

1. **SRAM Core**
   - Cross-coupled inverter pair for data storage
   - Stores complementary data bits (Q and Q_bar)
   - Pass transistors for access control
   - Connected to bit lines (BL and BLB)

2. **Sense Amplifier (QBAR Block)**
   - Detects inverted stored bit (Q_bar output)
   - Differential voltage amplification
   - Output: QBAR signal

3. **Sense Amplifier (Q Block)**
   - Detects normal stored bit (Q output)
   - Mirrors QBAR for complementary sensing
   - Output: Q signal

4. **Decoder**
   - Address decoder for word line generation
   - Inputs: W_EN (Write Enable), DIN (Data Input)
   - Output: WL (Word Line) to SRAM core
   - Enables selective cell access in arrays

5. **Write Driver**
   - Provides write data to bit lines during write operations
   - Inputs: WIN (Write Input), DIN (Data Input)
   - Outputs: BL, BLB (driven with complementary data)
   - Strong drive capability for reliable writes

6. **Isolation Switch (ISO)**
   - Controls power supply to SRAM core
   - For power-gating and leakage reduction
   - Controlled by ISO signal

7. **Secondary Sense Amplifier (SSA)**
   - Additional sensing path
   - Provides SSA output signal

## Signal Description

### Input Signals
- **WIN**: Write Input - Input data to write into cell
- **DIN**: Data Input - Secondary write data
- **WL**: Word Line - Row selection (from decoder)
- **PR**: Pre-charge signal - Initializes bit lines
- **ISO**: Isolation control - Power management
- **True**: Enable true output path

### Output Signals
- **Q**: Normal stored bit output (High level = '1')
- **QBAR**: Inverted stored bit output (Low level = '0')
- **COMPLEMENT**: Complement signal output
- **BL, BLB**: Bit line signals (sensing/writing)

### Power Signals
- **VDD**: Positive supply voltage (1.98V typical)
- **GND**: Ground reference (0V)

## Operation Modes

### Write Operation
1. Decoder sets WL high based on address
2. Write driver places data on BL and BLB
3. Pass transistors conduct, forcing data into core latch
4. After write time, WL goes low, latching new data

### Read Operation
1. PR signal pre-charges BL and BLB to VDD
2. Decoder sets WL high for selected word
3. Core inverters discharge the appropriate bit line
4. Small differential voltage develops on bit lines
5. Sense amplifiers detect and amplify this difference
6. Outputs Q and QBAR reach rail voltages

### Standby Operation
1. WL remains low (no access)
2. PR inactive (no pre-charge)
3. SRAM core maintains stored state
4. ISO may be low for power gating

## Design Parameters

### Technology
- Process: GPDK090 (90nm CMOS)
- Supply Voltage: 1.98V (nominal)
- Temperature: 27°C

### Performance
- Access Time: ~10-12ns (read)
- Write Time: ~10-15ns (write)
- Power Supply: Single 1.98V
- Low power standby with gating

## Connectivity Summary
- **Instances**: 8 major blocks
- **Nets**: 12 signal interconnections
- **Pins**: 6+ external connections
- **Hierarchical**: Modular design for scalability
