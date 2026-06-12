#!/usr/bin/env python3
"""
Extract performance metrics from Cadence Spectre simulation results.

This script processes simulation output files and extracts key performance
metrics such as read time, write time, power consumption, etc.

Usage:
    python extract_metrics.py --technology CMOS --results_dir results/CMOS/
    python extract_metrics.py --technology FinFET --results_dir results/FinFET/
"""

import json
import os
import argparse
from pathlib import Path
from typing import Dict, List, Any


class MetricsExtractor:
    """Extract metrics from Spectre simulation outputs."""

    def __init__(self, results_dir: str, technology: str):
        """Initialize the metrics extractor.
        
        Args:
            results_dir: Path to the results directory
            technology: Technology name (CMOS or FinFET)
        """
        self.results_dir = Path(results_dir)
        self.technology = technology
        self.metrics = {}

    def parse_waveform_file(self, filepath: str) -> Dict[str, Any]:
        """Parse waveform file and extract metrics.
        
        Args:
            filepath: Path to the waveform file
            
        Returns:
            Dictionary containing extracted metrics
        """
        # This is a placeholder function
        # In practice, you would parse actual Spectre output files (PSF format)
        # or CSV waveform exports
        metrics = {
            "read_time_us": 0.0,
            "write_time_us": 0.0,
            "sense_amp_delay_us": 0.0,
            "average_power_uw": 0.0,
            "leakage_power_uw": 0.0,
            "dynamic_power_uw": 0.0,
        }
        return metrics

    def extract_all_metrics(self) -> Dict[str, Any]:
        """Extract metrics from all waveform files in the results directory.
        
        Returns:
            Dictionary containing all extracted metrics
        """
        waveform_dir = self.results_dir / "waveforms"
        
        if not waveform_dir.exists():
            print(f"Warning: Waveform directory not found at {waveform_dir}")
            return {}

        all_metrics = {}
        
        # Find all waveform files
        for waveform_file in waveform_dir.glob("*.csv"):
            print(f"Processing {waveform_file.name}...")
            metrics = self.parse_waveform_file(str(waveform_file))
            all_metrics[waveform_file.stem] = metrics

        return all_metrics

    def save_metrics_json(self, output_file: str) -> None:
        """Save extracted metrics to JSON file.
        
        Args:
            output_file: Path to output JSON file
        """
        metrics = self.extract_all_metrics()
        
        output_data = {
            "technology": self.technology,
            "metrics": metrics
        }
        
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"Metrics saved to {output_file}")

    def print_summary(self) -> None:
        """Print a summary of extracted metrics."""
        metrics = self.extract_all_metrics()
        
        print(f"\n{'='*50}")
        print(f"Metrics Summary for {self.technology}")
        print(f"{'='*50}")
        
        for test_name, test_metrics in metrics.items():
            print(f"\n{test_name}:")
            for metric_name, metric_value in test_metrics.items():
                print(f"  {metric_name}: {metric_value}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract metrics from Cadence Spectre simulation results"
    )
    parser.add_argument(
        "--technology",
        choices=["CMOS", "FinFET"],
        required=True,
        help="Technology type"
    )
    parser.add_argument(
        "--results_dir",
        type=str,
        required=True,
        help="Path to results directory"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output JSON file path (optional)"
    )

    args = parser.parse_args()

    # Create extractor instance
    extractor = MetricsExtractor(args.results_dir, args.technology)

    # Save metrics to JSON if output specified
    if args.output:
        extractor.save_metrics_json(args.output)
    
    # Print summary
    extractor.print_summary()


if __name__ == "__main__":
    main()
