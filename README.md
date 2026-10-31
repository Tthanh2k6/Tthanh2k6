# Trung Thanh Tran — B2B Data Extraction, Workflow Automation & Systems Engineer

**Deterministic async Python scrapers (`< 50 MB RAM`), anti-bot hidden-API pipelines, `MCP` tool servers, and failure-isolated `n8n` / `FastAPI` / `ERP` automations shipped in 24–72 hours.**

- **Availability:** Open for **1-Week Paid Trial Sprints**, **24–48h Custom Data/Automation Builds**, and **White-Label Agency Overflow** (`UTC+7` — overnight delivery for US/UK/EU teams; real-time overlap with AU/SG).
- **Direct Engineering Contact:** [ttrungthanh90@gmail.com](mailto:ttrungthanh90@gmail.com)
- **Live Architecture & Case Studies:** [trungthanhtran.vercel.app](https://trungthanhtran.vercel.app)
- **Zero-Fee Escrow Milestones:** [Upwork (`@trungthanhtrandev` — `$0` Freelancer Fee on Direct Contracts)](https://www.upwork.com/freelancers/trungthanhtrandev)
- **Published Cloud Microservices:** [Apify Store (`@thanh81646` — 6 Commercial Actors)](https://apify.com/thanh81646) · [Engineering Benchmarks (`dev.to/tthanh2k6`)](https://dev.to/tthanh2k6)

---

## Verified Production Benchmarks (Why B2B Teams Replace Fragile Bots With Deterministic Pipelines)

| Bottleneck in Typical Agency / Startup Stacks | Production Architecture Shipped | Measured Engineering Delta |
| :--- | :--- | :--- |
| **OOM Crashes & High Cloud Bills on Headless Scrapers** | Direct XHR / GraphQL / Next.js RSC & JSON-LD state interception in `Python 3.11` (`httpx.AsyncClient` + bounded `asyncio.Semaphore` + connection pooling), falling back to `Playwright` only for token minting | **`1,850 MB` Chromium cluster -> `24 MB` async container** (`51x` faster throughput; runs inside `$0.002/1k` serverless micro-containers) |
| **Broken LLM JSON & Silent Data Loss in `n8n` / `Make.com`** | Strict Pydantic v2 / OpenAI Structured Outputs (`strict: true`), idempotency keys, dead-letter queues, and completeness-gated catalog diffing (`is_complete` circuit breakers) | **`0.00%` schema drift** across multi-step CRM, ERP, Shopify, and webhook ingestion pipelines |
| **Expensive Clay / SaaS Credit Burn on Niche Verticals** | Custom Python / FastAPI enrichment sidecars joining federal registries (e.g., **CMS NPPES NPI v2.1**), DNS/MX checks, booking widget technographics, and corporate chain / DSO filters | **`85–95%` lower per-lead enrichment cost** with verified first-party signals unavailable in off-the-shelf databases |
| **E-Commerce, Webhook & Legacy Portal Sync Drift** | Stateful SKU price/inventory delta monitors, Stripe/Shopify/GHL idempotent webhook routers, Google Sheets / Apps Script V8 chunked batch runners, and PHP/Node/PostgreSQL backend rescue | **Zero duplicate CRM/ERP writes** and sub-minute anomaly alerting |

---

## 6 Commercial Cloud Actors in Production ([Apify Store — `@thanh81646`](https://apify.com/thanh81646))

Every engine below is containerized (`256 MB RAM`), whitelisted for **Agentic / MCP execution**, and inspectable on GitHub:

| # | Production System | Target Vertical & Output Schema | Live Cloud & Source |
| :-: | :--- | :--- | :--- |
| **01** | **B2B Domain Lead, Contact & Tech-Stack Enricher** | Async extraction of MX-verified emails, phones, social profiles, Schema.org entities, and MarTech stack (`HubSpot`, `Shopify`, `GHL`, `WordPress`) | [Apify Store](https://apify.com/thanh81646/apify-b2b-lead-and-contact-enricher) · [Source](https://github.com/Tthanh2k6/apify-b2b-lead-and-contact-enricher) · [RapidAPI](https://rapidapi.com/Tthanh2k6/api/b2b-website-email-phone-and-tech-stack-enricher) |
| **02** | **Shopify & WooCommerce Price, Variant Stock & JSON-LD Monitor** | Real-time SKU pricing, variant-level `in_stock` tracking, currency normalization, and structured Product JSON-LD delta extraction | [Apify Store](https://apify.com/thanh81646/apify-ecommerce-price-and-stock-monitor) · [Source](https://github.com/Tthanh2k6/apify-ecommerce-price-and-stock-monitor) · [RapidAPI](https://rapidapi.com/Tthanh2k6/api/shopify-and-woocommerce-price-and-stock-monitor) |
| **03** | **US Healthcare Clinic, Federal NPI & Stealth DSO Detector** | Enriches US dental, medical, audiology & vet clinics with **CMS NPPES NPI** records, PMS booking widgets (`NexHealth`, `LocalMed`, `Weave`), and PE-backed DSO exclusion flags | [Apify Store](https://apify.com/thanh81646/apify-us-healthcare-clinic-contact-enricher) · [Source](https://github.com/Tthanh2k6/apify-us-healthcare-clinic-contact-enricher) |
| **04** | **TheFork EU Restaurant & Reservation Stack Extractor** | Extracts European hospitality listings alongside reservation software footprints (`Formitable`, `Zenchef`, `Guestplan`, `Resengo`, `SevenRooms`) | [Apify Store](https://apify.com/thanh81646/thefork-restaurant-and-booking-system-scraper) · [Source](https://github.com/Tthanh2k6/apify-thefork-restaurant-scraper) |
| **05** | **Malaysia KPKT TEDUH Licensed Property Developer Scraper** | Direct government JSON API harvester extracting `6,500+` licensed developers and `27,000+` housing project APDL records | [Apify Store](https://apify.com/thanh81646/malaysia-kpkt-teduh-property-developer-scraper) · [Source](https://github.com/Tthanh2k6/apify-malaysia-kpkt-teduh-property-scraper) |
| **06** | **Multi-Stop Geocoder & Deterministic 2-Opt TSP Route Optimizer** | Batch OSM Nominatim geocoding, road-circuity Haversine matrices, shift time-window budgeting, and 1-click multi-stop Google Maps dispatch URLs | [Source](https://github.com/Tthanh2k6/apify-multi-stop-route-and-distance-optimizer) · [Benchmark Study](https://dev.to/tthanh2k6/engineering-sub-second-b2b-lead-enrichment-2-opt-route-optimization-pipelines-in-python-1le8) |

---

## Core Open-Source Reference Repositories & Commercial Systems

- **[`ai-automation-and-rag-toolkit`](https://github.com/Tthanh2k6/ai-automation-and-rag-toolkit):** Production `FastAPI` + `n8n` reference architecture featuring Hybrid `BM25` + Vector `RRF` citation-grounded RAG, strict OpenAI Structured Outputs, stream backpressure control, Google Apps Script route automation, and PostgreSQL RLS `pgTAP` security tests.
- **[`web-scraping-showcase`](https://github.com/Tthanh2k6/web-scraping-showcase):** Async `httpx` + `Playwright` extraction patterns, XHR/GraphQL API sniffer CLI, exponential backoff, and idempotent `CSV` / `XLSX` / `SQLite` persistence (`pytest` verified).
- **[`burgershop-pod-tool`](https://github.com/Tthanh2k6/burgershop-pod-tool):** Dual-world (`ISOLATED` + `MAIN` bridge) Manifest V3 Chrome Extension automating multi-step e-commerce catalog listings, virtual-scroll variant tables, and post-write verification on Angular admin portals.
- **Production E-Commerce & Loyalty Infrastructure (`Madalena`):** Architected and shipped a cross-platform customer loyalty system (`React Native / Expo` + `REST API` + `MySQL`, JWT auth, QR check-in, scheduled jobs, live on Google Play), migrated backend hosting to cut recurring cloud spend, and built multi-marketplace price lifecycle intelligence across `23,000+` listings/run.

---

## Technical Stack & Verified Credentials

- **Languages & Runtimes:** Python (`3.11+`, `asyncio`, `httpx`, `Pydantic`, `FastAPI`, `Playwright`, `selectolax`), TypeScript / Node.js, SQL (`PostgreSQL`, `Supabase`, `MySQL`, `SQLite`, `DuckDB`), PHP, Google Apps Script (`V8`).
- **Automation & AI Systems:** `n8n` (self-hosted queue hardening & custom webhook nodes), `Make.com`, `Clay` HTTP enrichment sidecars, `MCP` (`Model Context Protocol`) servers, OpenAI / Anthropic Structured Outputs, Hybrid RAG.
- **6x Verified HackerRank Engineering Certifications:**
  `Software Engineer (3e14323f3998)` · `REST API Intermediate (0950402ec1b3)` · `SQL Advanced (f6214fbc9a7f)` · `Node.js Intermediate (aea6444671ab)` · `JavaScript Intermediate (73f0cc9845c4)` · `Problem Solving Intermediate (34ee18911edf)`

---

## Start a 24–48h Custom Build or 1-Week Paid Trial Sprint

1. **Sample-First Proof (`< 24h`):** Send a target URL, API spec, or workflow bottleneck to **[ttrungthanh90@gmail.com](mailto:ttrungthanh90@gmail.com)**. I validate the target schema and return a clean 20–50 row sample (`.csv` / `.xlsx` / `.json`) or architectural teardown before you commit.
2. **Frictionless Global Settlement:** Available via **Upwork Direct Contract (`$0` Freelancer Fee + Escrow Protection)** at [upwork.com/freelancers/trungthanhtrandev](https://www.upwork.com/freelancers/trungthanhtrandev) or direct commercial invoice (`Wise` / international bank transfer).
3. **Full Portfolio & Printable A4 CV:** [trungthanhtran.vercel.app](https://trungthanhtran.vercel.app) · [trungthanhtran.vercel.app/cv](https://trungthanhtran.vercel.app/cv)
