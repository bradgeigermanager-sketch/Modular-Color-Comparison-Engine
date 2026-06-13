# FILE: color_engine_module.py
# USE: Modular class for color comparison within SIS and forensic pipelines
# VERSION: 1.0.0

import math

class ColorComparisonEngine:
    """
    Modular engine for processing and comparing color vectors.
    """
    def __init__(self, color_map=None):
        self.color_map = color_map or {}

    @staticmethod
    def _to_rgb(hex_val):
        hex_val = hex_val.lstrip('#')
        return [int(hex_val[i:i+2], 16) for i in (0, 2, 4)]

    def compute_distance(self, hex1, hex2):
        """Calculates Euclidean distance for 3D RGB point comparison."""
        rgb1 = self._to_rgb(hex1)
        rgb2 = self._to_rgb(hex2)
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))

    def find_nearest(self, target_hex, candidates=None):
        """
        Maps a target color to the nearest match within a defined candidate list.
        Useful for normalizing noisy sensor data against the CSS_COLOR_MAP.
        """
        candidates = candidates or self.color_map
        best_match = None
        min_dist = float('inf')
        
        for name, data in candidates.items():
            dist = self.compute_distance(target_hex, data['hex'])
            if dist < min_dist:
                min_dist = dist
                best_match = name
        return best_match, min_dist

# Usage Note: Integrate this by passing your CSS_COLOR_MAP_001 
# dictionary to the constructor.

