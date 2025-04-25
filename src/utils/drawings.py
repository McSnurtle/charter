import json
import os
from typing import Any, Dict, List

def save_drawings(symbol: str, interval: str, drawings: List[Dict[str, Any]]) -> None:
    """Save drawings for a specific symbol and timeframe"""
    filename = f"data/drawings/{symbol}_{interval}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w') as f:
        json.dump(drawings, f, indent=2)

def load_drawings(symbol: str, interval: str) -> List[Dict[str, Any]]:
    """Load drawings for a specific symbol and timeframe"""
    filename = f"data/drawings/{symbol}_{interval}.json"
    
    if not os.path.exists(filename):
        return []
        
    with open(filename, 'r') as f:
        return json.load(f) 