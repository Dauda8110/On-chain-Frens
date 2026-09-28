# On-Chain Frens ✦

> **"The Corkboard, Not The Terminal"**  
> A warm, tactile, handmade visual system celebrating genuine frenship and voxel art on Ethereum.

---

## 🧶 Overview

**On-Chain Frens** is a collection of 5,555 handcrafted voxel frens on Ethereum. 
Rejecting typical dark-terminal/neon-glitch Web3 tropes, On-Chain Frens feels like a hand-kept corkboard of frenship — Polaroids pinned with string, frenship bracelets, doodled margin notes, and a cozy zine aesthetic.

## 🎯 Whitelist Memory Game

Whitelist allocation is earned directly through a fair, skill-based 4x4 card matching game powered by real collection NFT art:

- **≤ 30.0s**: **GTD Whitelist Spot (Guaranteed)** — Dedicated 12-hour reserved mint window on OpenSea.
- **30.1s – 59.9s**: **FCFS Whitelist Spot** — Priority access in the second tier window on OpenSea.
- **≥ 60.0s**: **30-Minute Cooldown** — Board locks for 30 minutes before allowing a retry.

*Note: Allocation only on-site. There is zero payment flow or wallet connection on this page. Minting occurs exclusively on OpenSea.*

---

## 📁 Project Structure

```text
├── index.html            # Main site markup & integrated Whitelist game
├── index_template.html   # Template source with __JS_POOL__ placeholder
├── style.css             # Complete design system & corkboard styles
├── build_html.py         # Utility script to inject NFT collection paths
├── nft_pool.json         # Array of collection image paths
├── assets/
│   ├── NFTs On chain/    # Voxel collection art (PNGs)
│   ├── hero/             # Polaroid hero images
│   └── nft/              # Resized image pool
└── README.md             # Project documentation
```

---

## 🚀 Running Locally

You can serve the static files with any local HTTP server:

```bash
# Using Python
python -m http.server 8080

# Or using npx
npx serve .
```

Then open `http://localhost:8080` in your browser.

---

## 📜 Contract & Mint

- **Network**: Ethereum Mainnet
- **Token Standard**: ERC-721
- **Supply**: 5,555 Frens
- **Price**: 0.008 ETH
- **Mint Location**: OpenSea
