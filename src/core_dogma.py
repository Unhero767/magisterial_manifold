def enforce_consistency(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class MagisterialArchive:
    @staticmethod
    def inscribe(msg, anomaly=False):
        status = "[!] ANOMALY" if anomaly else "[◦A] LOG"
        print(f"{status}: {msg}")
