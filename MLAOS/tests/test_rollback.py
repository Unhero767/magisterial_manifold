import pytest

def test_state_verification_after_rollback(db_session, baseline_snapshot):
    """
    Validates that the substrate reverts to the baseline 
    snapshot after a forced Metalogical Burn.
    """
    try:
        db_session.begin()
        db_session.execute("UPDATE table_a SET value='changed' WHERE id=3")
        raise Exception("Force rollback")
        db_session.commit()
    except Exception:
        db_session.rollback()
    finally:
        # Compare current state to baseline snapshot
        current_state = db_session.execute("SELECT * FROM table_a WHERE id=3").fetchone()
        assert current_state == baseline_snapshot
