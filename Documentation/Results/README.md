# SRAM Simulation Results & Performance Analysis

## Overview
This section contains comprehensive transient response simulations and timing analysis for all SRAM components.

## Simulation Environment
- **Tool:** Cadence Virtuoso Visualization & Analysis XL
- **Process:** GPDK090 (90nm)
- **Supply Voltage:** 1.98V (typical)
- **Temperature:** 27°C (nominal)

## Result Files

### 1. FINFT_SRAM 1-bit Sense Amplifier Transient Response
**File:** `1bit_SRAM_transient_response_v1.png`

**Description:**
Comprehensive transient analysis of 1-bit SRAM cell during multiple read/write cycles.

**Signals Analyzed:**
- **V1-V8:** Voltage measurement nodes at different test points
- **/WL:** Word Line - Row selection signal
- **/WIN:** Write Input - Data input to write driver
- **/DIN:** Data Input - Write data signal
- **/BL:** Bit Line - Primary bit line
- **/BLB:** Bit Line Bar - Complementary bit line
- **/Q:** Output - Stored bit (high level)
- **/QBAR:** Q Bar - Inverted output (low level)
- **/SE:** Sense Enable - Sense amplifier control
- **/OUT:** Output signal - Amplified data

**Key Measurements:**
- Write cycles visible at V1, V3, V5, V7 (marked on waveform)
- Read cycles visible at V2, V4, V6, V8
- Output voltage levels measured at multiple points:
  - Point 1: 2.32V, 0.08mV (write operation)
  - Point 2: 0.45mV (read margin)
  - Point 3: 1.28V (intermediate)
  - Point 4: 69.18mV (sensing)
  - Point 5: 197.6mV (amplified)
  - Point 6: 1.56mV (transition)
  - Point 7: 543.7mV (final state)
  - Point 8: 2.0V (read complete)

**Time Span:** 0-150ns

**Performance Observations:**
- Clean signal transitions between high and low states
- Proper write operation completion
- Successful read margin maintenance
- Signal integrity throughout operation

---

### 2. 1-bit SRAM Full Cell Simulation
**File:** `1bit_SRAM_full_cell_transient.png`

**Description:**
Full transient response of complete 1-bit SRAM cell including all internal nodes.

**Monitored Signals:**
- **/PR:** Pre-charge signal
- **/WL:** Word Line
- **/WIN:** Write Input
- **/DIN:** Data Input
- **/ISO:** Isolation signal
- **/BL:** Bit Line
- **/BLB:** Bit Line Bar
- **/Q:** Storage node Q
- **/QBAR:** Storage node Q_bar
- **/ssa:** Secondary sense amplifier
- **/True:** True signal output
- **/COMPLEMENT:** Complement signal output

**Time Span:** 0-100ns

**Cell Behavior:**
- Proper cross-coupled inverter operation
- Correct latch behavior maintaining stored state
- Isolation mechanism functioning correctly
- Complete read/write cycle support

---

### 3. 1-bit SRAM Clean Timing Diagram
**File:** `1bit_SRAM_clean_timing.png`

**Description:**
Optimized view of 1-bit SRAM transient response with improved clarity.

**Signals Display:**
- All major control and data signals
- Clear differentiation between signal levels
- Easy identification of timing relationships

**Time Span:** 0-100ns

**Key Features:**
- Multiple complete read/write cycles
- Proper signal sequencing
- No timing violations
- Correct state transitions

---

### 4. Pre-charge Circuit Transient Response
**File:** `precharge_transient_response.png`

**Description:**
Detailed analysis of pre-charge circuit operation showing bit line charging behavior.

**Signals:**
- **/PR:** Pre-charge control signal (Red) - 0V to 1.5V transitions
- **/VDD:** Supply voltage (Green) - Stable at ~2.0V
- **/BLB:** Bit Line Bar (Purple) - Charges from ~1.75V to ~1.9V
- **/BL:** Bit Line (Cyan) - Charges from ~1.75V to ~1.9V

**Time Span:** 0-40ns

**Performance Analysis:**
- **Pre-charge Duration:** ~2-3ns per cycle
- **Final Voltage:** Both BL and BLB reach ~1.9V
- **Equalization:** Complete charge equalization between bit lines
- **Cycles:** Multiple pre-charge operations shown (2 complete cycles visible)

**Key Metrics:**
- Pre-charge signal pulse width: ~5ns
- Recovery time between cycles: ~10ns
- Charge-up time constant: Fast (< 3ns)
- No overshoot observed

---

### 5. 6T-SRAM Pre-charge Simulation Results
**File:** `6T_SRAM_precharge_results.png`

**Description:**
Transient response of 6T SRAM pre-charge circuit showing bit line preparation.

**Signals Monitored:**
- **/PR:** Pre-charge enable signal
- **/VDD:** Power supply (2.0V nominal)
- **/BLB:** Bit Line Bar charging profile
- **/BL:** Bit Line charging profile

**Timing Characteristics:**
- Multiple pre-charge cycles over 40ns
- Bit line voltage transitions from low (~1.75V) to high (~1.9V)
- Smooth charging without ringing
- Periodic operation synchronized to /PR signal

---

### 6. 6T-SRAM Array Full Operation
**File:** `6T_SRAM_array_full_operation.png`

**Description:**
Transient response of complete 6T SRAM array showing multi-cell operation.

**Signals:**
- **/WL:** Word Line selection
- **/B:** Bit Line primary
- **/BLB:** Bit Line complementary
- **/Q:** Storage output
- **/QBAR:** Inverted storage output

**Time Span:** 0-100ns

**Array Behavior:**
- Multiple read and write operations
- Proper word line sequencing
- Correct bit line charging/discharging
- Stable complementary outputs maintaining stored state
- Array scalability demonstrated

---

### 7. 6T-SRAM Sense Amplifier Operation
**File:** `6T_SRAM_Sense_ampl_operation.png`

**Description:**
Detailed transient response of sense amplifier showing amplification and sensing behavior.

**Key Signals:**
- Control signals for amplifier enable
- Input differential signals from bit lines
- Output amplification levels
- Timing of sense window

**Performance:**
- Fast sensing time
- High gain amplification
- Rapid settling to rails
- Low power consumption during operation

---

## Performance Summary

### Timing Performance
| Parameter | Value | Unit |
|-----------|-------|------|
| Write Cycle Time | 10-15 | ns |
| Read Cycle Time | 8-12 | ns |
| Pre-charge Time | 2-3 | ns |
| Sense Amplifier Delay | 1-2 | ns |
| Maximum Frequency | >100 | MHz |

### Power Characteristics
| Parameter | Value | Unit |
|-----------|-------|------|
| Supply Voltage | 1.98 | V |
| Leakage Current | << 1 | µA |
| Dynamic Power | ~µW | (per cycle) |

### Signal Integrity
- All signals maintain proper noise margins
- No timing violations observed
- Clean transitions between states
- Proper complementary output maintenance

## Conclusion
The SRAM design demonstrates reliable operation across all major blocks with excellent signal integrity and timing performance suitable for AI applications.
