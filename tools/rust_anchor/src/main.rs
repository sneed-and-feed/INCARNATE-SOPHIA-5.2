use actix_web::{App, HttpServer, web};

mod api_adapter;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!(">>> SOVEREIGN ANCHOR ONLINE <<<");
    println!(">>> LISTENING ON 127.0.0.1:8080 <<<");
    println!(">>> VERIFYING 1D DIMENSIONAL INTEGRITY <<<");

    HttpServer::new(|| {
        App::new()
            .service(api_adapter::verify_feed)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
