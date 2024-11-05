import random
import nodes
        
class VideoPromptGenerator:
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Doctor-Tools"

    @classmethod
    def IS_CHANGED(cls):
        return float("NaN")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {}),
                "shot_type": (
                    ["random"] + VideoPromptGenerator.SHOT_TYPE,
                    {"default": "random"},
                ),
                "actions": (
                    ["random"] + VideoPromptGenerator.ACTIONS,
                    {"default": "random"},
                ),
                "style": (["random"] + VideoPromptGenerator.STYLE, {"default": "random"}),
                "director": (
                    ["random"] + VideoPromptGenerator.DIRECTOR,
                    {"default": "random"},
                ),
                "location": (["random"] + VideoPromptGenerator.LOCATION, {"default": "random"}),
                "lighting": (
                    ["random"] + VideoPromptGenerator.LIGHTING,
                    {"default": "random"},
                ),
            },
        }

    SHOT_TYPE = [
        "",
	"aerial shot",
        "bird's-eye view",
        "close-up",
        "cowboy shot",
        "crane shot",
        "cut-in",
        "cutaway",
        "dolly shot",
        "dolly zoom left",
        "dolly zoom right",
        "dutch angle",
        "establishing shot",
        "extreme close-up",
        "extreme long shot",
        "eye-level shot",
        "follow shot",
        "high-angle shot",
        "insert shot",
        "low-angle shot",
        "master shot",
        "medium close-up",
        "medium shot",
        "over-the-shoulder shot",
        "pan left",
        "pan right",
        "point-of-view (POV) shot",
        "pull-back shot",
        "reaction shot",
        "reverse-angle shot",
        "tilt up",
        "tilt down",
        "tracking shot",
        "two-shot",
        "wide shot",
    ]

    ACTIONS = [
        "",
        "adjusting clothing",
        "answering the phone",
        "apologizing sincerely",
        "arguing intensely",
        "asking a question",
        "biting lip nervously",
        "blinking rapidly",
        "brushing hair back",
        "bursting into laughter",
        "checking their watch",
        "clapping hands excitedly",
        "crossing arms defiantly",
        "crying softly",
        "dancing gracefully",
        "drinking from a glass",
        "eating hurriedly",
        "falling to the ground",
        "frowning deeply",
        "gesturing wildly",
        "glancing sideways suspiciously",
        "grinning mischievously",
        "laughing heartily",
        "looking around anxiously",
        "looking down in embarrassment",
        "looking up in awe",
        "looking surprised",
        "nodding in agreement",
        "pointing accusingly",
        "raising eyebrows in disbelief",
        "raising hand confidently",
        "running frantically",
        "scratching head in confusion",
        "shaking head in disbelief",
        "shivering from the cold",
        "shrugging indifferently",
        "sitting down slowly",
        "smiling warmly",
        "sneezing suddenly",
        "staring blankly",
        "standing up abruptly",
        "starting to run",
        "stepping back cautiously",
        "stretching arms wide",
        "sulking in silence",
        "turning around quickly",
        "walking purposefully",
        "waving enthusiastically",
        "whispering a secret",
        "yawning sleepily",
        "leaning in close",
        "holding back tears",
        "giving a thumbs up",
        "winking playfully",
        "folding hands thoughtfully",
        "covering mouth in shock",
        "fixing gaze intensely",
        "rolling eyes",
        "crossing legs casually",
        "adjusting glasses",
        "reaching out",
        "placing hand on heart",
        "taking a deep breath",
        "scanning the room",
        "mouthing words silently",
        "putting hands in pockets",
        "shaking hands warmly",
        "narrowing eyes suspiciously",
        "opening a door cautiously",
        "holding their head in pain",
        "wringing hands nervously",
        "breaking into a run",
        "throwing hands in the air",
        "snapping fingers",
        "giving a thumbs down",
    ]

    STYLE = [
        "",
	"Cinematic",
        "cctv footage",
        "surrealism",
        "futurism",
        "music video"

    ]

    DIRECTOR = [
        "",
	"David Fincher",
        "Quentin Tarantino",
    ]

    LOCATION = [
        "",
	"indoor",
        "outdoor",
        "at night",
        "in the park",
        "studio",
        "at a party",
        "at a festival",
        "at a concert",
        "on persons home planet",
        "magical portal with particles",
        "in a neon lit city",
        "in a cyberpunk city",
        "in a fantasy world",
        "fashion show",
        "at home",
        "at work",
        "at a cafe",
        "at a gym",
        "at a hotel",
        "at a concert performance",
        "at the beach",
        "at a museum",
        "in a hidden city deep in the rainforest",
        "in a floating island in the sky",
        "in an underground world beneath the earths surface ",
        "in a secret garden hidden in a mysterious maze",
        "in a grand castle on the top of a remote mountain",
        "in a enchanted forest with talking animals and magical creatures",
        "in a mystical island filled with ancient ruins and hidden treasure",
        "in a faraway planet with a unique and alien landscape",
        "in a hidden paradise hidden behind a waterfall",
        "in a dreamlike world where anything is possible and the impossible is real",
        "in a hidden oasis in the desert",
        "in a secret underground city",
        "in an underwater kingdom",
        "in a lost temple in the jungle",
        "in a castle in the clouds",
        "in a hidden valley in the mountains",
        "in a uturistic city on a distant planet",
        "in a mystical land of eternal twilight",
        "Smoke and ash in the air",
        "suburban america", 
        "suburbs", 
        "slums", 
        "at the sea", 
        "at the ocean",
        "at the lake",
        "at the river",
        "at the waterfall",
        "in the labyrinth",
        "in a lab"
    ]
    LIGHTING = [
        "",
	"popping colors, popart style",
        "bokeh",
        "dramatic lighting",
        "golden hour",
        "colorful lighting",
        "soft lighting",
        "studio lighting with strong rim light",
        "ambient lighting",
        "sun rays",
        "cinematic lighting",
        "characteristics of the light",
        "volumetric lighting",
        "natural point rose",
        "outdoor lighting",
        "soft pastel lighting colors scheme",
        "sensual lighting",
        "neon lights",
        "baroque",
        "rokoko",
        "rim light, iridescent accents",
        "neoclassicism",
        "realism",
        "fantastic colors",
        "accent lighting",
        "high key lighting",
        "low key lighting",
        "strong backlight",
        "artificial lighting",
        "laser lighting",
        "multi-colored lighting",
        "mood lighting",
        "accent lighting",
        "projection lighting",
        "bioluminiscent",
        "anamorphic lens flare",
        "sharp focus",
        "vivid colors",
        "masterpiece",
        "colors",
        "8k",
        "atmospheric",
        "cinematic sensual",
        "hyperrealistic",
        "big depth of field",
        "glow effect",
        "modelshoot style",
        "shallow depth of field",
        "hdr",
        "dynamic composition",
        "broad light",
        "natural lighting",
        "elegant pose",
        "flowing",
        "film photo",
        "extremely detailed",
        "big depth of field",
        "matte skin, pores, wrinkles",
        "hyperdetailed",
        "(abstract:1.3)",
        "intricate and low contrast detailed",
        "(composition)",
        "film grain",
        "(8k, RAW photo, best quality, masterpiece:1.2)",
        "(realistic, photo-realistic:1.37)",
        "beautiful detailed eyes, beautiful detailed lips, a captivating gaze, and an alluring expression",
        "beautiful dynamic dramatic dark moody lighting",
        "(detailed face:1.3)",
        "multilayered realism",
        "majestically strides forward toward us with abandon",
        "disintegrating moon",
        "extremely intricate details",
        "anatomical beauty",
        "high fantasy",
        "detailed skin pores",
        "flat color scheme",
        "80s music clip background",
        "Use a backlighting effect to add depth to the image. impressionistic painting style, john singer sarget, blue pallette",
        "(natural skin texture, hyperrealism, soft light, sharp:1.2)",
        "(cinematic, teal and orange:0.85)",
        "(intricate skin detail:1.3), (wrinkles:1.2),(skin blemishes:1.1),(skin pores:1.1),(detailed face:1.3), (lips slightly parted:1.0)",
        "(muted colors, dim colors, soothing tones:1.3), low saturation, (hyperdetailed:1.2)",
        "(noir:0.4), (intricate details:1.12), hdr, (intricate details, hyperdetailed:1.15)",
        "(neutral colors:1.2), art, (hdr:1.5), (muted colors:1.1), (pastel:0.2), hyperdetailed",
        "dramatic lighting",
        "((landscape view)), 4k unity, (best illumination)",
        "dynamic angle",
        "detailed freckles skin",
        "movie grain",
        "epic composition",
        "Tarot Card style",
        "(solo focus, one frame)",
        "(masterpiece, best quality, ultra-detailed, highres)",
        "biopunk",
        "dramatic Pull from the ghost of a virtual memory",
        "gritty industrial",
        "(soothing tones, insane details, intricate details, hyperdetailed,photorealistic,dim subdued lighting)",
    ]
    @staticmethod
    def generate_prompt(**kwargs):
        components = []

        # Get subject
        subject = kwargs.get("subject", "")
        if subject.lower() == "random":
            subject = random.choice(VideoPromptGenerator.SUBJECT)  # Ensure SUBJECT list is defined
        components.append(subject)

        # Get shot type
        shot_type = kwargs.get("shot_type", "")
        if shot_type.lower() == "random":
            shot_type = random.choice(VideoPromptGenerator.SHOT_TYPE)
        components.append(shot_type)

        # Get location
        location = kwargs.get("location", "")
        if location.lower() == "random":
            location = random.choice(VideoPromptGenerator.LOCATION)
        components.append(location)

        # Get style
        style = kwargs.get("style", "")
        if style.lower() == "random":
            style = random.choice(VideoPromptGenerator.STYLE)
        components.append(f"{style} style")

        # Get director
        director = kwargs.get("director", "")
        if director.lower() == "random":
            director = random.choice(VideoPromptGenerator.DIRECTOR)
        components.append(f"by {director}")

        # Get lighting
        lighting = kwargs.get("lighting", "")
        if lighting.lower() == "random":
            selected_lighting = ", ".join(random.sample(VideoPromptGenerator.LIGHTING, random.randint(2, 5)))
        else:
            selected_lighting = lighting
        components.append(selected_lighting)

        prompt = " ".join(filter(None, components))
        print(f"AUTOPROMPT: {prompt}")
        return (prompt,)

# Ensure these mappings point to the correct class
NODE_CLASS_MAPPINGS = {
    "VideoPromptGenerator": VideoPromptGenerator,
}

# Human readable names for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "VideoPromptGenerator": "Video Prompt Generator",
}
