# FILE: weighted_color_engine.py
# USE: Forensic-grade color signature matching with channel weighting
# VERSION: 1.2.0

import math

class WeightedColorEngine:
    """
    Computes distance using custom weights for R, G, and B channels.
    """
    def __init__(self, weights=(1.0, 1.0, 1.0)):
        # Normalize weights to ensure they sum to 3.0 (for consistency)
        total = sum(weights)
        self.weights = [3.0 * w / total for w in weights]

    def _to_rgb(self, hex_val):
        h = hex_val.lstrip('#')
        return [int(h[i:i+2], 16) for i in (0, 2, 4)]

    def compute_weighted_distance(self, hex1, hex2):
        """
        Distance = sqrt(wR*(dR)^2 + wG*(dG)^2 + wB*(dB)^2)
        """
        rgb1 = self._to_rgb(hex1)
        rgb2 = self._to_rgb(hex2)
        
        weighted_sq_sum = sum(
            self.weights[i] * ((rgb1[i] - rgb2[i]) ** 2) 
            for i in range(3)
        )
        return math.sqrt(weighted_sq_sum)

# Integration Example:
# forensic_engine = WeightedColorEngine(weights=(1.2, 0.8, 1.0))
# distance = forensic_engine.compute_weighted_distance("#FF0000", "#FF0005")

