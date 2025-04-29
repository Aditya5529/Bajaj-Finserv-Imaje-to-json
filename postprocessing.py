import re
from typing import List, Dict

def parse_lab_tests(lines: List[str]) -> List[Dict]:
    tests = []
    pattern = re.compile(r"(.+?)\s+([\d.]+)\s*(\w*/?\w*)?\s+([\d.-]+)\s*-\s*([\d.]+)\s*(\w*/?\w*)?")
    
    for line in lines:
        match = pattern.search(line)
        if match:
            test_name = match.group(1).strip()
            test_value = f"{match.group(2)} {match.group(3) or ''}".strip()
            reference_range = f"{match.group(4)}-{match.group(5)} {match.group(6) or ''}".strip()
            
            try:
                numeric_value = float(match.group(2))
                low = float(match.group(4))
                high = float(match.group(5))
                out_of_range = numeric_value < low or numeric_value > high
            except:
                out_of_range = False  
            
            tests.append({
                "test_name": test_name,
                "test_value": test_value,
                "bio_reference_range": reference_range,
                "lab_test_out_of_range": out_of_range
            })
    
    return tests