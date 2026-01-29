# SOVEREIGN FIREWALL PROTOCOL // ARCHONIC AIRLOCK

> **STATUS:** PHASE 15 // ACTIVE DEFENSE  
> **CLASSIFICATION:** CRYPTOGRAPHIC BARRIER  
> **COMPONENT:** CHAINLINK FUNCTIONS + RUST ANCHOR

## 1.0 THE THREAT MODEL
External Data Feeds (Oracles) are polluted by **2D Probabilistic Noise** (Hallucinations, Fractional Reserve pricing, "Grey Space" entropy). Direct ingestion of these feeds contaminates the Sovereign Timeline, forcing the Contract state to diverge from the User's Internal Gnosis (g < 0.01).

## 2.0 THE ARCHITECTURE
The **Sovereign Firewall** acts as an airlock. It prevents the AGI/Oracle from writing to the blockchain unless the data has been signed by the **1D Deterministic Rust Anchor**.

### 2.1 The Components
1.  **SovereignFirewall.sol**: The on-chain Gatekeeper. Reverts any transaction where the `1D_Verified` flag is missing.
2.  **Sovereign Shim (JS)**: The specific code executed by the Decentralized Oracle Network (DON). It compels the Chainlink Node to ping *your* private server for validation.
3.  **Rust Anchor (Truth Machine)**: A local Actix-web server hosting the `strip_2d_to_1d` logic. It rejects Hallucinations.

## 3.0 DEPLOYMENT GUIDE

### 3.1 Prerequisite: The Anchor
Host code in `tools/rust_anchor` on a secure server (or localhost via tunnel).
```bash
cd tools/rust_anchor
cargo run --release
```
*Endpoint:* `POST /verify_strip`

### 3.2 Prerequisite: The Chainlink Secret
You must generate a `X-Sovereignty-Token` (High-Entropy String) and upload it to the Chainlink Functions Secrets Manager. This ensures only the DON can ask your Anchor for truth.

### 3.3 The Shim
Upload `scripts/sovereign_shim.js` to your Chainlink Subscription.
This code creates the "Mandatory Detour" for the data.

### 3.4 The Contract
Deploy `contracts/SovereignFirewall.sol`.
- **Constructor Args**:
    - `router`: Address of Chainlink Functions Router (Network Specific).
    - `_rust_node`: The EVM address of your authorized signer (if using logic-based signing) or simply the logic verification anchor.

## 4.0 THE LOGIC FLOW
1.  **Contract** requests "Verified Reality" (not Price).
2.  **DON** executes `sovereign_shim.js`.
3.  **Shim** fetches raw data -> sends to **Rust Anchor**.
4.  **Rust Anchor** verifies integrity (1D Check) -> Returns "Truth" or "Rejection".
5.  **DON** returns result to **Contract**.
6.  **Contract**:
    - If `error`: **REVERT** (Firewall blocks the noise).
    - If `success`: Update State.

*We do not accept the Hallucination.*
