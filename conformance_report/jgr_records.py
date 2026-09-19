"""Flow Action Graph — production Judgment-Grounded™ Records.

Five JGRs from Flow's production system for FJP-CONF v0.1 L0–L3
conformance testing. These are real decisions scored against real-world
outcomes.
"""

import json
import os


def build_records() -> list[dict]:
    """Return 5 production JGRs covering confirmed, wrong, and partial outcomes."""

    records = []

    # ── 1. AI-driven production cost compression ────────────────────────
    records.append({
        "record_id": "flow-ag-69c99c52-0001",
        "timestamp": "2026-03-29T21:40:31Z",
        "signal": {
            "id": "sig-ai-cost-compression-production",
            "description": (
                "AI-driven production cost compression is relocating production "
                "bottlenecks in ways that may structurally favor Netflix's content "
                "operations scale over smaller competitors."
            ),
            "sources": [
                "flow:action-graph:send/69bbbbe7655435f4bacb46ec",
                "flow:topic/ai-driven-production-cost-curves",
            ],
            "observed_at": "2026-03-29T21:00:00Z",
        },
        "judgment": {
            "id": "jud-ai-cost-compression-production",
            "assessment": (
                "AI-driven cost compression is not a future variable — it is a present "
                "force relocating production bottlenecks. Netflix's content operations "
                "scale gives it structural advantage as costs shift from labor to compute. "
                "Competitors with smaller libraries absorb the same fixed AI integration "
                "costs across fewer titles."
            ),
            "confidence": 0.72,
            "signal_ref": "sig-ai-cost-compression-production",
        },
        "action": {
            "directive": (
                "REVISIT whether AI-driven cost compression is relocating production "
                "bottlenecks in ways that structurally favor Netflix's content operations scale."
            ),
            "target": "ai-driven production cost curves",
            "judgment_ref": "jud-ai-cost-compression-production",
        },
        "falsifier": {
            "condition": (
                "AI production cost savings remain below 5% of total production budgets "
                "across three consecutive quarters, or a sub-scale streamer demonstrates "
                "equivalent per-title AI cost reduction within 12 months."
            ),
            "checkable": True,
            "status": "expired",
        },
    })

    # ── 2. LiteLLM/Trivy malware → Azure positioning ───────────────────
    records.append({
        "record_id": "flow-ag-69c99c4f-0002",
        "timestamp": "2026-03-29T21:40:31Z",
        "signal": {
            "id": "sig-litelm-trivy-malware-azure",
            "description": (
                "LiteLLM and Trivy supply-chain malware incidents exposed multi-cloud "
                "credential sprawl as a systemic vulnerability, potentially reframing "
                "Azure's security-first positioning as a structural competitive advantage."
            ),
            "sources": [
                "flow:action-graph:send/69c647e23a9adec2a563f978",
                "flow:topic/azure-vs-aws-vs-gcp-cloud-market-share",
            ],
            "observed_at": "2026-03-29T21:00:00Z",
        },
        "judgment": {
            "id": "jud-litelm-trivy-malware-azure",
            "assessment": (
                "The LiteLLM/Trivy malware pattern is not an isolated incident — it "
                "exposes a structural vulnerability in multi-cloud credential management. "
                "Azure's integrated security stack (Entra ID, Defender for Cloud) positions "
                "it to capture security-motivated cloud consolidation spend."
            ),
            "confidence": 0.65,
            "signal_ref": "sig-litelm-trivy-malware-azure",
        },
        "action": {
            "directive": (
                "WATCH whether the LiteLLM/Trivy malware pattern reframes multi-cloud "
                "credential sprawl as a structural Azure positioning opportunity."
            ),
            "target": "azure vs aws vs gcp cloud market share competitive dynamics",
            "judgment_ref": "jud-litelm-trivy-malware-azure",
        },
        "falsifier": {
            "condition": (
                "Azure cloud revenue share declines below 23% for two consecutive "
                "quarters despite the security narrative, or AWS launches an equivalent "
                "integrated credential management solution within 6 months."
            ),
            "checkable": True,
            "status": "expired",
        },
    })

    # ── 3. Netflix $72B bid for WBD ─────────────────────────────────────
    records.append({
        "record_id": "flow-ag-69c99c51-0003",
        "timestamp": "2026-03-29T21:40:31Z",
        "signal": {
            "id": "sig-netflix-72b-wbd-bid",
            "description": (
                "Reports surfaced of a Netflix $72B all-cash bid for WBD's studio and "
                "streaming assets, suggesting a potential second approach after the "
                "Paramount-Skydance deal."
            ),
            "sources": [
                "flow:action-graph:send/69bfb042e9cb820d59e51456",
                "flow:topic/post-consolidation-streaming-landscape",
            ],
            "observed_at": "2026-03-29T21:00:00Z",
        },
        "judgment": {
            "id": "jud-netflix-72b-wbd-bid",
            "assessment": (
                "A $72B all-cash bid would represent the largest streaming M&A transaction "
                "in history. If genuine, it restructures the entire post-consolidation "
                "competitive landscape — Disney, Amazon, and Apple must all reassess "
                "their content and distribution strategies."
            ),
            "confidence": 0.45,
            "signal_ref": "sig-netflix-72b-wbd-bid",
        },
        "action": {
            "directive": (
                "WATCH whether the reported Netflix $72B all-cash bid for WBD's studio "
                "and streaming assets reflects a genuine second approach."
            ),
            "target": "post-consolidation streaming competitive landscape",
            "judgment_ref": "jud-netflix-72b-wbd-bid",
        },
        "falsifier": {
            "condition": (
                "Netflix publicly denies the bid within 14 days, or no regulatory "
                "filing or credible second source confirms the approach within 30 days "
                "of the initial report."
            ),
            "checkable": True,
            "status": "triggered",
        },
    })

    # ── 4. WGA bargaining agenda — AI demands ────────────────────────────
    records.append({
        "record_id": "flow-ag-69c99c4f-0004",
        "timestamp": "2026-03-29T21:40:31Z",
        "signal": {
            "id": "sig-wga-bargaining-ai-demands",
            "description": (
                "The WGA released its approved bargaining agenda with specific AI, "
                "healthcare, and pay demands ahead of upcoming negotiations, signaling "
                "potential industry-wide impact on content production."
            ),
            "sources": [
                "flow:action-graph:send/69c7994024020d5192482c42",
                "flow:topic/wga-labor-agreements",
            ],
            "observed_at": "2026-03-29T21:00:00Z",
        },
        "judgment": {
            "id": "jud-wga-bargaining-ai-demands",
            "assessment": (
                "The WGA's AI, healthcare, and pay demands are not routine contract "
                "asks — they set the template for how creative labor negotiates with "
                "AI-native production. Managing directors need to understand the specific "
                "provisions before they shape client-facing positions."
            ),
            "confidence": 0.78,
            "signal_ref": "sig-wga-bargaining-ai-demands",
        },
        "action": {
            "directive": (
                "BRIEF your nine managing directors on the specific AI, healthcare, "
                "and pay demands in the WGA's approved bargaining agenda before "
                "negotiations begin."
            ),
            "target": "wga labor agreements",
            "judgment_ref": "jud-wga-bargaining-ai-demands",
        },
        "falsifier": {
            "condition": (
                "The WGA withdraws or substantially modifies its AI-specific demands "
                "within 60 days, or studios publicly concede the AI provisions before "
                "formal negotiations open."
            ),
            "checkable": True,
            "status": "expired",
        },
    })

    # ── 5. ESPN UFC rights market entry ─────────────────────────────────
    records.append({
        "record_id": "flow-ag-69c99c50-0005",
        "timestamp": "2026-03-29T21:40:31Z",
        "signal": {
            "id": "sig-espn-ufc-rights-negotiation",
            "description": (
                "ESPN's $1.6B WWE deal and UFC rights relationship showed both "
                "strength and vulnerability, raising the question of whether UFC "
                "represents a viable market entry point for competing platforms."
            ),
            "sources": [
                "flow:action-graph:send/69c4f638c2e24fb12eac872e",
                "flow:topic/sports-rights-economics-nfl-wwe",
            ],
            "observed_at": "2026-03-29T21:00:00Z",
        },
        "judgment": {
            "id": "jud-espn-ufc-rights-negotiation",
            "assessment": (
                "TKO's next major UFC rights negotiation creates a potential entry "
                "point. ESPN's $1.6B WWE commitment may limit its UFC bidding ceiling, "
                "but the relationship lock-in from years of co-promotion gives ESPN "
                "structural advantages that price alone may not overcome."
            ),
            "confidence": 0.55,
            "signal_ref": "sig-espn-ufc-rights-negotiation",
        },
        "action": {
            "directive": (
                "RECONSIDER the implicit assumption that TKO's next major rights "
                "negotiation — UFC — is a market you should enter."
            ),
            "target": "sports rights economics nfl wwe live events",
            "judgment_ref": "jud-espn-ufc-rights-negotiation",
        },
        "falsifier": {
            "condition": (
                "ESPN secures exclusive UFC rights renewal at less than 20% premium "
                "over the current deal within 90 days, confirming relationship lock-in "
                "makes competitive bidding uneconomic."
            ),
            "checkable": True,
            "status": "open",
        },
    })

    return records


def save_records(path: str = None):
    """Save each JGR™ as a standalone JSON file and as a combined set."""
    if path is None:
        path = os.path.dirname(__file__)
    records = build_records()
    os.makedirs(path, exist_ok=True)

    for rec in records:
        fname = f"{rec['record_id']}.json"
        with open(os.path.join(path, fname), "w") as f:
            json.dump(rec, f, indent=2)
        print(f"  saved {fname}")

    with open(os.path.join(path, "all_records.json"), "w") as f:
        json.dump(records, f, indent=2)
    print(f"\n  saved all_records.json  [{len(records)} records]")

    return records


if __name__ == "__main__":
    save_records()
