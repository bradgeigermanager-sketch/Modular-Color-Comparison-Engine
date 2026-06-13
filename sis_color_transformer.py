# FILE: sis_color_transformer.py
# USE: Master controller for SIS color-signature routing
# VERSION: 2.0.0

from hex_canonical_mapper import HexCanonicalMapper
from weighted_color_engine import WeightedColorEngine

class SISColorTransformer:
    """
    Orchestrates the transformation of raw sensor inputs 
    into standardized signatures for the SIS Registry.
    """
    def __init__(self, registry_map):
        self.registry = registry_map # Your CSS_COLOR_MAP_001
        self.mapper = HexCanonicalMapper()
        self.engine = WeightedColorEngine(weights=(1.0, 1.0, 1.0))

    def process_input(self, raw_hex):
        # STAGE 1: Canonicalization
        canonical_hex = self.mapper.normalize(raw_hex)
        
        # STAGE 2: Registry Routing & Comparison
        best_match, distance = self._route_to_registry(canonical_hex)
        
        return {
            "input": raw_hex,
            "canonical": canonical_hex,
            "match": best_match,
            "integrity_score": distance
        }

    def _route_to_registry(self, target_hex):
        best_match = None
        min_dist = float('inf')
        
        for name, data in self.registry.items():
            dist = self.engine.compute_weighted_distance(target_hex, data['hex'])
            if dist < min_dist:
                min_dist = dist
                best_match = name
        return best_match, min_dist

# Usage:
# transformer = SISColorTransformer(CSS_COLOR_MAP_001)
# result = transformer.process_input("#f0f8ff")

