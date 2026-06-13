# FILE: multi_hue_engine_module.py
# USE: Modular engine for N-way color signature comparison
# VERSION: 1.1.0

import math

class MultiHueEngine:
    """
    Modular engine for comparing a primary color against a collection of hues.
    """
    
    @staticmethod
    def _to_rgb(hex_val):
        hex_val = hex_val.lstrip('#')
        return [int(hex_val[i:i+2], 16) for i in (0, 2, 4)]

    def _calc_dist(self, rgb1, rgb2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))

    def compare_to_batch(self, target_hex, hue_list):
        """
        Calculates similarity distances for an arbitrary number of hues.
        :param target_hex: The primary signature color
        :param hue_list: A list of dicts [{'name': '...', 'hex': '...'}]
        :return: List of results sorted by closeness
        """
        target_rgb = self._to_rgb(target_hex)
        results = []
        
        for hue in hue_list:
            dist = self._calc_dist(target_rgb, self._to_rgb(hue['hex']))
            results.append({
                'name': hue['name'],
                'distance': round(dist, 4)
            })
            
        # Return sorted by distance (Ascending: smallest distance is closest)
        return sorted(results, key=lambda x: x['distance'])

# Implementation Note: 
# This engine supports the AARM framework by allowing 
# multi-point forensic color signatures to be ranked 
# against standard registry values.

