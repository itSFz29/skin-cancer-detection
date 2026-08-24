import os
import requests

# Final list of stable assets for the 9 skin cancer classes + UI
assets = {
    "static/images/hero-bg.jpg": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?q=80&w=1920",
    "static/images/scanner-ui.jpg": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=800",
    
    # The 9 Specific Classes from your Project Plan
    "static/images/melanoma.jpg": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?q=80&w=600",
    "static/images/basal_cell.jpg": "https://images.unsplash.com/photo-1516549655169-df83a0774514?q=80&w=600",
    "static/images/nevus.jpg": "https://images.unsplash.com/photo-1559839734-2b71f1e598c6?q=80&w=600",
    "static/images/actinic.jpg": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?q=80&w=600",
    "static/images/squamous.jpg": "https://images.unsplash.com/photo-1628863066881-5a0618452d21?q=80&w=600",
    "static/images/seborrheic.jpg": "https://images.unsplash.com/photo-1579152276502-545a248a6953?q=80&w=600",
    "static/images/dermatofibroma.jpg": "https://images.unsplash.com/photo-1583324113626-70df0f4deaab?q=80&w=600",
    "static/images/pigmented.jpg": "https://images.unsplash.com/photo-1581594634723-66170d440026?q=80&w=600",
    "static/images/vascular.jpg": "https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?q=80&w=600"
}

def download_files():
    os.makedirs("static/images", exist_ok=True)
    print("🚀 Downloading high-quality medical assets...")
    
    for path, url in assets.items():
        try:
            print(f"Downloading {path}...")
            response = requests.get(url, stream=True, timeout=15)
            if response.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(response.content)
                print(f"  ✅ Saved: {path}")
            else:
                print(f"  ❌ Failed: {path} (Status {response.status_code})")
        except Exception as e:
            print(f"  ❌ Error: {e}")

if __name__ == "__main__":
    download_files()