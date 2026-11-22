class QuantileTracker:
    def __init__(self): self.samples = []
    def observe(self, ms): self.samples.append(ms)
    def quantile(self, q):
        s = sorted(self.samples)
        idx = min(len(s)-1, int(q * len(s)))
        return s[idx]

if __name__ == "__main__":
    qt = QuantileTracker()
    for x in range(1, 101): qt.observe(x)
    assert qt.quantile(0.50) == 51 and qt.quantile(0.99) == 100
    print("[PASS] 030_tdigest_quantiles")
