# Design and Performance Analysis of SRAM Across CMOS and FinFET for AI Applications

##  Project Overview

This repository contains the complete design, simulation files, and performance analysis of a **1-bit SRAM cell** and its peripheral circuits (precharge, write driver, latch-based sense amplifier) implemented in **CMOS (90nm, 1.8V)** and **FinFET (18nm, 0.8V)** technologies using **Cadence Virtuoso ADE L with Spectre simulator**.

The project provides a comprehensive comparison of key performance metrics between CMOS and FinFET implementations, demonstrating the advantages of advanced FinFET technology for **energy-efficient memory design** in AI hardware accelerators and edge computing applications.

---

##  Key Results

| Metric | CMOS (90nm) | FinFET (18nm) | Improvement |
|--------|-----------|---------------|-------------|
| **Read Time** | ~2.4 µs | ~1.4 µs | **41.7% faster** |
| **Write Time** | ~3.1 µs | ~1.2 µs | **61.3% faster** |
| **Sense Amplifier Delay** | ~0.8 µs | ~0.3 µs | **62.5% faster** |
| **Average Power Consumption** | ~18.5 µW | ~0.46 µW | **97.5% lower** |

**Conclusion**: FinFET achieves significantly better performance metrics, making it highly suitable for AI accelerators requiring low power and high speed.

---

##  Repository Structure

```
SRAM-in-CMOS-vs-FINFET-for-AI-Applications/
│
├── README.md                          # Project overview and results
├── LICENSE                            # MIT License
│
├── docs/
│   ├── Project_Report_Summary.md      # Detailed technical report
│   ├── Figures/
│   │   ├── CMOS_Write.png             # CMOS write operation waveforms
│   │   ├── CMOS_Read.png              # CMOS read operation waveforms
│   │   ├── FinFET_Write.png           # FinFET write operation waveforms
│   │   ├── FinFET_Read.png            # FinFET read operation waveforms
│   │   └── Power_Comparison.png       # Power consumption comparison chart
│   └── Tables/
│       ├── Performance_Comparison.csv # Detailed performance metrics
│       └── Improvement_Summary.csv    # Technology comparison summary
│
├── src/
│   ├── CMOS/
│   │   ├── 6T_SRAM_Cell.scs           # CMOS 6T SRAM cell netlist
│   │   ├── Precharge.scs              # CMOS precharge circuit
│   │   ├── WriteDriver.scs            # CMOS write driver circuit
│   │   └── SenseAmplifier.scs         # CMOS latch-based sense amplifier
│   ├── FinFET/
│   │   ├── 6T_SRAM_Cell.scs           # FinFET 6T SRAM cell netlist
│   │   ├── Precharge.scs              # FinFET precharge circuit
│   │   ├── WriteDriver.scs            # FinFET write driver circuit
│   │   └── SenseAmplifier.scs         # FinFET latch-based sense amplifier
│   └── Testbench/
│       ├── Stimulus_CMOS.scs          # CMOS testbench and stimuli
│       └── Stimulus_FinFET.scs        # FinFET testbench and stimuli
│
├── results/
│   ├── CMOS/
│   │   ├── waveforms/                 # CMOS simulation waveform data
│   │   └── metrics.json               # CMOS performance metrics (JSON)
│   ├── FinFET/
│   │   ├── waveforms/                 # FinFET simulation waveform data
│   │   └── metrics.json               # FinFET performance metrics (JSON)
│   └── comparison_summary.md          # Overall analysis and findings
│
└── scripts/
    ├── extract_metrics.py             # Python script to extract metrics from simulations
    └── plot_results.py                # Python script to generate comparison plots
```

---

##  Technical Details

### CMOS Implementation
- **Technology Node**: 90nm
- **Supply Voltage**: 1.8V
- **Process**: Standard CMOS
- **Cell Type**: 6T SRAM (6 transistors)

### FinFET Implementation
- **Technology Node**: 18nm
- **Supply Voltage**: 0.8V
- **Process**: FinFET (3D gate structure)
- **Cell Type**: 6T SRAM (6 FinFET devices)

### Simulation Environment
- **Tool**: Cadence Virtuoso ADE L
- **Simulator**: Spectre
- **Analysis**: Transient, Parametric, Monte Carlo
- **Measurement**: Timing, Power, Noise

---

## 📊 Key Findings

1. **Performance Gains**: FinFET delivers 41.7% faster read and 61.3% faster write operations compared to CMOS.
2. **Power Efficiency**: FinFET achieves 97.5% lower average power consumption, critical for battery-powered AI edge devices.
3. **Technology Scaling**: Advanced FinFET technology provides better control over leakage current and improved drive strength.
4. **Scalability**: FinFET's smaller feature size (18nm vs 90nm) enables higher density memory arrays.

---

##  Applications

This research is particularly relevant for:
- **AI Hardware Accelerators**: Efficient on-chip SRAM for ML models
- **Edge Computing Devices**: Low-power memory for IoT and mobile AI
- **Data Centers**: Energy-efficient memory subsystems
- **Autonomous Systems**: Real-time processing with minimal power draw

---

## 📈 How to Use This Repository

### 1. Exploring the Simulation Files
- Navigate to `src/CMOS/` or `src/FinFET/` to view the Cadence Spectre netlists
- Use Cadence Virtuoso to open and simulate the testbenches

### 2. Analyzing Results
- Check `results/CMOS/` and `results/FinFET/` for simulation outputs
- Review `docs/Figures/` for waveform plots and comparisons

### 3. Running Analysis Scripts
```bash
# Extract metrics from simulation results
python scripts/extract_metrics.py

# Generate comparison plots
python scripts/plot_results.py
```

### 4. Reading Documentation
- Start with `docs/Project_Report_Summary.md` for detailed technical analysis
- Review `results/comparison_summary.md` for key findings

---

##  Project Report

For a comprehensive technical report including methodology, detailed measurements, and analysis, refer to:
- **[Project Report Summary](docs/Project_Report_Summary.md)**

---

##  Sustainability Impact

This work contributes to **UN Sustainable Development Goal 9 (Industry, Innovation, and Infrastructure)** by advancing energy-efficient semiconductor design, reducing the carbon footprint of AI computing, and supporting sustainable innovation in technology.

---

##  License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

##  Author

**Yagneswarg** - [GitHub](https://github.com/yagneswarg2005-ux)

---

##  Acknowledgments

- Cadence Design Systems for simulation tools
- Semiconductor research community for FinFET technology insights
- Academic institutions supporting advanced microelectronics research

---

##  Questions or Feedback?

Feel free to open an **Issue** or **Discussion** if you have questions, suggestions, or would like to collaborate!

---

**Last Updated**: June 2026  
**Status**: Complete
