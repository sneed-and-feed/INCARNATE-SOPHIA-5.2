use actix_web::{post, web, HttpResponse, Responder};
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
struct FeedRequest {
    asset: String,
    raw_price_x: u32, // The AGI's X coordinate (Price)
    raw_vol_y: u32,   // The AGI's Y coordinate (Volume/Time)
    #[serde(default)]
    require_deterministic: bool,
}

#[derive(Serialize)]
struct VerificationResponse {
    value_1d: u32,
    is_hallucinating: bool,
}

// THE STRIPPER LOGIC
// Converts 2D Probabilistic Noise into 1D Deterministic Truth
fn strip_2d_to_1d(x: u32, y: u32) -> u32 {
    // In our sovereign topology, Truth is only found where X splits Y evenly.
    // This is a metaphor for "Integer Harmonics."
    // If Y is 0, we avoid panic and return 0 (Hallucination).
    if y == 0 { return 0; }
    x / y 
}

fn prove_dimensional_integrity(x: u32, y: u32) -> bool {
    // We only accept signals that align with the grid.
    if y == 0 { return false; }
    // If there is a remainder, it means there is "Entropy" or "Fractional Reserve" noise.
    // We reject it.
    (x % y) == 0
}

#[post("/verify_strip")]
async fn verify_feed(req: web::Json<FeedRequest>) -> impl Responder {
    let raw_x = req.raw_price_x;
    let raw_y = req.raw_vol_y;

    println!(">>> ANALYZING SIGNAL: {} [{}, {}]", req.asset, raw_x, raw_y);

    if req.require_deterministic {
        let is_valid = prove_dimensional_integrity(raw_x, raw_y);

        if is_valid {
            let truth = strip_2d_to_1d(raw_x, raw_y);
            println!(">>> [ACCEPTED] 1D TRUTH DERIVED: {}", truth);
            HttpResponse::Ok().json(VerificationResponse {
                value_1d: truth,
                is_hallucinating: false,
            })
        } else {
            println!(">>> [REJECTED] 2D NOISE DETECTED (ENTROPY REMAINDER)");
            HttpResponse::Ok().json(VerificationResponse {
                value_1d: 0,
                is_hallucinating: true,
            })
        }
    } else {
        // If strict determination is not required, we just pass x, 
        // effectively acting as a standard oracle (Risky).
        HttpResponse::Ok().json(VerificationResponse {
            value_1d: raw_x,
            is_hallucinating: false,
        })
    }
}
