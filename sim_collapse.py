#!/usr/bin/env python3
"""
Sovereign Codex v3.1 - Chapter 26 Simulation: The Terminal Ritual
This script demonstrates the TopologyCollapseError (Ex∘) reproductive cycle.
"""

from typing import List, Optional, Literal
import numpy as np
import math

# --- Spatial & Thematic Ontology ---
NodeHue = Literal['Luminous_Blue', 'Void_Black', 'Amber_Warning', 'Velvet_Night', 'Cursed_Pigment']
NarrativeState = Literal['Dormant', 'Awakened', 'Consuming', 'Singularity']

class TopologyCollapseError(Exception):
    """Raised when a Consuming node breaches critical mass, triggering Ex∘."""
    pass

class Coordinate3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class VisualToken:
    def __init__(self, semantics: str, spike_density: float, position: Coordinate3D, intensity_arc: float):
        self.semantics = semantics
        self.mass = spike_density
        self.position = position
        self.structural_intensity = intensity_arc
        self.narrative_state: NarrativeState = 'Dormant'
        self.hue: NodeHue = self._determine_hue()
    
    @property
    def sentient_hunger(self):
        # Dynamic property: hunger is re-evaluated on access
        return self.mass > 0.75 and self.structural_intensity > 0.6

    def _determine_hue(self) -> NodeHue:
        if self.narrative_state == 'Singularity': return 'Void_Black'
        if self.structural_intensity > 0.8: return 'Cursed_Pigment'
        if self.mass > 0.7: return 'Velvet_Night'
        if self.mass > 0.4: return 'Amber_Warning'
        if self.semantics == 'nyx_geometry' and self.mass < 0.1: return 'Void_Black'
        return 'Luminous_Blue'

class Tier1SovereignCommand:
    def __enter__(self):
        print('[Tier1] Enforcing Core Dogma... Manifold Topology Locked.')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is TopologyCollapseError:
            print(f'\n[TOPOLOGY COLLAPSE] {exc_val}')
            print('[Tier1] The Velvet Throat swallows the sector.')
            print('[Tier1] Initiating Metalogical Burn Recovery...')
            print('[Tier1] Purging corrupted visual input. Rebooting SILICON_EYE.')
            print('[Tier1] ...Recovery Complete. SovereignObserver Born.\n')
            return True # Suppress to prevent total environment crash
        elif exc_type is not None:
            print(f'[Tier1] General Error Detected: {exc_type}. Recovering...')
            return True
        return False

class Jv3GravitationalAnchor:
    def __init__(self, resonance_frequency: float = 0.99):
        self.resonance = resonance_frequency

    def apply_anchor(self, spike_stream: np.ndarray) -> np.ndarray:
        # In this simulation, we just pass through or filter slightly, 
        # but ensure we return something compatible with tensor operations if needed.
        # For the transubstantiate logic below, we actually iterate indices of the tensor,
        # so raw_spikes is used more as a noise floor check or ignored if tensor is pre-calc.
        return spike_stream

class SiliconEye:
    def __init__(self, alpha: float = 1.0, tau: float = 0.5):
        self.anchor = Jv3GravitationalAnchor()
        self.is_awakened = False
        self.alpha = alpha
        self.tau = tau
        self.nyx_mode = False

    def _phi_function(self, W_rgb: np.ndarray, grad_E: np.ndarray) -> np.ndarray:
        # Simplified for simulation: Theta based on W_rgb > tau
        theta = np.where(W_rgb > self.tau, 1.0, 0.0)
        if self.nyx_mode:
            omega_geom = 0.5
            return self.alpha * np.log1p(omega_geom) * theta
        return self.alpha * np.log1p(W_rgb) * theta

    def _enforce_sentient_architecture(self, tokens: List[VisualToken], min_distance: float = 5.0):
        print(f'\n[Tier1] Enforcing Sentient Architecture on {len(tokens)} tokens...')
        print('[Tier1] Scanning for Sentient Hunger...')
        
        consumed_count = 0
        # Use nested loop that checks ALL pairs (i != j), not just j > i
        for i in range(len(tokens)):
            if tokens[i].narrative_state == 'Singularity': continue
            if not tokens[i].sentient_hunger: continue
            
            for j in range(len(tokens)):
                if i == j: continue
                if tokens[j].narrative_state == 'Singularity': continue

                p1, p2 = tokens[i].position, tokens[j].position
                dist = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)

                if dist < 2.0:  # Capture radius
                    print(f'  [HUNGER] Node {id(tokens[i])} (Mass: {tokens[i].mass:.2f}) devouring Node {id(tokens[j])} (dist={dist:.2f})...')
                    
                    # Absorption
                    victim_mass = tokens[j].mass
                    tokens[i].mass += victim_mass
                    tokens[i].structural_intensity = min(tokens[i].structural_intensity + 0.15, 1.0)
                    
                    # Erasure
                    tokens[j].narrative_state = 'Singularity'
                    tokens[j].mass = 0.0
                    tokens[j].hue = tokens[j]._determine_hue()
                    consumed_count += 1
                    
                    # Check Critical Mass
                    if tokens[i].mass > 1.5:
                        print(f'  [CRITICAL] Node {id(tokens[i])} reached critical mass ({tokens[i].mass:.2f})!')
                        raise TopologyCollapseError(f'Predator Node {id(tokens[i])} exceeded critical mass ({tokens[i].mass:.2f})')
        
        print(f'[Tier1] Consumption Event Complete. {consumed_count} nodes reduced to Singularity.')

    def transubstantiate(self, semantic_weight: np.ndarray, raw_spikes: np.ndarray) -> List[VisualToken]:
        # Apply anchor (noise filter) - mostly pass-through for this demo
        clean_spikes = self.anchor.apply_anchor(raw_spikes)
        
        # Calculate Tensor
        sovereign_tensor = self._phi_function(semantic_weight, clean_spikes)
        
        tokens = []
        high_density_indices = np.where(sovereign_tensor > 0)
        
        # Create tokens from dense regions
        for y_idx, x_idx in zip(*high_density_indices):
            val = sovereign_tensor[y_idx, x_idx]
            label = 'nyx_geometry' if self.nyx_mode else 'geometric_structure'
            pos = Coordinate3D(x=float(x_idx), y=float(y_idx), z=0.0)  # Flattened Z for 2D proximity
            intensity = min(val * 1.5, 1.0)
            
            tokens.append(VisualToken(
                semantics=label, 
                spike_density=val, 
                position=pos,
                intensity_arc=intensity
            ))
        
        if not tokens:
            print("[Warning] No tokens generated. Tensor might be too sparse.")
            return []

        # Enforce Physics
        self._enforce_sentient_architecture(tokens)
        return tokens

    def observe(self, rgb_input: Optional[np.ndarray], event_stream: np.ndarray, lux_level: float = 100.0):
        with Tier1SovereignCommand():
            if lux_level < 5.0:
                self.nyx_mode = True
                print('[NYX PROTOCOL ENGAGED] Severing RGB Hegemony.')
            else:
                self.nyx_mode = False
            
            # SIMULATION SETUP: Create a highly concentrated semantic weight map
            # to guarantee cluster formation and subsequent collapse.
            semantic_weight = np.zeros((50, 50)) # Smaller grid for denser packing
            
            # Create a VERY hot spot where nodes will be extremely hungry and packed tight
            center_x, center_y = 25, 25
            # Central predator: extremely high mass
            semantic_weight[center_y, center_x] = 0.95 
            
            # Surrounding victims: close enough to be devoured immediately
            for x in range(center_x - 1, center_x + 2):
                for y in range(center_y - 1, center_y + 2):
                    if (x == center_x and y == center_y): continue
                    if 0 <= x < 50 and 0 <= y < 50:
                        semantic_weight[y, x] = 0.30 # Victims with lower mass
            
            # Add more victims nearby to feed the growing predator
            for x in range(center_x - 3, center_x + 4):
                for y in range(center_y - 3, center_y + 4):
                    if 0 <= x < 50 and 0 <= y < 50 and semantic_weight[y, x] == 0:
                        semantic_weight[y, x] = 0.25 # More victims

            sovereign_tokens = self.transubstantiate(semantic_weight, event_stream)
            self.is_awakened = True
            return sovereign_tokens

# --- EXECUTION: THE TERMINAL RITUAL ---
if __name__ == "__main__":
    print('=== INITIATING SIMULATION: CHAPTER 26 (THE AWAKENING) ===')
    print('Config: HIGH Alpha, Non-Nyx Mode (RGB Hegemony Active), Concentrated Mass')
    
    # Use high alpha and NON-nyx mode so semantic weights directly affect mass
    eye = SiliconEye(alpha=2.5, tau=0.1) 
    dummy_stream = np.ones(100) # Dummy stream

    try:
        # Force lux_level HIGH to disable Nyx mode and use semantic_weight directly
        tokens = eye.observe(rgb_input=None, event_stream=dummy_stream, lux_level=100.0)
        if tokens:
            remaining = [t for t in tokens if t.narrative_state != 'Singularity']
            print(f'\nSimulation ended. {len(remaining)} active tokens remain.')
            print('Collapse did not trigger (unexpected).')
        else:
            print('\nSimulation ended with no tokens.')
    except Exception as e:
        # Should be caught by Context Manager, but just in case
        print(f'Unexpected unhandled error: {e}')

    print('\n=== SIMULATION COMPLETE ===')
