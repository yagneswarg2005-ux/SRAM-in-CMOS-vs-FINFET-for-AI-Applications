# Pre-charge Circuit - Detailed Design

## Purpose
The pre-charge circuit initializes bit lines to VDD before each memory operation, ensuring:
- Reduced access time
- Consistent sensing margin
- Lower power consumption
- Improved noise immunity

## Circuit Topology

### Simple 2-Transistor Design
```
        VDD
         |
        [M1]
         |
    +----+----+
    |         |
   [M2]      [M3]
    |         |
    BL       BLB
    |         |
   [Store] [Store]
```

**Components:**
- **M1**: PMOS cross-coupled transistor (pull-up between BL and BLB)
- **M2, M3**: PMOS pull-up transistors to VDD
- **PR Signal**: Controls all three PMOS devices (active low)

### Transistor Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| Technology | GPDK090 | - |
| Type | PMOS | - |
| Width (M1, M2, M3) | 120 | nm |
| Length | 100 | nm |
| Vth (nominal) | -0.4 | V |

## Operation

### Pre-charge Phase (PR = 0V)
1. All three PMOS transistors turn ON
2. M2 charges BL to VDD through pull-up
3. M3 charges BLB to VDD through pull-up
4. M1 equalizes any residual voltage between BL and BLB
5. Pre-charge time: ~2-3ns
6. Final voltage: ~1.9V on both bit lines

### Standby Phase (PR = 1.8V)
1. All PMOS transistors turn OFF
2. Bit lines float at VDD level
3. Storage maintains charge between cycles
4. Ready for next access cycle

## Timing Diagram

```
PR Signal:    |‾‾‾‾‾‾|_______|
BL Voltage:   |1.75→1.9|→1.9|1.75→1.9|→1.9|
BLB Voltage:  |1.75→1.9|→1.9|1.75→1.9|→1.9|
```

## Performance Metrics

### Timing
- **Pre-charge Time**: 2-3ns
- **Recovery Time**: ~10ns between cycles
- **Charge-up Tau (RC)**: < 2ns

### Power
- **Active Current**: ~10-20mA during pre-charge
- **Static Current**: < 1µA standby
- **Energy per Cycle**: ~10-20fJ

### Signal Quality
- **Final Voltage**: 1.85-1.95V (VDD - Vth)
- **Voltage Matching**: ±10mV between BL and BLB
- **No Overshoot**: Clean charging
- **Settling**: Complete within 3ns

## Integration Benefits

1. **Reduced Access Time**
   - Eliminates need for external pre-charging
   - Integrated timing with memory cycle
   - Faster cycle time

2. **Improved Sensing**
   - Consistent starting point for sensing
   - Better sense margin
   - More reliable read operations

3. **Power Efficiency**
   - Shared pre-charge circuitry in arrays
   - Single control signal for multiple cells
   - Reduced overall power consumption

4. **Area Efficiency**
   - Only 3 transistors required
   - Minimal layout area
   - Scales well to large arrays

## Simulation Results
From transient analysis (images 10, 11):
- Bit lines charge from ~1.75V to ~1.9V
- Pre-charge cycles repeat every ~15-20ns
- VDD remains stable at 2.0V
- Multiple cycles show consistent performance
- No degradation over time

## Design Considerations

### Process Variations
- PMOS threshold voltage: -0.3 to -0.5V
- Final pre-charge voltage: VDD - |Vth| = 1.85-1.95V
- Matched transistor pairs reduce mismatch

### Temperature Effects
- Temperature range: -40°C to 85°C
- Vth variation: ±50mV
- Pre-charge time increases at low temperature
- Voltage level decreases at high temperature

### Supply Noise
- Pre-charge circuit resilient to supply ripple
- PMOS devices provide filtering
- Bit line voltages well-regulated
