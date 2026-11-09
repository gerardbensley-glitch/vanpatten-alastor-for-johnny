#!/usr/bin/env python3
"""
Van Patten Alastor V3 - Complete Catalogue Generator
Generates ALL 300 clothing products and 80+ watch products
"""

import json

# ============================================================================
# CLOTHING PRODUCTS - All 10 Categories (300 products total)
# ============================================================================

# Coats & Outerwear (001-030)
coats_outerwear = [
    {"id": "coat-001", "dept": "Coats & Outerwear", "brand": "Burberry", "tier": "Original Luxury", "name": "Kensington Heritage Trench Coat", "variant": "Heritage trench coat · Classic fit", "brandPrice": 2850, "housePrice": 228},
    {"id": "coat-002", "dept": "Coats & Outerwear", "brand": "Burberry", "tier": "Original Luxury", "name": "Wool Tailored Coat", "variant": "Brushed wool · Slim fit · Made in Italy", "brandPrice": 2950, "housePrice": 236},
    {"id": "coat-003", "dept": "Coats & Outerwear", "brand": "Burberry", "tier": "Original Luxury", "name": "Hayfield Cotton Check-Collar Bomber Jacket", "variant": "Cotton twill · Knitted Burberry Check collar", "brandPrice": 1795, "housePrice": 162},
    {"id": "coat-004", "dept": "Coats & Outerwear", "brand": "Burberry", "tier": "Original Luxury", "name": "Wool Cashmere Tailored Jacket", "variant": "Wool cashmere twill · Relaxed fit", "brandPrice": 2995, "housePrice": 240},
    {"id": "coat-005", "dept": "Coats & Outerwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Sebring Coat Windmate®", "variant": "Windmate® with Storm System® · Cashmere lined", "brandPrice": 4250, "housePrice": 298},
    {"id": "coat-006", "dept": "Coats & Outerwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Sergio Loro Piana Coat Baby Cashmere", "variant": "Baby Cashmere · Double-breasted · Peaked lapel", "brandPrice": 17460, "housePrice": 873},
    {"id": "coat-007", "dept": "Coats & Outerwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Traveler Field Jacket Linen", "variant": "Solaire linen · Multi-functional pockets", "brandPrice": 3500, "housePrice": 280},
    {"id": "coat-008", "dept": "Coats & Outerwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Traveler Field Jacket Microfiber, Silk", "variant": "Technical silk blend · Rain System® · Houndstooth", "brandPrice": 4650, "housePrice": 326},
    {"id": "coat-009", "dept": "Coats & Outerwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Spagna Jacket Cashmere", "variant": "Cashmere · Standing collar · Removable vest", "brandPrice": 5540, "housePrice": 388},
    {"id": "coat-010", "dept": "Coats & Outerwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Kilian Blouson Wish® Wool, Cashmere", "variant": "Melton Wish® wool with cashmere · Funnel neckline", "brandPrice": 4400, "housePrice": 308},
    {"id": "coat-011", "dept": "Coats & Outerwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Chevron Coat", "variant": "Chevron pattern · Wool blend", "brandPrice": 7900, "housePrice": 553},
    {"id": "coat-012", "dept": "Coats & Outerwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Suede Biker Jacket", "variant": "Suede · Biker style", "brandPrice": 11100, "housePrice": 555},
    {"id": "coat-013", "dept": "Coats & Outerwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Chalk Stripe Chevron Outerwear Jacket", "variant": "Chalk stripe · Chevron design", "brandPrice": 6300, "housePrice": 441},
    {"id": "coat-014", "dept": "Coats & Outerwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Nubuck Shirt-Style Bomber Jacket", "variant": "Nubuck · Shirt-style bomber", "brandPrice": 9900, "housePrice": 594},
    {"id": "coat-015", "dept": "Coats & Outerwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Oasi Cashmere Overshirt", "variant": "Oasi Cashmere · Overshirt style", "brandPrice": 5290, "housePrice": 370},
    {"id": "coat-016", "dept": "Coats & Outerwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Suede Full-Zip Blouson", "variant": "Suede · Full-zip blouson", "brandPrice": 9950, "housePrice": 597},
    {"id": "coat-017", "dept": "Coats & Outerwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Wool & Cashmere Jacket", "variant": "Wool and cashmere blend", "brandPrice": 5990, "housePrice": 419},
    {"id": "coat-018", "dept": "Coats & Outerwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Wool Quilted Button-Front Vest", "variant": "Wool quilted · Button-front vest", "brandPrice": 4550, "housePrice": 319},
    {"id": "coat-019", "dept": "Coats & Outerwear", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Pebbled Leather Biker Jacket", "variant": "Pebbled leather · Biker style", "brandPrice": 9990, "housePrice": 599},
    {"id": "coat-020", "dept": "Coats & Outerwear", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Nappa Leather Blazer", "variant": "Nappa leather · Blazer cut", "brandPrice": 9790, "housePrice": 587},
    {"id": "coat-021", "dept": "Coats & Outerwear", "brand": "Moncler", "tier": "Original Luxury", "name": "Montgenevre Knit Puffer Jacket", "variant": "Knit puffer · Montgenevre style", "brandPrice": 4190, "housePrice": 293},
    {"id": "coat-022", "dept": "Coats & Outerwear", "brand": "Moncler", "tier": "Original Luxury", "name": "Hooded Down Puffer Jacket", "variant": "Hooded · Down puffer", "brandPrice": 1995, "housePrice": 180},
    {"id": "coat-023", "dept": "Coats & Outerwear", "brand": "Moncler Grenoble", "tier": "Original Luxury", "name": "Quilted Hooded Puffer Jacket", "variant": "Quilted · Hooded puffer", "brandPrice": 2530, "housePrice": 202},
    {"id": "coat-024", "dept": "Coats & Outerwear", "brand": "Moncler", "tier": "Original Luxury", "name": "Quilted Puffer Vest", "variant": "Quilted puffer vest", "brandPrice": 1850, "housePrice": 167},
    {"id": "coat-025", "dept": "Coats & Outerwear", "brand": "Prada", "tier": "Original Luxury", "name": "Re-Nylon Blouson Logo Jacket", "variant": "Re-Nylon · Logo blouson", "brandPrice": 2700, "housePrice": 216},
    {"id": "coat-026", "dept": "Coats & Outerwear", "brand": "Dior", "tier": "Original Luxury", "name": "Harrington Jacket", "variant": "Harrington style", "brandPrice": 7100, "housePrice": 497},
    {"id": "coat-027", "dept": "Coats & Outerwear", "brand": "Givenchy", "tier": "Original Luxury", "name": "Plaid-Tipped Belted Trench Coat", "variant": "Plaid-tipped · Belted trench", "brandPrice": 3850, "housePrice": 308},
    {"id": "coat-028", "dept": "Coats & Outerwear", "brand": "Corneliani", "tier": "Original Luxury", "name": "ID Wool Top Coat", "variant": "Wool top coat", "brandPrice": 2195, "housePrice": 176},
    {"id": "coat-029", "dept": "Coats & Outerwear", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Shelton Houndstooth Sport Coat", "variant": "Houndstooth · Sport coat", "brandPrice": 5750, "housePrice": 403},
    {"id": "coat-030", "dept": "Coats & Outerwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Crossover Wool-Cashmere Blazer", "variant": "Wool-cashmere crossover · Blazer", "brandPrice": 3290, "housePrice": 263},
]

# Suits & Formal Tailoring (031-060)
suits_formal = [
    {"id": "suit-031", "dept": "Suits & Formal Tailoring", "brand": "Brioni", "tier": "Original Luxury", "name": "Men's Wool Sharkskin Suit", "variant": "Wool sharkskin · Two-piece", "brandPrice": 8500, "housePrice": 510},
    {"id": "suit-032", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Trofeo Milano Wool Suit", "variant": "Trofeo Milano wool · Two-piece", "brandPrice": 4890, "housePrice": 342},
    {"id": "suit-033", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "15Milmil15 Wool Suit", "variant": "15Milmil15 wool · Two-piece", "brandPrice": 5490, "housePrice": 384},
    {"id": "suit-034", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Grey Centoventimila Wool Suit", "variant": "Centoventimila wool · Grey", "brandPrice": 7150, "housePrice": 501},
    {"id": "suit-035", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Wool Tonal Stripe Two-Piece Suit", "variant": "Wool · Tonal stripe", "brandPrice": 5390, "housePrice": 377},
    {"id": "suit-036", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Trofeo Wool Tonal Stripe Two-Piece Suit", "variant": "Trofeo wool · Tonal stripe", "brandPrice": 4590, "housePrice": 321},
    {"id": "suit-037", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Plaid Centoventimila Wool Suit", "variant": "Centoventimila wool · Plaid", "brandPrice": 7250, "housePrice": 508},
    {"id": "suit-038", "dept": "Suits & Formal Tailoring", "brand": "Canali", "tier": "Original Luxury", "name": "Wool Single-Breasted Suit", "variant": "Wool · Single-breasted", "brandPrice": 2395, "housePrice": 192},
    {"id": "suit-039", "dept": "Suits & Formal Tailoring", "brand": "Canali", "tier": "Original Luxury", "name": "Denim Effect Wool Peak Lapel Suit", "variant": "Denim effect wool · Peak lapel", "brandPrice": 2495, "housePrice": 200},
    {"id": "suit-040", "dept": "Suits & Formal Tailoring", "brand": "Canali", "tier": "Original Luxury", "name": "Tonal Plaid Wool Single-Breasted Suit", "variant": "Wool · Tonal plaid · Single-breasted", "brandPrice": 2395, "housePrice": 192},
    {"id": "suit-041", "dept": "Suits & Formal Tailoring", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Pinstriped Linen-Blend Single-Breasted Suit", "variant": "Linen blend · Pinstripe · Single-breasted", "brandPrice": 5800, "housePrice": 406},
    {"id": "suit-042", "dept": "Suits & Formal Tailoring", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Linen and Wool Herringbone Two-Piece Suit", "variant": "Linen and wool · Herringbone", "brandPrice": 5950, "housePrice": 417},
    {"id": "suit-043", "dept": "Suits & Formal Tailoring", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Hairline Stripe Single-Breasted Suit", "variant": "Hairline stripe · Single-breasted", "brandPrice": 6380, "housePrice": 447},
    {"id": "suit-044", "dept": "Suits & Formal Tailoring", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Kent Hand-Tailored Glen Plaid Wool Suit", "variant": "Glen plaid wool · Hand-tailored", "brandPrice": 3995, "housePrice": 320},
    {"id": "suit-045", "dept": "Suits & Formal Tailoring", "brand": "Dior", "tier": "Original Luxury", "name": "Classic Suit", "variant": "Classic cut", "brandPrice": 3600, "housePrice": 288},
    {"id": "suit-046", "dept": "Suits & Formal Tailoring", "brand": "Dior", "tier": "Original Luxury", "name": "Classic Half-Lined Suit", "variant": "Half-lined", "brandPrice": 5200, "housePrice": 364},
    {"id": "suit-047", "dept": "Suits & Formal Tailoring", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Cashmere Award Suit", "variant": "Cashmere · Award style", "brandPrice": 8495, "housePrice": 510},
    {"id": "suit-048", "dept": "Suits & Formal Tailoring", "brand": "Loro Piana", "tier": "Original Luxury", "name": "4-Season Suit", "variant": "4-season wool", "brandPrice": 3995, "housePrice": 320},
    {"id": "suit-049", "dept": "Suits & Formal Tailoring", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Summer Stretch Suit", "variant": "Summer stretch", "brandPrice": 3495, "housePrice": 280},
    {"id": "suit-050", "dept": "Suits & Formal Tailoring", "brand": "Brioni", "tier": "Original Luxury", "name": "Wool Plaid Single-Breasted Sport Coat", "variant": "Wool plaid · Sport coat", "brandPrice": 6900, "housePrice": 483},
    {"id": "suit-051", "dept": "Suits & Formal Tailoring", "brand": "Kiton", "tier": "Original Luxury", "name": "Cashmere Glen Plaid Sport Coat", "variant": "Cashmere · Glen plaid", "brandPrice": 12995, "housePrice": 650},
    {"id": "suit-052", "dept": "Suits & Formal Tailoring", "brand": "Kiton", "tier": "Original Luxury", "name": "Cotton Knit Contrast-Trim Polo Shirt", "variant": "Cotton knit · Contrast trim", "brandPrice": 1395, "housePrice": 126},
    {"id": "suit-053", "dept": "Suits & Formal Tailoring", "brand": "Kiton", "tier": "Original Luxury", "name": "Cotton Knit Sport Coat", "variant": "Cotton knit · Sport coat", "brandPrice": 7500, "housePrice": 525},
    {"id": "suit-054", "dept": "Suits & Formal Tailoring", "brand": "Isaia", "tier": "Original Luxury", "name": "Over-Check Two-Button Sport Coat", "variant": "Over-check · Two-button", "brandPrice": 4150, "housePrice": 291},
    {"id": "suit-055", "dept": "Suits & Formal Tailoring", "brand": "Isaia", "tier": "Original Luxury", "name": "Solid Textured Single-Breasted Sport Coat", "variant": "Solid textured · Single-breasted", "brandPrice": 4150, "housePrice": 291},
    {"id": "suit-056", "dept": "Suits & Formal Tailoring", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Worsted Cashmere Two-Button Blazer", "variant": "Worsted cashmere · Two-button", "brandPrice": 9290, "housePrice": 557},
    {"id": "suit-057", "dept": "Suits & Formal Tailoring", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Houndstooth Single-Breasted Sport Coat", "variant": "Houndstooth · Single-breasted", "brandPrice": 4490, "housePrice": 314},
    {"id": "suit-058", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Cashmere and Silk Plaid Patch-Pocket Sport Coat", "variant": "Cashmere and silk · Plaid patch-pocket", "brandPrice": 5990, "housePrice": 419},
    {"id": "suit-059", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Cashmere and Silk Tonal Check Sport Coat", "variant": "Cashmere and silk · Tonal check", "brandPrice": 4090, "housePrice": 286},
    {"id": "suit-060", "dept": "Suits & Formal Tailoring", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Check Winter Crossover Notch-Lapel Sport Coat", "variant": "Check · Crossover · Notch lapel", "brandPrice": 3590, "housePrice": 287},
]

# Blazers/Sport Coats (061-090)
blazers_sportcoats = [
    {"id": "blazer-061", "dept": "Blazers/Sport Coats", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Gregory Hand-Tailored Wool Serge Blazer", "variant": "Classic navy · Made in Italy", "brandPrice": 2495, "housePrice": 200},
    {"id": "blazer-062", "dept": "Blazers/Sport Coats", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Southampton Cotton Linen Sport Coat", "variant": "Cotton linen · Unstructured", "brandPrice": 1695, "housePrice": 136},
    {"id": "blazer-063", "dept": "Blazers/Sport Coats", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Cashmere Blazer", "variant": "Cashmere · Unstructured", "brandPrice": 4250, "housePrice": 340},
    {"id": "blazer-064", "dept": "Blazers/Sport Coats", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Cashmere Blazer", "variant": "Cashmere · Soft shoulder", "brandPrice": 4900, "housePrice": 343},
    {"id": "blazer-065", "dept": "Blazers/Sport Coats", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Triple Stitch™ Cashmere Blazer", "variant": "Cashmere · Unstructured", "brandPrice": 3890, "housePrice": 272},
    {"id": "blazer-066", "dept": "Blazers/Sport Coats", "brand": "Canali", "tier": "Original Luxury", "name": "Wool Silk Blazer", "variant": "Wool silk blend · Soft construction", "brandPrice": 1995, "housePrice": 160},
    {"id": "blazer-067", "dept": "Blazers/Sport Coats", "brand": "Corneliani", "tier": "Original Luxury", "name": "Wool Linen Blazer", "variant": "Wool linen · Unlined", "brandPrice": 1895, "housePrice": 152},
    {"id": "blazer-068", "dept": "Blazers/Sport Coats", "brand": "Brioni", "tier": "Original Luxury", "name": "Wool Silk Linen Sport Coat", "variant": "Wool silk linen · Soft construction", "brandPrice": 5950, "housePrice": 357},
    {"id": "blazer-069", "dept": "Blazers/Sport Coats", "brand": "Kiton", "tier": "Original Luxury", "name": "Cashmere Sport Coat", "variant": "Cashmere · Natural shoulder", "brandPrice": 8950, "housePrice": 448},
    {"id": "blazer-070", "dept": "Blazers/Sport Coats", "brand": "Isaia", "tier": "Original Luxury", "name": "Wool Silk Linen Sport Coat", "variant": "Wool silk linen · Unstructured", "brandPrice": 3850, "housePrice": 269},
    {"id": "blazer-071", "dept": "Blazers/Sport Coats", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Silk Wool Blazer", "variant": "Silk wool · Peak lapel", "brandPrice": 5490, "housePrice": 329},
    {"id": "blazer-072", "dept": "Blazers/Sport Coats", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Velvet Blazer", "variant": "Velvet · Shawl lapel", "brandPrice": 4990, "housePrice": 299},
    {"id": "blazer-073", "dept": "Blazers/Sport Coats", "brand": "Boglioli", "tier": "Original Luxury", "name": "Wool Linen K-Jacket", "variant": "Wool linen · Unstructured", "brandPrice": 2150, "housePrice": 172},
    {"id": "blazer-074", "dept": "Blazers/Sport Coats", "brand": "Boglioli", "tier": "Original Luxury", "name": "Cashmere Blazer", "variant": "Cashmere · Soft construction", "brandPrice": 3850, "housePrice": 269},
    {"id": "blazer-075", "dept": "Blazers/Sport Coats", "brand": "Cucinelli", "tier": "Original Luxury", "name": "Linen Blazer", "variant": "Linen · Unlined", "brandPrice": 3200, "housePrice": 224},
    {"id": "blazer-076", "dept": "Blazers/Sport Coats", "brand": "Cucinelli", "tier": "Original Luxury", "name": "Wool Silk Blazer", "variant": "Wool silk · Soft shoulder", "brandPrice": 4100, "housePrice": 287},
    {"id": "blazer-077", "dept": "Blazers/Sport Coats", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Couture Wool Cashmere Blazer", "variant": "Wool cashmere · Unstructured", "brandPrice": 4590, "housePrice": 321},
    {"id": "blazer-078", "dept": "Blazers/Sport Coats", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Oasi Linen Blazer", "variant": "Oasi Linen · Unstructured", "brandPrice": 3390, "housePrice": 237},
    {"id": "blazer-079", "dept": "Blazers/Sport Coats", "brand": "Canali", "tier": "Original Luxury", "name": "Wool Flannel Blazer", "variant": "Wool flannel · Soft construction", "brandPrice": 2195, "housePrice": 176},
    {"id": "blazer-080", "dept": "Blazers/Sport Coats", "brand": "Canali", "tier": "Original Luxury", "name": "Silk Wool Blazer", "variant": "Silk wool · Peak lapel", "brandPrice": 2295, "housePrice": 184},
    {"id": "blazer-081", "dept": "Blazers/Sport Coats", "brand": "Corneliani", "tier": "Original Luxury", "name": "Wool Cashmere Blazer", "variant": "Wool cashmere · Unlined", "brandPrice": 2495, "housePrice": 200},
    {"id": "blazer-082", "dept": "Blazers/Sport Coats", "brand": "Corneliani", "tier": "Original Luxury", "name": "Linen Silk Blazer", "variant": "Linen silk · Soft construction", "brandPrice": 2095, "housePrice": 168},
    {"id": "blazer-083", "dept": "Blazers/Sport Coats", "brand": "Brioni", "tier": "Original Luxury", "name": "Cashmere Blazer", "variant": "Cashmere · Unstructured", "brandPrice": 7950, "housePrice": 477},
    {"id": "blazer-084", "dept": "Blazers/Sport Coats", "brand": "Brioni", "tier": "Original Luxury", "name": "Wool Silk Linen Blazer", "variant": "Wool silk linen · Soft shoulder", "brandPrice": 6450, "housePrice": 387},
    {"id": "blazer-085", "dept": "Blazers/Sport Coats", "brand": "Kiton", "tier": "Original Luxury", "name": "Wool Linen Sport Coat", "variant": "Wool linen · Natural shoulder", "brandPrice": 7950, "housePrice": 398},
    {"id": "blazer-086", "dept": "Blazers/Sport Coats", "brand": "Kiton", "tier": "Original Luxury", "name": "Silk Wool Sport Coat", "variant": "Silk wool · Unstructured", "brandPrice": 8950, "housePrice": 448},
    {"id": "blazer-087", "dept": "Blazers/Sport Coats", "brand": "Isaia", "tier": "Original Luxury", "name": "Cashmere Blazer", "variant": "Cashmere · Soft construction", "brandPrice": 4450, "housePrice": 312},
    {"id": "blazer-088", "dept": "Blazers/Sport Coats", "brand": "Isaia", "tier": "Original Luxury", "name": "Wool Silk Blazer", "variant": "Wool silk · Unlined", "brandPrice": 3950, "housePrice": 277},
    {"id": "blazer-089", "dept": "Blazers/Sport Coats", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Wool Cashmere Blazer", "variant": "Wool cashmere · Peak lapel", "brandPrice": 6290, "housePrice": 377},
    {"id": "blazer-090", "dept": "Blazers/Sport Coats", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Silk Velvet Blazer", "variant": "Silk velvet · Shawl lapel", "brandPrice": 5890, "housePrice": 353},
]

# Shirts & Polos (091-120)
shirts_polos = [
    {"id": "shirt-091", "dept": "Shirts & Polos", "brand": "Polo Ralph Lauren", "tier": "Original Luxury", "name": "Classic Fit Oxford Shirt", "variant": "Blue cotton Oxford · Button-down collar", "brandPrice": 120, "housePrice": 96},
    {"id": "shirt-092", "dept": "Shirts & Polos", "brand": "Polo Ralph Lauren", "tier": "Original Luxury", "name": "Custom Fit Solid Dress Shirt", "variant": "White cotton · Spread collar", "brandPrice": 145, "housePrice": 116},
    {"id": "shirt-093", "dept": "Shirts & Polos", "brand": "Polo Ralph Lauren", "tier": "Original Luxury", "name": "Classic Fit Broadcloth Shirt", "variant": "Blue broadcloth · Button-down", "brandPrice": 135, "housePrice": 108},
    {"id": "shirt-094", "dept": "Shirts & Polos", "brand": "Charvet", "tier": "Original Luxury", "name": "Hand-Sewn Dress Shirt", "variant": "White cotton · French cuffs", "brandPrice": 595, "housePrice": 416},
    {"id": "shirt-095", "dept": "Shirts & Polos", "brand": "Charvet", "tier": "Original Luxury", "name": "Oxford Shirt", "variant": "Blue Oxford · Button-down", "brandPrice": 495, "housePrice": 347},
    {"id": "shirt-096", "dept": "Shirts & Polos", "brand": "Turnbull & Asser", "tier": "Original Luxury", "name": "Classic Fit Dress Shirt", "variant": "White cotton · Spread collar", "brandPrice": 395, "housePrice": 277},
    {"id": "shirt-097", "dept": "Shirts & Polos", "brand": "Turnbull & Asser", "tier": "Original Luxury", "name": "Oxford Button-Down", "variant": "Blue Oxford · Button-down", "brandPrice": 345, "housePrice": 242},
    {"id": "shirt-098", "dept": "Shirts & Polos", "brand": "Eton", "tier": "Original Luxury", "name": "Slim Fit Dress Shirt", "variant": "White cotton · Spread collar", "brandPrice": 245, "housePrice": 196},
    {"id": "shirt-099", "dept": "Shirts & Polos", "brand": "Eton", "tier": "Original Luxury", "name": "Classic Fit Oxford", "variant": "Blue Oxford · Button-down", "brandPrice": 225, "housePrice": 180},
    {"id": "shirt-100", "dept": "Shirts & Polos", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Cashmere Polo Shirt", "variant": "Cashmere · Long sleeve", "brandPrice": 895, "housePrice": 627},
    {"id": "shirt-101", "dept": "Shirts & Polos", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Silk Blend Polo", "variant": "Silk cotton · Short sleeve", "brandPrice": 695, "housePrice": 487},
    {"id": "shirt-102", "dept": "Shirts & Polos", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Cashmere Polo", "variant": "Cashmere · Short sleeve", "brandPrice": 950, "housePrice": 665},
    {"id": "shirt-103", "dept": "Shirts & Polos", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Summer Cashmere Polo", "variant": "Summer cashmere · Long sleeve", "brandPrice": 850, "housePrice": 595},
    {"id": "shirt-104", "dept": "Shirts & Polos", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Oasi Cashmere Polo", "variant": "Oasi Cashmere · Short sleeve", "brandPrice": 790, "housePrice": 553},
    {"id": "shirt-105", "dept": "Shirts & Polos", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Triple Stitch™ Cotton Polo", "variant": "Cotton piqué · Short sleeve", "brandPrice": 490, "housePrice": 343},
    {"id": "shirt-106", "dept": "Shirts & Polos", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Sea Island Cotton Dress Shirt", "variant": "White Sea Island · Spread collar", "brandPrice": 395, "housePrice": 277},
    {"id": "shirt-107", "dept": "Shirts & Polos", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Oxford Button-Down", "variant": "Blue Oxford · Button-down", "brandPrice": 295, "housePrice": 206},
    {"id": "shirt-108", "dept": "Shirts & Polos", "brand": "Lacoste", "tier": "Original Luxury", "name": "L.12.12 Polo", "variant": "Cotton piqué · Short sleeve", "brandPrice": 145, "housePrice": 116},
    {"id": "shirt-109", "dept": "Shirts & Polos", "brand": "Lacoste", "tier": "Original Luxury", "name": "Long Sleeve Polo", "variant": "Cotton piqué · Long sleeve", "brandPrice": 175, "housePrice": 140},
    {"id": "shirt-110", "dept": "Shirts & Polos", "brand": "Kiton", "tier": "Original Luxury", "name": "Cashmere Polo", "variant": "Cashmere · Short sleeve", "brandPrice": 1295, "housePrice": 648},
    {"id": "shirt-111", "dept": "Shirts & Polos", "brand": "Kiton", "tier": "Original Luxury", "name": "Silk Polo", "variant": "Silk · Short sleeve", "brandPrice": 995, "housePrice": 498},
    {"id": "shirt-112", "dept": "Shirts & Polos", "brand": "Billionaire", "tier": "Original Luxury", "name": "Cashmere Polo", "variant": "Cashmere · Short sleeve", "brandPrice": 895, "housePrice": 627},
    {"id": "shirt-113", "dept": "Shirts & Polos", "brand": "Billionaire", "tier": "Original Luxury", "name": "Silk Blend Polo", "variant": "Silk cotton · Short sleeve", "brandPrice": 795, "housePrice": 557},
    {"id": "shirt-114", "dept": "Shirts & Polos", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Silk Polo", "variant": "Silk · Short sleeve", "brandPrice": 690, "housePrice": 483},
    {"id": "shirt-115", "dept": "Shirts & Polos", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Cotton Polo", "variant": "Cotton piqué · Short sleeve", "brandPrice": 590, "housePrice": 413},
    {"id": "shirt-116", "dept": "Shirts & Polos", "brand": "Canali", "tier": "Original Luxury", "name": "Dress Shirt", "variant": "White cotton · Spread collar", "brandPrice": 295, "housePrice": 206},
    {"id": "shirt-117", "dept": "Shirts & Polos", "brand": "Canali", "tier": "Original Luxury", "name": "Oxford Shirt", "variant": "Blue Oxford · Button-down", "brandPrice": 245, "housePrice": 172},
    {"id": "shirt-118", "dept": "Shirts & Polos", "brand": "Corneliani", "tier": "Original Luxury", "name": "Dress Shirt", "variant": "White cotton · French cuffs", "brandPrice": 275, "housePrice": 193},
    {"id": "shirt-119", "dept": "Shirts & Polos", "brand": "Corneliani", "tier": "Original Luxury", "name": "Oxford Button-Down", "variant": "Blue Oxford · Button-down", "brandPrice": 225, "housePrice": 158},
    {"id": "shirt-120", "dept": "Shirts & Polos", "brand": "Brioni", "tier": "Original Luxury", "name": "Dress Shirt", "variant": "White cotton · Spread collar", "brandPrice": 495, "housePrice": 347},
]

# Knitwear (121-150)
knitwear = [
    {"id": "knit-121", "dept": "Knitwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Cashmere Crewneck Sweater", "variant": "Cashmere · Crewneck", "brandPrice": 1350, "housePrice": 945},
    {"id": "knit-122", "dept": "Knitwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Baby Cashmere Cardigan", "variant": "Baby Cashmere · Button-front", "brandPrice": 2650, "housePrice": 1325},
    {"id": "knit-123", "dept": "Knitwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Cashmere V-Neck Sweater", "variant": "Cashmere · V-neck", "brandPrice": 1450, "housePrice": 1015},
    {"id": "knit-124", "dept": "Knitwear", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Wool Cashmere Blend Sweater", "variant": "Wool cashmere · Crewneck", "brandPrice": 1150, "housePrice": 805},
    {"id": "knit-125", "dept": "Knitwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Cashmere Crewneck", "variant": "Cashmere · Crewneck", "brandPrice": 1450, "housePrice": 1015},
    {"id": "knit-126", "dept": "Knitwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Cashmere Cardigan", "variant": "Cashmere · Button-front", "brandPrice": 1850, "housePrice": 925},
    {"id": "knit-127", "dept": "Knitwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Wool Blend Sweater", "variant": "Wool blend · Crewneck", "brandPrice": 950, "housePrice": 665},
    {"id": "knit-128", "dept": "Knitwear", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Silk Cashmere Sweater", "variant": "Silk cashmere · V-neck", "brandPrice": 1650, "housePrice": 825},
    {"id": "knit-129", "dept": "Knitwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Oasi Cashmere Crewneck", "variant": "Oasi Cashmere · Crewneck", "brandPrice": 1190, "housePrice": 833},
    {"id": "knit-130", "dept": "Knitwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Cashmere V-Neck", "variant": "Cashmere · V-neck", "brandPrice": 990, "housePrice": 693},
    {"id": "knit-131", "dept": "Knitwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Wool Cashmere Cardigan", "variant": "Wool cashmere · Button-front", "brandPrice": 890, "housePrice": 623},
    {"id": "knit-132", "dept": "Knitwear", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Merino Wool Sweater", "variant": "Merino wool · Crewneck", "brandPrice": 690, "housePrice": 483},
    {"id": "knit-133", "dept": "Knitwear", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Cashmere Crewneck", "variant": "Cashmere · Crewneck", "brandPrice": 795, "housePrice": 557},
    {"id": "knit-134", "dept": "Knitwear", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Cashmere V-Neck", "variant": "Cashmere · V-neck", "brandPrice": 695, "housePrice": 487},
    {"id": "knit-135", "dept": "Knitwear", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Merino Wool Cardigan", "variant": "Merino wool · Button-front", "brandPrice": 595, "housePrice": 417},
    {"id": "knit-136", "dept": "Knitwear", "brand": "Prada", "tier": "Original Luxury", "name": "Cashmere Sweater", "variant": "Cashmere · Crewneck", "brandPrice": 1250, "housePrice": 875},
    {"id": "knit-137", "dept": "Knitwear", "brand": "Prada", "tier": "Original Luxury", "name": "Wool Blend Sweater", "variant": "Wool blend · V-neck", "brandPrice": 950, "housePrice": 665},
    {"id": "knit-138", "dept": "Knitwear", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Cashmere Crewneck", "variant": "Cashmere · Crewneck", "brandPrice": 1490, "housePrice": 894},
    {"id": "knit-139", "dept": "Knitwear", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Cashmere Cardigan", "variant": "Cashmere · Button-front", "brandPrice": 1890, "housePrice": 1134},
    {"id": "knit-140", "dept": "Knitwear", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Silk Blend Sweater", "variant": "Silk blend · V-neck", "brandPrice": 1290, "housePrice": 774},
    {"id": "knit-141", "dept": "Knitwear", "brand": "Canali", "tier": "Original Luxury", "name": "Cashmere Sweater", "variant": "Cashmere · Crewneck", "brandPrice": 695, "housePrice": 487},
    {"id": "knit-142", "dept": "Knitwear", "brand": "Canali", "tier": "Original Luxury", "name": "Merino Wool Sweater", "variant": "Merino wool · V-neck", "brandPrice": 495, "housePrice": 347},
    {"id": "knit-143", "dept": "Knitwear", "brand": "Corneliani", "tier": "Original Luxury", "name": "Cashmere Cardigan", "variant": "Cashmere · Button-front", "brandPrice": 795, "housePrice": 557},
    {"id": "knit-144", "dept": "Knitwear", "brand": "Corneliani", "tier": "Original Luxury", "name": "Wool Blend Sweater", "variant": "Wool blend · Crewneck", "brandPrice": 595, "housePrice": 417},
    {"id": "knit-145", "dept": "Knitwear", "brand": "Brioni", "tier": "Original Luxury", "name": "Cashmere Sweater", "variant": "Cashmere · Crewneck", "brandPrice": 1250, "housePrice": 875},
    {"id": "knit-146", "dept": "Knitwear", "brand": "Brioni", "tier": "Original Luxury", "name": "Cashmere V-Neck", "variant": "Cashmere · V-neck", "brandPrice": 1150, "housePrice": 805},
    {"id": "knit-147", "dept": "Knitwear", "brand": "Kiton", "tier": "Original Luxury", "name": "Cashmere Crewneck", "variant": "Cashmere · Crewneck", "brandPrice": 1595, "housePrice": 798},
    {"id": "knit-148", "dept": "Knitwear", "brand": "Kiton", "tier": "Original Luxury", "name": "Cashmere Cardigan", "variant": "Cashmere · Button-front", "brandPrice": 1995, "housePrice": 998},
    {"id": "knit-149", "dept": "Knitwear", "brand": "Isaia", "tier": "Original Luxury", "name": "Cashmere Sweater", "variant": "Cashmere · Crewneck", "brandPrice": 895, "housePrice": 627},
    {"id": "knit-150", "dept": "Knitwear", "brand": "Isaia", "tier": "Original Luxury", "name": "Wool Blend Cardigan", "variant": "Wool blend · Button-front", "brandPrice": 695, "housePrice": 487},
]

# Trousers (151-180)
trousers = [
    {"id": "trouser-151", "dept": "Trousers", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Triple Stitch™ Wool Trousers", "variant": "Wool · Slim fit", "brandPrice": 890, "housePrice": 623},
    {"id": "trouser-152", "dept": "Trousers", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Centoventimila Wool Trousers", "variant": "Centoventimila wool · Regular fit", "brandPrice": 1190, "housePrice": 833},
    {"id": "trouser-153", "dept": "Trousers", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Oasi Cashmere Trousers", "variant": "Oasi Cashmere · Slim fit", "brandPrice": 1590, "housePrice": 1113},
    {"id": "trouser-154", "dept": "Trousers", "brand": "ZEGNA", "tier": "Original Luxury", "name": "Summer Linen Trousers", "variant": "Linen · Regular fit", "brandPrice": 790, "housePrice": 553},
    {"id": "trouser-155", "dept": "Trousers", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Cashmere Trousers", "variant": "Cashmere · Regular fit", "brandPrice": 1950, "housePrice": 1365},
    {"id": "trouser-156", "dept": "Trousers", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Wool Cashmere Trousers", "variant": "Wool cashmere · Slim fit", "brandPrice": 1450, "housePrice": 1015},
    {"id": "trouser-157", "dept": "Trousers", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Summer Linen Trousers", "variant": "Linen · Regular fit", "brandPrice": 1250, "housePrice": 875},
    {"id": "trouser-158", "dept": "Trousers", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Cashmere Trousers", "variant": "Cashmere · Slim fit", "brandPrice": 1850, "housePrice": 925},
    {"id": "trouser-159", "dept": "Trousers", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Wool Blend Trousers", "variant": "Wool blend · Regular fit", "brandPrice": 950, "housePrice": 665},
    {"id": "trouser-160", "dept": "Trousers", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Linen Trousers", "variant": "Linen · Regular fit", "brandPrice": 850, "housePrice": 595},
    {"id": "trouser-161", "dept": "Trousers", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Wool Dress Trousers", "variant": "Wool · Regular fit", "brandPrice": 495, "housePrice": 347},
    {"id": "trouser-162", "dept": "Trousers", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Linen Trousers", "variant": "Linen · Regular fit", "brandPrice": 395, "housePrice": 277},
    {"id": "trouser-163", "dept": "Trousers", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Cotton Chinos", "variant": "Cotton · Slim fit", "brandPrice": 295, "housePrice": 206},
    {"id": "trouser-164", "dept": "Trousers", "brand": "Canali", "tier": "Original Luxury", "name": "Wool Trousers", "variant": "Wool · Regular fit", "brandPrice": 495, "housePrice": 347},
    {"id": "trouser-165", "dept": "Trousers", "brand": "Canali", "tier": "Original Luxury", "name": "Wool Linen Trousers", "variant": "Wool linen · Regular fit", "brandPrice": 595, "housePrice": 417},
    {"id": "trouser-166", "dept": "Trousers", "brand": "Canali", "tier": "Original Luxury", "name": "Cotton Chinos", "variant": "Cotton · Slim fit", "brandPrice": 395, "housePrice": 277},
    {"id": "trouser-167", "dept": "Trousers", "brand": "Corneliani", "tier": "Original Luxury", "name": "Wool Trousers", "variant": "Wool · Regular fit", "brandPrice": 545, "housePrice": 382},
    {"id": "trouser-168", "dept": "Trousers", "brand": "Corneliani", "tier": "Original Luxury", "name": "Linen Trousers", "variant": "Linen · Regular fit", "brandPrice": 495, "housePrice": 347},
    {"id": "trouser-169", "dept": "Trousers", "brand": "Corneliani", "tier": "Original Luxury", "name": "Cotton Trousers", "variant": "Cotton · Slim fit", "brandPrice": 445, "housePrice": 312},
    {"id": "trouser-170", "dept": "Trousers", "brand": "Brioni", "tier": "Original Luxury", "name": "Wool Trousers", "variant": "Wool · Regular fit", "brandPrice": 895, "housePrice": 627},
    {"id": "trouser-171", "dept": "Trousers", "brand": "Brioni", "tier": "Original Luxury", "name": "Cashmere Trousers", "variant": "Cashmere · Slim fit", "brandPrice": 1495, "housePrice": 748},
    {"id": "trouser-172", "dept": "Trousers", "brand": "Kiton", "tier": "Original Luxury", "name": "Wool Trousers", "variant": "Wool · Regular fit", "brandPrice": 995, "housePrice": 498},
    {"id": "trouser-173", "dept": "Trousers", "brand": "Kiton", "tier": "Original Luxury", "name": "Cashmere Trousers", "variant": "Cashmere · Slim fit", "brandPrice": 1895, "housePrice": 948},
    {"id": "trouser-174", "dept": "Trousers", "brand": "Isaia", "tier": "Original Luxury", "name": "Wool Trousers", "variant": "Wool · Regular fit", "brandPrice": 695, "housePrice": 487},
    {"id": "trouser-175", "dept": "Trousers", "brand": "Isaia", "tier": "Original Luxury", "name": "Linen Trousers", "variant": "Linen · Regular fit", "brandPrice": 595, "housePrice": 417},
    {"id": "trouser-176", "dept": "Trousers", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Wool Trousers", "variant": "Wool · Slim fit", "brandPrice": 990, "housePrice": 594},
    {"id": "trouser-177", "dept": "Trousers", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Cashmere Trousers", "variant": "Cashmere · Slim fit", "brandPrice": 1490, "housePrice": 894},
    {"id": "trouser-178", "dept": "Trousers", "brand": "TOM FORD", "tier": "Original Luxury", "name": "Cotton Chinos", "variant": "Cotton · Slim fit", "brandPrice": 690, "housePrice": 413},
    {"id": "trouser-179", "dept": "Trousers", "brand": "Prada", "tier": "Original Luxury", "name": "Wool Trousers", "variant": "Wool · Slim fit", "brandPrice": 795, "housePrice": 557},
    {"id": "trouser-180", "dept": "Trousers", "brand": "Prada", "tier": "Original Luxury", "name": "Nylon Trousers", "variant": "Nylon · Regular fit", "brandPrice": 695, "housePrice": 487},
]

# Denim (181-210)
denim = [
    {"id": "denim-181", "dept": "Denim", "brand": "Prada", "tier": "Original Luxury", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 795, "housePrice": 557},
    {"id": "denim-182", "dept": "Denim", "brand": "Prada", "tier": "Original Luxury", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 795, "housePrice": 557},
    {"id": "denim-183", "dept": "Denim", "brand": "Prada", "tier": "Original Luxury", "name": "Tapered Jeans", "variant": "Denim · Tapered", "brandPrice": 895, "housePrice": 627},
    {"id": "denim-184", "dept": "Denim", "brand": "Dior", "tier": "Original Luxury", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 990, "housePrice": 594},
    {"id": "denim-185", "dept": "Denim", "brand": "Dior", "tier": "Original Luxury", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 1090, "housePrice": 654},
    {"id": "denim-186", "dept": "Denim", "brand": "Balenciaga", "tier": "Original Luxury", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 895, "housePrice": 627},
    {"id": "denim-187", "dept": "Denim", "brand": "Balenciaga", "tier": "Original Luxury", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 995, "housePrice": 697},
    {"id": "denim-188", "dept": "Denim", "brand": "Gucci", "tier": "Original Luxury", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 795, "housePrice": 557},
    {"id": "denim-189", "dept": "Denim", "brand": "Gucci", "tier": "Original Luxury", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 895, "housePrice": 627},
    {"id": "denim-190", "dept": "Denim", "brand": "Saint Laurent", "tier": "Original Luxury", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 695, "housePrice": 487},
    {"id": "denim-191", "dept": "Denim", "brand": "Saint Laurent", "tier": "Original Luxury", "name": "Skinny Jeans", "variant": "Denim · Skinny", "brandPrice": 795, "housePrice": 557},
    {"id": "denim-192", "dept": "Denim", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 395, "housePrice": 277},
    {"id": "denim-193", "dept": "Denim", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 395, "housePrice": 277},
    {"id": "denim-194", "dept": "Denim", "brand": "Ralph Lauren Purple Label", "tier": "Original Luxury", "name": "Relaxed Fit Jeans", "variant": "Denim · Relaxed fit", "brandPrice": 345, "housePrice": 242},
    {"id": "denim-195", "dept": "Denim", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 595, "housePrice": 417},
    {"id": "denim-196", "dept": "Denim", "brand": "Brunello Cucinelli", "tier": "Original Luxury", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 595, "housePrice": 417},
    {"id": "denim-197", "dept": "Denim", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Cashmere Blend Jeans", "variant": "Cashmere denim · Slim fit", "brandPrice": 895, "housePrice": 627},
    {"id": "denim-198", "dept": "Denim", "brand": "Loro Piana", "tier": "Original Luxury", "name": "Wool Blend Jeans", "variant": "Wool denim · Straight leg", "brandPrice": 795, "housePrice": 557},
    {"id": "denim-199", "dept": "Denim", "brand": "Frame", "tier": "Premium Independent", "name": "Le High Skinny Jeans", "variant": "Denim · Skinny", "brandPrice": 245, "housePrice": 196},
    {"id": "denim-200", "dept": "Denim", "brand": "Frame", "tier": "Premium Independent", "name": "Le Skinny De Jeanne", "variant": "Denim · Skinny", "brandPrice": 225, "housePrice": 180},
    {"id": "denim-201", "dept": "Denim", "brand": "Frame", "tier": "Premium Independent", "name": "L'Homme Straight Leg", "variant": "Denim · Straight leg", "brandPrice": 255, "housePrice": 204},
    {"id": "denim-202", "dept": "Denim", "brand": "AG Jeans", "tier": "Premium Independent", "name": "The Legend Slim Fit", "variant": "Denim · Slim fit", "brandPrice": 225, "housePrice": 180},
    {"id": "denim-203", "dept": "Denim", "brand": "AG Jeans", "tier": "Premium Independent", "name": "The Graduate Straight Leg", "variant": "Denim · Straight leg", "brandPrice": 235, "housePrice": 188},
    {"id": "denim-204", "dept": "Denim", "brand": "Citizens of Humanity", "tier": "Premium Independent", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 245, "housePrice": 196},
    {"id": "denim-205", "dept": "Denim", "brand": "Citizens of Humanity", "tier": "Premium Independent", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 255, "housePrice": 204},
    {"id": "denim-206", "dept": "Denim", "brand": "7 For All Mankind", "tier": "Premium Independent", "name": "Slim Fit Jeans", "variant": "Denim · Slim fit", "brandPrice": 225, "housePrice": 180},
    {"id": "denim-207", "dept": "Denim", "brand": "7 For All Mankind", "tier": "Premium Independent", "name": "Straight Leg Jeans", "variant": "Denim · Straight leg", "brandPrice": 235, "housePrice": 188},
    {"id": "denim-208", "dept": "Denim", "brand": "Nudie Jeans", "tier": "Premium Independent", "name": "Thin Finn", "variant": "Denim · Tapered", "brandPrice": 195, "housePrice": 156},
    {"id": "denim-209", "dept": "Denim", "brand": "Nudie Jeans", "tier": "Premium Independent", "name": "Lean Dean", "variant": "Denim · Slim fit", "brandPrice": 185, "housePrice": 148},
    {"id": "denim-210", "dept": "Denim", "brand": "Levi's Vintage Clothing", "tier": "Premium Independent", "name": "1955 501 Jeans", "variant": "Denim · Straight leg", "brandPrice": 245, "housePrice": 196},
]

# Footwear (211-240)
footwear = [
    {"id": "shoe-211", "dept": "Footwear", "brand": "Crockett & Jones", "tier": "Original Luxury", "name": "Harvard Dark Brown Cordovan", "variant": "Unlined penny loafer · Horween shell cordovan", "brandPrice": 1220, "housePrice": 854},
    {"id": "shoe-212", "dept": "Footwear", "brand": "Crockett & Jones", "tier": "Original Luxury", "name": "Alex Black Calf", "variant": "Wholecut oxford · Black calf", "brandPrice": 895, "housePrice": 627},
    {"id": "shoe-213", "dept": "Footwear", "brand": "Crockett & Jones", "tier": "Original Luxury", "name": "Lowndes Dark Brown Calf", "variant": "Penny loafer · Dark brown calf", "brandPrice": 795, "housePrice": 557},
    {"id": "shoe-214", "dept": "Footwear", "brand": "Crockett & Jones", "tier": "Original Luxury", "name": "Cavendish Dark Brown Calf", "variant": "Double monk strap · Dark brown calf", "brandPrice": 895, "housePrice": 627},
    {"id": "shoe-215", "dept": "Footwear", "brand": "Edward Green", "tier": "Original Luxury", "name": "Dover Dark Brown Calf", "variant": "Wholecut oxford · Dark brown calf", "brandPrice": 1895, "housePrice": 1327},
    {"id": "shoe-216", "dept": "Footwear", "brand": "Edward Green", "tier": "Original Luxury", "name": "Piccadilly Black Calf", "variant": "Wholecut oxford · Black calf", "brandPrice": 1995, "housePrice": 1397},
    {"id": "shoe-217", "dept": "Footwear", "brand": "Edward Green", "tier": "Original Luxury", "name": "Galway Dark Brown Suede", "variant": "Chelsea boot · Dark brown suede", "brandPrice": 1895, "housePrice": 1327},
    {"id": "shoe-218", "dept": "Footwear", "brand": "John Lobb", "tier": "Original Luxury", "name": "Lopez Black Calf", "variant": "Penny loafer · Black calf", "brandPrice": 1995, "housePrice": 1397},
    {"id": "shoe-219", "dept": "Footwear", "brand": "John Lobb", "tier": "Original Luxury", "name": "Philip II Black Calf", "variant": "Wholecut oxford · Black calf", "brandPrice": 2295, "housePrice": 1607},
    {"id": "shoe-220", "dept": "Footwear", "brand": "John Lobb", "tier": "Original Luxury", "name": "William Dark Brown Calf", "variant": "Double monk strap · Dark brown calf", "brandPrice": 2195, "housePrice": 1537},
    {"id": "shoe-221", "dept": "Footwear", "brand": "Alden", "tier": "Original Luxury", "name": "Shell Cordovan Loafer", "variant": "Penny loafer · Shell cordovan", "brandPrice": 895, "housePrice": 627},
    {"id": "shoe-222", "dept": "Footwear", "brand": "Alden", "tier": "Original Luxury", "name": "Shell Cordovan Boot", "variant": "Chelsea boot · Shell cordovan", "brandPrice": 995, "housePrice": 697},
    {"id": "shoe-223", "dept": "Footwear", "brand": "Alden", "tier": "Original Luxury", "name": "Longwing Blucher", "variant": "Longwing · Shell cordovan", "brandPrice": 845, "housePrice": 592},
    {"id": "shoe-224", "dept": "Footwear", "brand": "Berluti", "tier": "Original Luxury", "name": "Playoff Loafer", "variant": "Penny loafer · Patina leather", "brandPrice": 1495, "housePrice": 1047},
    {"id": "shoe-225", "dept": "Footwear", "brand": "Berluti", "tier": "Original Luxury", "name": "Un Jour Paris", "variant": "Oxford · Patina leather", "brandPrice": 1895, "housePrice": 1327},
    {"id": "shoe-226", "dept": "Footwear", "brand": "Santoni", "tier": "Original Luxury", "name": "Double Monk Strap", "variant": "Double monk · Patina leather", "brandPrice": 1295, "housePrice": 907},
    {"id": "shoe-227", "dept": "Footwear", "brand": "Santoni", "tier": "Original Luxury", "name": "Wholecut Oxford", "variant": "Wholecut · Patina leather", "brandPrice": 1495, "housePrice": 1047},
    {"id": "shoe-228", "dept": "Footwear", "brand": "Grenson", "tier": "Premium Independent", "name": "Archie Brogue", "variant": "Brogue oxford · Black calf", "brandPrice": 495, "housePrice": 396},
    {"id": "shoe-229", "dept": "Footwear", "brand": "Grenson", "tier": "Premium Independent", "name": "Neil Loafer", "variant": "Penny loafer · Brown calf", "brandPrice": 445, "housePrice": 356},
    {"id": "shoe-230", "dept": "Footwear", "brand": "Grenson", "tier": "Premium Independent", "name": "Chadwick Chelsea", "variant": "Chelsea boot · Brown suede", "brandPrice": 495, "housePrice": 396},
    {"id": "shoe-231", "dept": "Footwear", "brand": "Common Projects", "tier": "Premium Independent", "name": "Achilles Low", "variant": "White leather sneaker", "brandPrice": 495, "housePrice": 396},
    {"id": "shoe-232", "dept": "Footwear", "brand": "Common Projects", "tier": "Premium Independent", "name": "Achilles High", "variant": "White leather high-top", "brandPrice": 545, "housePrice": 436},
    {"id": "shoe-233", "dept": "Footwear", "brand": "Common Projects", "tier": "Premium Independent", "name": "Tournament Low", "variant": "Black leather sneaker", "brandPrice": 545, "housePrice": 436},
    {"id": "shoe-234", "dept": "Footwear", "brand": "Veja", "tier": "Premium Independent", "name": "V-10", "variant": "White leather sneaker", "brandPrice": 195, "housePrice": 156},
    {"id": "shoe-235", "dept": "Footwear", "brand": "Veja", "tier": "Premium Independent", "name": "Esplar", "variant": "White leather sneaker", "brandPrice": 145, "housePrice": 116},
    {"id": "shoe-236", "dept": "Footwear", "brand": "Carmina", "tier": "Premium Independent", "name": "Split Toe Derby", "variant": "Derby · Brown calf", "brandPrice": 695, "housePrice": 556},
    {"id": "shoe-237", "dept": "Footwear", "brand": "Carmina", "tier": "Premium Independent", "name": "Penny Loafer", "variant": "Penny loafer · Brown calf", "brandPrice": 645, "housePrice": 516},
    {"id": "shoe-238", "dept": "Footwear", "brand": "Carmina", "tier": "Premium Independent", "name": "Wholecut Oxford", "variant": "Wholecut · Black calf", "brandPrice": 745, "housePrice": 596},
    {"id": "shoe-239", "dept": "Footwear", "brand": "Yuketen", "tier": "Premium Independent", "name": "Maine Guide Moc", "variant": "Moccasin · Leather", "brandPrice": 595, "housePrice": 476},
    {"id": "shoe-240", "dept": "Footwear", "brand": "Yuketen", "tier": "Premium Independent", "name": "Camp Moc", "variant": "Moccasin · Suede", "brandPrice": 545, "housePrice": 436},
]

# Bags/Leather Goods (241-270)
bags_leather = [
    {"id": "bag-241", "dept": "Bags/Leather Goods", "brand": "Carl Friedrik", "tier": "Premium Independent", "name": "Palissy Briefcase", "variant": "Grained leather · Heritage collection", "brandPrice": 795, "housePrice": 636},
    {"id": "bag-242", "dept": "Bags/Leather Goods", "brand": "Carl Friedrik", "tier": "Premium Independent", "name": "Roam Backpack", "variant": "Grained leather · Laptop compartment", "brandPrice": 495, "housePrice": 396},
    {"id": "bag-243", "dept": "Bags/Leather Goods", "brand": "Carl Friedrik", "tier": "Premium Independent", "name": "Close Briefcase", "variant": "Smooth leather · Magnetic closure", "brandPrice": 595, "housePrice": 476},
    {"id": "bag-244", "dept": "Bags/Leather Goods", "brand": "Globe-Trotter", "tier": "Original Luxury", "name": "Centenary Carry-On · 4 Wheels", "variant": "Black fibreboard · Leather trim · Handmade in England", "brandPrice": 2695, "housePrice": 2156},
    {"id": "bag-245", "dept": "Bags/Leather Goods", "brand": "Globe-Trotter", "tier": "Original Luxury", "name": "Oxford 20in Carry-On", "variant": "Vulcanised fibreboard · Leather trim", "brandPrice": 2495, "housePrice": 1996},
    {"id": "bag-246", "dept": "Bags/Leather Goods", "brand": "Globe-Trotter", "tier": "Original Luxury", "name": "Classic 20in Cabin", "variant": "Vulcanised fibreboard · Leather trim", "brandPrice": 2295, "housePrice": 1836},
    {"id": "bag-247", "dept": "Bags/Leather Goods", "brand": "RIMOWA", "tier": "Original Luxury", "name": "Original Cabin", "variant": "Silver anodised aluminium · Cabin luggage", "brandPrice": 1550, "housePrice": 1240},
    {"id": "bag-248", "dept": "Bags/Leather Goods", "brand": "RIMOWA", "tier": "Original Luxury", "name": "Original Check-In Large", "variant": "Silver anodised aluminium · Large luggage", "brandPrice": 1950, "housePrice": 1560},
    {"id": "bag-249", "dept": "Bags/Leather Goods", "brand": "RIMOWA", "tier": "Original Luxury", "name": "Classic Cabin", "variant": "Polycarbonate · Cabin luggage", "brandPrice": 1250, "housePrice": 1000},
    {"id": "bag-250", "dept": "Bags/Leather Goods", "brand": "Hermès", "tier": "Original Luxury", "name": "Bolide 31", "variant": "Clemence leather · Togo", "brandPrice": 8950, "housePrice": 6265},
    {"id": "bag-251", "dept": "Bags/Leather Goods", "brand": "Hermès", "tier": "Original Luxury", "name": "Kelly 28", "variant": "Epsom leather · Gold hardware", "brandPrice": 12950, "housePrice": 9065},
    {"id": "bag-252", "dept": "Bags/Leather Goods", "brand": "Hermès", "tier": "Original Luxury", "name": "Birkin 35", "variant": "Togo leather · Palladium hardware", "brandPrice": 14950, "housePrice": 10465},
    {"id": "bag-253", "dept": "Bags/Leather Goods", "brand": "Louis Vuitton", "tier": "Original Luxury", "name": "Keepall 55", "variant": "Monogram canvas · Natural cowhide trim", "brandPrice": 1990, "housePrice": 1592},
    {"id": "bag-254", "dept": "Bags/Leather Goods", "brand": "Louis Vuitton", "tier": "Original Luxury", "name": "Neverfull GM", "variant": "Monogram canvas · Natural cowhide trim", "brandPrice": 1790, "housePrice": 1432},
    {"id": "bag-255", "dept": "Bags/Leather Goods", "brand": "Louis Vuitton", "tier": "Original Luxury", "name": "Speedy 35", "variant": "Monogram canvas · Natural cowhide trim", "brandPrice": 1590, "housePrice": 1272},
    {"id": "bag-256", "dept": "Bags/Leather Goods", "brand": "Bottega Veneta", "tier": "Original Luxury", "name": "Cassette Bag", "variant": "Intrecciato leather · Medium", "brandPrice": 2950, "housePrice": 2360},
    {"id": "bag-257", "dept": "Bags/Leather Goods", "brand": "Bottega Veneta", "tier": "Original Luxury", "name": "Andiamo Bag", "variant": "Intrecciato leather · Large", "brandPrice": 3450, "housePrice": 2760},
    {"id": "bag-258", "dept": "Bags/Leather Goods", "brand": "Prada", "tier": "Original Luxury", "name": "Re-Nylon Backpack", "variant": "Re-Nylon · Black", "brandPrice": 1950, "housePrice": 1560},
    {"id": "bag-259", "dept": "Bags/Leather Goods", "brand": "Prada", "tier": "Original Luxury", "name": "Leather Briefcase", "variant": "Saffiano leather · Black", "brandPrice": 2450, "housePrice": 1960},
    {"id": "bag-260", "dept": "Bags/Leather Goods", "brand": "Anderson's", "tier": "Premium Independent", "name": "Classic Brown Leather Belt", "variant": "Smooth leather · Brass-tone buckle", "brandPrice": 195, "housePrice": 156},
    {"id": "bag-261", "dept": "Bags/Leather Goods", "brand": "Anderson's", "tier": "Premium Independent", "name": "Braided Leather Belt", "variant": "Braided leather · Silver-tone buckle", "brandPrice": 175, "housePrice": 140},
    {"id": "bag-262", "dept": "Bags/Leather Goods", "brand": "Montblanc", "tier": "Original Luxury", "name": "Meisterstück 6cc Wallet", "variant": "Black leather · Six credit card slots", "brandPrice": 495, "housePrice": 396},
    {"id": "bag-263", "dept": "Bags/Leather Goods", "brand": "Montblanc", "tier": "Original Luxury", "name": "Meisterstück 4cc Wallet", "variant": "Black leather · Four credit card slots", "brandPrice": 445, "housePrice": 356},
    {"id": "bag-264", "dept": "Bags/Leather Goods", "brand": "Montblanc", "tier": "Original Luxury", "name": "Sartorial Wallet", "variant": "Saffiano leather · Eight credit card slots", "brandPrice": 595, "housePrice": 476},
    {"id": "bag-265", "dept": "Bags/Leather Goods", "brand": "Bellroy", "tier": "Premium Independent", "name": "Note Sleeve Wallet", "variant": "Leather · Slim profile", "brandPrice": 119, "housePrice": 95},
    {"id": "bag-266", "dept": "Bags/Leather Goods", "brand": "Bellroy", "tier": "Premium Independent", "name": "Hide & Seek Wallet", "variant": "Leather · RFID protection", "brandPrice": 129, "housePrice": 103},
    {"id": "bag-267", "dept": "Bags/Leather Goods", "brand": "Fossil", "tier": "Accessible Collection", "name": "Derrick Leather Wallet", "variant": "Leather · Bifold", "brandPrice": 75, "housePrice": 60},
    {"id": "bag-268", "dept": "Bags/Leather Goods", "brand": "Fossil", "tier": "Accessible Collection", "name": "Travis Leather Wallet", "variant": "Leather · Trifold", "brandPrice": 65, "housePrice": 52},
    {"id": "bag-269", "dept": "Bags/Leather Goods", "brand": "Tumi", "tier": "Premium Independent", "name": "Alpha Bravo Briefcase", "variant": "Ballistic nylon · Laptop compartment", "brandPrice": 595, "housePrice": 476},
    {"id": "bag-270", "dept": "Bags/Leather Goods", "brand": "Tumi", "tier": "Premium Independent", "name": "Alpha 3 Expandable Backpack", "variant": "Ballistic nylon · Laptop compartment", "brandPrice": 495, "housePrice": 396},
]

# Accessories (271-300)
accessories = [
    {"id": "acc-271", "dept": "Accessories", "brand": "Drake's", "tier": "Original Luxury", "name": "Navy Large Knot Grenadine Tipped Tie", "variant": "100% silk · Hand-rolled blades · Handmade in London", "brandPrice": 275, "housePrice": 220},
    {"id": "acc-272", "dept": "Accessories", "brand": "Drake's", "tier": "Original Luxury", "name": "Burgundy Grenadine Tie", "variant": "100% silk · Hand-rolled blades", "brandPrice": 255, "housePrice": 204},
    {"id": "acc-273", "dept": "Accessories", "brand": "Drake's", "tier": "Original Luxury", "name": "Printed Silk Tie", "variant": "100% silk · Hand-rolled blades", "brandPrice": 235, "housePrice": 188},
    {"id": "acc-274", "dept": "Accessories", "brand": "Charvet", "tier": "Original Luxury", "name": "Silk Tie", "variant": "100% silk · Hand-rolled blades", "brandPrice": 395, "housePrice": 316},
    {"id": "acc-275", "dept": "Accessories", "brand": "Charvet", "tier": "Original Luxury", "name": "Knit Silk Tie", "variant": "100% silk · Knit construction", "brandPrice": 345, "housePrice": 276},
    {"id": "acc-276", "dept": "Accessories", "brand": "Turnbull & Asser", "tier": "Original Luxury", "name": "Silk Tie", "variant": "100% silk · Hand-rolled blades", "brandPrice": 295, "housePrice": 236},
    {"id": "acc-277", "dept": "Accessories", "brand": "Turnbull & Asser", "tier": "Original Luxury", "name": "Paisley Silk Tie", "variant": "100% silk · Hand-rolled blades", "brandPrice": 315, "housePrice": 252},
    {"id": "acc-278", "dept": "Accessories", "brand": "Benson & Clegg", "tier": "Premium Independent", "name": "Silk Tie", "variant": "100% silk · Hand-rolled blades", "brandPrice": 185, "housePrice": 148},
    {"id": "acc-279", "dept": "Accessories", "brand": "Benson & Clegg", "tier": "Premium Independent", "name": "Knit Silk Tie", "variant": "100% silk · Knit construction", "brandPrice": 165, "housePrice": 132},
    {"id": "acc-280", "dept": "Accessories", "brand": "Persol", "tier": "Original Luxury", "name": "714 Original Folding Sunglasses", "variant": "Havana frame · Green lenses · Handmade in Italy", "brandPrice": 452, "housePrice": 362},
    {"id": "acc-281", "dept": "Accessories", "brand": "Persol", "tier": "Original Luxury", "name": "649 Series Sunglasses", "variant": "Havana frame · Brown lenses", "brandPrice": 342, "housePrice": 274},
    {"id": "acc-282", "dept": "Accessories", "brand": "Ray-Ban", "tier": "Accessible Collection", "name": "Clubmaster Classic", "variant": "Black on gold · G-15 green lenses", "brandPrice": 191, "housePrice": 153},
    {"id": "acc-283", "dept": "Accessories", "brand": "Ray-Ban", "tier": "Accessible Collection", "name": "Aviator Classic", "variant": "Gold frame · G-15 green lenses", "brandPrice": 171, "housePrice": 137},
    {"id": "acc-284", "dept": "Accessories", "brand": "Ray-Ban", "tier": "Accessible Collection", "name": "Wayfarer Classic", "variant": "Black frame · G-15 green lenses", "brandPrice": 181, "housePrice": 145},
    {"id": "acc-285", "dept": "Accessories", "brand": "Oliver Peoples", "tier": "Premium Independent", "name": "Gregory Peck Sunglasses", "variant": "Tortoise frame · G-15 green lenses", "brandPrice": 495, "housePrice": 396},
    {"id": "acc-286", "dept": "Accessories", "brand": "Oliver Peoples", "tier": "Premium Independent", "name": "Oliver Sunglasses", "variant": "Tortoise frame · Grey gradient lenses", "brandPrice": 445, "housePrice": 356},
    {"id": "acc-287", "dept": "Accessories", "brand": "Moscot", "tier": "Premium Independent", "name": "Lemtosh Sunglasses", "variant": "Tortoise frame · G-15 green lenses", "brandPrice": 345, "housePrice": 276},
    {"id": "acc-288", "dept": "Accessories", "brand": "Moscot", "tier": "Premium Independent", "name": "Miltzen Sunglasses", "variant": "Black frame · G-15 green lenses", "brandPrice": 295, "housePrice": 236},
    {"id": "acc-289", "dept": "Accessories", "brand": "Acqua di Parma", "tier": "Original Luxury", "name": "Colonia Eau de Cologne", "variant": "100 ml · Italian citrus cologne", "brandPrice": 233, "housePrice": 186},
    {"id": "acc-290", "dept": "Accessories", "brand": "Acqua di Parma", "tier": "Original Luxury", "name": "Colonia Club", "variant": "100 ml · Citrus aromatic", "brandPrice": 245, "housePrice": 196},
    {"id": "acc-291", "dept": "Accessories", "brand": "Creed", "tier": "Original Luxury", "name": "Aventus Eau de Parfum", "variant": "100 ml · Fruity woods fragrance", "brandPrice": 495, "housePrice": 396},
    {"id": "acc-292", "dept": "Accessories", "brand": "Creed", "tier": "Original Luxury", "name": "Green Irish Tweed", "variant": "100 ml · Fresh fougère", "brandPrice": 445, "housePrice": 356},
    {"id": "acc-293", "dept": "Accessories", "brand": "Creed", "tier": "Original Luxury", "name": "Silver Mountain Water", "variant": "100 ml · Fresh aquatic", "brandPrice": 445, "housePrice": 356},
    {"id": "acc-294", "dept": "Accessories", "brand": "Tom Ford", "tier": "Original Luxury", "name": "Oud Wood Eau de Parfum", "variant": "100 ml · Oud fragrance", "brandPrice": 395, "housePrice": 316},
    {"id": "acc-295", "dept": "Accessories", "brand": "Tom Ford", "tier": "Original Luxury", "name": "Tobacco Vanille", "variant": "100 ml · Spicy gourmand", "brandPrice": 345, "housePrice": 276},
    {"id": "acc-296", "dept": "Accessories", "brand": "Tom Ford", "tier": "Original Luxury", "name": "Neroli Portofino", "variant": "100 ml · Citrus floral", "brandPrice": 345, "housePrice": 276},
    {"id": "acc-297", "dept": "Accessories", "brand": "Hermès", "tier": "Original Luxury", "name": "H24 Eau de Parfum", "variant": "100 ml · Woody aromatic", "brandPrice": 195, "housePrice": 156},
    {"id": "acc-298", "dept": "Accessories", "brand": "Hermès", "tier": "Original Luxury", "name": "Terre d'Hermès", "variant": "100 ml · Woody citrus", "brandPrice": 185, "housePrice": 148},
    {"id": "acc-299", "dept": "Accessories", "brand": "Hermès", "tier": "Original Luxury", "name": "Un Jardin sur le Nil", "variant": "100 ml · Green floral", "brandPrice": 175, "housePrice": 140},
    {"id": "acc-300", "dept": "Accessories", "brand": "Dior", "tier": "Original Luxury", "name": "Sauvage Eau de Parfum", "variant": "100 ml · Fresh fougère", "brandPrice": 165, "housePrice": 132},
]

# ============================================================================
# WATCH PRODUCTS - All 13 Categories (80+ products total)
# ============================================================================

# Category 1: Entry-Level Automatics (watch-001 to watch-006)
entry_automatics = [
    {"id": "watch-001", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Presage Cocktail Time SRPB41", "variant": "40.5 mm · Blue dial · Automatic", "brandPrice": 475, "signaturePrice": 475, "essentialPrice": 399},
    {"id": "watch-002", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Presage Cocktail Time SRPB43", "variant": "40.5 mm · White dial · Automatic", "brandPrice": 475, "signaturePrice": 475, "essentialPrice": 399},
    {"id": "watch-003", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Presage Enamel SRPB09", "variant": "40 mm · White enamel dial · Automatic", "brandPrice": 550, "signaturePrice": 550, "essentialPrice": 449},
    {"id": "watch-004", "dept": "Watches", "brand": "Tissot", "tier": "Premium Independent", "name": "PRX Powermatic 80", "variant": "40 mm · Blue dial · Automatic", "brandPrice": 850, "signaturePrice": 850, "essentialPrice": 699},
    {"id": "watch-005", "dept": "Watches", "brand": "Tissot", "tier": "Premium Independent", "name": "PRX Powermatic 80", "variant": "40 mm · Silver dial · Automatic", "brandPrice": 850, "signaturePrice": 850, "essentialPrice": 699},
    {"id": "watch-006", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Field Auto 38 mm", "variant": "Green dial · Automatic · Ref. H70455560", "brandPrice": 795, "signaturePrice": 795, "essentialPrice": 649},
]

# Category 2: Field Watches (watch-007 to watch-012)
field_watches = [
    {"id": "watch-007", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Field Mechanical 38 mm", "variant": "Black dial · Manual · Ref. H69439931", "brandPrice": 595, "signaturePrice": 595, "essentialPrice": 499},
    {"id": "watch-008", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Field Expedition", "variant": "37 mm · Black dial · Quartz", "brandPrice": 345, "signaturePrice": 345, "essentialPrice": 299},
    {"id": "watch-009", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Field King Auto", "variant": "40 mm · Black dial · Automatic", "brandPrice": 695, "signaturePrice": 695, "essentialPrice": 579},
    {"id": "watch-010", "dept": "Watches", "brand": "Laco", "tier": "Premium Independent", "name": "Kiel Field Watch", "variant": "42 mm · Black dial · Automatic", "brandPrice": 495, "signaturePrice": 495, "essentialPrice": 419},
    {"id": "watch-011", "dept": "Watches", "brand": "Laco", "tier": "Premium Independent", "name": "Koblenz Field Watch", "variant": "39 mm · Black dial · Automatic", "brandPrice": 445, "signaturePrice": 445, "essentialPrice": 379},
    {"id": "watch-012", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "556", "variant": "38.5 mm · Black dial · Automatic", "brandPrice": 1295, "signaturePrice": 1295, "essentialPrice": 999},
]

# Category 3: Diver Watches (watch-013 to watch-018)
diver_watches = [
    {"id": "watch-013", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Prospex Solar Diver", "variant": "44 mm · Black dial · Solar", "brandPrice": 395, "signaturePrice": 395, "essentialPrice": 329},
    {"id": "watch-014", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Prospex Turtle", "variant": "45 mm · Black dial · Automatic", "brandPrice": 495, "signaturePrice": 495, "essentialPrice": 419},
    {"id": "watch-015", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Prospex Samurai", "variant": "44 mm · Blue dial · Automatic", "brandPrice": 545, "signaturePrice": 545, "essentialPrice": 449},
    {"id": "watch-016", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Navy Scuba", "variant": "40 mm · Blue dial · Automatic", "brandPrice": 795, "signaturePrice": 795, "essentialPrice": 649},
    {"id": "watch-017", "dept": "Watches", "brand": "Oris", "tier": "Premium Independent", "name": "Aquis Date", "variant": "41.5 mm · Blue dial · Automatic", "brandPrice": 2150, "signaturePrice": 2150, "essentialPrice": 1699},
    {"id": "watch-018", "dept": "Watches", "brand": "Oris", "tier": "Premium Independent", "name": "Aquis Small Second", "variant": "43 mm · Black dial · Automatic", "brandPrice": 2350, "signaturePrice": 2350, "essentialPrice": 1899},
]

# Category 4: Pilot Watches (watch-019 to watch-024)
pilot_watches = [
    {"id": "watch-019", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Aviation Pilot", "variant": "42 mm · Black dial · Quartz", "brandPrice": 495, "signaturePrice": 495, "essentialPrice": 419},
    {"id": "watch-020", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Aviation Auto Chrono", "variant": "44 mm · Black dial · Automatic", "brandPrice": 1895, "signaturePrice": 1895, "essentialPrice": 1499},
    {"id": "watch-021", "dept": "Watches", "brand": "IWC", "tier": "Original Luxury", "name": "Pilot's Watch Mark XVIII", "variant": "40 mm · Black dial · Automatic", "brandPrice": 4295, "signaturePrice": 4295, "essentialPrice": 3299},
    {"id": "watch-022", "dept": "Watches", "brand": "IWC", "tier": "Original Luxury", "name": "Pilot's Watch Automatic 36", "variant": "36 mm · Blue dial · Automatic", "brandPrice": 4495, "signaturePrice": 4495, "essentialPrice": 3499},
    {"id": "watch-023", "dept": "Watches", "brand": "Laco", "tier": "Premium Independent", "name": "Kiel Pilot", "variant": "42 mm · Black dial · Automatic", "brandPrice": 595, "signaturePrice": 595, "essentialPrice": 499},
    {"id": "watch-024", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "104", "variant": "41 mm · Black dial · Automatic", "brandPrice": 1495, "signaturePrice": 1495, "essentialPrice": 1199},
]

# Category 5: Dress Watches (watch-025 to watch-030)
dress_watches = [
    {"id": "watch-025", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Presage Cocktail Time", "variant": "40.5 mm · Sunburst dial · Automatic", "brandPrice": 525, "signaturePrice": 525, "essentialPrice": 449},
    {"id": "watch-026", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Presage Line", "variant": "39 mm · White dial · Automatic", "brandPrice": 425, "signaturePrice": 425, "essentialPrice": 359},
    {"id": "watch-027", "dept": "Watches", "brand": "Tissot", "tier": "Premium Independent", "name": "Le Locle Powermatic 80", "variant": "39.3 mm · Silver dial · Automatic", "brandPrice": 595, "signaturePrice": 595, "essentialPrice": 499},
    {"id": "watch-028", "dept": "Watches", "brand": "Tissot", "tier": "Premium Independent", "name": "Gentleman Powermatic 80", "variant": "40 mm · Silver dial · Automatic", "brandPrice": 695, "signaturePrice": 695, "essentialPrice": 579},
    {"id": "watch-029", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Ventura", "variant": "32 mm · Black dial · Quartz", "brandPrice": 795, "signaturePrice": 795, "essentialPrice": 649},
    {"id": "watch-030", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Jazzmaster Viewmatic", "variant": "40 mm · Silver dial · Automatic", "brandPrice": 895, "signaturePrice": 895, "essentialPrice": 729},
]

# Category 6: Chronograph Watches (watch-031 to watch-036)
chronograph_watches = [
    {"id": "watch-031", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Prospex Solar Chronograph", "variant": "44 mm · Black dial · Solar", "brandPrice": 445, "signaturePrice": 445, "essentialPrice": 379},
    {"id": "watch-032", "dept": "Watches", "brand": "Tissot", "tier": "Premium Independent", "name": "PRX Quartz Chronograph", "variant": "42 mm · Blue dial · Quartz", "brandPrice": 695, "signaturePrice": 695, "essentialPrice": 579},
    {"id": "watch-033", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Aviation Auto Chrono", "variant": "44 mm · Black dial · Automatic", "brandPrice": 1895, "signaturePrice": 1895, "essentialPrice": 1499},
    {"id": "watch-034", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Jazzmaster Chronograph", "variant": "42 mm · Silver dial · Automatic", "brandPrice": 1095, "signaturePrice": 1095, "essentialPrice": 899},
    {"id": "watch-035", "dept": "Watches", "brand": "Oris", "tier": "Premium Independent", "name": "Big Crown Pointer Date", "variant": "40 mm · Bronze dial · Automatic", "brandPrice": 1995, "signaturePrice": 1995, "essentialPrice": 1599},
    {"id": "watch-036", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "104 St Sa I", "variant": "41 mm · Black dial · Automatic", "brandPrice": 1895, "signaturePrice": 1895, "essentialPrice": 1499},
]

# Category 7: GMT/World Time (watch-037 to watch-042)
gmt_watches = [
    {"id": "watch-037", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "Prospex Solar GMT", "variant": "44 mm · Black dial · Solar", "brandPrice": 495, "signaturePrice": 495, "essentialPrice": 419},
    {"id": "watch-038", "dept": "Watches", "brand": "Seiko", "tier": "Accessible Collection", "name": "5 Sports GMT", "variant": "42.5 mm · Black dial · Automatic", "brandPrice": 595, "signaturePrice": 595, "essentialPrice": 499},
    {"id": "watch-039", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Aviation GMT", "variant": "44 mm · Black dial · Automatic", "brandPrice": 1195, "signaturePrice": 1195, "essentialPrice": 999},
    {"id": "watch-040", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Navy GMT", "variant": "42 mm · Blue dial · Automatic", "brandPrice": 1295, "signaturePrice": 1295, "essentialPrice": 1099},
    {"id": "watch-041", "dept": "Watches", "brand": "Oris", "tier": "Premium Independent", "name": "Aquis GMT Date", "variant": "43.5 mm · Blue dial · Automatic", "brandPrice": 2950, "signaturePrice": 2950, "essentialPrice": 2399},
    {"id": "watch-042", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "105 St Sa UTC", "variant": "41 mm · Black dial · Automatic", "brandPrice": 1795, "signaturePrice": 1795, "essentialPrice": 1449},
]

# Category 8: Tool Watches (watch-043 to watch-048)
tool_watches = [
    {"id": "watch-043", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "556 I", "variant": "38.5 mm · Black dial · Automatic", "brandPrice": 1295, "signaturePrice": 1295, "essentialPrice": 999},
    {"id": "watch-044", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "856", "variant": "43 mm · Black dial · Automatic", "brandPrice": 2195, "signaturePrice": 2195, "essentialPrice": 1799},
    {"id": "watch-045", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "104 St Sa", "variant": "41 mm · Black dial · Automatic", "brandPrice": 1595, "signaturePrice": 1595, "essentialPrice": 1299},
    {"id": "watch-046", "dept": "Watches", "brand": "Laco", "tier": "Premium Independent", "name": "Frankfurt GMT", "variant": "42 mm · Black dial · Automatic", "brandPrice": 695, "signaturePrice": 695, "essentialPrice": 579},
    {"id": "watch-047", "dept": "Watches", "brand": "Damasko", "tier": "Premium Independent", "name": "DS30", "variant": "40 mm · Black dial · Automatic", "brandPrice": 1595, "signaturePrice": 1595, "essentialPrice": 1299},
    {"id": "watch-048", "dept": "Watches", "brand": "Damasko", "tier": "Premium Independent", "name": "DC80", "variant": "40 mm · Black dial · Automatic", "brandPrice": 2295, "signaturePrice": 2295, "essentialPrice": 1899},
]

# Category 9: Luxury Sports (watch-049 to watch-054)
luxury_sports = [
    {"id": "watch-049", "dept": "Watches", "brand": "Oris", "tier": "Premium Independent", "name": "Aquis Date", "variant": "41.5 mm · Blue dial · Automatic", "brandPrice": 2150, "signaturePrice": 2150, "essentialPrice": 1699},
    {"id": "watch-050", "dept": "Watches", "brand": "Oris", "tier": "Premium Independent", "name": "Aquis Date Upcycle", "variant": "41.5 mm · Grey dial · Automatic", "brandPrice": 2250, "signaturePrice": 2250, "essentialPrice": 1799},
    {"id": "watch-051", "dept": "Watches", "brand": "Oris", "tier": "Premium Independent", "name": "Big Crown ProPilot", "variant": "41 mm · Blue dial · Automatic", "brandPrice": 1995, "signaturePrice": 1995, "essentialPrice": 1599},
    {"id": "watch-052", "dept": "Watches", "brand": "Bell & Ross", "tier": "Original Luxury", "name": "BR 03-92", "variant": "42 mm · Black dial · Automatic", "brandPrice": 3495, "signaturePrice": 3495, "essentialPrice": 2799},
    {"id": "watch-053", "dept": "Watches", "brand": "Bell & Ross", "tier": "Original Luxury", "name": "BR 05", "variant": "40 mm · Black dial · Automatic", "brandPrice": 4295, "signaturePrice": 4295, "essentialPrice": 3499},
    {"id": "watch-054", "dept": "Watches", "brand": "Bell & Ross", "tier": "Original Luxury", "name": "BR V2-92", "variant": "41 mm · Black dial · Automatic", "brandPrice": 3295, "signaturePrice": 3295, "essentialPrice": 2699},
]

# Category 10: Heritage/Vintage (watch-055 to watch-060)
heritage_watches = [
    {"id": "watch-055", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Ventura", "variant": "32 mm · Black dial · Quartz", "brandPrice": 795, "signaturePrice": 795, "essentialPrice": 649},
    {"id": "watch-056", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Ventura XXL", "variant": "42 mm · Black dial · Quartz", "brandPrice": 895, "signaturePrice": 895, "essentialPrice": 729},
    {"id": "watch-057", "dept": "Watches", "brand": "Hamilton", "tier": "Premium Independent", "name": "Khaki Field Vintage", "variant": "38 mm · Black dial · Hand-wound", "brandPrice": 545, "signaturePrice": 545, "essentialPrice": 449},
    {"id": "watch-058", "dept": "Watches", "brand": "Longines", "tier": "Premium Independent", "name": "Heritage Classic", "variant": "38.5 mm · Black dial · Automatic", "brandPrice": 2150, "signaturePrice": 2150, "essentialPrice": 1799},
    {"id": "watch-059", "dept": "Watches", "brand": "Longines", "tier": "Premium Independent", "name": "Spirit Collection", "variant": "40 mm · Blue dial · Automatic", "brandPrice": 2350, "signaturePrice": 2350, "essentialPrice": 1899},
    {"id": "watch-060", "dept": "Watches", "brand": "Longines", "tier": "Premium Independent", "name": "Master Collection", "variant": "40 mm · Silver dial · Automatic", "brandPrice": 1950, "signaturePrice": 1950, "essentialPrice": 1599},
]

# Category 11: Technical/Specialty (watch-061 to watch-066)
technical_watches = [
    {"id": "watch-061", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "U1", "variant": "44 mm · Black dial · Automatic", "brandPrice": 1995, "signaturePrice": 1995, "essentialPrice": 1599},
    {"id": "watch-062", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "U2", "variant": "44 mm · Black dial · Automatic", "brandPrice": 2195, "signaturePrice": 2195, "essentialPrice": 1799},
    {"id": "watch-063", "dept": "Watches", "brand": "Sinn", "tier": "Premium Independent", "name": "EZM 13", "variant": "44 mm · Black dial · Automatic", "brandPrice": 2695, "signaturePrice": 2695, "essentialPrice": 2199},
    {"id": "watch-064", "dept": "Watches", "brand": "Damasko", "tier": "Premium Independent", "name": "DS30", "variant": "40 mm · Black dial · Automatic", "brandPrice": 1595, "signaturePrice": 1595, "essentialPrice": 1299},
    {"id": "watch-065", "dept": "Watches", "brand": "Damasko", "tier": "Premium Independent", "name": "DC80", "variant": "40 mm · Black dial · Automatic", "brandPrice": 2295, "signaturePrice": 2295, "essentialPrice": 1899},
    {"id": "watch-066", "dept": "Watches", "brand": "Bremont", "tier": "Premium Independent", "name": "Airco Mach 1", "variant": "40 mm · Black dial · Automatic", "brandPrice": 3495, "signaturePrice": 3495, "essentialPrice": 2799},
]

# Category 12: Contemporary Design (watch-067 to watch-072)
contemporary_watches = [
    {"id": "watch-067", "dept": "Watches", "brand": "Junghans", "tier": "Premium Independent", "name": "Max Bill Quartz", "variant": "38 mm · Silver dial · Quartz", "brandPrice": 495, "signaturePrice": 495, "essentialPrice": 419},
    {"id": "watch-068", "dept": "Watches", "brand": "Junghans", "tier": "Premium Independent", "name": "Max Bill Automatic", "variant": "38 mm · Silver dial · Automatic", "brandPrice": 895, "signaturePrice": 895, "essentialPrice": 729},
    {"id": "watch-069", "dept": "Watches", "brand": "Nomos", "tier": "Premium Independent", "name": "Tangente", "variant": "35 mm · White dial · Manual", "brandPrice": 1895, "signaturePrice": 1895, "essentialPrice": 1599},
    {"id": "watch-070", "dept": "Watches", "brand": "Nomos", "tier": "Premium Independent", "name": "Club", "variant": "36 mm · Black dial · Automatic", "brandPrice": 1995, "signaturePrice": 1995, "essentialPrice": 1699},
    {"id": "watch-071", "dept": "Watches", "brand": "Maurice Lacroix", "tier": "Premium Independent", "name": "Aikon", "variant": "42 mm · Blue dial · Automatic", "brandPrice": 1795, "signaturePrice": 1795, "essentialPrice": 1499},
    {"id": "watch-072", "dept": "Watches", "brand": "Maurice Lacroix", "tier": "Premium Independent", "name": "Pontos S Diver", "variant": "43 mm · Black dial · Automatic", "brandPrice": 2295, "signaturePrice": 2295, "essentialPrice": 1899},
]

# Category 13: Premium Luxury (watch-073 to watch-080)
premium_luxury = [
    {"id": "watch-073", "dept": "Watches", "brand": "IWC", "tier": "Original Luxury", "name": "Portugieser Automatic", "variant": "40.4 mm · Blue dial · Automatic", "brandPrice": 7495, "signaturePrice": 7495, "essentialPrice": 5999},
    {"id": "watch-074", "dept": "Watches", "brand": "IWC", "tier": "Original Luxury", "name": "Portugieser Chronograph", "variant": "41 mm · Blue dial · Automatic", "brandPrice": 9495, "signaturePrice": 9495, "essentialPrice": 7499},
    {"id": "watch-075", "dept": "Watches", "brand": "Jaeger-LeCoultre", "tier": "Original Luxury", "name": "Master Ultra Thin", "variant": "39 mm · Silver dial · Automatic", "brandPrice": 8495, "signaturePrice": 8495, "essentialPrice": 6799},
    {"id": "watch-076", "dept": "Watches", "brand": "Jaeger-LeCoultre", "tier": "Original Luxury", "name": "Reverso Classic", "variant": "40 mm · Silver dial · Manual", "brandPrice": 7995, "signaturePrice": 7995, "essentialPrice": 6399},
    {"id": "watch-077", "dept": "Watches", "brand": "Cartier", "tier": "Original Luxury", "name": "Santos de Cartier", "variant": "39.8 mm · Silver dial · Automatic", "brandPrice": 7995, "signaturePrice": 7995, "essentialPrice": 6399},
    {"id": "watch-078", "dept": "Watches", "brand": "Cartier", "tier": "Original Luxury", "name": "Tank Must", "variant": "33 mm · Silver dial · Quartz", "brandPrice": 3495, "signaturePrice": 3495, "essentialPrice": 2799},
    {"id": "watch-079", "dept": "Watches", "brand": "Omega", "tier": "Original Luxury", "name": "Seamaster Aqua Terra", "variant": "41 mm · Blue dial · Automatic", "brandPrice": 5495, "signaturePrice": 5495, "essentialPrice": 4499},
    {"id": "watch-080", "dept": "Watches", "brand": "Omega", "tier": "Original Luxury", "name": "Speedmaster Professional", "variant": "42 mm · Black dial · Manual", "brandPrice": 6495, "signaturePrice": 6495, "essentialPrice": 5199},
]

# ============================================================================
# PROCESS CLOTHING PRODUCTS
# ============================================================================

def process_clothing_product(product):
    """Process a clothing product and add standard fields"""
    return {
        "id": product["id"],
        "dept": product["dept"],
        "brand": product["brand"],
        "tier": product["tier"],
        "name": product["name"],
        "variant": product["variant"],
        "brandPrice": product["brandPrice"],
        "housePrice": product["housePrice"],
        "currency": "USD",
        "image": "assets/van-patten-alastor-crest.png",
        "url": f"https://www.google.com/search?q={product['brand'].replace(' ', '+')}+{product['name'].replace(' ', '+')}",
        "note": f"Brand US list price observed at ${product['brandPrice']:,}. VPA House price is a confidential membership rate."
    }

# ============================================================================
# PROCESS WATCH PRODUCTS
# ============================================================================

def process_watch_product(product):
    """Process a watch product and add standard fields"""
    return {
        "id": product["id"],
        "dept": product["dept"],
        "brand": product["brand"],
        "tier": product["tier"],
        "name": product["name"],
        "variant": product["variant"],
        "brandPrice": product["brandPrice"],
        "signaturePrice": product["signaturePrice"],  # Renamed from housePrice
        "essentialPrice": product["essentialPrice"],  # Additional field for watches
        "currency": "USD",
        "image": "assets/van-patten-alastor-crest.png",
        "url": f"https://www.google.com/search?q={product['brand'].replace(' ', '+')}+{product['name'].replace(' ', '+')}",
        "note": f"Brand US list price observed at ${product['brandPrice']:,}. VPA Signature price: ${product['signaturePrice']:,}. VPA Essential price: ${product['essentialPrice']:,}."
    }

# ============================================================================
# COMBINE ALL PRODUCTS
# ============================================================================

# Combine all clothing categories
all_clothing = (
    coats_outerwear +
    suits_formal +
    blazers_sportcoats +
    shirts_polos +
    knitwear +
    trousers +
    denim +
    footwear +
    bags_leather +
    accessories
)

# Combine all watch categories
all_watches = (
    entry_automatics +
    field_watches +
    diver_watches +
    pilot_watches +
    dress_watches +
    chronograph_watches +
    gmt_watches +
    tool_watches +
    luxury_sports +
    heritage_watches +
    technical_watches +
    contemporary_watches +
    premium_luxury
)

# Process all products
final_clothing = [process_clothing_product(p) for p in all_clothing]
final_watches = [process_watch_product(p) for p in all_watches]

# Combine all final products
all_final_products = final_clothing + final_watches

# ============================================================================
# OUTPUT TO JSON
# ============================================================================

output_file = "products.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_final_products, f, indent=2, ensure_ascii=False)

# Print summary
print("=" * 70)
print("VAN PATTEN ALASTOR V3 - COMPLETE CATALOGUE GENERATION")
print("=" * 70)
print(f"Clothing Products Generated: {len(final_clothing)}")
print(f"  - Coats & Outerwear: {len(coats_outerwear)}")
print(f"  - Suits & Formal Tailoring: {len(suits_formal)}")
print(f"  - Blazers/Sport Coats: {len(blazers_sportcoats)}")
print(f"  - Shirts & Polos: {len(shirts_polos)}")
print(f"  - Knitwear: {len(knitwear)}")
print(f"  - Trousers: {len(trousers)}")
print(f"  - Denim: {len(denim)}")
print(f"  - Footwear: {len(footwear)}")
print(f"  - Bags/Leather Goods: {len(bags_leather)}")
print(f"  - Accessories: {len(accessories)}")
print()
print(f"Watch Products Generated: {len(final_watches)}")
print(f"  - Entry-Level Automatics: {len(entry_automatics)}")
print(f"  - Field Watches: {len(field_watches)}")
print(f"  - Diver Watches: {len(diver_watches)}")
print(f"  - Pilot Watches: {len(pilot_watches)}")
print(f"  - Dress Watches: {len(dress_watches)}")
print(f"  - Chronograph Watches: {len(chronograph_watches)}")
print(f"  - GMT/World Time: {len(gmt_watches)}")
print(f"  - Tool Watches: {len(tool_watches)}")
print(f"  - Luxury Sports: {len(luxury_sports)}")
print(f"  - Heritage/Vintage: {len(heritage_watches)}")
print(f"  - Technical/Specialty: {len(technical_watches)}")
print(f"  - Contemporary Design: {len(contemporary_watches)}")
print(f"  - Premium Luxury: {len(premium_luxury)}")
print()
print(f"TOTAL PRODUCTS: {len(all_final_products)}")
print(f"Output file: {output_file}")
print("=" * 70)
