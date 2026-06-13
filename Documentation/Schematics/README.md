# SRAM Schematics Documentation

## Overview
This section contains detailed circuit schematics for all SRAM components designed and simulated for this project.

## Schematic Files

### 1. 1-bit SRAM Cell Schematic
**File:** `1bit_SRAM_schematic.png`

**Description:**
- Complete 1-bit SRAM cell implementation using 6 transistors (6T configuration)
- High-level block diagram showing interconnections
- Major blocks:
  - QBAR: Sense Amplifier for inverted output
  - Q: Sense Amplifier for normal output
  - Decoder: Word line address decoder (W_EN, DIN inputs)
  - Write Driver: Data writing circuitry
  - Isolation Switch: ISO control for power gating
  - SRAM Core: Primary storage element with cross-coupled inverters
  - SSA: Secondary Sense Amplifier

**I/O Signals:**
- WIN, DIN: Write input data
- WL: Word line (row selection)
- VDD, GND: Power supply
- PR: Precharge signal
- QBAR, Q: Complementary outputs
- ISO: Isolation control
- True, COMPLEMENT: Complementary output signals

**Transistor Configuration:**
- GPDK090 technology (90nm CMOS)
- Multiple device sizes for optimization
- Interconnect routing optimized for signal integrity

---

### 2. FINFT_SRAM 1-bit SRAM Cell Schematic
**File:** `FINFT_1bit_sram_schematic.png`

**Description:**
- FinFET-based 1-bit SRAM cell implementation
- Detailed transistor-level schematic
- Cross-coupled latch topology for data storage
- Pass-gate transistors for read/write access
- Internal nodes: Q and Q_bar (complementary storage nodes)

**Key Features:**
- BL and BLB (Bit Line and Bit Line Bar) for read/write operations
- WL (Word Line) for cell access
- VDD and GND power connections
- Optimized for FinFET technology characteristics

---

### 3. Sense Amplifier Schematic
**File:** `FINFT_Sense_ampl_schematic.png`

**Description:**
- Differential sense amplifier circuit for SRAM
- Detects small voltage differences on bit lines (BL and BLB)
- Amplifies differential signals to full rail voltage
- Critical component for read operation reliability

**Components:**
- Differential pair transistors for input stage
- Latch stage for holding amplified signal
- Enable signal for timing control
- Output nodes: OUT and QBAR

**Functionality:**
- Low-power differential sensing
- High gain amplification
- Fast settling time

---

### 4. Pre-charge Circuit Schematic
**File:** `FINFT_Pre_charge_schematic.png`

**Description:**
- Pre-charge circuit for bit line equalization
- Essential for reducing access time and power consumption
- Uses PMOS transistor pull-up network

**Components:**
- Pre-charge transistors (PMOS devices)
- Pull-up to VDD through controlled devices
- Cross-connected structure for balanced charging

**Signals:**
- PR: Pre-charge control signal
- BL, BLB: Bit lines being charged
- VDD: Supply voltage

---

### 5. 6T-SRAM Array Schematic
**File:** `6T_SRAM_SRAM_ARRAY_schematic.png`

**Description:**
- Multi-cell SRAM array architecture
- 4×4 configuration (16 cells total)
- Word lines (WL1-WL4) for row selection
- Bit lines (BL, BLB) for column data access
- Pre-charge circuits (I7-I20) distributed at bottom

**Key Features:**
- Hierarchical organization for scalability
- Shared bit lines and word lines
- Distributed pre-charge circuits
- Ground infrastructure for low impedance
- Cyan/blue nodes indicate signal routing

**Instances:** 20 (cell instances)
**Nets:** 46 (signal interconnections)
**Pins:** 14 (external connections)

---

### 6. 6T-SRAM Pre-charge Schematic (Detailed)
**File:** `6T_SRAM_precharge_schematic.png`

**Description:**
- Detailed pre-charge circuit implementation
- Two PMOS transistors in pull-up configuration
- Transistor specifications: W:120n, L:100n
- Gate specifications: L:100n, m:1 (multiplier)

**Transistor Details:**
- **Left PMOS:** gpdk090_pmos1v with W:120n, L:100n
- **Right PMOS:** gpdk090_pmos1v with W:120n, L:100n
- Both transistors controlled by PR signal

**Connections:**
- VDD: Supply voltage rail
- PR: Pre-charge control (inverted logic)
- BL: Bit line (gets charged to VDD)
- BLB: Bit line bar (gets charged to VDD)

**Operation:**
- When PR is low, both PMOS devices turn ON
- Charges BL and BLB to VDD level
- Equalizes bit line voltages before read/write operations

---

### 7. 6T-SRAM Sense Amplifier and Write Driver
**File:** `6T_SRAM_Sense_ampl_schematic.png`

**Description:**
- Complete sense amplifier implementation for 6T SRAM
- Latch-based differential amplifier
- Uses cross-coupled inverter pairs
- Low-power, high-speed design

**Schematic Components:**
- Differential input transistors
- Cross-coupled NMOS latch
- Enable signal (EN) for power gating
- PMOS pull-up devices
- Output nodes: Q and Q_bar

**Performance Characteristics:**
- Fast settling time
- Low-voltage operation
- Minimal sensing current

