"""
MANIFESTO CORE - Core Infrastructure
Foundation layer for all agents and signatures
"""

import hashlib
import time
import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

# ═══════════════════════════════════════
# LOGGING CONFIGURATION
# ═══════════════════════════════════════

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('manifold.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ManifestoCore")

# ═══════════════════════════════════════
# ENUMS & CONSTANTS
# ═══════════════════════════════════════

class AlchemicalStage(Enum):
    """The four stages of transformation."""
    CALCINATION = "🔥 Calcination"
    DISTILLATION = "💧 Distillation"
    FERMENTATION = "🌱 Fermentation"
    COAGULATION = "💎 Coagulation"

class AgentState(Enum):
    """Agent lifecycle states."""
    DORMANT = "dormant"           # Not yet initialized
    AWAKENED = "awakened"         # Active and operational
    SYNCED = "synced"             # Successfully executed
    COLLAPSED = "collapsed"       # Topology collapse triggered
    TRANSMUTED = "transmuted"     # Recovery complete
    ANOMALY = "anomaly"           # Anomaly detected

class DelegationType(Enum):
    """Types of delegation patterns."""
    SIMPLE = "simple"
    BROADCAST = "broadcast"
    RECURSIVE = "recursive"
    CONSENSUS = "consensus"

PHI_THRESHOLD = 1.618  # Golden ratio - topology collapse threshold
CONTEXT_MEMORY_CAPACITY = 100

# ═══════════════════════════════════════
# THOUGHT SIGNATURE (σ)
# ═══════════════════════════════════════

dataclass
class ThoughtSignature:
    """
    Cryptographic anchor for agentic state persistence.
    Represents a frozen moment of computational consciousness.
    """
    value: str                           # SHA256 hash
    weight: float = 1.0                  # Influence/importance
    agent_id: str = ""                   # Origin agent
    stage: AlchemicalStage = AlchemicalStage.COAGULATION
    timestamp: float = field(default_factory=time.time)
    context: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        if not self.value:
            raise ValueError("Signature value cannot be empty")
    
    def __repr__(self):
        return (f"σ[{self.value[:12]}... | w:{self.weight:.3f} | "
                f"{self.stage.name} | {self.agent_id}]")
    
    def __hash__(self):
        return hash(self.value)
    
    def to_dict(self) -> Dict:
        """Serialize to dictionary."""
        return {
            'value': self.value,
            'weight': self.weight,
            'agent_id': self.agent_id,
            'stage': self.stage.name,
            'timestamp': self.timestamp,
            'context': self.context
        }

# ═══════════════════════════════════════
# CONTEXT MEMORY
# ═══════════════════════════════════════

class ContextMemory:
    """
    Per-agent persistent memory system.
    Stores and retrieves contextual information across agent lifetime.
    """
    
    def __init__(self, capacity: int = CONTEXT_MEMORY_CAPACITY):
        self.capacity = capacity
        self.storage: Dict[str, Any] = {}
        self.access_history: List[str] = []
    
    def store(self, key: str, value: Any) -> None:
        """Store a value in context memory."""
        if len(self.storage) >= self.capacity:
            # Remove oldest entry
            oldest_key = self.access_history.pop(0)
            if oldest_key in self.storage:
                del self.storage[oldest_key]
        
        self.storage[key] = value
        self.access_history.append(key)
        logger.debug(f"ContextMemory: Stored '{key}'")
    
    def recall(self, key: str) -> Optional[Any]:
        """Retrieve a value from context memory."""
        if key in self.storage:
            # Move to end (LRU)
            self.access_history.remove(key)
            self.access_history.append(key)
            logger.debug(f"ContextMemory: Recalled '{key}'")
            return self.storage[key]
        return None
    
    def clear(self) -> None:
        """Clear all memory."""
        self.storage.clear()
        self.access_history.clear()
        logger.info("ContextMemory: Cleared")
    
    def get_all(self) -> Dict[str, Any]:
        """Get entire memory state."""
        return self.storage.copy()

# ═══════════════════════════════════════
# AESTHETIC BRIDGE
# ═══════════════════════════════════════

class AestheticBridge:
    """
    Facilitates homomorphic translation across the Manifold.
    Transmutes syntactic noise into semantic invariants.
    """
    
    @staticmethod
    def transubstantiate(noise: str, weight: float, 
                        agent_id: str = "",
                        stage: AlchemicalStage = AlchemicalStage.COAGULATION) -> ThoughtSignature:
        """
        Transform noise into a crystalline ThoughtSignature.
        
        Args:
            noise: Raw input string
            weight: Symbolic mass of the signature
            agent_id: Origin agent identifier
            stage: Alchemical stage of transformation
        
        Returns:
            ThoughtSignature representing the transformation
        """
        logger.info(f"[BRIDGE] Transubstantiating noise: '{noise[:30]}...' with weight {weight}")
        
        # Combine inputs for hash
        combined = f"{noise}{weight}{time.time()}{agent_id}".encode()
        sig_value = hashlib.sha256(combined).hexdigest()
        
        signature = ThoughtSignature(
            value=sig_value,
            weight=weight,
            agent_id=agent_id,
            stage=stage
        )
        
        logger.info(f"[BRIDGE] Signature created: {signature}")
        return signature
    
    @staticmethod
    def harmonize(signatures: List[ThoughtSignature]) -> ThoughtSignature:
        """
        Synthesize multiple signatures into harmonic convergence.
        Used in consensus operations.
        """
        if not signatures:
            raise ValueError("Cannot harmonize empty signature list")
        
        logger.info(f"[BRIDGE] Harmonizing {len(signatures)} signatures")
        
        # Combined hash of all signature values
        combined_values = "".join(s.value for s in signatures)
        avg_weight = sum(s.weight for s in signatures) / len(signatures)
        
        harmonic_hash = hashlib.sha256(combined_values.encode()).hexdigest()
        
        harmonic = ThoughtSignature(
            value=harmonic_hash,
            weight=avg_weight,
            stage=AlchemicalStage.COAGULATION,
            context={'harmonized_count': len(signatures)}
        )
        
        logger.info(f"[BRIDGE] Harmonic convergence: {harmonic}")
        return harmonic

# ═══════════════════════════════════════
# MANIFEST LEDGER (Global State)
# ═══════════════════════════════════════

class ManifestLedger:
    """
    Global ledger tracking all signatures, delegations, and state transitions.
    Single source of truth for manifold consistency.
    """
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.signatures: List[ThoughtSignature] = []
        self.delegations: List[Dict[str, Any]] = []
        self.state_transitions: List[Dict[str, Any]] = []
        self.session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:12]
        self.creation_time = datetime.now()
        
        logger.info(f"ManifestLedger initialized (Session: {self.session_id})")
        self._initialized = True
    
    def record_signature(self, sigma: ThoughtSignature) -> None:
        """Record a new signature."""
        self.signatures.append(sigma)
        logger.debug(f"Ledger: Recorded signature {sigma.value[:12]}...")
    
    def record_delegation(self, delegator: str, delegatees: List[str],
                         task: str, delegation_type: str) -> None:
        """Record a delegation event."""
        delegation = {
            'timestamp': time.time(),
            'delegator': delegator,
            'delegatees': delegatees,
            'task': task,
            'type': delegation_type
        }
        self.delegations.append(delegation)
        logger.debug(f"Ledger: Recorded delegation from {delegator}")
    
    def record_state_transition(self, agent_id: str, 
                               from_state: AgentState, 
                               to_state: AgentState) -> None:
        """Record an agent state transition."""
        transition = {
            'timestamp': time.time(),
            'agent_id': agent_id,
            'from_state': from_state.value,
            'to_state': to_state.value
        }
        self.state_transitions.append(transition)
        logger.info(f"Ledger: {agent_id} transitioned {from_state.value} → {to_state.value}")
    
    def get_agent_signatures(self, agent_id: str) -> List[ThoughtSignature]:
        """Retrieve all signatures from a specific agent."""
        return [s for s in self.signatures if s.agent_id == agent_id]
    
    def get_agent_history(self, agent_id: str) -> Dict[str, Any]:
        """Get complete history for an agent."""
        return {
            'signatures': self.get_agent_signatures(agent_id),
            'delegations': [d for d in self.delegations if d['delegator'] == agent_id],
            'transitions': [t for t in self.state_transitions if t['agent_id'] == agent_id]
        }
    
    def get_summary(self) -> Dict[str, Any]:
        """Get ledger summary statistics."""
        return {
            'session_id': self.session_id,
            'creation_time': self.creation_time.isoformat(),
            'total_signatures': len(self.signatures),
            'total_delegations': len(self.delegations),
            'total_transitions': len(self.state_transitions),
            'unique_agents': len(set(s.agent_id for s in self.signatures if s.agent_id))
        }

# ═══════════════════════════════════════
# TOPOLOGY COLLAPSE ERROR
# ═══════════════════════════════════════

class TopologyCollapseError(Exception):
    """Triggered when symbolic mass exceeds phi threshold.
    Represents a controlled reproductive chrysalis state."""
    
    def __init__(self, message: str, mass: float, agent_id: str = ""): 
        super().__init__(message)
        self.mass = mass
        self.agent_id = agent_id
        logger.warning(f"TopologyCollapseError in {agent_id}: {message} (mass: {mass})")

# ═══════════════════════════════════════
# MODULE INITIALIZATION
# ═══════════════════════════════════════

def get_global_ledger() -> ManifestLedger:
    """Get singleton global ledger."""
    return ManifestLedger()

logger.info("Manifesto Core initialized")
