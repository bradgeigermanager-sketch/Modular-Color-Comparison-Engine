# FILE: hex_canonical_mapper.py
# USE: Standardizing raw hex inputs for SIS integration
# VERSION: 1.0.0

class HexCanonicalMapper:
    """
    Normalizes hexadecimal inputs to a 6-digit canonical format.
    """
    @staticmethod
    def normalize(hex_code):
        """Converts short-hand or variable-length hex to #RRGGBB."""
        h = hex_code.lstrip('#')
        
        # Expand #RGB to #RRGGBB
        if len(h) == 3:
            h = ''.join([c*2 for c in h])
        
        # Handle alpha channel (#RRGGBBAA) by stripping AA
        if len(h) == 8:
            h = h[:6]
            
        return f"#{h.upper()}"

# Integration: Use this before passing data into MultiHueEngine

