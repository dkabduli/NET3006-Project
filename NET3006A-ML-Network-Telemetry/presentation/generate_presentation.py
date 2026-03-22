#!/usr/bin/env python3
"""
Generate NET3006A Project Presentation — ML for Network Telemetry
Team: Abdul Rehman, Esam Mukbil, Hashim Kshim
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

# ── colour palette ──────────────────────────────────────────────
DARK_BG       = RGBColor(0x1B, 0x1F, 0x3B)   # deep navy
ACCENT_BLUE   = RGBColor(0x00, 0x9F, 0xFD)   # bright cyan-blue
ACCENT_TEAL   = RGBColor(0x00, 0xC9, 0xA7)   # teal green
ACCENT_PURPLE = RGBColor(0x84, 0x5E, 0xC2)   # soft purple
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY    = RGBColor(0xCC, 0xCC, 0xCC)
MID_GRAY      = RGBColor(0x99, 0x99, 0x99)
SECTION_BG    = RGBColor(0x0F, 0x14, 0x2E)   # slightly darker navy
TABLE_HEADER  = RGBColor(0x00, 0x7A, 0xC1)
TABLE_ROW_ALT = RGBColor(0x16, 0x1A, 0x35)
ORANGE        = RGBColor(0xFF, 0x8C, 0x00)

SLIDE_WIDTH  = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_WIDTH
prs.slide_height = SLIDE_HEIGHT


# ── helper functions ────────────────────────────────────────────
def add_bg(slide, color=DARK_BG):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_accent_bar(slide, left=0, top=0, width=Inches(0.15), height=None, color=ACCENT_BLUE):
    if height is None:
        height = SLIDE_HEIGHT
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_bottom_bar(slide, color=ACCENT_BLUE, height=Inches(0.08)):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, SLIDE_HEIGHT - height, SLIDE_WIDTH, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_textbox(slide, left, top, width, height, text, font_size=18,
                color=WHITE, bold=False, alignment=PP_ALIGN.LEFT,
                font_name='Calibri', line_spacing=1.2):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    p.space_after = Pt(0)
    if line_spacing != 1.0:
        p.line_spacing = Pt(font_size * line_spacing)
    return txBox


def add_bullet_slide_content(tf, bullets, font_size=18, color=WHITE, bold=False,
                              indent_level=0, font_name='Calibri', spacing=6):
    for i, bullet in enumerate(bullets):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = bullet
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.bold = bold
        p.font.name = font_name
        p.level = indent_level
        p.space_after = Pt(spacing)
        p.space_before = Pt(2)


def add_presenter_tag(slide, name, color=ACCENT_BLUE):
    add_textbox(slide, Inches(10.2), Inches(6.85), Inches(3), Inches(0.5),
                f"Presenter: {name}", font_size=12, color=color,
                bold=True, alignment=PP_ALIGN.RIGHT)


def add_slide_number(slide, num, total):
    add_textbox(slide, Inches(0.4), Inches(6.9), Inches(1.5), Inches(0.4),
                f"{num} / {total}", font_size=10, color=MID_GRAY,
                alignment=PP_ALIGN.LEFT)


def add_section_header(slide, section_title, color=ACCENT_BLUE):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(2.8), SLIDE_WIDTH, Inches(1.8)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0x10, 0x15, 0x30)
    shape.line.fill.background()
    add_textbox(slide, Inches(1), Inches(3.0), Inches(11), Inches(1.4),
                section_title, font_size=40, color=color, bold=True,
                alignment=PP_ALIGN.CENTER, font_name='Calibri')


def make_title_subtitle(slide, title, subtitle, presenter,
                         title_size=36, subtitle_size=18,
                         title_color=WHITE, subtitle_color=LIGHT_GRAY):
    add_textbox(slide, Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.7),
                title, font_size=title_size, color=title_color,
                bold=True, font_name='Calibri')
    if subtitle:
        add_textbox(slide, Inches(0.8), Inches(1.05), Inches(11.5), Inches(0.45),
                    subtitle, font_size=subtitle_size, color=subtitle_color,
                    font_name='Calibri')
    add_presenter_tag(slide, presenter)


TOTAL_SLIDES = 20


# ═══════════════════════════════════════════════════════════════
# SLIDE 1 — Title Slide
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
add_bg(slide)
add_accent_bar(slide, left=0, top=0, width=SLIDE_WIDTH, height=Inches(0.1), color=ACCENT_BLUE)
add_bottom_bar(slide, color=ACCENT_TEAL)

add_textbox(slide, Inches(1.5), Inches(1.2), Inches(10.3), Inches(1.2),
            "Machine Learning for Network Telemetry",
            font_size=44, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
add_textbox(slide, Inches(1.5), Inches(2.5), Inches(10.3), Inches(0.7),
            "A Survey of Methods, Applications, and Emerging Trends",
            font_size=24, color=ACCENT_BLUE, alignment=PP_ALIGN.CENTER)

# decorative line
shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
    Inches(4.5), Inches(3.3), Inches(4.3), Inches(0.04))
shape.fill.solid()
shape.fill.fore_color.rgb = ACCENT_TEAL
shape.line.fill.background()

add_textbox(slide, Inches(1.5), Inches(3.8), Inches(10.3), Inches(0.5),
            "NET3006A — Network Management and Machine Learning",
            font_size=18, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)
add_textbox(slide, Inches(1.5), Inches(4.3), Inches(10.3), Inches(0.5),
            "Carleton University  |  Winter 2026  |  Dr. Jie Gao",
            font_size=16, color=MID_GRAY, alignment=PP_ALIGN.CENTER)

add_textbox(slide, Inches(1.5), Inches(5.3), Inches(10.3), Inches(0.5),
            "Abdul Rehman    |    Esam Mukbil    |    Hashim Kshim",
            font_size=20, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
add_textbox(slide, Inches(1.5), Inches(5.85), Inches(10.3), Inches(0.4),
            "Option 1: Survey / Reading Project  —  Topic 2",
            font_size=14, color=MID_GRAY, alignment=PP_ALIGN.CENTER)

add_slide_number(slide, 1, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 2 — Agenda / Outline
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Presentation Outline", None, "Abdul Rehman")

items = [
    ("1.", "Introduction & Motivation", "Abdul Rehman"),
    ("2.", "What is Network Telemetry?", "Abdul Rehman"),
    ("3.", "Why ML for Network Telemetry?", "Abdul Rehman"),
    ("4.", "ML Methods for Anomaly Detection", "Abdul Rehman"),
    ("5.", "Anomaly Detection: Key Findings", "Abdul Rehman"),
    ("6.", "ML for Performance Prediction", "Esam Mukbil"),
    ("7.", "ML for QoS Optimization", "Esam Mukbil"),
    ("8.", "Performance & QoS: Key Findings", "Esam Mukbil"),
    ("9.", "Telemetry Data Pipeline & Architecture", "Esam Mukbil"),
    ("10.", "Industry: Nokia's Telemetry Solutions", "Hashim Kshim"),
    ("11.", "Industry: Ericsson's AI-Driven Telemetry", "Hashim Kshim"),
    ("12.", "Emerging Trends: 6G & GenAI for Telemetry", "Hashim Kshim"),
    ("13.", "Open Challenges & Future Directions", "Hashim Kshim"),
    ("14.", "Conclusion & Key Takeaways", "Hashim Kshim"),
]

start_y = Inches(1.6)
for i, (num, title, presenter) in enumerate(items):
    y = start_y + Inches(i * 0.38)
    c = ACCENT_BLUE if "Abdul" in presenter else (ACCENT_TEAL if "Esam" in presenter else ACCENT_PURPLE)
    add_textbox(slide, Inches(1.2), y, Inches(0.6), Inches(0.35),
                num, font_size=14, color=c, bold=True)
    add_textbox(slide, Inches(1.8), y, Inches(6), Inches(0.35),
                title, font_size=14, color=WHITE)
    add_textbox(slide, Inches(9.0), y, Inches(3.5), Inches(0.35),
                presenter, font_size=12, color=c, alignment=PP_ALIGN.RIGHT)

# legend
for j, (name, clr) in enumerate([
    ("Abdul Rehman", ACCENT_BLUE), ("Esam Mukbil", ACCENT_TEAL), ("Hashim Kshim", ACCENT_PURPLE)
]):
    dot = slide.shapes.add_shape(MSO_SHAPE.OVAL,
        Inches(1.2) + Inches(j * 3.5), Inches(7.05), Inches(0.15), Inches(0.15))
    dot.fill.solid()
    dot.fill.fore_color.rgb = clr
    dot.line.fill.background()
    add_textbox(slide, Inches(1.45) + Inches(j * 3.5), Inches(6.95),
                Inches(2.5), Inches(0.35), name, font_size=11, color=clr)

add_slide_number(slide, 2, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 3 — Section Divider: Abdul Rehman
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, SECTION_BG)
add_bottom_bar(slide, color=ACCENT_BLUE)

add_textbox(slide, Inches(1), Inches(1.5), Inches(11), Inches(0.5),
            "PART 1", font_size=16, color=ACCENT_BLUE, bold=True,
            alignment=PP_ALIGN.CENTER, font_name='Calibri')
add_section_header(slide, "Introduction & ML for Anomaly Detection", ACCENT_BLUE)
add_textbox(slide, Inches(1), Inches(5.0), Inches(11), Inches(0.5),
            "Presenter: Abdul Rehman", font_size=20, color=WHITE,
            alignment=PP_ALIGN.CENTER)
add_slide_number(slide, 3, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 4 — What is Network Telemetry?
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_BLUE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "What is Network Telemetry?",
                    "Real-time, automated collection and streaming of network data",
                    "Abdul Rehman")

txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(6.0), Inches(4.8))
tf = txBox.text_frame
tf.word_wrap = True
bullets = [
    "Network telemetry = automated, real-time collection of operational data from network devices and infrastructure",
    "Data sources include flow statistics, packet traces, SNMP counters, syslog, and in-band network telemetry (INT)",
    "Evolved from traditional polling-based monitoring (SNMP) to push-based streaming models",
    "Enables fine-grained visibility into network state: latency, jitter, packet loss, throughput, error rates",
    "Foundation for closed-loop network automation — observe, orient, decide, act",
    "Critical for modern networks: 5G, SDN/NFV, cloud-native, and multi-domain environments",
]
add_bullet_slide_content(tf, bullets, font_size=16, color=WHITE, spacing=8)

# right-side info box
box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(7.4), Inches(1.7), Inches(5.4), Inches(4.5))
box.fill.solid()
box.fill.fore_color.rgb = RGBColor(0x14, 0x18, 0x32)
box.line.color.rgb = ACCENT_BLUE
box.line.width = Pt(1.5)

add_textbox(slide, Inches(7.7), Inches(1.9), Inches(4.8), Inches(0.5),
            "Key Telemetry Data Types", font_size=16, color=ACCENT_BLUE, bold=True)
types_box = slide.shapes.add_textbox(Inches(7.7), Inches(2.5), Inches(4.8), Inches(3.5))
tf2 = types_box.text_frame
tf2.word_wrap = True
type_bullets = [
    "Flow Statistics — NetFlow/IPFIX records of traffic flows",
    "Packet Traces — Full or sampled packet captures",
    "In-Band Telemetry (INT) — Hop-by-hop metadata embedded in packets",
    "Device Metrics — CPU, memory, interface counters via gNMI/gRPC",
    "Network Logs — Syslog, event logs, configuration changes",
]
add_bullet_slide_content(tf2, type_bullets, font_size=13, color=LIGHT_GRAY, spacing=6)

add_presenter_tag(slide, "Abdul Rehman")
add_slide_number(slide, 4, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 5 — Why ML for Network Telemetry?
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_BLUE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Why Apply ML to Network Telemetry?",
                    "The volume and complexity of telemetry data demands intelligent analysis",
                    "Abdul Rehman")

challenges = [
    ("Volume & Velocity", "Modern networks generate terabytes of telemetry daily; manual analysis is infeasible"),
    ("Complex Patterns", "Anomalies and performance degradation involve subtle, multi-dimensional correlations"),
    ("Real-Time Demands", "Network operators need sub-second detection and response times"),
    ("Dynamic Environments", "Traffic patterns, topologies, and workloads constantly evolve — static rules fail"),
    ("Automation Gap", "5G/6G and SDN require autonomous, closed-loop management at scale"),
]

for i, (title, desc) in enumerate(challenges):
    y = Inches(1.75) + Inches(i * 0.95)
    # accent dot
    dot = slide.shapes.add_shape(MSO_SHAPE.OVAL,
        Inches(0.9), y + Inches(0.08), Inches(0.18), Inches(0.18))
    dot.fill.solid()
    dot.fill.fore_color.rgb = ACCENT_BLUE
    dot.line.fill.background()
    add_textbox(slide, Inches(1.3), y, Inches(11), Inches(0.35),
                title, font_size=18, color=ACCENT_BLUE, bold=True)
    add_textbox(slide, Inches(1.3), y + Inches(0.35), Inches(11), Inches(0.45),
                desc, font_size=15, color=LIGHT_GRAY)

# right box: survey scope
box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(8.5), Inches(1.7), Inches(4.5), Inches(2.5))
box.fill.solid()
box.fill.fore_color.rgb = RGBColor(0x14, 0x18, 0x32)
box.line.color.rgb = ACCENT_TEAL
box.line.width = Pt(1.5)

add_textbox(slide, Inches(8.8), Inches(1.85), Inches(4.0), Inches(0.4),
            "Our Survey Scope", font_size=15, color=ACCENT_TEAL, bold=True)
scope_box = slide.shapes.add_textbox(Inches(8.8), Inches(2.35), Inches(4.0), Inches(1.7))
tf3 = scope_box.text_frame
tf3.word_wrap = True
scope_items = [
    "Anomaly detection in telemetry",
    "Performance prediction & QoS",
    "Industry implementations",
    "Emerging trends (6G, GenAI)",
]
add_bullet_slide_content(tf3, scope_items, font_size=13, color=LIGHT_GRAY, spacing=5)

add_presenter_tag(slide, "Abdul Rehman")
add_slide_number(slide, 5, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 6 — ML Methods for Anomaly Detection
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_BLUE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "ML Methods for Anomaly Detection in Telemetry",
                    "Detecting unusual patterns in network data streams",
                    "Abdul Rehman")

methods = [
    ("Autoencoders (AE)", "Unsupervised", "Learn normal traffic patterns; flag high-reconstruction-error samples as anomalies. Effective for zero-day attack detection."),
    ("LSTM / GRU Networks", "Deep Learning", "Capture temporal dependencies in time-series telemetry. Predict expected values; deviations signal anomalies."),
    ("Isolation Forest", "Unsupervised", "Tree-based method that isolates anomalies efficiently. Low computational cost, suitable for real-time streaming."),
    ("One-Class SVM", "Semi-supervised", "Learns a boundary around normal data. Effective when labeled anomaly data is scarce or unavailable."),
    ("GAN-based Detection", "Generative", "Generator learns normal distribution; discriminator detects out-of-distribution samples as anomalies."),
]

for i, (method, category, desc) in enumerate(methods):
    y = Inches(1.7) + Inches(i * 1.05)
    # category badge
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.8), y, Inches(1.6), Inches(0.32))
    badge.fill.solid()
    badge_colors = [ACCENT_BLUE, ACCENT_TEAL, ACCENT_BLUE, ACCENT_PURPLE, ORANGE]
    badge.fill.fore_color.rgb = badge_colors[i]
    badge.line.fill.background()
    add_textbox(slide, Inches(0.8), y + Inches(0.02), Inches(1.6), Inches(0.3),
                category, font_size=10, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
    add_textbox(slide, Inches(2.6), y, Inches(4.5), Inches(0.35),
                method, font_size=17, color=WHITE, bold=True)
    add_textbox(slide, Inches(2.6), y + Inches(0.35), Inches(10), Inches(0.55),
                desc, font_size=13, color=LIGHT_GRAY)

add_presenter_tag(slide, "Abdul Rehman")
add_slide_number(slide, 6, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 7 — Anomaly Detection: Key Findings
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_BLUE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Anomaly Detection: Key Findings from the Literature",
                    "Patterns and insights across surveyed papers",
                    "Abdul Rehman")

findings = [
    "Deep learning methods (LSTM, Autoencoders) consistently outperform traditional statistical approaches for multi-variate telemetry anomaly detection",
    "Unsupervised methods are favored in practice — labeled anomaly data is extremely scarce in real network environments",
    "Hybrid approaches (e.g., Autoencoder + Isolation Forest) combine strengths: representation learning with efficient anomaly scoring",
    "Real-time detection remains challenging: most deep learning models require significant computational resources for inference at line-rate",
    "Transfer learning shows promise for generalizing anomaly detection across different network domains without full retraining",
    "In-band telemetry (INT) provides richer features than traditional flow data, improving detection accuracy by 15–25% in recent studies",
]

txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.5), Inches(5.0))
tf = txBox.text_frame
tf.word_wrap = True

for i, finding in enumerate(findings):
    if i == 0:
        p = tf.paragraphs[0]
    else:
        p = tf.add_paragraph()
    p.text = finding
    p.font.size = Pt(16)
    p.font.color.rgb = WHITE
    p.font.name = 'Calibri'
    p.space_after = Pt(12)
    p.space_before = Pt(4)

# highlight box
box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(8.2), Inches(5.0), Inches(4.8), Inches(1.5))
box.fill.solid()
box.fill.fore_color.rgb = RGBColor(0x14, 0x18, 0x32)
box.line.color.rgb = ACCENT_BLUE
box.line.width = Pt(1.5)
add_textbox(slide, Inches(8.5), Inches(5.15), Inches(4.2), Inches(0.4),
            "Key Takeaway", font_size=14, color=ACCENT_BLUE, bold=True)
add_textbox(slide, Inches(8.5), Inches(5.55), Inches(4.2), Inches(0.8),
            "Unsupervised deep learning is the dominant paradigm — driven by the scarcity of labeled anomaly data in production networks.",
            font_size=12, color=LIGHT_GRAY)

add_presenter_tag(slide, "Abdul Rehman")
add_slide_number(slide, 7, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 8 — Section Divider: Esam Mukbil
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, SECTION_BG)
add_bottom_bar(slide, color=ACCENT_TEAL)

add_textbox(slide, Inches(1), Inches(1.5), Inches(11), Inches(0.5),
            "PART 2", font_size=16, color=ACCENT_TEAL, bold=True,
            alignment=PP_ALIGN.CENTER)
add_section_header(slide, "ML for Performance Prediction & QoS", ACCENT_TEAL)
add_textbox(slide, Inches(1), Inches(5.0), Inches(11), Inches(0.5),
            "Presenter: Esam Mukbil", font_size=20, color=WHITE,
            alignment=PP_ALIGN.CENTER)
add_slide_number(slide, 8, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 9 — ML for Performance Prediction
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_TEAL)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "ML for Network Performance Prediction",
                    "Forecasting delay, jitter, packet loss, and throughput from telemetry data",
                    "Esam Mukbil")

items_left = [
    ("Time-Series Forecasting", [
        "LSTM and GRU networks model temporal dependencies in traffic metrics",
        "Predict future values of delay, jitter, and throughput",
        "Sliding-window approaches on streaming telemetry data",
    ]),
    ("Graph Neural Networks (GNNs)", [
        "Model network topology as a graph — nodes = devices, edges = links",
        "RouteNet-Fermi: GNN architecture for per-flow delay/jitter prediction",
        "Capture spatial correlations that time-series models miss",
    ]),
]

y_pos = Inches(1.7)
for title, bullets in items_left:
    add_textbox(slide, Inches(0.8), y_pos, Inches(5.8), Inches(0.4),
                title, font_size=18, color=ACCENT_TEAL, bold=True)
    y_pos += Inches(0.45)
    for b in bullets:
        add_textbox(slide, Inches(1.1), y_pos, Inches(5.5), Inches(0.4),
                    f"• {b}", font_size=14, color=LIGHT_GRAY)
        y_pos += Inches(0.35)
    y_pos += Inches(0.2)

# right column
items_right = [
    ("Ensemble & Hybrid Methods", [
        "Combine multiple models (e.g., LSTM + Random Forest) for robust predictions",
        "Stacking and boosting improve accuracy over single models",
        "Adaptive ensembles handle concept drift in network traffic",
    ]),
    ("Attention Mechanisms", [
        "Transformer-based models capture long-range dependencies",
        "Self-attention weights highlight which telemetry features matter most",
        "Emerging as state-of-the-art for multi-variate network forecasting",
    ]),
]

y_pos = Inches(1.7)
for title, bullets in items_right:
    add_textbox(slide, Inches(7.0), y_pos, Inches(5.8), Inches(0.4),
                title, font_size=18, color=ACCENT_TEAL, bold=True)
    y_pos += Inches(0.45)
    for b in bullets:
        add_textbox(slide, Inches(7.3), y_pos, Inches(5.5), Inches(0.4),
                    f"• {b}", font_size=14, color=LIGHT_GRAY)
        y_pos += Inches(0.35)
    y_pos += Inches(0.2)

add_presenter_tag(slide, "Esam Mukbil", ACCENT_TEAL)
add_slide_number(slide, 9, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 10 — ML for QoS Optimization
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_TEAL)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "ML for QoS Optimization",
                    "Using predicted telemetry to maintain service-level agreements",
                    "Esam Mukbil")

qos_methods = [
    ("Reinforcement Learning (RL)", "Agents learn optimal routing/scheduling policies by interacting with the network environment. DQN and PPO are widely used for real-time QoS-aware traffic engineering."),
    ("Deep Q-Networks (DQN)", "Map network state (telemetry features) to optimal actions (e.g., rerouting flows). Effective for dynamic bandwidth allocation and load balancing."),
    ("Multi-Objective Optimization", "Balance competing QoS metrics (latency vs. throughput vs. fairness) using Pareto-optimal ML solutions. Neural networks approximate the Pareto front."),
    ("Federated Learning", "Train QoS models across distributed network domains without sharing raw telemetry data. Preserves privacy while enabling cross-domain optimization."),
]

for i, (method, desc) in enumerate(qos_methods):
    y = Inches(1.7) + Inches(i * 1.3)
    # accent line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
        Inches(0.8), y, Inches(0.08), Inches(1.0))
    line.fill.solid()
    line.fill.fore_color.rgb = ACCENT_TEAL
    line.line.fill.background()
    add_textbox(slide, Inches(1.1), y, Inches(11.5), Inches(0.35),
                method, font_size=18, color=ACCENT_TEAL, bold=True)
    add_textbox(slide, Inches(1.1), y + Inches(0.38), Inches(11.5), Inches(0.7),
                desc, font_size=14, color=LIGHT_GRAY)

add_presenter_tag(slide, "Esam Mukbil", ACCENT_TEAL)
add_slide_number(slide, 10, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 11 — Performance & QoS Key Findings
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_TEAL)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Performance Prediction & QoS: Key Findings",
                    "Insights from recent academic and industry literature",
                    "Esam Mukbil")

findings = [
    ("GNNs > Time-Series for Topology-Aware Prediction",
     "Graph neural networks outperform pure time-series models when network topology matters — they capture how congestion propagates across paths and links."),
    ("RL for QoS Is Promising but Hard to Deploy",
     "Reinforcement learning achieves near-optimal QoS policies in simulation, but real-world deployment faces challenges: safety constraints, exploration risk, and training instability."),
    ("Data Quality Is the Bottleneck",
     "Prediction accuracy depends heavily on telemetry data quality. Missing values, sampling artifacts, and clock synchronization issues degrade model performance significantly."),
    ("Proactive > Reactive Management",
     "ML-driven proactive management (predict-then-act) reduces SLA violations by 30–50% compared to reactive threshold-based approaches in studied deployments."),
]

for i, (title, desc) in enumerate(findings):
    y = Inches(1.7) + Inches(i * 1.3)
    num_shape = slide.shapes.add_shape(MSO_SHAPE.OVAL,
        Inches(0.75), y + Inches(0.02), Inches(0.38), Inches(0.38))
    num_shape.fill.solid()
    num_shape.fill.fore_color.rgb = ACCENT_TEAL
    num_shape.line.fill.background()
    add_textbox(slide, Inches(0.75), y + Inches(0.04), Inches(0.38), Inches(0.35),
                str(i + 1), font_size=16, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
    add_textbox(slide, Inches(1.3), y, Inches(11.5), Inches(0.35),
                title, font_size=17, color=ACCENT_TEAL, bold=True)
    add_textbox(slide, Inches(1.3), y + Inches(0.38), Inches(11.5), Inches(0.7),
                desc, font_size=14, color=LIGHT_GRAY)

add_presenter_tag(slide, "Esam Mukbil", ACCENT_TEAL)
add_slide_number(slide, 11, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 12 — Telemetry Pipeline Architecture
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_TEAL)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "ML-Enhanced Network Telemetry Pipeline",
                    "How ML integrates into modern telemetry architectures",
                    "Esam Mukbil")

stages = [
    ("1. Collection", "gNMI, gRPC,\nINT, NetFlow", ACCENT_BLUE),
    ("2. Ingestion", "Stream processing\nKafka, Flink", RGBColor(0x00, 0xB4, 0xD8)),
    ("3. Storage", "Time-series DB\nData lakes", ACCENT_TEAL),
    ("4. ML Analysis", "Anomaly detection\nPrediction, RL", ACCENT_PURPLE),
    ("5. Action", "Auto-remediation\nPolicy updates", ORANGE),
]

box_width = Inches(2.1)
gap = Inches(0.25)
start_x = Inches(0.8)
box_y = Inches(2.3)
box_h = Inches(2.0)

for i, (title, desc, color) in enumerate(stages):
    x = start_x + (box_width + gap) * i
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, box_y, box_width, box_h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0x14, 0x18, 0x32)
    box.line.color.rgb = color
    box.line.width = Pt(2)
    add_textbox(slide, x + Inches(0.15), box_y + Inches(0.2), box_width - Inches(0.3), Inches(0.35),
                title, font_size=15, color=color, bold=True, alignment=PP_ALIGN.CENTER)
    add_textbox(slide, x + Inches(0.15), box_y + Inches(0.7), box_width - Inches(0.3), Inches(1.2),
                desc, font_size=13, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)
    # arrow between boxes
    if i < len(stages) - 1:
        arrow_x = x + box_width
        arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
            arrow_x, box_y + Inches(0.85), gap, Inches(0.3))
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = MID_GRAY
        arrow.line.fill.background()

# bottom note
add_textbox(slide, Inches(0.8), Inches(4.8), Inches(11.5), Inches(1.5),
            "Modern telemetry pipelines are evolving from passive data collection to active, ML-driven closed-loop systems. "
            "The integration of ML at the analysis stage enables proactive network management — transforming raw telemetry "
            "into actionable insights and automated responses in near real-time.",
            font_size=14, color=LIGHT_GRAY, line_spacing=1.4)

add_presenter_tag(slide, "Esam Mukbil", ACCENT_TEAL)
add_slide_number(slide, 12, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 13 — Section Divider: Hashim Kshim
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, SECTION_BG)
add_bottom_bar(slide, color=ACCENT_PURPLE)

add_textbox(slide, Inches(1), Inches(1.5), Inches(11), Inches(0.5),
            "PART 3", font_size=16, color=ACCENT_PURPLE, bold=True,
            alignment=PP_ALIGN.CENTER)
add_section_header(slide, "Industry, Emerging Trends & Conclusion", ACCENT_PURPLE)
add_textbox(slide, Inches(1), Inches(5.0), Inches(11), Inches(0.5),
            "Presenter: Hashim Kshim", font_size=20, color=WHITE,
            alignment=PP_ALIGN.CENTER)
add_slide_number(slide, 13, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 14 — Nokia's Telemetry Solutions
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_PURPLE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Industry: Nokia's Modern Broadband Network Telemetry",
                    "From reactive monitoring to AI-driven network intelligence",
                    "Hashim Kshim")

# left column
left_bullets = [
    "Nokia's broadband telemetry platform collects streaming data from millions of endpoints in real time",
    "Employs ML for predictive maintenance — detecting degrading CPE and fiber links before failures occur",
    "Automated root-cause analysis reduces mean time to resolution (MTTR) from hours to minutes",
    "Leverages unsupervised clustering to group similar network behaviors and detect fleet-wide anomalies",
    "Integration with Nokia AVA platform for AI-as-a-service in telco environments",
]

txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(6.0), Inches(4.8))
tf = txBox.text_frame
tf.word_wrap = True
add_bullet_slide_content(tf, left_bullets, font_size=15, color=LIGHT_GRAY, spacing=10)

# right box
box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(7.2), Inches(1.7), Inches(5.6), Inches(3.5))
box.fill.solid()
box.fill.fore_color.rgb = RGBColor(0x14, 0x18, 0x32)
box.line.color.rgb = ACCENT_PURPLE
box.line.width = Pt(1.5)

add_textbox(slide, Inches(7.5), Inches(1.9), Inches(5.0), Inches(0.4),
            "Nokia's Key ML Capabilities", font_size=15, color=ACCENT_PURPLE, bold=True)
cap_box = slide.shapes.add_textbox(Inches(7.5), Inches(2.4), Inches(5.0), Inches(2.6))
tf_cap = cap_box.text_frame
tf_cap.word_wrap = True
caps = [
    "Predictive maintenance using supervised ML models",
    "Anomaly detection via unsupervised clustering",
    "Customer experience scoring with ensemble models",
    "Network capacity forecasting with time-series DL",
    "Automated incident correlation and root-cause analysis",
]
add_bullet_slide_content(tf_cap, caps, font_size=13, color=LIGHT_GRAY, spacing=6)

add_presenter_tag(slide, "Hashim Kshim", ACCENT_PURPLE)
add_slide_number(slide, 14, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 15 — Ericsson's AI-Driven Telemetry
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_PURPLE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Industry: Ericsson's AI-Driven Network Telemetry",
                    "Data mesh architecture and Transport Automation Controller",
                    "Hashim Kshim")

left_items = [
    ("From Data Mess to AI-Ready Data Mesh", [
        "Ericsson advocates a 'data mesh' approach to telemetry",
        "Distributed data ownership with domain-specific telemetry pipelines",
        "Self-serve data infrastructure enabling ML teams across domains",
        "Focus on data quality, governance, and real-time accessibility",
    ]),
]

right_items = [
    ("Transport Automation Controller (TAC)", [
        "AI/ML at the helm of transport network performance visualization",
        "Automated anomaly detection on KPI time-series data",
        "Predictive analytics for proactive capacity planning",
        "Closed-loop automation: detect → diagnose → remediate",
    ]),
]

y_start = Inches(1.7)
for title, bullets in left_items:
    add_textbox(slide, Inches(0.8), y_start, Inches(5.5), Inches(0.4),
                title, font_size=17, color=ACCENT_PURPLE, bold=True)
    y = y_start + Inches(0.5)
    for b in bullets:
        add_textbox(slide, Inches(1.1), y, Inches(5.2), Inches(0.35),
                    f"• {b}", font_size=14, color=LIGHT_GRAY)
        y += Inches(0.35)

for title, bullets in right_items:
    add_textbox(slide, Inches(7.0), y_start, Inches(5.5), Inches(0.4),
                title, font_size=17, color=ACCENT_PURPLE, bold=True)
    y = y_start + Inches(0.5)
    for b in bullets:
        add_textbox(slide, Inches(7.3), y, Inches(5.2), Inches(0.35),
                    f"• {b}", font_size=14, color=LIGHT_GRAY)
        y += Inches(0.35)

# bottom insight
box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(4.5), Inches(11.7), Inches(1.8))
box.fill.solid()
box.fill.fore_color.rgb = RGBColor(0x14, 0x18, 0x32)
box.line.color.rgb = ACCENT_PURPLE
box.line.width = Pt(1.5)

add_textbox(slide, Inches(1.1), Inches(4.65), Inches(11.2), Inches(0.35),
            "Key Industry Insight", font_size=15, color=ACCENT_PURPLE, bold=True)
add_textbox(slide, Inches(1.1), Inches(5.05), Inches(11.2), Inches(1.0),
            "Both Nokia and Ericsson are converging on AI-native telemetry architectures: "
            "moving from centralized, rule-based monitoring to distributed, ML-driven systems "
            "that can autonomously detect issues, predict failures, and initiate remediation. "
            "The data mesh paradigm reflects the industry's recognition that telemetry data "
            "management is as critical as the ML models themselves.",
            font_size=13, color=LIGHT_GRAY, line_spacing=1.4)

add_presenter_tag(slide, "Hashim Kshim", ACCENT_PURPLE)
add_slide_number(slide, 15, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 16 — Emerging Trends: 6G & GenAI
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_PURPLE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Emerging Trends: 6G & GenAI for Network Telemetry",
                    "Next-generation technologies reshaping telemetry and network management",
                    "Hashim Kshim")

trends = [
    ("6G & Next-Gen Telemetry", ACCENT_TEAL, [
        "6G networks target sub-millisecond latency and Tbps throughput — demanding real-time ML inference at the edge",
        "Digital twin networks: ML-powered virtual replicas of physical networks for simulation and what-if analysis",
        "Semantic telemetry: intelligent data reduction at the source — only transmit meaningful changes, not raw streams",
        "Native AI architecture: 6G standards embed ML as a first-class network function, not an add-on",
    ]),
    ("Generative AI & LLMs for Telemetry", ORANGE, [
        "LLMs for natural language querying of telemetry data: 'Show me all anomalies in the US-East backbone last week'",
        "GenAI for synthetic telemetry data generation — augmenting scarce labeled datasets for training",
        "Automated incident report generation from raw telemetry events",
        "Foundation models for network data: pre-trained on diverse telemetry, fine-tuned for specific tasks",
    ]),
]

y = Inches(1.7)
for title, color, bullets in trends:
    add_textbox(slide, Inches(0.8), y, Inches(12), Inches(0.4),
                title, font_size=20, color=color, bold=True)
    y += Inches(0.5)
    for b in bullets:
        add_textbox(slide, Inches(1.1), y, Inches(11.5), Inches(0.4),
                    f"• {b}", font_size=14, color=LIGHT_GRAY)
        y += Inches(0.38)
    y += Inches(0.3)

add_presenter_tag(slide, "Hashim Kshim", ACCENT_PURPLE)
add_slide_number(slide, 16, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 17 — Open Challenges
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_PURPLE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "Open Challenges & Future Directions",
                    "Key issues that remain unsolved in ML for network telemetry",
                    "Hashim Kshim")

challenges = [
    ("Data Scarcity & Labeling", "Labeled anomaly/fault data is rare in production networks. Self-supervised and few-shot learning are active research areas."),
    ("Scalability & Real-Time Inference", "ML models must process millions of telemetry records per second. Edge inference and model compression are essential."),
    ("Explainability & Trust", "Network operators need to understand why an ML model flagged an anomaly. Black-box models hinder adoption."),
    ("Concept Drift", "Network traffic patterns change over time. Models must adapt continuously without catastrophic forgetting."),
    ("Cross-Domain Generalization", "Models trained on one network often fail on another. Domain adaptation and transfer learning need further development."),
    ("Privacy & Security", "Telemetry data may contain sensitive information. Federated and differential-privacy-preserving ML are emerging solutions."),
]

for i, (title, desc) in enumerate(challenges):
    col = 0 if i < 3 else 1
    row = i % 3
    x = Inches(0.8) + col * Inches(6.3)
    y = Inches(1.7) + row * Inches(1.7)
    # card
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
        x, y, Inches(5.8), Inches(1.45))
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(0x14, 0x18, 0x32)
    card.line.color.rgb = ACCENT_PURPLE if col == 0 else ORANGE
    card.line.width = Pt(1.2)
    add_textbox(slide, x + Inches(0.2), y + Inches(0.15), Inches(5.4), Inches(0.35),
                title, font_size=16, color=ACCENT_PURPLE if col == 0 else ORANGE, bold=True)
    add_textbox(slide, x + Inches(0.2), y + Inches(0.55), Inches(5.4), Inches(0.75),
                desc, font_size=12, color=LIGHT_GRAY)

add_presenter_tag(slide, "Hashim Kshim", ACCENT_PURPLE)
add_slide_number(slide, 17, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 18 — Conclusion & Key Takeaways
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, left=0, top=0, width=SLIDE_WIDTH, height=Inches(0.1), color=ACCENT_TEAL)
add_bottom_bar(slide, color=ACCENT_BLUE)
make_title_subtitle(slide, "Conclusion & Key Takeaways", None, "Hashim Kshim")

takeaways = [
    ("ML is transforming network telemetry",
     "From passive data collection to intelligent, proactive network management across anomaly detection, performance prediction, and QoS optimization."),
    ("Deep learning leads, but unsupervised methods dominate in practice",
     "Due to the scarcity of labeled data, autoencoders, clustering, and self-supervised methods are most practical for real-world deployment."),
    ("Industry is moving toward AI-native telemetry",
     "Nokia and Ericsson are building telemetry platforms with embedded ML — autonomous, closed-loop, and data-mesh-driven architectures."),
    ("6G and GenAI will accelerate the transformation",
     "Next-generation networks will require ML as a native function, while LLMs promise to democratize telemetry analysis through natural language interfaces."),
    ("Key challenges remain: scalability, explainability, and generalization",
     "Real-world adoption requires solving data scarcity, concept drift, real-time inference, and cross-domain transfer."),
]

for i, (title, desc) in enumerate(takeaways):
    y = Inches(1.5) + Inches(i * 1.1)
    # numbered circle
    circ = slide.shapes.add_shape(MSO_SHAPE.OVAL,
        Inches(0.75), y + Inches(0.02), Inches(0.42), Inches(0.42))
    circ.fill.solid()
    colors = [ACCENT_BLUE, ACCENT_TEAL, ACCENT_PURPLE, ORANGE, RGBColor(0xE0, 0x40, 0x40)]
    circ.fill.fore_color.rgb = colors[i]
    circ.line.fill.background()
    add_textbox(slide, Inches(0.75), y + Inches(0.05), Inches(0.42), Inches(0.38),
                str(i + 1), font_size=18, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
    add_textbox(slide, Inches(1.4), y, Inches(11.5), Inches(0.35),
                title, font_size=17, color=colors[i], bold=True)
    add_textbox(slide, Inches(1.4), y + Inches(0.38), Inches(11.5), Inches(0.6),
                desc, font_size=14, color=LIGHT_GRAY)

add_presenter_tag(slide, "Hashim Kshim", ACCENT_PURPLE)
add_slide_number(slide, 18, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 19 — Thank You & Q&A
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, SECTION_BG)
add_accent_bar(slide, left=0, top=0, width=SLIDE_WIDTH, height=Inches(0.1), color=ACCENT_BLUE)
add_bottom_bar(slide, color=ACCENT_TEAL)

add_textbox(slide, Inches(1.5), Inches(2.0), Inches(10.3), Inches(1.0),
            "Thank You!", font_size=52, color=WHITE, bold=True,
            alignment=PP_ALIGN.CENTER)
add_textbox(slide, Inches(1.5), Inches(3.2), Inches(10.3), Inches(0.7),
            "Questions & Discussion", font_size=30, color=ACCENT_TEAL,
            alignment=PP_ALIGN.CENTER)

# decorative line
shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
    Inches(4.5), Inches(4.1), Inches(4.3), Inches(0.04))
shape.fill.solid()
shape.fill.fore_color.rgb = ACCENT_BLUE
shape.line.fill.background()

add_textbox(slide, Inches(1.5), Inches(4.5), Inches(10.3), Inches(0.5),
            "Abdul Rehman    |    Esam Mukbil    |    Hashim Kshim",
            font_size=20, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
add_textbox(slide, Inches(1.5), Inches(5.2), Inches(10.3), Inches(0.5),
            "NET3006A — Machine Learning for Network Telemetry",
            font_size=16, color=MID_GRAY, alignment=PP_ALIGN.CENTER)

add_slide_number(slide, 19, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SLIDE 20 — References
# ═══════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_accent_bar(slide, color=ACCENT_BLUE)
add_bottom_bar(slide, color=ACCENT_TEAL)
make_title_subtitle(slide, "References", None, "All Members")

references = [
    "[1]  Nokia, \"Modern Broadband Network Telemetry,\" Nokia White Paper, 2024.",
    "[2]  Ericsson, \"From data mess to AI-ready data mesh,\" Ericsson Blog, 2024.",
    "[3]  Ericsson, \"Visualizing network performance: Transport Automation Controller with AI/ML at the helm,\" Ericsson, 2024.",
    "[4]  Z. Yuan et al., \"iTeleScope: Softwarized Network Middle-Box for Real-Time Video Telemetry and Classification,\" IEEE/ACM Trans. Netw., 2023.",
    "[5]  A. Dogra et al., \"6G Network Architecture: QoS Paradigms and Data Lifecycle Management for Next-Generation Networks,\" IEEE Commun. Surveys Tuts., 2024.",
    "[6]  S. Falkner et al., \"Mobile Network Data Synthesis with Generative AI: Challenges and Solutions,\" IEEE Network, 2024.",
    "[7]  M. Boban et al., \"Autonomous network operations: from reactive management to intent-driven optimization,\" Ericsson Technology Review, 2024.",
    "[8]  Ericsson, \"Four ways generative AI is set to transform the telecom industry,\" Ericsson Blog, 2024.",
    "[9]  ATIS, \"Advancing Generative AI Implementation in Telecommunications Networks,\" ATIS White Paper, 2024.",
    "[10] R. Boutaba et al., \"A comprehensive survey on machine learning for networking,\" ACM Comput. Surv., vol. 51, no. 5, 2018.",
    "[11] P. Mishra et al., \"A detailed investigation and analysis of using ML techniques for intrusion detection,\" IEEE Commun. Surveys Tuts., 2019.",
    "[12] F. Tang et al., \"A survey on machine learning for traffic classification,\" IEEE Trans. on Network and Service Management, 2022.",
]

txBox = slide.shapes.add_textbox(Inches(0.6), Inches(1.3), Inches(12.1), Inches(5.8))
tf = txBox.text_frame
tf.word_wrap = True

for i, ref in enumerate(references):
    if i == 0:
        p = tf.paragraphs[0]
    else:
        p = tf.add_paragraph()
    p.text = ref
    p.font.size = Pt(11)
    p.font.color.rgb = LIGHT_GRAY
    p.font.name = 'Calibri'
    p.space_after = Pt(4)
    p.space_before = Pt(1)

add_slide_number(slide, 20, TOTAL_SLIDES)


# ═══════════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════════
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, "NET3006A_ML_Network_Telemetry_Presentation.pptx")
prs.save(output_path)
print(f"Presentation saved to: {output_path}")
print(f"Total slides: {TOTAL_SLIDES}")
