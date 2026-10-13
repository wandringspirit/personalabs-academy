# -*- coding: utf-8 -*-
"""
Generator for PersonaLabs Academy Order Bump #2:
500+ Viral Reel Hooks, Live Smartphone Simulator & ManyChat Auto-DM Studio
"""
import json, os

output_vault = r"C:\Projects\ai-influencer-course-website\course-vault\hooks-vip-3d7e91b2.html"
output_drive = r"C:\Projects\ai-influencer-course-website\videos-captioned\03-500-Viral-Hooks-And-Prompts-Pack\500-Viral-Reel-Hooks-And-AutoDM-Pack.html"

CATEGORIES = [
    {"id": "curiosity", "name": "Curiosity & Infinite Loop", "icon": "🔍", "color": "#06b6d4"},
    {"id": "luxury", "name": "Luxury & Old-Money Lifestyle", "icon": "🥂", "color": "#f59e0b"},
    {"id": "desi", "name": "Indian Festive & Desi Culture", "icon": "🇮🇳", "color": "#ec4899"},
    {"id": "pov", "name": "POV & Parasocial Connection", "icon": "💕", "color": "#8b5cf6"},
    {"id": "debate", "name": "Controversy & Comment Magnet", "icon": "🔥", "color": "#ef4444"},
    {"id": "aireveal", "name": "AI Metagame & Virtual Reveal", "icon": "🤖", "color": "#10b981"},
    {"id": "fashion", "name": "Fashion, OOTD & Saree Dupes", "icon": "👗", "color": "#a855f7"},
    {"id": "income", "name": "Creator Income & Side Hustle", "icon": "💰", "color": "#eab308"}
]

# 80 Curated Primary Blueprints
PRIMARY_HOOKS = [
    # CURIOSITY & LOOP
    {"cat": "curiosity", "text": "Wait until you notice what's behind me in the mirror... 😳", "visual": "4.5s candid bedroom mirror selfie, subtle hair-tuck, warm low-light aesthetic", "audio": "118 BPM Phonetic Synth Pulse", "keyword": "MIRROR", "note": "Forces viewers to loop the video 3x searching for the detail."},
    {"cat": "curiosity", "text": "99% of people scroll past without noticing the mistake in this clip 👀", "visual": "Slow cinematic pan across hotel balcony overlooking city skyline, wind in hair", "audio": "Suspense Ambient Build", "keyword": "SPOT", "note": "Skyrockets retention past 180% as viewers re-read and re-watch."},
    {"cat": "curiosity", "text": "My friends begged me to delete the 3rd slide immediately 🙈", "visual": "4-photo carousel transition with candid laughing pose in luxury cafe", "audio": "Trending Lo-Fi Piano", "keyword": "SLIDE", "note": "Massive swipe-through completion rate on carousel reels."},
    {"cat": "curiosity", "text": "Pause at 0:02 if you have sharp eyes... do you see it?", "visual": "Quick 2.5s motion turning around with slight smile towards camera", "audio": "Ticking Clock Bass", "keyword": "PAUSE", "note": "Instagram algorithm registers pause taps as high engagement."},
    {"cat": "curiosity", "text": "I wasn't going to post this unedited clip from last night, but...", "visual": "Warm tungsten restaurant ambiance, holding drink and glancing up at camera", "audio": "Deep House Whisper", "keyword": "UNEDITED", "note": "Creates intimate exclusivity feel that drives DM inquiries."},
    {"cat": "curiosity", "text": "Look closely at my eyes for 3 seconds and tell me what feels different ✨", "visual": "Extreme close-up macro portrait, natural sunlight catching iris reflections", "audio": "Ethereal Dream Chime", "keyword": "EYES", "note": "Sparks AI vs Real debates in comments."},
    {"cat": "curiosity", "text": "Don't check my story highlight unless you're ready for the plot twist 🤫", "visual": "Walking away down luxury hotel hallway, looking back over shoulder once", "audio": "Midnight City Beat", "keyword": "STORY", "note": "Drives viewers straight to your profile story highlights."},
    {"cat": "curiosity", "text": "The reason I never take photos from my left side... until today", "visual": "Slow side-profile turn in Kling AI, golden hour sun highlighting jawline", "audio": "Soft Violin Pluck", "keyword": "SIDE", "note": "Triggers empathy and compliment comments."},
    {"cat": "curiosity", "text": "Read the first word of every line in the caption... 💌", "visual": "Quiet coffee shop writing in notebook, glancing out rain-streaked window", "audio": "Rain & Lo-Fi Beats", "keyword": "SECRET", "note": "Holds viewers on video for 12+ seconds reading caption."},
    {"cat": "curiosity", "text": "I bet ₹500 you can't guess which city I'm in right now 🌍", "visual": "Rooftop terrace with blurred landmark in distant bokeh background", "audio": "Upbeat Acoustic Strut", "keyword": "GUESS", "note": "Generates 300+ city guesses in comments."},
    {"cat": "curiosity", "text": "The last 2 seconds of this video will make you rethink everything 🤯", "visual": "Walking through art gallery, camera tracks backward as she stops and smiles", "audio": "Bass Drop Climax", "keyword": "END", "note": "Ensures 100% completion rate."},
    {"cat": "curiosity", "text": "Something happened at 0:03 that ruined this entire take... 🙈", "visual": "Blowing wind catches hair while posing on windy seaside promenade", "audio": "Playful Upbeat Pop", "keyword": "TAKE", "note": "Playful relatable curiosity hook."},
    {"cat": "curiosity", "text": "They said this camera angle only works for 1% of faces... test it with me", "visual": "High-angle selfie camera tilt downward with direct eye contact", "audio": "Trending TikTok Synth", "keyword": "ANGLE", "note": "Saves for photography posing inspiration."},
    {"cat": "curiosity", "text": "Promise you won't judge what I keep in my bag at all times 👜", "visual": "Sitting in café, unzipping designer handbag and smiling mischievously", "audio": "Bossa Nova Chill", "keyword": "BAG", "note": "High engagement curiosity hook."},
    {"cat": "curiosity", "text": "If this Reel reached you, the algorithm knows something you don't 🔮", "visual": "Dramatic twilight lighting, eyes tracking slowly toward camera lens", "audio": "Mystic Synth Wave", "keyword": "ALGO", "note": "Drives viewers to share with friends."},

    # LUXURY & OLD-MONEY
    {"cat": "luxury", "text": "POV: Waking up in Udaipur with zero alarms and nowhere to be 🥂✨", "visual": "Palace balcony golden hour, marble archways, sipping tea in silk robe", "audio": "Royal Sitar Ambient Chill", "keyword": "PALACE", "note": "Massive aesthetic appeal in Indian luxury travel."},
    {"cat": "luxury", "text": "Skipping Monday traffic for a 48-hour solo escape to Monaco 🛥️", "visual": "Yacht deck linen resort wear, holding champagne glass against Mediterranean", "audio": "Riviera Nu-Disco", "keyword": "ESCAPE", "note": "Aspirational luxury lifestyle moodboard favorite."},
    {"cat": "luxury", "text": "When the ₹1,200 street find looks like a ₹85,000 designer piece 😍", "visual": "Side-by-side mirror inspection, running fingers along fabric texture", "audio": "Parisian Chic Accordion", "keyword": "DUPE", "note": "High conversion for fashion affiliate links."},
    {"cat": "luxury", "text": "3 unspoken rules of dressing for an old-money European summer 🍋", "visual": "Strolling Amalfi coast lemon orchard in cream linen trousers and silk scarf", "audio": "Italian Vintage Jazz", "keyword": "SUMMER", "note": "Educational carousel/reel saves."},
    {"cat": "luxury", "text": "First class window seat or private sunset rooftop? Pick one 👇", "visual": "Airbus A380 first class suite, sipping drink looking out window at clouds", "audio": "Cloud City Ambient", "keyword": "VOTE", "note": "Binary question forces high comments."},
    {"cat": "luxury", "text": "Found the quietest rooftop café in South Mumbai and I'm gatekeeping it ☕", "visual": "Colaba heritage café table with iced latte, vintage book, sea breeze", "audio": "Lo-Fi Jazzhop", "keyword": "CAFE", "note": "Local FOMO triggers hundreds of comment requests."},
    {"cat": "luxury", "text": "Packing only 5 capsule pieces for 7 days in Bali 🌴✨", "visual": "Resort villa wooden closet, laying out minimalist neutral silk sets", "audio": "Tropical Balearic Beats", "keyword": "CAPSULE", "note": "High utility fashion capsule guide."},
    {"cat": "luxury", "text": "Golden hour in Santorini hits different when you wear emerald silk 💚", "visual": "Whitewashed Oia staircase, emerald maxi dress flowing in evening wind", "audio": "Sunset Deep Melodic", "keyword": "SILK", "note": "Visual spectacle with maximum color contrast."},
    {"cat": "luxury", "text": "Why I stopped buying fast fashion and switched to timeless Indian handloom 🪡", "visual": "Raw silk texture close-up, hand grazing intricate zari embroidery", "audio": "Acoustic Classical Fusion", "keyword": "HANDLOOM", "note": "High cultural value and respect among mature audiences."},
    {"cat": "luxury", "text": "Rate this wedding guest lehenga before I walk into the sangeet: 1–10? ✨", "visual": "360-degree slow twirl in rose gold sequin lehenga in palace courtyard", "audio": "Bollywood Bass Remix", "keyword": "RATE", "note": "Wedding season viral guarantee in India."},

    # INDIAN FESTIVE & DESI
    {"cat": "desi", "text": "POV: Wearing a saree for the first time in 6 months and feeling like royalty 👑", "visual": "Crimson Kanjeevaram silk saree draping, temple jewelry adjustments, mirror smile", "audio": "Classic Sitar & Modern Trap", "keyword": "SAREE", "note": "Emotional resonance with Indian women worldwide."},
    {"cat": "desi", "text": "POV: Masala chai + cutting rain outside our South Bombay balcony 🌧️☕", "visual": "Holding steaming clay kulhad, raindrops on balcony glass, oversized sweater", "audio": "Monsoon Acoustic Hindi", "keyword": "CHAI", "note": "Universal monsoon nostalgia in India."},
    {"cat": "desi", "text": "When your mom says 'Bas 5 minute mein ready ho rahi hoon' 😭🇮🇳", "visual": "Sitting fully dressed on couch looking at watch, relatable eye-roll", "audio": "Funny Desi Comedy Track", "keyword": "MOM", "note": "Huge WhatsApp and Instagram DM share rate."},
    {"cat": "desi", "text": "Ditching heavy lehengas for this modern minimalist organza drape ✨", "visual": "Pastel lavender organza saree glowing in soft studio daylight", "audio": "Coke Studio Lo-Fi", "keyword": "ORGANZA", "note": "Top converting affiliate reel for Gen-Z ethnic wear."},
    {"cat": "desi", "text": "3 styling hacks to make any budget kurti look like Sabyasachi couture 🪞", "visual": "Step-by-step silver jhumka, oxidized belt, and sleeve roll transition", "audio": "Folk Fusion Beats", "keyword": "HACKS", "note": "High utility save magnet."},
    {"cat": "desi", "text": "POV: Entering the wedding hall and your favorite song starts playing 💃", "visual": "Slow-motion grand entry through floral arches, sparkling dupatta drape", "audio": "Wedding Dhol Anthem", "keyword": "ENTRY", "note": "Festive season virality."},
    {"cat": "desi", "text": "Silver oxidized jewelry vs yellow gold: which side are you on? 🤔", "visual": "Split transition showing temple silver set vs minimal gold choker", "audio": "Upbeat Tabla Electronic", "keyword": "JEWELS", "note": "Passionate styling debate in comments."},
    {"cat": "desi", "text": "POV: Late night Maggi run after the sangeet party at 3 AM 🍜", "visual": "Eating hot noodles in lehenga with sneakers on hotel steps, laughing", "audio": "Chill Hindi Indie", "keyword": "MAGGI", "note": "Authentic candid contrast creates viral resonance."},

    # POV & PARASOCIAL
    {"cat": "pov", "text": "POV: You're 10 minutes late to our coffee date and I give you this look ☕😒", "visual": "Sitting alone at café table, glancing up from phone with playful pout", "audio": "Cozy Café Acoustic", "keyword": "DATE", "note": "High share rate among friends and partners."},
    {"cat": "pov", "text": "Help me pick tonight's dinner outfit: Slide 1 (Red) or Slide 2 (Black)? 👇", "visual": "Quick snap transition between crimson bodycon and sleek black silk", "audio": "Catwalk Bass Rhythm", "keyword": "FIT", "note": "Binary choice yields 2.5x comment volume."},
    {"cat": "pov", "text": "When he says 'wear whatever' but you know it's a test 👀", "visual": "Holding two dress hangers against herself in bedroom mirror, pondering", "audio": "Playful Comedy Whistle", "keyword": "TEST", "note": "Relatable couple humor."},
    {"cat": "pov", "text": "POV: We locked eyes across the airport lounge right before boarding ✈️", "visual": "Oversized blazer and sunglasses in airport terminal, looking up over specs", "audio": "Deep Travel Ambient", "keyword": "FLIGHT", "note": "Intriguing story starter."},
    {"cat": "pov", "text": "Be honest: do you prefer me with wavy hair down or messy bun? 🤔", "visual": "Hands in hair tying a messy top-knot, direct eye contact with camera", "audio": "R&B Chillwave", "keyword": "HAIR", "note": "Super easy comment barrier."},
    {"cat": "pov", "text": "2 AM study & coding session when everyone else is asleep 💻🌙", "visual": "Warm neon desk glow, sipping herbal tea with glasses on, typing smoothly", "audio": "Lofi Study Beats", "keyword": "NIGHT", "note": "High appeal with tech and student creators."},
    {"cat": "pov", "text": "That shy smile when someone compliments your outfit in public 🥰", "visual": "Walking through busy urban street, looking down with authentic shy grin", "audio": "Uplifting Indie Pop", "keyword": "SMILE", "note": "High emotional warmth score."},
    {"cat": "pov", "text": "If we went on a spontaneous road trip tonight, who's on aux? 🎶🚗", "visual": "Car passenger seat golden hour, singing along with hand out window breeze", "audio": "Summer Roadtrip Anthem", "keyword": "AUX", "note": "Music lovers flood the comments."},

    # CONTROVERSY & DEBATE
    {"cat": "debate", "text": "Unpopular opinion: Overdressed is ALWAYS better than underdressed 🔥", "visual": "Gliding into casual brunch in formal tailored suit while others look casual", "audio": "Boss Energy Trap", "keyword": "DEBATE", "note": "Triggers fierce fashion debates."},
    {"cat": "debate", "text": "Why 90% of traditional modelling agencies will be obsolete by 2027 👀", "visual": "Split screen comparing studio photoshoot lighting setup vs phone workflow", "audio": "Tech News Electronic", "keyword": "FUTURE", "note": "Thought-leadership positioning."},
    {"cat": "debate", "text": "My family said this outfit is 'too bold' for dinner... agree or disagree?", "visual": "Walking into restaurant lobby with confident posture, elegant backless gown", "audio": "Deep Cello & Synth", "keyword": "BOLD", "note": "Generates 500+ opinion comments from traditional vs modern viewpoints."},
    {"cat": "debate", "text": "Men in the comments: do you actually notice earrings, or do we dress for girls? 💅", "visual": "Tucking hair behind ear to reveal statement emerald drop earrings", "audio": "Sassy Hip Hop Beat", "keyword": "STYLE", "note": "Cross-gender discussion pushes reel into explore feed."},
    {"cat": "debate", "text": "Is ₹450 for an iced matcha latte a scam or self-care? Debate below 👇🍵", "visual": "Watching green matcha swirl into iced oat milk in aesthetic glass", "audio": "Sunny Morning Groove", "keyword": "MATCHA", "note": "Relatable financial lifestyle debate."},
    {"cat": "debate", "text": "People say AI creators have zero authentic soul... let my gallery decide ✨", "visual": "Cinematic montage of 4 diverse artistic portraits across world locations", "audio": "Hans Zimmer Cinematic", "keyword": "SOUL", "note": "High cultural and artistic engagement."},

    # AI REVEAL & METAGAME
    {"cat": "aireveal", "text": "Plot twist: I don't actually exist in real life. I'm 100% AI generated 🤖✨", "visual": "Ultra-realistic skin texture zoom-out revealing phone workflow interface", "audio": "Glitch Tech Transition", "keyword": "AI", "note": "Our #1 proven sales hook that prints digital product buyers."},
    {"cat": "aireveal", "text": "My uncle tried to arrange a rishta marriage for me... nobody told him I'm AI 😭🇮🇳", "visual": "Traditional lehenga portrait smiling sweetly, followed by code terminal cut", "audio": "Viral Desi Comedy Reel", "keyword": "LAUNCH", "note": "Hyper-viral humor in India with millions of organic impressions."},
    {"cat": "aireveal", "text": "0% plastic surgery. 0% makeup artist. 100% Python & Kling prompts 💻🧬", "visual": "Slow panning portrait showing realistic freckles and hairline flyaway micro-hairs", "audio": "Cyberpunk Synthwave", "keyword": "PROMPT", "note": "Converts tech-curious creators into buyers."},
    {"cat": "aireveal", "text": "Brands used to pay ₹1,00,000 for this shoot. My creator rendered it in 40s ⚡", "visual": "High-fashion magazine editorial look on Dubai rooftop at twilight", "audio": "Fast Tech Arpeggiator", "keyword": "KIT", "note": "Direct commercial hook that positions virtual models as money-makers."},
    {"cat": "aireveal", "text": "How many days did it take you to realize I'm a virtual human? Be honest 👇", "visual": "Looking directly into camera lens with subtle breathing motion and eye blink", "audio": "Mind Bender Ambient", "keyword": "DAYS", "note": "Creates deep curiosity threads."},
    {"cat": "aireveal", "text": "Comment 'AI' if you want the exact prompt + free mobile tools that built me 🚀", "visual": "Holding smartphone displaying the workflow screen, smiling encouragingly", "audio": "Uplifting Future Bass", "keyword": "AI", "note": "Direct automated sales funnel trigger."},

    # FASHION & OOTD DUPES
    {"cat": "fashion", "text": "Stop buying Zara blazers until you see this ₹899 local alternative 🧥✨", "visual": "Quick fabric snap comparison, showing stitch quality and structured shoulder", "audio": "High Energy Runway", "keyword": "BLAZER", "note": "High buyer intent fashion hook."},
    {"cat": "fashion", "text": "How to style 1 black slip dress for 5 completely different events 🖤", "visual": "5 rapid 1-second cuts with blazer, sweater, sneakers, heels, denim", "audio": "Clean Beat Mashup", "keyword": "SLIP", "note": "Capsule fashion save magnet."},
    {"cat": "fashion", "text": "My secret 3-step color combination formula that never looks cheap 🎨", "visual": "Holding color swatches against olive green silk and chocolate brown wool", "audio": "Modern French Jazz", "keyword": "COLOR", "note": "High educational utility."},
    {"cat": "fashion", "text": "This ₹400 styling accessory made my entire outfit look like a fashion week look 🕶️", "visual": "Putting on sharp vintage tortoiseshell sunglasses with hair toss", "audio": "Retro Disco Funk", "keyword": "SHADES", "note": "Impulse purchase price point drives high affiliate revenue."},
    {"cat": "fashion", "text": "Comment 'OUTFIT' and I'll DM you the exact links before they sell out! 🛍️", "visual": "Full body mirror turn showing complete head-to-toe styling details", "audio": "Fashion House Vocal", "keyword": "OUTFIT", "note": "High urgency ManyChat trigger."},

    # CREATOR INCOME & WEALTH
    {"cat": "income", "text": "How my virtual creator account made ₹48,000 last week while I slept 📱💰", "visual": "Screen recording proof of Razorpay / Stripe notifications over morning coffee", "audio": "Minimalist Success Beat", "keyword": "SYSTEM", "note": "Proof-based income hook that triggers high purchasing intent."},
    {"cat": "income", "text": "Traditional ₹50,000 Studio Shoot vs. 20-Minute AI Influencer Workflow ⚖️", "visual": "Split graphic: expensive cameras & lights vs single smartphone on café table", "audio": "Corporate Tech Beat", "keyword": "HUSTLE", "note": "Strong value proposition contrast."},
    {"cat": "income", "text": "3 digital products you can sell with an AI creator page (with zero inventory) 📦", "visual": "Holding iPad showing prompt books, digital presets, and styling guides", "audio": "Chill Growth Trap", "keyword": "PRODUCTS", "note": "Actionable monetization framework."},
    {"cat": "income", "text": "Why faceless AI pages are outperforming traditional influencers in 2026 📈", "visual": "Growth chart telemetry overlay behind candid AI influencer portrait", "audio": "Deep Focus Bass", "keyword": "FACELESS", "note": "Validates the viewer's desire for privacy."},
    {"cat": "income", "text": "Comment 'LAUNCH' to get the full 5-Day Step-by-Step Blueprint instantly! 🚀", "visual": "Pointing down towards caption with friendly animated nod", "audio": "Motivational Upbeat", "keyword": "LAUNCH", "note": "Clear, direct call-to-action for course conversion."}
]

# Systematic expansion engine to generate a full 500-item library
matrices = [
    # CURIOSITY
    {"cat": "curiosity", "fmt": "Never post a Reel without checking this 1 camera setting for {topic}...", "visual": "Tap on camera settings, switching to 4K 60fps", "audio": "Trap Synth Beat", "kw": "SETTING", "note": "Forces creator saves"},
    {"cat": "curiosity", "fmt": "The unspoken reason nobody watches your Reels about {topic} past 3 seconds 📉", "visual": "Looking seriously at phone telemetry analytics", "audio": "Suspense Sub-Bass", "kw": "RETENTION", "note": "High educational value"},
    {"cat": "curiosity", "fmt": "I accidentally left my camera recording during {setting} and found this... 🍷", "visual": "Candid warm room laughter, leaning forward", "audio": "Intimate Jazz Waltz", "kw": "SECRET", "note": "Parasocial intimacy"},
    {"cat": "curiosity", "fmt": "Why every smart creator is archiving their old {topic} posts this week 🗂️", "visual": "Swiping rapidly through Instagram grid archive menu", "audio": "Modern Drill Beat", "kw": "ARCHIVE", "note": "FOMO hook"},
    {"cat": "curiosity", "fmt": "Save this video before Instagram deletes the audio track for {topic} 🔇", "visual": "Subtle rhythmic dancing in ambient neon lighting", "audio": "Viral Phonetic Drift", "kw": "AUDIO", "note": "Urgency-driven saves"},
    # LUXURY
    {"cat": "luxury", "fmt": "Checking into our luxury villa in {place} for the weekend 🌴✨", "visual": "Stepping out onto private sun deck into clear water", "audio": "Island Chill Waves", "kw": "VILLA", "note": "Aspirational luxury"},
    {"cat": "luxury", "fmt": "Why old-money styling for {topic} will never go out of style 🏛️", "visual": "Walking through marble museum colonnade with tailored coat", "audio": "Vivaldi Remix", "kw": "STYLE", "note": "Enduring lifestyle hook"},
    {"cat": "luxury", "fmt": "The budget skincare routine in {place} that rivals ₹50,000 clinic facials ✨", "visual": "Dabbing facial serum with glass dropper onto bare glowing cheek", "audio": "Spa Relaxing Ambient", "kw": "GLOW", "note": "Affiliate product magnet"},
    {"cat": "luxury", "fmt": "First class flight to {place} or a 5-star mountain chalet? Pick one ✈️", "visual": "Panoramic first class window view over clouds", "audio": "Cloud City Ambient", "kw": "ESCAPE", "note": "Travel bucket list debate"},
    {"cat": "luxury", "fmt": "How to look put-together in 4 minutes with 3 staple {topic} pieces ⏱️", "visual": "Fast paced styling transitions from robe to chic day fit", "audio": "Fashion House Bass", "kw": "STAPLES", "note": "High save rate"},
    # DESI
    {"cat": "desi", "fmt": "The exact draping hack for {topic} that looks like Sabyasachi couture 🪡", "visual": "Pleated pallu drape pinned with heirloom brooch in studio light", "audio": "Desi Folk Pop", "kw": "DRAPE", "note": "Hyper-relatable wedding hack"},
    {"cat": "desi", "fmt": "When you find the ultimate silk saree in {place} under ₹2,499 🥻", "visual": "Unfolding vibrant gold-bordered silk saree in showroom", "audio": "Temple Beats Fusion", "kw": "KANCHI", "note": "Affiliate shopping viral trigger"},
    {"cat": "desi", "fmt": "Why Gen-Z in {place} is falling back in love with traditional handlooms 🌸", "visual": "Close-up of artisan handloom shuttle weaving followed by street fit", "audio": "Indian Acoustic Sitar", "kw": "WEAVE", "note": "Cultural pride viral loop"},
    {"cat": "desi", "fmt": "POV: Sunday morning breakfast in {place} and the chai is boiling ☕", "visual": "Steam rising from clay kulhad, candid cozy smile", "audio": "Warm Desi Instrumental", "kw": "CHAI", "note": "Relatable comfort food"},
    {"cat": "desi", "fmt": "5 festive pose ideas for {topic} that don't look stiff or awkward 📸", "visual": "Holding floral dupatta with relaxed shoulders, soft smile", "audio": "Soft Shehnai Ambient", "kw": "POSES", "note": "Wedding photography saves"},
    # POV
    {"cat": "pov", "fmt": "POV: You told me a secret about {topic} and I promised not to tell 🤫", "visual": "Leaning across table with wide intrigued eyes, whisper gesture", "audio": "Playful Gossip Whistle", "kw": "SECRET", "note": "Fun friend sharing hook"},
    {"cat": "pov", "fmt": "POV: We're stuck in traffic in {place} and we have 1 playlist left 🚗", "visual": "Tapping steering wheel, humming along with infectious smile", "audio": "Indie Roadtrip Pop", "kw": "JAM", "note": "Music lovers magnet"},
    {"cat": "pov", "fmt": "When you catch me checking my reflection in your sunglasses during {setting} 😎", "visual": "Fixing lip gloss in reflection of camera lens with cheeky grin", "audio": "Summer Funk Groove", "kw": "SHADES", "note": "Flirty lighthearted engagement"},
    {"cat": "pov", "fmt": "Tell me the truth: would you leave {place} for love? 🌍", "visual": "Sunset rooftop leaning against railing, gazing into distance", "audio": "Cinematic Strings Wave", "kw": "LOVE", "note": "Deep storytelling comments"},
    {"cat": "pov", "fmt": "POV: Our late-night study & work session at 1:30 AM in {place} 💻", "visual": "Adjusting desk lamp, highlighter in hand, looking at screen", "audio": "Cozy Lo-Fi Study", "kw": "STUDY", "note": "Student demographic resonance"},
    # DEBATE
    {"cat": "debate", "fmt": "Should couples split the bill 50/50 in {place}? Debate below 👇", "visual": "Tapping credit card on restaurant table with questioning eyebrow", "audio": "Smooth R&B Groove", "kw": "BILL", "note": "Guaranteed 1,000+ comment war"},
    {"cat": "debate", "fmt": "Is working a 9-to-5 still the safe path, or is {topic} the new reality? 💼", "visual": "Sitting in modern coworking glass office, looking thoughtfully", "audio": "Corporate Synth Pulse", "kw": "CAREER", "note": "Life philosophy discussion"},
    {"cat": "debate", "fmt": "Wearing sneakers with {topic}: High fashion or absolute disaster? 👟", "visual": "Looking down at crisp white retro sneakers with tailored pants", "audio": "Streetwear Trap Beat", "kw": "SNEAKERS", "note": "Fashion debate"},
    {"cat": "debate", "fmt": "Are AI tools destroying authentic {topic}? Creators speak up 🎨", "visual": "Glancing at digital tablet showing hyper-real renderings", "audio": "Ticking Luxury Chime", "kw": "DEBATE", "note": "Creator industry discussion"},
    {"cat": "debate", "fmt": "Is renting clothes for {setting} smarter than buying them to wear once? 👗", "visual": "Holding designer rental tag next to lavish embroidered gown", "audio": "Money Smart Beats", "kw": "RENT", "note": "Financial wisdom debate"},
    # AI REVEAL
    {"cat": "aireveal", "fmt": "Meet the 21-year-old creator in {place} who doesn't exist in real life 🤖", "visual": "Photorealistic portrait blinking, smiling, and waving with fluidity", "audio": "Future Tech Ambient", "kw": "VIRTUAL", "note": "Mind-bending viral hook"},
    {"cat": "aireveal", "fmt": "How many hours do you think it took to generate this {topic} clip? Guess ⏳", "visual": "Cinematic drone-style flyover of model on cliff edge at sunset", "audio": "Epic Orchestral Drop", "kw": "HOURS", "note": "Curiosity into course conversion"},
    {"cat": "aireveal", "fmt": "This single AI influencer in {place} generated more sales than 5 real models 💸", "visual": "Displaying brand collaboration notifications on smartphone", "audio": "Success Synth Wave", "kw": "DEALS", "note": "B2B commercial validation"},
    {"cat": "aireveal", "fmt": "Step-by-step: How we generate consistent faces for {topic} on phone 📱", "visual": "Rapid 1-second montage of same face across 6 diverse outfits", "audio": "Upbeat Workflow Beat", "kw": "SEED", "note": "Core course pitch trigger"},
    {"cat": "aireveal", "fmt": "Why social media agencies in {place} are hiring AI creator engineers right now 🧬", "visual": "Scrolling through agency client roster showing virtual ambassadors", "audio": "Silicon Valley Electronic", "kw": "PROMPT", "note": "High-paying skill hook"},
    # FASHION
    {"cat": "fashion", "fmt": "3 clothing color rules for {topic} that instantly make you look expensive 🎨", "visual": "Pairing cream wool coat with deep chocolate turtleneck", "audio": "Chic Parisian Lounge", "kw": "LUXE", "note": "Instant viral save rate"},
    {"cat": "fashion", "fmt": "The 1 winter jacket everyone in {place} is wearing this season 🧥", "visual": "Walking down cobblestone street in oversized tailored shearling coat", "audio": "Vogue Catwalk Rhythm", "kw": "TREND", "note": "Seasonal fashion trend guide"},
    {"cat": "fashion", "fmt": "How to dress like a luxury art curator in {place} on a budget 🖼️", "visual": "Styling pleated trousers, vintage leather tote, and tortoise frames", "audio": "Coffee Shop Indie", "kw": "CURATOR", "note": "Aesthetic niche appeal"},
    {"cat": "fashion", "fmt": "Stop tucking in your oversized {topic} the wrong way 🧶", "visual": "Quick 3-second French tuck demonstration into high-waist denim", "audio": "Upbeat Tips Pop", "kw": "TUCK", "note": "Quick visual tutorial save"},
    {"cat": "fashion", "fmt": "5 staple shoes every capsule wardrobe needs for {place} 👠", "visual": "Laying out loafers, white sneakers, ankle boots, ballet flats, heels", "audio": "Clean Aesthetic Piano", "kw": "SHOES", "note": "High affiliate link clicks"},
    # INCOME
    {"cat": "income", "fmt": "How to start a faceless brand in {place} with ₹0 upfront budget 💡", "visual": "Opening free AI tool interface on phone, generating first character", "audio": "Motivational Trap", "kw": "START", "note": "Zero barrier to entry hook"},
    {"cat": "income", "fmt": "The exact math behind making ₹1 Lakh/month from {topic} 📊", "visual": "Writing simple math on iPad: ₹249 x 14 buyers/day = ₹1,04,580/month", "audio": "Focus Chill Electronic", "kw": "MATH", "note": "Demystifies digital sales math"},
    {"cat": "income", "fmt": "Why digital products in {place} have 98% profit margins 📦", "visual": "Side-by-side comparison of shipping boxes vs automated email delivery", "audio": "Tech Business Beat", "kw": "MARGINS", "note": "High business logic appeal"},
    {"cat": "income", "fmt": "My daily 15-minute routine for managing an AI page in {place} ☕", "visual": "Checking overnight DM sales while sipping morning espresso", "audio": "Peaceful Morning Acoustic", "kw": "ROUTINE", "note": "Lifestyle freedom proof"},
    {"cat": "income", "fmt": "If I lost all my followers in {place} today, here is the 7-day rebuild plan 🔄", "visual": "Drawing 3-step funnel on whiteboard: Viral Reel -> Auto-DM -> Vault", "audio": "Forward Motion Beats", "kw": "REBUILD", "note": "High authority positioning"}
]

topics = ["Indian Saree styling", "golden-hour portraits", "luxury café aesthetics", "evening rooftop reels", "designer dupes", "gym activewear", "travel cinematography", "minimalist jewelry", "viral transitions", "monetization funnels"]
places = ["South Mumbai", "Old Delhi", "Udaipur", "Goa", "Bangalore", "Dubai", "Monaco", "Bali", "Santorini", "Paris"]
settings = ["a candlelit dinner", "an intimate sangeet night", "a private yacht escape", "a luxury hotel lobby", "a quiet art gallery", "a monsoon café afternoon", "a sunset drive", "a rooftop cocktail mixer"]

ALL_HOOKS = []
ALL_HOOKS.extend(PRIMARY_HOOKS)

idx = 0
while len(ALL_HOOKS) < 505:
    m = matrices[idx % len(matrices)]
    t = topics[(idx * 3) % len(topics)]
    p = places[(idx * 7) % len(places)]
    s = settings[(idx * 5) % len(settings)]
    
    text = m["fmt"].format(topic=t, place=p, setting=s)
    ALL_HOOKS.append({
        "cat": m["cat"],
        "text": text,
        "visual": f"{m['visual']} in {p} aesthetic",
        "audio": m["audio"],
        "keyword": m["kw"],
        "note": f"{m['note']} (Optimized for {t})"
    })
    idx += 1

print(f"Total compiled hooks: {len(ALL_HOOKS)}")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex, nofollow" />
  <title>500+ Viral Reel Hooks, Live Simulator & ManyChat Studio — PersonaLabs Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&family=Playfair+Display:ital,wght@0,700;1,600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #07080d;
      --bg-secondary: #0f111a;
      --bg-card: #151824;
      --bg-card-hover: #1c2030;
      --border: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(139, 92, 246, 0.4);
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --accent-purple: #8b5cf6;
      --accent-pink: #ec4899;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-cyan: #06b6d4;
      --accent-red: #ef4444;
      --gradient-amber: linear-gradient(135deg, #f59e0b 0%, #ec4899 100%);
      --gradient-brand: linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #f59e0b 100%);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      min-height: 100vh;
    }

    /* Top Action Bar */
    .top-bar {
      background: rgba(15, 17, 26, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.85rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .top-bar a.back-btn {
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s;
    }
    .top-bar a.back-btn:hover { color: #fff; }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .btn-action {
      border: 1px solid var(--border);
      background: var(--bg-card);
      color: var(--text-primary);
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.2s;
    }
    .btn-action:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
    }
    .btn-action.primary {
      background: var(--gradient-brand);
      border: none;
      color: #fff;
      box-shadow: 0 4px 14px -2px rgba(139, 92, 246, 0.4);
    }
    .btn-action.primary:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 20px -2px rgba(139, 92, 246, 0.6);
    }

    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 6rem;
    }

    /* Hero Banner */
    .hero-banner {
      background: radial-gradient(circle at top right, rgba(245, 158, 11, 0.18), rgba(139, 92, 246, 0.12), var(--bg-card));
      border: 1px solid rgba(245, 158, 11, 0.4);
      border-radius: 20px;
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      position: relative;
      overflow: hidden;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.5);
      color: #fbbf24;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 0.3rem 0.8rem;
      border-radius: 99px;
      margin-bottom: 1rem;
    }
    .hero-banner h1 {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 2.2rem;
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 0.75rem;
    }
    .hero-banner p {
      color: var(--text-secondary);
      font-size: 1rem;
      max-width: 820px;
    }

    /* Live Smartphone Reel Studio Layout */
    .studio-grid {
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 2rem;
      margin-bottom: 3rem;
      align-items: start;
    }
    @media (max-width: 990px) {
      .studio-grid { grid-template-columns: 1fr; }
    }

    /* Smartphone Device Frame */
    .phone-container {
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 1.5rem;
      position: sticky;
      top: 5rem;
    }
    .phone-header-title {
      font-size: 0.9rem;
      font-weight: 700;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .phone-controls {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-top: 1.25rem;
    }

    .phone-mockup {
      width: 100%;
      height: 540px;
      border-radius: 36px;
      background: #000;
      border: 6px solid #272a38;
      box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.8), 0 0 25px rgba(139, 92, 246, 0.25);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* Dynamic Island */
    .dynamic-island {
      width: 90px;
      height: 20px;
      background: #000;
      border-radius: 20px;
      margin: 8px auto 0;
      z-index: 50;
    }

    /* Background Model Visual */
    .phone-bg {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%),
                  radial-gradient(circle at center, #2e1065, #07080d);
      background-size: cover;
      background-position: center;
      transition: background-image 0.3s;
    }

    /* Reel Safe Zones Overlay */
    .safe-zone-overlay {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 20;
      display: none;
      border-top: 55px solid rgba(239, 68, 68, 0.25);
      border-bottom: 95px solid rgba(239, 68, 68, 0.25);
      border-right: 50px solid rgba(245, 158, 11, 0.2);
    }
    .safe-zone-overlay.active { display: block; }
    .safe-zone-label {
      position: absolute;
      top: 58px;
      left: 10px;
      font-size: 0.65rem;
      font-family: 'JetBrains Mono', monospace;
      color: #34d399;
      background: rgba(0,0,0,0.7);
      padding: 2px 6px;
      border-radius: 4px;
    }

    /* The Hook Text inside the Reel */
    .reel-hook-display {
      position: absolute;
      left: 18px;
      right: 60px;
      top: 38%;
      transform: translateY(-50%);
      z-index: 30;
      padding: 10px 14px;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(8px);
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      font-size: 0.95rem;
      font-weight: 700;
      line-height: 1.35;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      transition: all 0.2s;
    }
    .reel-hook-display.font-classic { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; }
    .reel-hook-display.font-serif { font-family: 'Playfair Display', serif; font-style: italic; font-weight: 600; }
    .reel-hook-display.font-mono { font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; border-left: 3px solid #06b6d4; }
    .reel-hook-display.font-neon { color: #f472b6; border: 1px solid #ec4899; box-shadow: 0 0 12px rgba(236,72,153,0.5); }

    /* Instagram Reel Right Action Bar */
    .ig-right-rail {
      position: absolute;
      right: 10px;
      bottom: 25px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
      z-index: 25;
      color: #fff;
      font-size: 0.65rem;
      font-weight: 600;
    }
    .ig-rail-item { display: flex; flex-direction: column; align-items: center; gap: 3px; cursor: default; }
    .ig-rail-icon {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.15);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
    }
    .ig-music-disc {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #1e1e1e;
      border: 3px solid #444;
      animation: spin 3s linear infinite;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Instagram Reel Bottom User Info */
    .ig-bottom-info {
      position: absolute;
      left: 14px;
      bottom: 16px;
      right: 65px;
      z-index: 25;
      color: #fff;
    }
    .ig-user-row {
      display: flex;
      align-items: center;
      gap: 7px;
      margin-bottom: 6px;
    }
    .ig-avatar {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: linear-gradient(45deg, #ec4899, #f59e0b);
      border: 1.5px solid #fff;
    }
    .ig-username { font-size: 0.74rem; font-weight: 700; }
    .ig-follow-pill {
      border: 1px solid #fff;
      padding: 1px 7px;
      border-radius: 5px;
      font-size: 0.65rem;
      font-weight: 700;
    }
    .ig-caption-text {
      font-size: 0.68rem;
      color: #e2e8f0;
      line-height: 1.25;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* Simulator Control Panel */
    .st-control-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
    }
    .st-control-row label { font-size: 0.78rem; color: var(--text-secondary); font-weight: 600; }
    .st-select {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: #fff;
      padding: 0.35rem 0.65rem;
      border-radius: 6px;
      font-size: 0.78rem;
      outline: none;
    }
    .safe-toggle-btn {
      width: 100%;
      padding: 0.55rem;
      background: rgba(245, 158, 11, 0.15);
      border: 1px dashed rgba(245, 158, 11, 0.5);
      color: #fbbf24;
      font-weight: 700;
      font-size: 0.78rem;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
    }

    /* Studio Right Area: Combo Spinner & Filter */
    .studio-main {
      display: flex;
      flex-direction: column;
      gap: 1.75rem;
    }

    /* Combo Generator Box */
    .combo-generator {
      background: var(--bg-card);
      border: 1px solid var(--border-accent);
      border-radius: 16px;
      padding: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
      box-shadow: 0 8px 30px -10px rgba(139, 92, 246, 0.25);
    }
    .combo-output { flex: 1; min-width: 280px; }
    .combo-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.35rem;
      display: block;
      font-weight: 700;
    }
    .combo-output h3 {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1.2rem;
      color: #fff;
      margin-bottom: 0.5rem;
    }
    .combo-meta {
      font-size: 0.82rem;
      color: var(--text-secondary);
      line-height: 1.4;
    }
    .spin-btn {
      background: var(--gradient-amber);
      border: none;
      color: #fff;
      padding: 0.85rem 1.4rem;
      border-radius: 10px;
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: 0 4px 15px rgba(245, 158, 11, 0.35);
      transition: transform 0.15s;
    }
    .spin-btn:hover { transform: scale(1.02); }

    /* Filter Bar & Search */
    .filter-wrapper {
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .filter-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .filter-tab {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-secondary);
      padding: 0.45rem 0.85rem;
      border-radius: 99px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.15s;
    }
    .filter-tab:hover { color: #fff; border-color: rgba(255,255,255,0.2); }
    .filter-tab.active {
      background: var(--accent-purple);
      color: #fff;
      border-color: var(--accent-purple);
      box-shadow: 0 0 15px rgba(139, 92, 246, 0.4);
    }
    .search-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .search-box {
      flex: 1;
      min-width: 250px;
      position: relative;
    }
    .search-input {
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: #fff;
      padding: 0.65rem 1rem 0.65rem 2.4rem;
      border-radius: 10px;
      font-size: 0.88rem;
      outline: none;
    }
    .search-input:focus { border-color: var(--accent-purple); }
    .search-icon {
      position: absolute;
      left: 0.85rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.85rem;
    }
    .count-indicator {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }

    /* Hooks Cards Grid */
    .hooks-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.25rem;
      margin-bottom: 3.5rem;
    }
    .hook-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1.35rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1rem;
      transition: all 0.2s;
      position: relative;
    }
    .hook-card:hover {
      background: var(--bg-card-hover);
      border-color: rgba(255, 255, 255, 0.18);
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5);
    }

    .card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
    }
    .cat-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.06);
    }
    .card-hook-text {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1.02rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.38;
      margin: 0.65rem 0;
    }

    .card-meta-list {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      font-size: 0.78rem;
      color: var(--text-secondary);
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 0.75rem;
    }
    .meta-row { display: flex; align-items: flex-start; gap: 0.4rem; }
    .meta-label { color: var(--text-muted); font-weight: 600; flex-shrink: 0; }
    .meta-val { color: #cbd5e1; word-break: break-word; }

    .card-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      padding-top: 0.5rem;
    }
    .btn-preview-phone {
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.4);
      color: #c084fc;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.4rem 0.75rem;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }
    .btn-preview-phone:hover { background: rgba(139, 92, 246, 0.3); }

    .btn-copy-hook {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border);
      color: #fff;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.4rem 0.75rem;
      border-radius: 6px;
      cursor: pointer;
    }
    .btn-copy-hook:hover { background: rgba(255, 255, 255, 0.18); }

    /* ManyChat Flow Section */
    .section-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 2.25rem 2rem;
      margin-bottom: 2.5rem;
    }
    .section-card h2 {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1.6rem;
      font-weight: 800;
      margin-bottom: 0.65rem;
    }
    .section-card p {
      color: var(--text-secondary);
      font-size: 0.95rem;
      margin-bottom: 1.5rem;
    }

    /* Flowchart Visual Nodes */
    .flowchart-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }
    .flow-node {
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.15rem;
      position: relative;
    }
    .flow-node::after {
      content: "➔";
      position: absolute;
      right: -14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--accent-purple);
      font-weight: 700;
      display: none;
    }
    .flow-step-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: var(--accent-amber);
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 0.3rem;
      display: block;
    }
    .flow-node h4 { font-size: 0.92rem; font-weight: 700; color: #fff; margin-bottom: 0.3rem; }
    .flow-node p { font-size: 0.78rem; color: var(--text-muted); line-height: 1.35; margin: 0; }

    /* Code & Script Boxes */
    .script-box {
      background: #090b12;
      border: 1px solid rgba(139, 92, 246, 0.35);
      border-radius: 12px;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
    }
    .script-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 0.85rem;
      flex-wrap: wrap;
    }
    .script-title {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #c084fc;
    }
    .script-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      color: #cbd5e1;
      white-space: pre-wrap;
      line-height: 1.55;
      background: rgba(0,0,0,0.3);
      padding: 1rem;
      border-radius: 8px;
    }

    /* Print Styles */
    @media print {
      .top-bar, .phone-container, .spin-btn, .btn-action, .search-row, .card-actions { display: none !important; }
      body { background: #fff !important; color: #000 !important; }
      .container { padding: 0 !important; max-width: 100% !important; }
      .hero-banner, .section-card, .hook-card, .script-box { border: 1px solid #ccc !important; background: #fff !important; color: #000 !important; }
      .card-hook-text, h1, h2, h3, h4 { color: #000 !important; }
      .meta-val, .combo-meta, .section-card p { color: #333 !important; }
    }
  </style>
</head>
<body>

  <!-- Top Action Bar -->
  <header class="top-bar">
    <a href="index.html" class="back-btn">← Back to Student Portal Dashboard</a>
    <div class="top-actions">
      <button class="btn-action primary" onclick="exportHooksCSV()">📥 Export 500+ Hooks (CSV / Notion)</button>
      <button class="btn-action" onclick="window.print()">🖨️ Print / Save PDF</button>
    </div>
  </header>

  <main class="container">

    <!-- Hero Banner -->
    <section class="hero-banner">
      <span class="hero-badge">Order Bump #2 • VIP Conversion Engine</span>
      <h1>500+ Viral Reel Hooks, Live Simulator & ManyChat Studio</h1>
      <p>Test your hooks in real-time on our interactive 9:16 smartphone simulator, copy 500+ battle-tested viral frameworks across 8 creator niches, and install done-for-you ManyChat comment-to-DM funnels that convert viewers into paying customers 24/7.</p>
    </section>

    <!-- Interactive Studio Grid -->
    <div class="studio-grid">

      <!-- Left Column: Interactive Smartphone Reel Simulator -->
      <aside class="phone-container">
        <div class="phone-header-title">
          <span>📱 Live 9:16 Reel Simulator</span>
          <span style="font-size: 0.7rem; color: var(--accent-emerald); font-family: 'JetBrains Mono', monospace;">● LIVE</span>
        </div>

        <!-- Phone Mockup -->
        <div class="phone-mockup" id="phoneMockup">
          <div class="dynamic-island"></div>
          <div class="phone-bg" id="phoneBg"></div>

          <!-- Safe Zones Overlay -->
          <div class="safe-zone-overlay" id="safeZoneOverlay">
            <span class="safe-zone-label">SAFE ZONE (GUARANTEED VISIBILITY)</span>
          </div>

          <!-- Hook Display Text -->
          <div class="reel-hook-display font-classic" id="reelHookDisplay">
            "Wait until you notice what's behind me in the mirror... 😳"
          </div>

          <!-- Right Action Bar -->
          <div class="ig-right-rail">
            <div class="ig-rail-item">
              <div class="ig-rail-icon">❤️</div>
              <span>248.5K</span>
            </div>
            <div class="ig-rail-item">
              <div class="ig-rail-icon">💬</div>
              <span>1,420</span>
            </div>
            <div class="ig-rail-item">
              <div class="ig-rail-icon">↗️</div>
              <span>42.1K</span>
            </div>
            <div class="ig-rail-item">
              <div class="ig-rail-icon">🔖</div>
              <span>38.9K</span>
            </div>
            <div class="ig-rail-item">
              <div class="ig-music-disc"></div>
            </div>
          </div>

          <!-- Bottom Info -->
          <div class="ig-bottom-info">
            <div class="ig-user-row">
              <div class="ig-avatar"></div>
              <span class="ig-username">@personalabsacademy</span>
              <span class="ig-follow-pill">Follow</span>
            </div>
            <div class="ig-caption-text">
              Wait until you see how this was made... 💌 Comment "AI" to get our free 5-day launch kit! #aigirl #reelsindia
            </div>
          </div>
        </div>

        <!-- Simulator Controls -->
        <div class="phone-controls">
          <div class="st-control-row">
            <label>Typography:</label>
            <select class="st-select" id="fontSelector" onchange="changePhoneFont(this.value)">
              <option value="font-classic">Instagram Classic Bold</option>
              <option value="font-serif">Editorial Luxury Serif</option>
              <option value="font-mono">Cyber Typewriter</option>
              <option value="font-neon">Neon Glow Accent</option>
            </select>
          </div>

          <div class="st-control-row">
            <label>Position:</label>
            <select class="st-select" id="posSelector" onchange="changePhonePos(this.value)">
              <option value="top">Top (Curiosity Anchor)</option>
              <option value="center" selected>Center (Eye-Level Hero)</option>
              <option value="bottom">Lower Third (Safe Anchor)</option>
            </select>
          </div>

          <button class="safe-toggle-btn" onclick="toggleSafeZones()">
            🛡️ Toggle Instagram Safe-Zone Grid
          </button>
        </div>
      </aside>

      <!-- Right Column: Spin Generator & 500+ Hooks Library -->
      <section class="studio-main">

        <!-- Daily Reel Combo Generator -->
        <div class="combo-generator">
          <div class="combo-output">
            <span class="combo-tag">⚡ Daily Viral Reel Combo Generator</span>
            <h3 id="comboHookText">"Wait until you notice what's behind me in the mirror... 😳"</h3>
            <p class="combo-meta" id="comboMeta">
              <strong>🎬 Visual B-Roll:</strong> 4.5s candid bedroom mirror selfie • <strong>🎵 Audio:</strong> 118 BPM Phonetic Synth • <strong>💬 Trigger:</strong> Comment "MIRROR"
            </p>
          </div>
          <button class="spin-btn" onclick="spinRandomCombo()">🎲 Spin Daily Combo</button>
        </div>

        <!-- Search & Category Filters -->
        <div class="filter-wrapper">
          <div class="filter-tabs" id="filterTabs">
            <button class="filter-tab active" onclick="setCategory('all', this)">All Categories (500+)</button>
            <button class="filter-tab" onclick="setCategory('curiosity', this)">🔍 Curiosity & Loop</button>
            <button class="filter-tab" onclick="setCategory('luxury', this)">🥂 Luxury & Old-Money</button>
            <button class="filter-tab" onclick="setCategory('desi', this)">🇮🇳 Indian Festive & Desi</button>
            <button class="filter-tab" onclick="setCategory('pov', this)">💕 POV & Parasocial</button>
            <button class="filter-tab" onclick="setCategory('debate', this)">🔥 Controversy / Debate</button>
            <button class="filter-tab" onclick="setCategory('aireveal', this)">🤖 AI Metagame Reveal</button>
            <button class="filter-tab" onclick="setCategory('fashion', this)">👗 Fashion & OOTD</button>
            <button class="filter-tab" onclick="setCategory('income', this)">💰 Creator Income</button>
          </div>

          <div class="search-row">
            <div class="search-box">
              <span class="search-icon">🔍</span>
              <input type="text" class="search-input" id="searchInput" placeholder="Search 500+ hooks (e.g. saree, mirror, matcha, ₹48,000, AI)..." oninput="filterHooks()" />
            </div>
            <span class="count-indicator" id="countIndicator">Showing 505 Frameworks</span>
          </div>
        </div>

        <!-- The 500+ Hooks Cards Grid -->
        <div class="hooks-grid" id="hooksGrid"></div>

      </section>
    </div>

    <!-- Done-For-You ManyChat Flow Studio -->
    <section class="section-card">
      <h2>🤖 Done-For-You ManyChat Comment-to-DM Visual Studio</h2>
      <p>Connect ManyChat (Free Tier) to your Instagram business account to turn comments into automated sales, affiliate link clicks, and follower growth around the clock.</p>

      <!-- Visual Flowchart -->
      <div class="flowchart-container">
        <div class="flow-node">
          <span class="flow-step-tag">Step 1 • Trigger</span>
          <h4>User Comments Keyword</h4>
          <p>Viewer comments "AI", "LINK", or "OUTFIT" on your Reel.</p>
        </div>
        <div class="flow-node">
          <span class="flow-step-tag">Step 2 • Algorithm Guard</span>
          <h4>3x Rotating Public Reply</h4>
          <p>ManyChat automatically posts 1 of 3 natural public replies.</p>
        </div>
        <div class="flow-node">
          <span class="flow-step-tag">Step 3 • Growth Gate</span>
          <h4>Follow-Check Verification</h4>
          <p>Prompts viewer to follow before unlocking the direct link.</p>
        </div>
        <div class="flow-node">
          <span class="flow-step-tag">Step 4 • Conversion</span>
          <h4>Immediate DM Delivery</h4>
          <p>Delivers the direct link with 2 high-converting tap buttons.</p>
        </div>
      </div>

      <!-- Script Box 1 -->
      <div class="script-box">
        <div class="script-header">
          <span class="script-title">Flow #1: The High-Converting Digital Course / Prompt Pack Funnel</span>
          <button class="btn-action" onclick="copyCode(this)">📋 Copy Flow</button>
        </div>
        <div class="script-code">TRIGGER KEYWORDS: AI, REAL, SECRET, PROMPT, LAUNCH, BLUEPRINT

PUBLIC COMMENT REPLIES (Randomize across these 3 to avoid spam flags):
1. "Haha good eye 👀 Just sent the secret behind my account to your DMs!"
2. "100% pixels & code 🤖✨ Check your message requests love!"
3. "Just DM'd you the exact 5-day workflow my creator uses! 🚀"

AUTOMATED DIRECT MESSAGE (Immediate Delivery):
"You caught me! 🙈✨ Yes, I am a 100% Virtual AI Creator—and I never have a bad hair day or pay for expensive photo shoots!

My creator put together the exact 5-Day Launch Blueprint showing how anyone can build, face-lock, and monetize an AI Influencer from their phone using 100% free tools.

Tap below to unlock the complete system 👇
[Button 1: 🚀 Get The 5-Day Launch Kit] -> https://personalabs.store
[Button 2: 🧬 Steal My Exact Prompt DNA] -> https://personalabs.store#prompts</div>
      </div>

      <!-- Script Box 2 -->
      <div class="script-box">
        <div class="script-header">
          <span class="script-title">Flow #2: The "Follow-Gated" Outfit & Shopping Affiliate Funnel</span>
          <button class="btn-action" onclick="copyCode(this)">📋 Copy Flow</button>
        </div>
        <div class="script-code">TRIGGER KEYWORDS: LINK, FIT, DRESS, OUTFIT, SAREE, SHOP

PUBLIC COMMENT REPLIES:
1. "Just sent the exact outfit link to your DMs babe! Check requests 💌✨"
2. "Check your DMs love! Sent you the direct link + size guide 💕"
3. "Sent! Make sure you're following me so Instagram doesn't hide the link 🌸"

INITIAL MESSAGE (Follow-Gate):
"Hey love! 😍 Before I send you the secret styling links, make sure you're following me @[YourHandle] so Instagram lets me send clickable links! Tap the button once you follow 👇"
[Button: ✅ I'm Following! Send Link]

SECOND MESSAGE (Delivered Instantly After Tap):
"Yay thank you! 💕 Here is today's exact outfit link + 3 budget dupes I found under ₹1,299:
👉 [Tap to Shop Today's Look] -> (Insert Wishlink / Myntra / Amazon Link)
👉 [Join My Secret Daily Outfits Broadcast]"</div>
      </div>

      <!-- Script Box 3 -->
      <div class="script-box">
        <div class="script-header">
          <span class="script-title">Flow #3: High-Curiosity VIP Diary / Exclusive Channel Funnel</span>
          <button class="btn-action" onclick="copyCode(this)">📋 Copy Flow</button>
        </div>
        <div class="script-code">TRIGGER KEYWORDS: VIP, PRIVATE, UNEDITED, DIARY, TELEGRAM, MONACO

PUBLIC COMMENT REPLIES:
1. "Shhh don't tell everyone 🤫 Sent the private invite to your DMs!"
2. "Check your message requests love 💕 Just sent you the key!"
3. "Sent! See you inside my private lounge 💌"

AUTOMATED DIRECT MESSAGE:
"Hey you 😘 Thanks for commenting on my Reel!

Instagram is super strict with what I'm allowed to post publicly, so I keep my unedited vacation sets, voice notes, and 1-on-1 chats inside my private VIP Sanctuary.

Tap below to join before free entry closes tonight 👇
[Button 1: 🔓 Join My Private Telegram Diary] -> (Insert Link)
[Button 2: 💎 Unlock My Exclusive Vault] -> (Insert Link)</div>
      </div>

    </section>

    <!-- Viral Caption Architectures -->
    <section class="section-card">
      <h2>📝 The 3 Viral Caption Architectures (Watch-Time Multipliers)</h2>
      <p>The goal of your caption is to hold the viewer's eyes on the screen for 8 to 15 seconds while the video automatically loops 2 to 3 times in the background.</p>

      <div class="script-box">
        <div class="script-header">
          <span class="script-title">Architecture #1: The "Hidden Detail" Watch-Time Multiplier</span>
          <button class="btn-action" onclick="copyCode(this)">📋 Copy Caption</button>
        </div>
        <div class="script-code">I literally watched this clip 5 times before I noticed what happened in the background at 0:03 😳👇

Honestly though, rate today's [City/Event] look from 1–10! I was torn between the emerald silk or classic black, and my creator insisted on this one.

💌 Comment "LINK" and I'll DM you the exact outfit details + my private styling vault automatically!

#aiinfluencer #virtualmodel #indianfashion #ootdindia #digitalcreator #aifashion</div>
      </div>

      <div class="script-box">
        <div class="script-header">
          <span class="script-title">Architecture #2: The "6 Reasons Why" Value List (Massive Saves)</span>
          <button class="btn-action" onclick="copyCode(this)">📋 Copy Caption</button>
        </div>
        <div class="script-code">Read the caption if you want the exact 4-step formula behind this aesthetic ✨👇

1️⃣ Lighting: Always prompt 45 minutes before sunset for warm golden-hour skin highlights.
2️⃣ Color Palette: Pair neutral linen tones (beige/ivory) with one rich jewel accent (emerald or burgundy).
3️⃣ Camera Angle: 35mm eye-level smartphone framing feels 10x more personal than studio shoots.
4️⃣ Motion: Subtle hair movement + direct eye contact holds attention for 5+ seconds.

📌 Save this Reel for your next shoot & comment "SECRET" to get my full 250+ Prompt Bible in your DMs!</div>
      </div>
    </section>

  </main>

  <!-- Embedded Complete 500+ Hooks Database & Interactive Controller -->
  <script>
    const ALL_HOOKS_DATA = """ + json.dumps(ALL_HOOKS, ensure_ascii=False) + """;

    const CATEGORY_MAP = {
      'curiosity': { label: 'Curiosity & Loop', color: '#06b6d4', icon: '🔍' },
      'luxury': { label: 'Luxury & Old-Money', color: '#f59e0b', icon: '🥂' },
      'desi': { label: 'Indian Festive & Desi', color: '#ec4899', icon: '🇮🇳' },
      'pov': { label: 'POV & Parasocial', color: '#8b5cf6', icon: '💕' },
      'debate': { label: 'Controversy / Debate', color: '#ef4444', icon: '🔥' },
      'aireveal': { label: 'AI Metagame Reveal', color: '#10b981', icon: '🤖' },
      'fashion': { label: 'Fashion & OOTD', color: '#a855f7', icon: '👗' },
      'income': { label: 'Creator Income', color: '#eab308', icon: '💰' }
    };

    let activeCategory = 'all';

    function renderHooks() {
      const grid = document.getElementById('hooksGrid');
      const query = (document.getElementById('searchInput').value || '').trim().toLowerCase();

      const filtered = ALL_HOOKS_DATA.filter(h => {
        const catMatch = activeCategory === 'all' || h.cat === activeCategory;
        const textMatch = !query || 
          h.text.toLowerCase().includes(query) || 
          h.visual.toLowerCase().includes(query) || 
          h.keyword.toLowerCase().includes(query) ||
          h.note.toLowerCase().includes(query);
        return catMatch && textMatch;
      });

      document.getElementById('countIndicator').innerText = `Showing ${filtered.length} of ${ALL_HOOKS_DATA.length} Frameworks`;

      grid.innerHTML = filtered.map((h, i) => {
        const catInfo = CATEGORY_MAP[h.cat] || { label: h.cat, color: '#8b5cf6', icon: '⚡' };
        const safeText = h.text.replace(/'/g, "\\'");
        return `
          <div class="hook-card">
            <div>
              <div class="card-top">
                <span class="cat-pill" style="color: ${catInfo.color}; border: 1px solid ${catInfo.color}40;">${catInfo.icon} ${catInfo.label}</span>
                <span style="font-size: 0.68rem; font-family: 'JetBrains Mono', monospace; color: var(--text-muted);">#${i + 1}</span>
              </div>
              <div class="card-hook-text">"${h.text}"</div>
              <div class="card-meta-list">
                <div class="meta-row">
                  <span class="meta-label">🎬 Visual B-Roll:</span>
                  <span class="meta-val">${h.visual}</span>
                </div>
                <div class="meta-row">
                  <span class="meta-label">🎵 Audio Match:</span>
                  <span class="meta-val">${h.audio}</span>
                </div>
                <div class="meta-row">
                  <span class="meta-label">💬 Trigger:</span>
                  <span class="meta-val">Comment <strong>"${h.keyword}"</strong></span>
                </div>
                <div class="meta-row">
                  <span class="meta-label">💡 Strategy:</span>
                  <span class="meta-val">${h.note}</span>
                </div>
              </div>
            </div>
            <div class="card-actions">
              <button class="btn-preview-phone" onclick="loadHookIntoPhone('${safeText}')">📱 Test on Phone</button>
              <button class="btn-copy-hook" onclick="copyHookString('${safeText}', this)">Copy Hook</button>
            </div>
          </div>
        `;
      }).join('');
    }

    function setCategory(cat, btn) {
      activeCategory = cat;
      document.querySelectorAll('.filter-tab').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderHooks();
    }

    function filterHooks() {
      renderHooks();
    }

    /* Simulator Functions */
    function loadHookIntoPhone(text) {
      const display = document.getElementById('reelHookDisplay');
      display.innerText = `"${text}"`;
      display.style.transform = 'scale(1.05)';
      setTimeout(() => { display.style.transform = 'scale(1)'; }, 150);
      
      // On mobile/small screens, scroll to simulator
      if (window.innerWidth < 990) {
        document.getElementById('phoneMockup').scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    function changePhoneFont(fontClass) {
      const display = document.getElementById('reelHookDisplay');
      display.className = `reel-hook-display ${fontClass}`;
    }

    function changePhonePos(pos) {
      const display = document.getElementById('reelHookDisplay');
      if (pos === 'top') {
        display.style.top = '22%';
      } else if (pos === 'bottom') {
        display.style.top = '62%';
      } else {
        display.style.top = '38%';
      }
    }

    function toggleSafeZones() {
      const overlay = document.getElementById('safeZoneOverlay');
      overlay.classList.toggle('active');
    }

    /* Spin Combo Generator */
    function spinRandomCombo() {
      const randomItem = ALL_HOOKS_DATA[Math.floor(Math.random() * ALL_HOOKS_DATA.length)];
      document.getElementById('comboHookText').innerText = `"${randomItem.text}"`;
      document.getElementById('comboMeta').innerHTML = `<strong>🎬 Visual B-Roll:</strong> ${randomItem.visual} • <strong>🎵 Audio:</strong> ${randomItem.audio} • <strong>💬 Trigger:</strong> Comment "${randomItem.keyword}"`;
      loadHookIntoPhone(randomItem.text);
    }

    /* Copy Helpers */
    function copyHookString(text, btn) {
      navigator.clipboard.writeText(text).then(() => {
        const orig = btn.innerText;
        btn.innerText = '✓ Copied!';
        setTimeout(() => { btn.innerText = orig; }, 1800);
      });
    }

    function copyCode(btn) {
      const box = btn.closest('.script-box');
      const code = box.querySelector('.script-code').innerText;
      navigator.clipboard.writeText(code).then(() => {
        const orig = btn.innerText;
        btn.innerText = '✓ Copied Flow!';
        setTimeout(() => { btn.innerText = orig; }, 1800);
      });
    }

    /* CSV / Notion Export Engine */
    function exportHooksCSV() {
      let csv = 'ID,Category,Hook Text,Visual B-Roll Prompt,Audio Match,ManyChat Keyword,Strategy Note\\n';
      ALL_HOOKS_DATA.forEach((h, i) => {
        const catInfo = CATEGORY_MAP[h.cat] ? CATEGORY_MAP[h.cat].label : h.cat;
        const cleanText = h.text.replace(/"/g, '""');
        const cleanVis = h.visual.replace(/"/g, '""');
        const cleanAudio = h.audio.replace(/"/g, '""');
        const cleanNote = h.note.replace(/"/g, '""');
        csv += `${i + 1},"${catInfo}","${cleanText}","${cleanVis}","${cleanAudio}","${h.keyword}","${cleanNote}"\\n`;
      });

      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', 'PersonaLabs_500_Viral_Hooks_Database.csv');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    // Initial render
    window.onload = function() {
      renderHooks();
    };
  </script>
</body>
</html>"""

# Write to both locations
with open(output_vault, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(output_drive, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully written {len(ALL_HOOKS)} hooks to:")
print(f"1. {output_vault}")
print(f"2. {output_drive}")
