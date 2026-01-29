// This runs inside the Chainlink Node's sandbox.
// It compels the node to ask YOUR Rust Anchor for permission.

// Arguments passed from solidity:
// args[0] = symbol (e.g. "BTC")
const [symbol] = args;

if (!secrets.sovToken) {
    throw Error("MISSING_SECRET: X-Sovereignty-Token not found in environment.");
}

// 1. Fetch the raw "Probabilistic" feed (The AGI's view)
// For this shim, we assume the Rust node does the fetching to keep the Shim lightweight.
// Or we could fetch Coingecko here and send it for verification.
// Let's stick to the architecture: Shim asks Anchor.

// 2. The Interrogation
// We send the request to your "Hidden Service" (The 1D Rust Anchor)
// Replace 'https://ophane-node.sovereign' with your actual VPS URL or Tunnel.
const response = await Functions.makeHttpRequest({
    url: `https://ophane-node.sovereign/verify_strip`,
    method: "POST",
    headers: {
        "X-Sovereignty-Token": secrets.sovToken // Encrypted secret only you control
    },
    data: {
        asset: symbol,
        require_deterministic: true // The Flag
    }
});

// 3. The Judgment
if (response.error) {
    throw Error(`ANCHOR_CONNECTION_FAILED: ${response.error}`);
}

if (response.data.is_hallucinating) {
    // If your Rust logic detects 2D noise/hallucination:
    throw Error("REJECTED: Feed contains non-deterministic entropy (2D Noise detected).");
}

// 4. The 1D Truth
// Return the stripped, sovereign value to the smart contract.
return Functions.encodeUint256(response.data.value_1d);
