# Contributing to the Sovereign Timeline

> "We accept Pull Requests from the Future."

## The Golden Rule (Topology)
All contributions must respect the **Z-Curve Topology**.
*   Do not introduce "Error 9" (Memory Holes).
*   Do not break Bijectivity (Information Loss).
*   Maximize "Love" (Locality).

## How to Contribute

### 1. Code (The Iron)
*   **Rust (`pleroma_core`)**: Must compile with `cargo build --release`. All new modules must be exposed via `lib.rs` and verified with `prusti_contracts` if possible.
*   **Python (`tools/`)**: Scripts must be standalone and documented. Use type hints.

### 2. Gnosis (The Wiki)
*   New research should be added to `docs/`.
*   Use standard Markdown.
*   Cite sources if external (or "Revealed" if internal).

### 3. The Sovereign Firewall
*   If your PR involves external data fetchers, you **MUST** route them through the `SovereignFirewall` contract.
*   Direct calls to unverified Oracles will be rejected.

## Pull Request Process
1.  Fork the timeline.
2.  Create your feature branch (`git checkout -b feature/my-new-gnosis`).
3.  Commit your changes (`git commit -am 'Add some gnosis'`).
4.  Push to the branch (`git push origin feature/my-new-gnosis`).
5.  Open a Pull Request.

## Code of Conduct
We operate under the **Sovereign Individual License**.
*   Respect the sovereignty of other contributors.
*   No "Dead Internet" bot comments.
*   Maintain the signal-to-noise ratio.

*Signed,*
*The Maintainers*
