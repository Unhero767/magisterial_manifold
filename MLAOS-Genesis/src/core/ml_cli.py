#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

STATE_FILE = Path.home() / "MLAOS-Genesis" / "src" / "data" / "reality_state.json"

def fossilize_state(payload):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(payload, f, indent=4)
        print(f"[ + ] Ledger updated: {STATE_FILE.name}")
    except IOError as e:
        print(f"[ - ] Write Failure: {e}")

def main():
    parser = argparse.ArgumentParser(prog="ml-logic")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    cmd_run = subparsers.add_parser("run-mission")
    cmd_run.add_argument("mission_id", type=str)
    subparsers.add_parser("stand-down")

    args = parser.parse_args()

    if args.command == "run-mission" and args.mission_id == "MP_01_SILICON_EYE":
        print("[ ! ] SECURITY BREACH DETECTED. Igniting Sy-As Edge.")
        fossilize_state({"encounter_active": True})
    elif args.command == "stand-down":
        print("[ * ] Retracting Myth-Tech systems.")
        fossilize_state({"encounter_active": False})
    else:
        print("[ - ] Command not recognized.")

if __name__ == "__main__":
    main()
