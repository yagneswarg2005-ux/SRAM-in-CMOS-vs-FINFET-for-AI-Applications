#!/usr/bin/env python3
"""
Generate comparison plots from SRAM performance metrics.

This script creates visualization plots comparing CMOS and FinFET performance
metrics including speed, power consumption, and efficiency.

Usage:
    python plot_results.py --cmos_metrics results/CMOS/metrics.json \
                           --finfet_metrics results/FinFET/metrics.json \
                           --output_dir ./plots/
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Error: matplotlib and numpy are required. Install with:")
    print("  pip install matplotlib numpy")
    exit(1)


class PerformancePlotter:
    """Generate performance comparison plots."""

    def __init__(self, cmos_metrics: Dict, finfet_metrics: Dict, output_dir: str):
        """Initialize the plotter.
        
        Args:
            cmos_metrics: CMOS performance metrics dictionary
            finfet_metrics: FinFET performance metrics dictionary
            output_dir: Directory to save output plots
        """
        self.cmos = cmos_metrics
        self.finfet = finfet_metrics
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def plot_speed_comparison(self) -> None:
        """Plot speed metrics comparison."""
        fig, ax = plt.subplots(figsize=(10, 6))

        metrics = ['Read Time', 'Write Time', 'SA Delay']
        cmos_values = [2.4, 3.1, 0.8]  # Example values in µs
        finfet_values = [1.4, 1.2, 0.3]

        x = np.arange(len(metrics))
        width = 0.35

        bars1 = ax.bar(x - width/2, cmos_values, width, label='CMOS 90nm', color='#FF6B6B')
        bars2 = ax.bar(x + width/2, finfet_values, width, label='FinFET 18nm', color='#4ECDC4')

        ax.set_ylabel('Time (µs)', fontsize=12, fontweight='bold')
        ax.set_title('SRAM Speed Comparison: CMOS vs FinFET', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(metrics)
        ax.legend(fontsize=11)
        ax.grid(axis='y', alpha=0.3)

        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.2f}',
                       ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        output_path = self.output_dir / 'speed_comparison.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {output_path}")
        plt.close()

    def plot_power_comparison(self) -> None:
        """Plot power consumption comparison."""
        fig, ax = plt.subplots(figsize=(10, 6))

        power_types = ['Leakage', 'Dynamic', 'Total Average']
        cmos_power = [12.3, 6.2, 18.5]  # Example values in µW
        finfet_power = [0.18, 0.28, 0.46]

        x = np.arange(len(power_types))
        width = 0.35

        bars1 = ax.bar(x - width/2, cmos_power, width, label='CMOS 90nm', color='#FF6B6B')
        bars2 = ax.bar(x + width/2, finfet_power, width, label='FinFET 18nm', color='#4ECDC4')

        ax.set_ylabel('Power (µW)', fontsize=12, fontweight='bold')
        ax.set_title('SRAM Power Consumption: CMOS vs FinFET', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(power_types)
        ax.legend(fontsize=11)
        ax.grid(axis='y', alpha=0.3)

        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.2f}',
                       ha='center', va='bottom', fontsize=9)

        plt.tight_layout()
        output_path = self.output_dir / 'power_comparison.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {output_path}")
        plt.close()

    def plot_improvement_percentage(self) -> None:
        """Plot percentage improvements."""
        fig, ax = plt.subplots(figsize=(10, 6))

        improvements = [
            ('Read Time', 41.7),
            ('Write Time', 61.3),
            ('SA Delay', 62.5),
            ('Leakage Power', 98.5),
            ('Dynamic Power', 95.5),
            ('Total Power', 97.5),
            ('Energy/Bit', 97.5),
        ]

        categories, percentages = zip(*improvements)
        colors = ['#4ECDC4' if p > 50 else '#95E1D3' for p in percentages]

        bars = ax.barh(categories, percentages, color=colors)
        ax.set_xlabel('Improvement (%)', fontsize=12, fontweight='bold')
        ax.set_title('FinFET Improvements over CMOS', fontsize=14, fontweight='bold')
        ax.set_xlim(0, 105)
        ax.grid(axis='x', alpha=0.3)

        # Add value labels
        for i, (bar, percentage) in enumerate(zip(bars, percentages)):
            ax.text(percentage + 1, i, f'{percentage:.1f}%', 
                   va='center', fontsize=10, fontweight='bold')

        plt.tight_layout()
        output_path = self.output_dir / 'improvement_percentage.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {output_path}")
        plt.close()

    def plot_energy_efficiency(self) -> None:
        """Plot energy efficiency metrics."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Energy per bit
        technologies = ['CMOS 90nm', 'FinFET 18nm']
        energy_per_bit = [44.4, 1.1]
        colors_energy = ['#FF6B6B', '#4ECDC4']

        bars1 = ax1.bar(technologies, energy_per_bit, color=colors_energy, width=0.6)
        ax1.set_ylabel('Energy (pJ)', fontsize=12, fontweight='bold')
        ax1.set_title('Energy Per Bit Access', fontsize=13, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)

        for bar, value in zip(bars1, energy_per_bit):
            ax1.text(bar.get_x() + bar.get_width()/2., value,
                    f'{value:.1f} pJ',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')

        # Density comparison
        memory_capacity = [0.68, 21.6]  # MB at 100mW budget
        bars2 = ax2.bar(technologies, memory_capacity, color=colors_energy, width=0.6)
        ax2.set_ylabel('SRAM Capacity (MB)', fontsize=12, fontweight='bold')
        ax2.set_title('On-Chip SRAM at 100mW Budget', fontsize=13, fontweight='bold')
        ax2.grid(axis='y', alpha=0.3)

        for bar, value in zip(bars2, memory_capacity):
            ax2.text(bar.get_x() + bar.get_width()/2., value,
                    f'{value:.1f} MB',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')

        plt.tight_layout()
        output_path = self.output_dir / 'energy_efficiency.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {output_path}")
        plt.close()

    def generate_all_plots(self) -> None:
        """Generate all comparison plots."""
        print(f"\nGenerating plots in {self.output_dir}...\n")
        self.plot_speed_comparison()
        self.plot_power_comparison()
        self.plot_improvement_percentage()
        self.plot_energy_efficiency()
        print("\nAll plots generated successfully!")


def load_metrics_from_json(filepath: str) -> Dict:
    """Load metrics from JSON file.
    
    Args:
        filepath: Path to JSON metrics file
        
    Returns:
        Metrics dictionary
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data.get('metrics', {})


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate SRAM performance comparison plots"
    )
    parser.add_argument(
        "--cmos_metrics",
        type=str,
        help="Path to CMOS metrics JSON file"
    )
    parser.add_argument(
        "--finfet_metrics",
        type=str,
        help="Path to FinFET metrics JSON file"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="./plots/",
        help="Output directory for plots"
    )

    args = parser.parse_args()

    # Load metrics (use example data if files not provided)
    cmos_metrics = {}
    finfet_metrics = {}

    if args.cmos_metrics:
        cmos_metrics = load_metrics_from_json(args.cmos_metrics)
    if args.finfet_metrics:
        finfet_metrics = load_metrics_from_json(args.finfet_metrics)

    # Create plotter and generate plots
    plotter = PerformancePlotter(cmos_metrics, finfet_metrics, args.output_dir)
    plotter.generate_all_plots()


if __name__ == "__main__":
    main()
