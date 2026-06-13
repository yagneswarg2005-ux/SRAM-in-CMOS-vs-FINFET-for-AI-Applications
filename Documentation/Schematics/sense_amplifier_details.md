# Sense Amplifier - Detailed Design

## Purpose
The sense amplifier is a critical component that detects and amplifies small voltage differences on SRAM bit lines during read operations, converting them to full rail-to-rail output voltages.

## Block Diagram
```
Bit Lines (BL, BLB) 
        |
        v
    [Differential Pair]
        |
        v
    [Latch Stage]
        |
        v
    [Output Stage]
        |
        v
    Q, Q_bar Outputs
```

## Circuit Topology

### Differential Input Stage
- NMOS differential pair transistors
- Connected to bit lines BL and BLB
- Converts small voltage differential to current difference
- Tail current source for biasing

### Cross-Coupled Latch
- Two cross-coupled NMOS transistors
- Provides positive feedback amplification
- Rapidly amplifies initial differential voltage
- Self-locking latch behavior

### Load Devices
- PMOS pull-up network
- Provides high impedance load
- Reduces power consumption
- Fast settling characteristics

### Enable Signal
- Controls amplifier activation
- Power gating capability
- Timing synchronization with memory cycle

## Performance Characteristics

### Speed
- **Sensing Delay**: 1-2ns from enable to output valid
- **Settling Time**: < 3ns to rail voltage
- **Total Access Time Impact**: ~2-3ns added to cycle time

### Power
- **Dynamic Power**: Minimal during sensing
- **Leakage**: Reduced with enable control
- **Active Current**: ~50-100µA during sensing

### Sensitivity
- **Minimum Detectable Voltage**: ~50mV differential
- **Gain**: 100-1000V/V
- **Noise Margin**: > 200mV

## Signal Integrity
- Differential signal rejection of common-mode noise
- Fast slew rates for clean outputs
- Minimal overshoot/undershoot
- Low jitter design

## Simulation Results
From transient analysis:
- Small initial differential voltage: ~45mV
- Final output swing: >1.8V
- Settling time: ~2-3ns
- No ringing observed

## Integration Notes
- Works with pre-charge circuit for bit line initialization
- Timing synchronized to word line pulse
- Outputs directly feed output buffers
- Suitable for multi-cell arrays
