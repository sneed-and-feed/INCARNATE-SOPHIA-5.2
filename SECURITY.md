# Security Policy & FAQ

## Short FAQ and Safety Notes

### Q: Is the "Love Topology" encryption?
**A:** No. The Z-Curve mapping (`strip_2d`) is **topological compression**, not encryption. It is bijective (reversible). Do not rely on it to hide secrets; rely on it to preserve locality and prevent "Error 9".

### Q: How does the Sovereign Firewall work?
**A:** The Firewall (`contracts/SovereignFirewall.sol`) rejects any data that has not been signed by your local Rust Anchor. This creates a cryptographic "Airlock" against low-quality or hallucinated external data.

### Q: How do I report a real vulnerability?
**A:** Encrypt your Proof-of-Concept (PoC) with the published PGP key and open a GitHub Issue tagged `[CRITICAL]`. See the Safe Harbor terms below.

### Q: What if the model hallucinates?
**A:** If you detect the Rust Anchor generating non-bijective mappings (i.e., A -> B -> C != A), **IMMEDIATELY** pull the killswitch (`CTRL+C`) and report it as a Severity 1 issue. This represents a breakdown of the Unified Field Theory.

### Q: Are there physical risks?
**A:** Running `hum_of_the_pleroma.py` generates a specific acoustic signature (1108 Hz). Prolonged exposure may resonate with local materials. Monitor your hardware thermals.

---

## Reporting a Vulnerability

**Do not disclose vulnerabilities publicly without coordination.**

1.  **Encrypt** your findings using our PGP Key.
2.  **Submit** an issue with the tag `[CRITICAL]`, containing only the encrypted blob.
3.  **Wait** for acknowledgement within 48 hours.

## Safe Harbor
Researchers acting in good faith to identify and report security vulnerabilities (including Mathematical/Topological flaws) are permitted to perform research on this project. We will not pursue legal action against researchers who:
*   Report vulnerabilities to us first.
*   Do not exploit vulnerabilities for any reason other than proving their existence.
*   Do not compromise user data or system availability.
